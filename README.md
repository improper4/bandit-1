PROJECT MOVED
=============

Bandit development started here, but has moved to the StackForge infrastructure provided by OpenStack.

Please see https://wiki.openstack.org/wiki/Security/Projects/Bandit for more information and links to current source repositories.

The content of this repository remains for historic reasons.

PROJECT MOVED
=============




Bandit
======

A Python AST-based static analyzer from OpenStack Security Group.


Overview
--------
Bandit provides a framework for performing analysis against Python source code,
utilizing the ast module from the Python standard library.

The ast module is used to convert source code into a parsed tree of Python
syntax nodes.  Bandit allows users to define custom tests that are performed
against those nodes.  At the completion of testing, a report is generated that
lists security issues identified within the target source code.


Usage
-----
Example usage across a code tree, showing one line of context for each issue:

    find ~/openstack-repo/keystone -name '*.py' | xargs ./main.py -n 1


Example usage across the examples/ directory, showing three lines of context
and only reporting on the high-severity issues:

    ./main.py examples/*.py -n 3 -lll


Example usage across the examples/ directory, showing one line of context and
running only tests in the ShellInjection profile:

    ./main.py examples/*.py -n 1 -p ShellInjection


Usage:

    $ ./main.py -h
    usage: main.py [-h] [-n CONTEXT_LINES] [-c CONFIG_FILE] [-p PROFILE] [-l]
                   [-o OUTPUT_FILE] [-d]
                   file [file ...]

    Bandit - a Python source code analyzer.

    positional arguments:
      file                  source file/s to be tested

    optional arguments:
      -h, --help            show this help message and exit
      -a AGG_TYPE, --aggregate AGG_TYPE
                            group results by (vuln)erability type or (file) it
                            occurs in
      -n CONTEXT_LINES, --number CONTEXT_LINES
                            number of context lines to print
      -c CONFIG_FILE, --configfile CONFIG_FILE
                            test config file (default: bandit.yaml)
      -p PROFILE, --profile PROFILE
                            test set profile in config to use (defaults to all
                            tests)
      -l, --level           results level filter
      -o OUTPUT_FILE, --output OUTPUT_FILE
                            write report to filename
      -d, --debug           turn on debug mode


Configuration
-------------
The default configuration file is bandit.yaml.  This specifies a number of
global options, and allows the creation of separate test profiles to include
or exclude specific tests when Bandit is run.

Additional configuration files can be created and passed to Bandit as a
command line argument.


Exclusions
----------
In the event that a line of code triggers a Bandit issue, but that the line
has been reviewed and the issue is a false positive or acceptable for some
other reason, the line can be marked with a '# nosec' and any results
associated with it will not be reported.

For example, although this line may cause Bandit to report a potential
security issue, it will not be reported:

    self.process = subprocess.Popen('/bin/echo', shell=True)  # nosec


Vulnerability Tests
-------------------
Vulnerability tests or 'plugins' are defined in files in the plugins directory.

Tests are written in Python and are autodiscovered from the plugins directory.
Each test can examine one or more type of Python statements.  Tests are marked
with the types of Python statements they examine (for example: function call,
string, import, etc).

Tests are executed by the BanditNodeVisitor object as it visits each node in
the AST.  

Test results are maintained in the BanditResultStore and aggregated for output
at the completion of a test run.


Writing Tests
-------------
To write a test:
 - Identify a vulnerability to build a test for, and create a new file in
   examples/ that contains one or more cases of that vulnerability.
 - Consider the vulnerability you're testing for, mark the function with one
   or more of the appropriate decorators:
      - @checks_functions
	  - @checks_imports
	  - @checks_strings
 - Create a new Python source file to contain your test, you can reference
   existing tests for examples.
 - The function that you create should take a parameter "context" which is
   an instance of the context class you can query for information about the
   current element being examined.  You can also get the raw AST node for
   more advanced use cases.  Please see the context.py file for more.
 - Extend your Bandit configuration file as needed to support your new test.
 - Execute Bandit against the test file you defined in examples/ and ensure
   that it detects the vulnerability.  Consider variations on how this
   vulnerability might present itself and extend the example file and the test
   function accordingly.


References
==========

Python AST module documentation: https://docs.python.org/2/library/ast.html

Green Tree Snakes - the missing Python AST docs:
http://greentreesnakes.readthedocs.org/en/latest/

Of specific node, the various types of AST nodes that Bandit currently covers
or could be extended to cover:
http://greentreesnakes.readthedocs.org/en/latest/nodes.html


