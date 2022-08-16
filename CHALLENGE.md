Coding Challenge
================

The following document is a coding challenge. Read all of the directions before
you begin. Each example is designed to test a specific part of your programming
knowledge.

Here are the rules:

+ You have 60 minutes
+ You may use any language for any task
+ You must write the programs in the order given
+ You may not copy-paste from any of your previous code
+ You may not copy-paste anything from the Internet

## Hello World ##

Write a program the prints "Hello World".

Intent: Show that your programming environment actually works

## FizzBuzz ##

Print the numbers from 1-100 except:

+ If the number is divisible by 3, print "Fizz" instead
+ If the number is divisible by 5, print "Buzz" instead
+ If the number is divisible by 3 and 5, print "FizzBuzz" instead

Intent: Show you can solve a problem using loops and conditionals

## Hello Again ##

Write a program the runs your hello world program from above, captures its
output and appends ", again!" at the end. The output should be one line.

Intent:

+ Show you know how to run programs from other programs
+ Show you know how to capture output from another program

## Descriptive Statistics ##

Write a program that calculates the median, mean, and standard deviation of
values that are given in a file.

Intent:

+ Show you know how to read files
+ Show you know how to use arrays to store data
+ Show you know how to access arrays sequentially and by index

## Sequence Coverage ##

Simulate re-sequencing a genome. How much of a genome is not sequenced at 3x
coverage? The value of 3x must be a command line parameter.

Intent:

+ Show you know how to use arrays, loops, and conditionals
+ Show you know how to read data from the command line

## Hydropathy ##

Write a program that computes the local hydropathy of a sequence. There must be
parameters for window size and the sequence. You may use any Kyte-Doolittle or
any other hydropathy scale. The output should be tabular, with columns for
position and hydropathy.

Intent:

+ Show you know how to create a dictionary for efficent lookup
+ Show use of one-dimensional data structures, loops, and conditionals

## Codon Usage ##

Write a program that reports the codon usage for a file of coding sequences.

Intent: Show you know how to use a dictionary for recording data

## Birthday Paradox ##

Write a simulation of the birthday paradox. That is, given a classroom of size
X, when is the probability of two people sharing the same birthday greater than
50%.

Intent: Show your ability to use a combination of loops, conditionals, and
arrays to perform moderately complex logic

## FASTA File ##

Write a function to read FASTA files and put it in a library.

+ Intent:

+ Show your knowledge of FASTA files
+ Show your ability to read a strange file format
+ Show you know how to create libraries

## Position Weight Matrix ##

Given a FASTA file of sequences, create a representative PWM. Use your library
file from above.

+ Intent:

+ Show you know how to create a 2-dimensional data structure
+ Show you know how to use your own libraries

## Entropy Filter ##

Write a complexity filter for nucleotide sequences. The program must use
argparse. There must be a positional argument for the fasta file and named
parameters for window size and entropy threshold. The named parameters must have
default values. The program must be executable from anywhere on your computer.

+ Intent:

+ Show you know how to use argparse
+ Show you know how to make programs into proper Unix executables
+ Show you understand how Linux programs should look and feel
