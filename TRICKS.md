TRICKS
======

A collection of random tricks and tips to help you.


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



GitHub
------

To make your GitHub Personal Access Token persist (so you don't have to
copy-paste it again and again).

```
git config --global user.name "username"
git config --global credential.helper store
```
