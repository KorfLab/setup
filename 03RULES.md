Rules
=====

These might be called "best practices" except they are too important for that.

+ Rule #1: Create dev data
+ Rule #2: All code in GitHub
+ Rule #3: Prioritize beauty


Rule #1: Create Dev Data
------------------------

Before you start on a project, the most important thing to do is to build a
minimal dataset for development and testing. We call this our "dev set", "test
set", or "debug set". A dev set is probably not a single file. You should have
data that represents positive and negative controls. Dev sets are sometimes
created by hand, sometimes created synthetically, and sometimes sampled from
real data. We use dev sets for multiple purposes:

+ Minimize debugging time
+ Functional tests
+ Tutorials

Software development takes much more time than you expect. The debugging stage
can be very long. In order to reduce the downtime between debugging sessions,
we need a small data set that can be processed very quickly, and whose outputs
are uncomplicated.

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
into the git repository where the code lives. Ideally, the entire repo is
small. Under 100M is good. Under 10M is better. 1M is ideal. Creating a test
set for an RNA-seq project means making a miniaturized version of the human
genome and curating some reads that align to that part of the genome.
Obviously, the region of the genome matters. You probably want some areas with
high coverage and some areas with low coverage. It may take a week or more to
create a test set. And later, you may have to make a better one. It will be
worth it in the long run. This part of our work is sort of like making reagents
and calibrating instruments. It's a pain but must be done to ensure
reproducibility.


Rule #2: All Code in GitHub
---------------------------

All of the code you write should be managed in a GitHub repository. Generally,
there is no need to make it private.

Code should be documented in Markdown format. Make your Markdown files look
like final versions of documents and not just pre-processor code for HTML.

Every project should have a small sample of data with your programs for testing
purposes (see Rule #1).

Programs belong in git repos. Experimental data should **not** be stored in git
repos. For this reason, your programs and data should be in very different
places on your computer.

If you're a programmer of some kind, which you must be to be in the lab, your
programming activity is part of your CV. Your GitHub profile and activity are
therefore part of your CV. 


Rule #3: Prioritize Beauty
--------------------------

A programming project has many facets.

+ Beautiful - it is visually appealing
+ Clear - it is easy to explain to others
+ Clever - it is intellectually appealing
+ Correct - it solves the problem as intended
+ Documented - it has documents for users and/or developers
+ Efficient - it doesn't use much memory
+ Extensible - it can be used for other projects
+ Fast - it doesn't take long to run
+ Friendly - it is bundled with a tutorial
+ Novel - it is the first of its kind
+ Robust - it has unit and/or functional tests
+ Simple - it is easy to understand

Biologists focus on their program being correct. They have a specific problem
to solve and want a solution to that problem. Being so focused on their problem
they tend to lose sight of the bigger picture that involves other users and
other developers.

Computer scientists focus their efforts on being clever, efficient, and novel.
Their goal is to prove how smart they are. They might not care about users or
other developers.

Scientific programming exists in an environment with transient users and
developers. Code must be developed in such a way that new users and new
developers can deploy and extend the project. Beautiful code is simple, clear,
robust, and extensible. Because beautiful code is easy to understand, it can be
made correct, friendly, and robust, and derivative works can be made efficient,
fast, novel, and clever.


The 10 Commandments of KorfLab Bioinformatics
=============================================

1. Thou shalt openly share your data (444) and code (644)
2. Thou shalt not duplicate data files on a storage device
3. Thou shalt create synthetic and subsetted test data
4. Thou shalt manage all source code via GitHub
5. Thou shalt not hard-code paths
6. Thou shalt follow the style guide
7. Thou shalt perform automated testing
8. Thou shalt use conda for virtual environments and software installation
9. Thou shalt estimate memory and cpu requirements before running large jobs
10. Thou shalt not copy-paste

----

(1) We believe in making both data and source code as free and open as
possible. Sometimes you may have to hold back before publication, but in
general, be open. This lets others learn from us and makes our efforts more
transparent and more robust. On the filesystem, data should not have write
permissions (444) because it might accidentally be edited or deleted. You don't
need to let other people write your files (644) because they already have
access to your code via GitHub.

(2) Duplicated data is a waste of space and creates an opportunity to become
edited, and out of sync with the original data. Data should exist in one shared
location and symbolically linked elsewhere when convenience is desired.

(3) All projects begin with test/dev data. This is data that is just large
enough to test the software under development. Some test data should be
synthetic (made up by you) and some should be subsets of real data (e.g. 1
percent of a genome). Test data is used for development, automated testing, and
tutorials.

(4) All source code should be regularly backed up and managed by revision
control software. GitHub makes this very simple and free.

(5) Hard-coding directory paths makes software non-portable. Try not to
hard-code anything, but especially directory paths.

(6) Every language has an official style guide. Follow it as much as you can so
that other people can easily follow your code.

(7) Unit tests and functional tests are an essential part of robust software
engineering. It's like putting latex gloves on in the lab.

(8) The main reason we use Conda is for reproducibility. Also, installing
software with complex dependancies is a difficult task that conda manages
pretty well. Not all software is available via conda, though, so when you run
into those packages, make very careful notes in your README.

(9) Use test data of various sizes to determine the memory footprint and run
time of your job. This will help you understand how your job scales with size
and helps you estimate when it will complete.

(10) Typing code helps you understand what code does. Copy-paste robs you of
that learning experience and is one of the greatest sources of major bugs.
Resist.
