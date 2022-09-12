Bioinformatics Exam
===================

The following document is designed to test your bioinformatics skills. It
contains a mixture of Git, Unix, and Python.

After passing the exam, you will be listed in the `DEVELOPERS.md` document and
receive an official "KorfLab Bioinformatics Developer" certificate if you want
one.


Rules
-----

1. You may not copy-paste anything while doing the challenge
2. You may not get help from anyone

Yes, you may look things up on the Internet, but don't copy other peoples'
code. The point of this exam isn't to _finish_ but to assess your own
abilities.

Suggestions
-----------

1. Program in Python using a text editor and terminal
2. After you finish each program, `git push` it to your repo.


Tasks
-----

These are the tasks you will be given. Each one is described below.

+ GitHub repo
+ Hello World
+ FizzBuzz
+ Factorial
+ Descriptive statistics
+ Birthday paradox
+ Hydropathy
+ AA composition
+ IPC
+ FASTA file
+ Entropy filter
+ Overlaps
+ Fork setup


GitHub Repo
-----------

Create a repository called `korflab_exam` and invite `iankorf` as a
collaborator.


Hello World
-----------

Write a program that prints "Hello World" in your terminal.

Intent: Demonstrate that your programming environment works in a command line
environment.


FizzBuzz
--------

Write a program that prints the numbers from 1-100 except:

+ If the number is divisible by 3, print "Fizz" instead
+ If the number is divisible by 5, print "Buzz" instead
+ If the number is divisible by 3 and 5, print "FizzBuzz" instead

Intent: Demonstrate you know how to use loops and conditionals.


Factorial
---------

Write a program that computes the factorial of a number given on the command
line. Your program must report an error if the command line parameter is
illegal. The error must be sent to stderr, and the program must exit with
non-zero status.

Intent: Demonstrate that you can read a value from the command line and use it
with loops and conditionals. Also, that you know how to report errors.


Descriptive Statistics
----------------------

Write a program that calculates the median, mean, and standard deviation of
values that are given on the command line. You are not allowed to import any
statistics packages. Illegal values should be skipped but create a warning that
is sent to stderr.

Intent: Demonstrate you know how to use arrays along with loops and
conditionals. Also, that you know how to generate a warning.


Birthday Paradox
----------------

Write a simulation of the birthday paradox. That is, what is the probability
that two people share the same birthday?

Intent: Demonstrate your ability to use a combination of loops, conditionals,
and arrays to perform moderately complex logic


Hydropathy
----------

Write a program that computes the local hydrophilicity/hydrophobicity in a
sequence. The sequence and window size are command line parameters. You may use
Kyte-Doolittle or any other hydropathy scale. The output should be tabular,
with columns for position and average hydropathy at the position.

See https://en.wikipedia.org/wiki/Hydrophilicity_plot

Intent: Demonstrate you know how to create a dictionary and read values from
it. Also, that you can write a simple windowing algorithm.


AA Composition
--------------

Write a program that computes the amino acid composition of a sequence given on
the command line. The output should be sorted alphabetically.

Intent: Demonstrate you know how to work with dictionaries.


IPC
---

Write a program that runs your AA Composition program (from above), captures
the output, and reports the most and least common amino acids.

Intent: Demonstrate you can run other programs and read their output.

Example:
```
python3 ipc.py
```


FASTA File
----------

Write a function to read FASTA files and put it in a library.

Intent: Demonstrate you know how to create and use a library and also to parse
a common file format.


Entropy Filter
--------------

Write a complexity filter for nucleotide sequences. The program must use a
standard CLI library (e.g argparse in Python). There must be a positional
argument for the fasta file and named parameters for window size and entropy
threshold. The named parameters must have default values. The program must be
executable from anywhere on your computer.

Intent: Demonstrate you know how to create a proper Unix program.


Overlaps
--------

Given two GFF files, report which features overlap each other (e.g. where do
exons overlap ChIP-seq peaks?).

Intent: Demonstrate you can model sequence features and make comparisons among
them.


Fork Setup
----------

+ Fork the KorfLab/setup repository
+ Add your name to the end of the list in `DEVELOPERS.md`
+ Send a pull request


Meet with Ian
-------------

Schedule an appointment to meet with Ian to determine if you passed and what
level of pass you achieved.

+ Bronze - you passed
+ Silver - you passsed and your code is efficient or elegant
+ Gold - you passewd and your code is both efficient and elegant
