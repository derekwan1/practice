# Practice
A lightweight utility that converts markdown problems into interactive HTML quiz.

All files containing questions are placed under `source/` and must following the
folllowing format.

```
Question: <question goes here>
Option: <Answer choice goes here>
Option: <Answer choice goes here>
...
```

You can add as many options as you need and as many questions as you need. Here
is a sample questions file that you may have.

```
Question: What is 2+3?
Option: 3
Option: 4
Option: 6
Option: 5
```
This file is accepted as input and then rewritten as HTML, using the following
command, for a source file `source/question.md`

```
python practice.py source/question.md
```

We can also read from source directories. In which case, `practice.py` will simply
run the generation script for all files in the directory. Consider a directory
`source/source1`.

```
python practice.py source/source1
```
