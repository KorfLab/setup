Rules
=====

These might be called "best practices" except they are too important for that.

+ Rule #1: Create Dev Data
+ Rule #2: All Code in GitHub
+ Rule #3: Everything is Portable
+ Rule #4: Prioritize Beauty


Rule #1: Create Dev Data
------------------------

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
places on whatever computer you're using.

If you're a programmer of some kind, which you must be to be in the lab, your
programming activity is part of your CV. Your GitHub profile and activity are
therefore part of your CV.


Rule #3: Everything Is Portable
-------------------------------

Always develop your software and analysis pipelines so that they can be run on
multiple computers. One way to ensure this is to work on several computers in
parallel. This might be a laptop, desktop, cluster, cloud service, or a VM. If
you're wondering how you can you run an analysis inside the minimal VM on your
laptop when it lacks the 5 TB of free space needed... see Rule #1. If you are
using only one computer, you are probably guaranteeing that whatever you're
doing is not reproducible. As scientists, that's sort of unforgivable.
Personally, I bounce between different operating systems on a daily basis.

- Use Miniforge (conda) to manage your software environment (where possible)
- Never hard-code paths


Rule #4: Prioritize Beauty
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
+ Robust - it has unit, functional, and integration tests
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
