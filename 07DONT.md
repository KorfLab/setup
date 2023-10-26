Plase Don't
===========

+ Don't copy-paste code
+ Don't attach large files to emails
+ Don't use pixel graphics
+ Don't take screenshots with your phone
+ Don't run a job without estimating resources

## Copy-Paste ##

If you want to improve your coding skills, write code. If you want to improve
your copy-paste skills, copy-paste. Every time you copy-paste code instead of
typing, brain cells die.

## Email Attachments ##

Please don't send large email attachments. If you must send someone data via
email, always compress it first. The better way to share data is to send a URL
to a file or directory in the cloud (Google Drive, Dropbox, Box, Mega, etc).

## Pixel Graphics ##

Image formats like GIF, HEIC, JPG, PNG, and TIFF store graphics as pixels. They
don't scale well and can take up enormous amounts of storage. It's much better
to make graphics in vector format (e.g. SVG, Illustrator). PDF can be a mixture
of formats, so don't be fooled into thinking that PDF is vector.

## Screenshots ##

Screenshots are rarely necessary. If you're working in a terminal and get an
error message, you can copy-paste the error message into Slack or whatever
(it's okay to copy-paste error messages, but not code). Screenshots use a lot
more storage. If you take a picture with you phone, the file may be really
large. Even though computers today have lots of storage, it's always a good
idea to be mindful of how much space things take.

## Resources ##

There are 4 resources on a computer.

+ CPUs
+ Memory
+ Disk
+ Network

Before you run a big job, you should be able to estimate how much of each
resource will be required. If you don't know how much, you shouldn't run the
job. To gain appreciation for each resource, use `top` to monitor smaller jobs.

CPUs are the easiest resource to share. Even a single CPU can run multiple
jobs. Memory isn't easily shared. If you use all the memory, the machine will
become sluggish or unusable for all users. Using up all of a disk will prevent
anyone on the same filesystem from writing their files. If you fill up the
space on the OS disk, you can kill the machine for all users. Network usually
isn't a problem, but if you set up hundreds of jobs with high I/O needs, you
can saturate a network and everyone will hate you.