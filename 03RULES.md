Rules
=====

These might be called "best practices" except they are too important for that.

- Rule #1: Create Dev Data
- Rule #2: Everything is Portable
- Rule #3: All Code in GitHub
- Rule #4: Beautifully Simple
- RUle #5: Refactoring Happens
- Rule #6: Don't be a Robot

## Rule #1: Create Dev Data ##

Before you start on a project, the most important thing to do is to build a
minimal dataset for development and testing. We call this our "dev data", "test
set", or "debug set". Dev data is probably not a single file. You should have
data that represents positive and negative controls. Dev data is sometimes
created by hand, sometimes created synthetically, and sometimes sampled from
real data. We use dev data for multiple purposes:

- Minimize debugging time
- Functional tests
- Tutorials

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

Some examples of Rule #1 data are in the `init/data` directory.

## Rule #2: Everything Is Portable ##

Two very important words in science are _rigor_ and _reproducibility_. Science
should be repeatable. One way to ensure that your work can be replicated by
others is to simultaneously develop your software on multiple computers. This
might be a laptop, desktop, cluster, cloud service, or a VM. If you're
wondering how you can you run an analysis inside the minimal VM on your laptop
when it lacks the 5 TB of free space needed... see Rule #1. If you are using
only one computer, you are probably guaranteeing that whatever you're doing is
not reproducible. As scientists, that's sort of unforgivable. Personally, I
bounce between different systems on a daily basis.

- Use Miniforge (conda) to manage your software environment (where possible)
- Never, never, never hard-code paths

## Rule #3: All Code in GitHub ##

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

## Rule #4: Beautifully Simple ##

A programming project has many facets.

- Beautiful - it is visually appealing
- Clear - it is easy to explain to others
- Clever - it is intellectually appealing
- Correct - it solves the problem as intended
- Documented - it has documents for developers
- Efficient - it doesn't use much memory
- Extensible - it can be used for other projects
- Fast - it doesn't take long to run
- Friendly - it has documents for users, including a tutorial
- Novel - it is the first of its kind
- Robust - it has unit, functional, and integration tests
- Simple - it is not complex

Biologists focus on their program being correct. They have a specific problem
to solve and want a solution to that problem. Being so focused on their
problem, they tend to lose sight of the bigger picture that involves other
users and other developers.

Computer scientists focus their efforts on being clever, efficient, and novel.
Their goal is to prove how smart they are. They might not care about users or
other developers.

Software engineers focus on building robust and extensible systems. They may
spend so much effort engineering the perfect abstraction that they miss their
target audience.

Scientific programming exists in an environment with transient users and
developers. Code must be developed in such a way that new users and new
developers can deploy and extend the project. If you can describe your software
as "beautifully simple" then you will have solved most of the difficult
problems. Beautifully simple code is easy to understand. This makes it easy to
debug and extend. When making programming choices, don't program for yourself,
but rather the less experienced person who comes after.

## Rule #5: Refactoring Happens ##

No code is correct the first time it is written. Oftentimes, we only know how
to start a project after we have gotten to the end. For this reason, it's a
good idea to push some small part of the project as far as possible before the
refactoring begins. Don't spend too much time up front engineering the perfect
solution. Odds are, you didn't understand the question perfectly and you're
going to have to do a ground-zero rewrite. The more over-engineering you do at
the start, the more painful it will be to tear it all down later.

This doesn't mean you're encouraged to write shitty code. You should always
strive to write code you are proud of. If you can't show your code to the PI
and say "isn't this great?" then re-write it and make it great.

## Rule #6: Don't be a Robot ##

- Do you find yourself copy-pasting argparse from one program to another?
- Have you forgotten how to write a simple windowing algorithm?
- Do you have to look up the syntax of a `lambda` function every time?
- Are you just the go-between from an LLM to your text editor?
- Have you become a robot?

Well stop doing it. Stop copy-pasting code. Stop looking up everthing on the
Internet. Stop asking ChatGPT for answers. Stop using code completion. Use your
brain. Write every character of every line yourself, and when you get stuck as
a person for help. Yes, this will take longer. But you're here to learn, not to
act like a robot.
