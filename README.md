# 🗓 Syllabus to Calendar

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

## Inspiration
Missing our own deadlines and forgetting about the quizzes and exams as we did not put down the dates in our calendars so we decided to build something that does it for us

## What it does
Reads assignment dates from pdfs and put it into a csv file that we can import in our google calendars

## How we built it
Using SUtime a nlp tool that detects the dates and difflib library of python

## What's next for 🗓 ***Syllabus to calendar***
A webapp and chrome extension work on the accuracy and support multiple syllabus formats add a reminder system that reminds us of the exams and quiz regularly like 2 weeks before the actual date
