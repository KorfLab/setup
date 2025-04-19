Style Guide
===========

In general, we follow the style guides of the languages we write in.

## General ##

These "rules" apply to all languages:

+ Don't use language-specific constructs just because you can
+ Follow the 80 column rule (lines should be less than 80 characters)
+ Variables are nouns, functions are verbs
+ The larger the scope of a variable, the longer the name
+ The larger the scope of a function, the shorter the name
+ Use tabs for left-side indentation unless the language says NO
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

Follow the Python style guide as much as possible, but if you're working in the
KorfLab codebase, indent with tabs, not spaces. In addition, follow these
"rules".

+ Use `argparse` for CLI.
+ Documentation > annotations > comments
+ Limit `if __name__ == '__main__'` to specific use cases
	- For testing code, but then why not actual unit tests?
	- For multi-processing, but then why not a faster language?
+ Limit dunders and decorators to where they are necessary
+ Limit vertical inheritence to 1 level

Libraries from external sources are generally installed with `pip3` but
libraries we develop aren't typically distributed that way (although they
should). Instead, libraries are stored locally (e.g. a symlink in `~/Code/lib`)
and found by python via `PYTHONPATH`.

## R ##

Use the latest tidyverse style guide with Google supplements.

+ Use snake_case for variables and MixedCase for functions
+ Use tibbles instead of data.frames
+ Don't use row names, but since you're using tibbles you can't, right?
+ Since you're using tibbles, use tidyverse for **everything**
+ Oh, you're using $ or ~? FFS, use tidyverse!

### Scripts and Programs ###

Scripts and programs are generally synonymous. A script that is used very often
might as well be called a program. In this case, drop the suffix, add an
interpreter directive, give it executable permissions, and put it in your PATH.

### Testing ###

We prefer...

### Documentation ###

We prefer...

## C ##

+ Indentation is "one true brace" (opening brace on the first line)
+ Constuctors return pointers to structs
+ Always use a Makefile
