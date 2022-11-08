Bioinformatics Exam
===================

The following document is designed to test your bioinformatics skills. It
contains a mixture of Git, Unix, and Python.

After passing the exam, you will be listed in the `DEVELOPERS.md` document and
receive an official "KorfLab Bioinformatics Developer Certificate".


Rules
-----

1. You may not copy-paste anything while doing the challenge
2. You may not get help from anyone

Yes, you may look things up on the Internet for inspiration, but don't copy
other peoples' code.


Suggestions
-----------

1. Program in Python using a text editor and terminal
2. After you finish each program, `git push` it to your repo
3. Take the exam more than once
	+ See how far you can get in 60 minutes
	+ Try to improve your speed
	+ Try to pass the exam at the Silver or Gold levels


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
+ Meet with Ian


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

Write a simulation of the birthday paradox. That is, in a classroom of size n,
what is the probability that two people will share the same birthday? You can
find more information here: https://en.wikipedia.org/wiki/Birthday_problem

Your solution must use arrays only and must simulate the problem with randomly
assigned birthdays. Don't solve it analytically. Dictionaries, sets, and other
data structures are not allowed.

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


FASTA File
----------

Write a function to read FASTA files and put it in a library.

Intent: Demonstrate you know how to create and use a library and also to parse
a common file format. Since FASTA files can be huge, the best solutions will
use minimal memory (read one sequence at a time).


Entropy Filter
--------------

Write a complexity filter for nucleotide sequences. The program must use a
standard CLI library (e.g argparse in Python). There must be a positional
argument for the fasta file and named parameters for window size and entropy
threshold. The named parameters must have default values. The program must be
executable from anywhere on your computer. The output should be a FASTA file
with the low complexity regions masked with Ns or lowercase letters. There
should be an option to specifify which.

Intent: Demonstrate you know how to create a proper Unix program. The best
solutions will be efficient even with very large window sizes.


Overlaps
--------

Given two GFF files, report which features overlap each other (e.g. where do
exons overlap ChIP-seq peaks?). The CLI should use argparse.

Intent: Demonstrate you can model sequence features and make comparisons among
them. GFF files can be huge. The best solutions will be efficient in time and
memory.


Fork Setup
----------

+ Fork the KorfLab/setup repository
+ Add your name to the end of the list in `DEVELOPERS.md`
+ Send a pull request


Meet with Ian
-------------

Schedule an appointment to meet with Ian to determine if you passed and what
level of pass you achieved.

+ Bronze - you passed, but your code has some issues
+ Silver - you passed, and your code is pretty good
+ Gold - you passed, and your code is excellent

In order to pass at the higher levels, your code must have the following
properties.

+ Follows the prompt exactly
+ Beautiful code
	+ Consistent and standard style
	+ Appropriate variable and function names
	+ Useful comments
+ Efficient in time and space
