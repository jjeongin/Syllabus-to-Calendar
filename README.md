# 🗓 Syllabus to Calendar
Automatic calendar event generator for Google Calendar from your Syllabus using NLP model 📚

## Installation
1. Install [Maven](https://maven.apache.org/install.html) if you don't have one.

``` brew install maven ```

2. Install Python wrapper for Stanford CoreNLP's [SUTime](https://nlp.stanford.edu/software/sutime.shtml) Java library. Detailed Instruction can be found [here](https://github.com/FraBle/python-sutime).


```bash
>> # Ideally, create a virtual environment before installing any dependencies
>> pip install sutime
>> # Install Java dependencies
>> mvn dependency:copy-dependencies -DoutputDirectory=./jars -f $(python3 -c 'import importlib; import pathlib; print(pathlib.Path(importlib.util.find_spec("sutime").origin).parent / "pom.xml")')
```

3. Install PyPDF2 library.


```pip install PyPDF2```

4. Download ***Syllabus to Calendar*** to your local computer ✨

```git clone https://github.com/jjeongin/Syllabus-to-Calendar.git```

## Demo
*Example Syllabus:* 

<img width="500" alt="Screen Shot 2021-11-06 at 2 32 51 PM" src="https://user-images.githubusercontent.com/68997923/140606519-a1f1b499-c2c2-417c-9296-ecb69c853233.png">

- Copy and Paste texts including important schedules to our program. The dates will be detected using Stanford's SUTime NLP model.
You can also check the aproximate output in
[*SUTime web demo.*](http://nlp.stanford.edu:8080/sutime/process)
<img width="900" alt="Screen Shot 2021-11-06 at 2 19 41 PM" src="https://user-images.githubusercontent.com/68997923/140606692-9ab65582-500d-41e9-8825-4c68cb11a2a4.png">

- After running the python program, ou can either specify pdf file path or custom string in terminal to get .csv file for your calendar.

*Example CSV Output:*

<img width="900" alt="Screen Shot 2021-11-06 at 2 37 58 PM" src="https://user-images.githubusercontent.com/68997923/140606685-dd03757b-cf52-411e-867e-266978622e23.png">

- Import .csv file to your Google Calendar.

*Google Calendar Screenshot:*

<img width="600" alt="Screen Shot 2021-11-06 at 3 05 50 PM" src="https://user-images.githubusercontent.com/68997923/140607362-906173f2-13ed-4374-9957-6df3a494c0a1.png">

<img width="600" alt="Screen Shot 2021-11-06 at 3 05 57 PM" src="https://user-images.githubusercontent.com/68997923/140607363-6ec4c33f-c011-49cf-bfd9-dcfa1bdc43dd.png">

## Inspiration
Missing our own deadlines and forgetting about the quizzes and exams as we did not put down the dates in our calendars so we decided to build something that does it for us

## What it does
Reads assignment dates from pdfs and put it into a csv file that we can import in our google calendars

## How we built it
Using SUtime a nlp tool that detects the dates and difflib library of python

## What's next for 🗓 ***Syllabus to calendar***
A webapp and chrome extension work on the accuracy and support multiple syllabus formats add a reminder system that reminds us of the exams and quiz regularly like 2 weeks before the actual date
