
Rules
=====

These thoughts are important enough that they are called "rules".


Rule #1: Create Test/Dev Data
-----------------------------

Before you start on a project, the most important thing to do is to build a
minimal dataset for development and testing. We call this our "test set" or
"dev set". We do this for several reasons.

+ Minimize debugging time
+ Functional tests
+ Tutorials

Software development takes much more time than you expect. The debugging stage
can be very long. In order to reduce the downtime between debugging sessions,
we need a small data set that can be processed very quickly.

Software changes over time. Even if we make no changes to our code, our
software depends on other software, which may change silently. In order to
ensure that our software continues to produce the same output as before, we
must perform "functional tests" that automatically compare the current output
to the previous, expected output.

When it comes time to distribute our software, there should be a tutorial that
shows how to use the software. The test data is useful here and also to ensure
that the software passes the functional tests at another location.

Making test data can take some time. For example, let's imagine your project
involves RNA-seq on the human genome. What is the proper test set? Not the
entire human genome and 10 RNA-seq libraries. The test set should fit neatly
into the github repository where the code lives. Ideally, the entire repo is
small. Under 100M is good. Under 10M is better. 1M is ideal. Creating a test
set for an RNA-seq project means making a miniaturized version of the human
genome and curating some reads that align to that part of the genome.
Obviously, the region of the genome matters. You probably want some areas with
high coverage and some areas with low coverage. It may take a week to create a
test set. And later, you may have to make a better one. This part of our work
is sort of like making reagents and calibrating instruments. It's a pain but
must be done to ensure reproducibility.


Rule #2: All Code in GitHub
---------------------------

All of the code you write should be managed in a GitHub repository. Generally,
there is no need to make it private.

Code should be documented in Markdown format. Make your Markdown files look
like final versions of documents and not just pre-processor code for HTML.

You should have a small sample of data with your programs for testing purposes.
