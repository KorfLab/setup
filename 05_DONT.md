Plase Don't
===========

- Don't copy-paste code
- Don't indent with spaces
- Don't run a job on a cluster without estimating resources
- Don't attach large files
- Don't use pixel graphics
- Don't take screenshots with your phone
- Don't justify poor practices with "just"
- Don't suffer in silence

## Don't copy-paste ##

If you want to improve your coding skills, write code. If you want to improve
your copy-paste skills, copy-paste. Every time you copy-paste code instead of
typing, brain cells die. You're here to learn, not be a copy-paste robot.

## Don't indent with spaes ##

I don't give a fuck if 4 space indent is preferred in Python, it's not
preferred in this lab. Indent with tabs. If you can't tell the difference
between the two lines below, please learn. If you're reading this on GitHub,
they will look different because GitHub indents by 8. Read this file in your
text editor.

```
while True
	# indented with a tab
    # indented with 4 spaces
```

When wrapping long lines, do not pad to the opening brace.

```
while this_function_is_reall_long_and_has_lots_of_arguments(foo, bar, cat, dog
                                                            cow, pig):
```

## Don't run a job on a cluster without estimating resources ##

There are 5 resources for every job.

- CPUs
- RAM
- Storage
- Network
- Time

If you're about to run a large job on a cluster and don't have an accurate
estimate of how much each resource your job will take, you don't have any
buisness running the job. How do you estimate these? Using `top` or
`/usr/bin/time` with dev data (see Rule #1).

## Don't attach large files ##

Please don't send large attachments in email or team messaging. If you must
send someone data files, always compress it first. The better way to share data
is to send a URL to a file or directory in the cloud (Google Drive, Dropbox,
Box, Mega, etc).

## Don't use pixel graphics ##

Image formats like GIF, HEIC, JPG, PNG, and TIFF store graphics as pixels. They
don't scale well and can take up enormous amounts of storage. It's much better
to make graphics in vector format (e.g. SVG, Illustrator). PDF can be a mixture
of formats, so don't be fooled into thinking that PDF is all vector.

## Don't take screenshots with your phone ##

Screenshots are rarely necessary. If you're working in a terminal and get an
error message, you can copy-paste the text of the error message (it's okay to
copy-paste error messages, but not code). Screenshots use a lot more storage.
If you take a picture with your phone, the file may be really large. Even
though computers today have lots of storage, it's always a good idea to be
mindful of how much space things take.

## Don't justify poor practices with "just" ##

When someone says "I'm not a racist, but..." you know the next thing out of
their mouth will expose their racism. Similarly, when a programmer says "I was
just...", you know they are about to make an excuse for some programming
transgressions like hard-coded paths. Laziness leads to poor programming
practices. Try to code the right way 99% of the time.

## Don't suffer in silence ##

Whether you can't figure out how to debug a random error or anxiety prevents
you from leaving the house, don't suffer alone. Ask for help. Your lab is part
of your family and wants to help you if you give them half a chance.
