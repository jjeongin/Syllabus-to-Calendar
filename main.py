import PyPDF2
from dateutil.parser import parse
from sutime.sutime import SUTime
import difflib
import datetime # to change date string format
import os
import csv

# sutime configuration
jar_files = os.path.join(os.path.dirname(__file__), 'sutime/jars')
sutime = SUTime(jars=jar_files, mark_time_ranges=True)

keywords=["exam", "assignment", "hw", "homework1", "homework","homework2", "homework3" "midterm", "assign ","quiz","ment", "test", "home", "work", "essay", "finalessay", "essay3", "essay1", "assignment_1","assignment_2", "assignment_3", "assignment_4", "midterm2", "finals", "essay1", "essay4", "mid-term", "final"]

# User can enter input by 2 ways: (1) specifying pdf path or (2) directly entering texts including schedules
# (1) import text from pdf
def pdf_to_text():
    fileName=input("Enter your file name: ")
    pdfObject = open(os.path.join(os.path.dirname(__file__), fileName), 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfObject)
    pgnum=pdfReader.numPages

    s=""
    for i in range(pgnum):
        pageObj = pdfReader.getPage(i)
        s+=pageObj.extractText()

    pdfObject.close()
    return s

# (2) get user input
def get_user_input():
    string = input("Enter your text: ")
    return string

def find_event(d, string):
    index_range = 16 # custom value

    start = string.find( d["text"] ) - index_range
    string = string[start:start + index_range*2]
    string = string.lower() # handle string
    string_list = string.split()

    for k in keywords:
        close_match = difflib.get_close_matches(k, string_list, n=1, cutoff=0.1)
    d["event"] = close_match[0] # we can now add the closes matching event to the dictionary

def find_dates(string):
    sutime = SUTime(mark_time_ranges=True, include_range=True)
    dates = sutime.parse(string)

    for d in dates: # loop through detected dates
        if d["type"] == "DATE": 
            d["value"] = datetime.datetime.strptime(d["value"], "%Y-%m-%d").strftime('%m/%d/%y') # change date format for google cal export
            find_event(d, string) # call find_event function to add event name to the dict 

    # alternative library
    # p = parsedatetime.Calendar()
    # d = p.parse(string)
    # print(d)

    return dates

def write_calendar_csv(events):
    with open(os.path.join(os.path.dirname(__file__), 'calendar.csv'), mode='w', newline='') as calendar_csv:

        # write header
        fieldnames = ['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time', 'All Day Event', 'Description', 'Location', 'Private']
        calendar_writer = csv.DictWriter(calendar_csv, fieldnames=fieldnames)

        calendar_writer.writeheader()
        for e in events:
            if e["type"] == "DATE":
                calendar_writer.writerow({'Subject': e['event'], 'Start Date': e["value"], 'End Date': e["value"], 'All Day Event': True})

    calendar_csv.close()

# sample string
s = """Quizzes
10%
-
Assignment 1
5%
Sep. 22
CLO 1
Assignment 2
5%
Oct. 6
CLO 5
Assignment 3
10%
Nov. 15
CLO 3, CLO 4
Assignment 4
10%
Dec. 6
CLO 3, CLO 4
ParWcipaWon
5%
-
CLO 9
Mid-Term Exam
25%
Oct. 13
-
Final exam
30%
Final’s week
-"""

## MAIN LOGIC
# s = pdf_to_text()
# s = get_user_input()
events = find_dates(s)
write_calendar_csv(events)