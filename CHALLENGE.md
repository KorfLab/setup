Coding Challenge
================

The following document is a coding challenge. Read all of the directions before
you begin. Each example is designed to test a specific part of your programming
knowledge.

Here are the rules:

+ You have 60 minutes
+ You must use Python (you can also do this in other langauges after Python)
+ You must write the programs in the order given
+ You may not copy-paste from any of your previous code
+ You may not copy-paste anything from the Internet


## Hello World ##

Write a program the prints "Hello World".

Intent: Demonstrate that your programming environment works.

Example: 

```
python3 hello.py
```

## FizzBuzz ##

Print the numbers from 1-100 except:

+ If the number is divisible by 3, print "Fizz" instead
+ If the number is divisible by 5, print "Buzz" instead
+ If the number is divisible by 3 and 5, print "FizzBuzz" instead

Intent: Demonstrate you know how to use loops and conditionals.

Example:

```
python3 fizzbuzz.py
```

## Factorial ##

Compute the factorial of a number given on the command line. Your program must
report an error if the command line parameter is illegal.

Intent: Demonstrate that you can read a value from the command line and use it
with loops and conditionals. Also, that you know how to report errors.

Example:

```
python3 factorial.py 5
```

## Descriptive Statistics ##

Write a program that calculates the median, mean, and standard deviation of
values that are given on the command line. You are not allowed to import any
statistics packages. Illegal values should be skipped but create a warning.

Intent: Demonstrate you know how to use arrays along with loops and
conditionals. Also, that you know how to create a warning.

Example:

```
python3 stats.py 1 0 -1 3.14 2.718 Foo 2 7
```

## Sequence Coverage ##

Simulate re-sequencing a genome. How much of a genome is not sequenced at X
coverage? The value of X must be a command line parameter.

Intent: Demonstrate accessing arrays by index as well as more loops and
conditionals.

Example:

```
python3 coverage.py 3.0
```


## Hydropathy ##

Write a program that computes the local hydropathy of a sequence. The sequence
and window size are command line parameters. You may use Kyte-Doolittle or any
other hydropathy scale. The output should be tabular, with columns for position
and average hydropathy at the position.

Intent: Demonstrate you know how to create a dictionary and read values from it.

Example:

```
python3 hydropathy.py NGTEGKNFYIPMSNKTGIVRSPYEYQQYYMVDPMIY 11
```

## AA Composition ##

Write a program that computes the amino acid composiiton of a sequence given on
the command line.

Intent: Demonstrate you know how to fill an empty dictionary.

Example:

```
python3 aacomp.py NGTEGKNFYIPMSNKTGIVRSPYEYQQYYMVDPMIY
```


## Birthday Paradox ##

Write a simulation of the birthday paradox. That is, given a classroom of size
X, what is the probability that two people share the same birthday? The size of
the classroom must be a command line parameter.

Intent: Demonstrate your ability to use a combination of loops, conditionals,
and arrays to perform moderately complex logic

Example:

```
python3 birthday.py 23
```

## Swap Columns ##

Write a program that reads a tabular text file and swaps the first two columns.

Intent: Demonstrate you can read a text file and split it into fields.

Example:

```
python3 swap.py whatever
```

## IPC ##

Write a program that runs your AA Composition program (from above), captures the
output, and reports the most and least common amino acid. You must store the
data internally in a dictionary.

Intent: Demonstrate you can run other programs and read their output. Also, that
you know how to sort a dictionary.

Example:
```
python3 ipc.py
```


## FASTA File ##

Write a function to read FASTA files and put it in a library.

Intent: Demonstrate you know how to use a library and also to parse a common
file format.


## Position Weight Matrix ##

Given a FASTA file of sequences, create a representative PWM. Use your library
file from above.

Intent: Demonstrate you know how to build and navigate a 2-dimensional data
structure.


## Entropy Filter ##

Write a complexity filter for nucleotide sequences. The program must use
argparse. There must be a positional argument for the fasta file and named
parameters for window size and entropy threshold. The named parameters must have
default values. The program must be executable from anywhere on your computer.

Intent: Demonstrate you know how to create a proper Unix program.
