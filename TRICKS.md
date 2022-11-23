TRICKS
======

A collection of random tricks and tips to help you.

+ Getting `git` to remember your password
+ Inter-process communication in Python and Perl
+ Summing probabilities in log-space


Git password persistence
------------------------

To make your GitHub Personal Access Token persist (so you don't have to
copy-paste it again and again).

```
git config --global user.name "username"
git config --global credential.helper store
```


IPC
---

That stands for interprocess communication. In Perl, if you want to capture the
output of a command and store it in a variable, you simply use backticks. This
works with scalars to store the entire file or with arrays to store
line-by-line.

```
my $thing = `ls -a`
my @stuff = `ls -a`
```

It's a bit more complex to do this in Python.

```
from subprocess import run
stuff = run('ls -a', shell=True, capture_output=True).stdout.decode().split('\n')
```


Summing probabilities in log-space
----------------------------------

Since multiplying probabilities over and over can lead to underflow errors, we 
tend to do math in log-space. Summing log-probabilities can be probematic 
because you can't simply de-log the numbers, sum them, and then return the log. 
Here's one solution, which is to transform the log to a higher power, then do 
the math, then transform back to a lower power. The function below also 
short-circuits and returns the higher number if the numbers are too dissimilar.

```
def sumlogp2(a, b, mag=40):
	assert(a <= 0)
	assert(b <= 0)
	if abs(a - b) > mag: return max(a, b)
	return math.log2(1 + 2**(b - a)) + a
```

Of course, if you're working in Python, you can use `numpy.logaddexp2(a, b)` to 
do the same calculation. But not every language has this built in. Also, the 
numpy version is slightly slower than the pure python.
