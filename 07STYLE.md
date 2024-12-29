Style Guide
===========

In general, we follow the style guides of the languages we write in.

## General ##

+ 80 column rule (lines should be less than 80 characters)
+ Use tabs for left-side indentation and spaces everywhere else
+ Never hard-code file or directory paths
+ Avoid nesting

```
if a:
	if b:
		if c:
			do something

if not a: continue
if not b: continue
if not c: contine
do something
```


## Markdown ##

Your Markdown files should look good as plain text files in any editor or
pager. Markdown is not just pre-processing for HTML, PDF, etc. Markdown is the
primary way we read and write documentation. For this reason, your Markdown
should follow the 80-column rule whenever possible.

## Python ##

Follow the Python style guide as much as possible, but indent with tabs.

+ Don't use function annotations. Write documentation instead.
+ Avoid dunders. Whatever you're doing with them is better solved elsewhere.
+ Use `argparse` always.

### Scripts and Programs ###

Scripts and programs are generally synonymous. A script that is used very often
might as well be called a program. In this case, drop the `.py` suffix, add an
interpreter directive, give it executable permissions, and put it in your PATH.

### Libraries ###

Libraries from external sources are generally installed with `pip3` but
libraries we develop aren't typically distributed that way (although they
should). Instead, libraries are stored locally (e.g. a symlink in `~/Code/lib`)
and found by python via `PYTHONPATH`.

### Classes ###

We don't tend to do a lot of OOP, but here are some recommendations...

### Testing ###

We prefer...

### Documentation ###

We prefer...

## C ##

+ Indentation is "one true brace" (opening brace on the first line)
+ Constuctors return pointers to structs
+ Do you really want to program in C?
