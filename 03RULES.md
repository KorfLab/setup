Rules
=====

These might be called "best practices" except they are too important for that.

+ Rule #1: Create development data
+ Rule #2: All code in GitHub
+ Rule #3: Prioritize beauty


Rule #1: Create Development Data
--------------------------------

Before you start on a project, the most important thing to do is to build a
minimal dataset for development and testing. We call this our "dev data", "test
set", or "debug set". Dev data is probably not a single file. You should have
data that represents positive and negative controls. Dev data is sometimes
created by hand, sometimes created synthetically, and sometimes sampled from
real data. We use dev data for multiple purposes:

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
to the previous, expected output. Dev data is used during automated testing.

When it comes time to distribute our software, there should be a tutorial that
shows how to use the software. The dev data is useful again here.

Making dev data can take some time. For example, let's imagine your project
involves RNA-seq on the human genome. What is the proper test set? Not the
entire human genome and 10 RNA-seq libraries. The test set should fit neatly
into the git repository where the code lives. Ideally, the entire repo is
small. Under 100M is good. Under 10M is better. Creating a test set for an
RNA-seq project means making a miniaturized version of the human genome and
curating some reads that align to that part of the genome. Obviously, the
region of the genome matters. You probably want some areas with high coverage
and some areas with low coverage. It may take a week or more to create a proper
set of files. And later, you may have to make a better one. It will be worth it
in the long run. This part of our work is sort of like making reagents and
calibrating instruments. It's a pain but must be done to speed up debugging
time and improve reproducibility.


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
+ Documented - it has documents for developers
+ Efficient - it doesn't use much memory
+ Extensible - it can be used for other projects
+ Fast - it doesn't take long to run
+ Friendly - it has documents for users, including a tutorial
+ Novel - it is the first of its kind
+ Robust - it has unit and/or functional tests
+ Simple - it is not complex

Biologists focus on their program being correct. They have a specific problem
to solve and want a solution to that problem. Being so focused on their
problem, they tend to lose sight of the bigger picture that involves other
users and other developers.

Computer scientists focus their efforts on being clever, efficient, and novel.
Their goal is to prove how smart they are. They might not care about users or
other developers.

Scientific programming exists in an environment with transient users and
developers. Code must be developed in such a way that new users and new
developers can deploy and extend the project. Beautiful code is simple, clear,
robust, and extensible. Because beautiful code is easy to understand, it can be
made correct, friendly, and robust, and derivative works can be made efficient,
fast, novel, and clever.


The 10 Commandmants of KorfLab Bioinformatics
=============================================

0. Thou shalt not suck at Unix
1. Thou shalt create dev data
2. Thou shalt manage code via GitHub
3. Thou shalt prioritize beauty
4. Thou shalt openly share your code and data
5. Thou shalt not duplicate data files on a storage device
6. Thou shalt not hard-code paths
7. Thou shalt follow the style guide
8. Thou shalt estimate resources before running large jobs
9. Thou shalt not copy-paste

----

(0) Unix is our lab bench. Use the command line wherever possible, especially
if you're new to Unix/Linux.

(1) Before you start a project, create the datasets that will let you debug and
test your procedures. Some data may be synthetic while others may be subsets of
real data.

(2) Use GitHub to manage your code and track your activity. Your GitHub repos
are part of your CV.

(3) Beautiful code is easy to read, maintain, and improve. Attempts to be
clever often end in inefficient, buggy, and ultimately abandoned code.

(4) We support free open-source software and open data. On the filesystem, your
code should have 644 permissions while data should be 444.

(5) Duplicated data is a waste of space and creates an opportunity to be
edited, and out of sync with the original data. Data should exist in one shared
location and symbolically linked elsewhere when convenience is desired.

(6) Hard-coding directory paths makes software non-portable. Try not to
hard-code anything, but especially directory paths.

(7) Every language has an official style guide. Follow it as much as you can so
that other people can easily follow your code. No, you're not allowed to
completely make up your own style.

(8) Use test data of various sizes to determine the memory footprint and run
time of your job. This will help you understand how your job scales with size
and helps you estimate when it will complete. If you can't estimate how much
resources your job will take, you have no business running it.

(9) Typing code helps you understand what code does. Copy-paste robs you of
that learning experience and is one of the greatest sources of major bugs.
Resist.
