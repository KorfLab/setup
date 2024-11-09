Style Guide
===========

In general, we follow the style guides of the languages we write in.

## General ##

+ 80 column rule (lines should be less than 80 characters)
+ Use tabs for left-side indentation and spaces everywhere else
+ Don't hard-code file or directory paths
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

+ Don't use function annotations
+ Don't use dunders
+ Don't use decorators

## C ##

+ Indentation is "one true brace" (opening brace on the first line)
+ Constuctors return pointers to structs
