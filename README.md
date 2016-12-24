# Practice
A lightweight utility that converts markdown problems into interactive HTML quiz

by Derek Wan, with contributions from Alvin Wan

All files containing questions are placed under `source/` and must following the
following format.

```
Question: <question goes here>
Option: <Answer choice goes here>
Option: <Answer choice goes here>
...
Correct: <Correct answer choice goes here>
```

You can add as many `option`s as you need and as many `question`s as you need.
Here is a sample questions file that you may have.

```
Question: What is 2+3?
Option: 3
Option: 4
Option: 6
Correct: 5
```

This file is accepted as input and then rewritten as HTML, using the following
command, for a source file `source/question.md`

```
python practice.py source/question.md
```

We can also read from source directories. In which case, `practice.py` will
simply run the generation script for all files in the directory. Consider a
directory `source/source1` for the following command.

```
python practice.py source/source1
```

This produces output in `outputs/source/source1/`, where each file resembles
the following.

<img width="589" alt="screen shot 2016-12-23 at 9 23 49 pm" src="https://cloud.githubusercontent.com/assets/2068077/21465381/26d64164-c956-11e6-83c5-a1ac211639b2.png">

Selecting an answer and clicking an answer then provides immediate feedback.

<img width="457" alt="screen shot 2016-12-23 at 9 24 01 pm" src="https://cloud.githubusercontent.com/assets/2068077/21465382/26f01882-c956-11e6-8b1a-844dc948eb8d.png">
