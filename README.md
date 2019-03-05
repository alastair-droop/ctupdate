# ctupdate

This is a simple script that allows batch updates to the [ctime](https://en.wikipedia.org/wiki/Stat_(system_call)#ctime) attribute for all files provided in a given input file.

This is particularly useful when storing files on shared systems that utilise automatic deletion of files "unused" for a certain time.

For an individual file, this has a similar effect to using [`touch`](http://pubs.opengroup.org/onlinepubs/9699919799/utilities/touch.html) to mark the file as modified. However, `ctupdate` will *not* create files that are not present.

## Warning
Many shared HPC systems use a "play fair" agreement for storage space. By updating all your stored files rather than carefully deciding which should be kept and which should be moved elsewhere, you are violating the fair play agreement, and degrading the system utility for all users. This tool is intended for use with small datasets (for example reference sequences) that are frequently used, but are not regularly modified.

***Please think carefully before using this tool to prevent automatic deletion of data that could be moved to other storage locations.***

## Usage

~~~bash
ctupdate [-h] [-v] [-s] [-l | -i] <file>
~~~

The `file` supplied is read line at a time, and if the line is itself a valid filename, the ctime attribute for the referenced file is updated.

* `-h` shows commandline help, and exits
* `-v` shows the program version, and exits
* `-s` suppresses notification messages
* `-l` lists the files, instead of updating them
* `-i` prompts for action for each file. Valid responses are:
  * `y` update the file
  * `n` do not update the file
  * `c` do not update the file, and stop processing the file list
  * `a` update the file and all subsequent files without prompting

The arguments `-l` and `-i` are mutually exclusive.

## Installation

Installation should be as simple as:

~~~bash
git clone https://github.com/alastair-droop/ctupdate.git
cd ctupate
python setup.py install
~~~

If you do not have admin privileges, you can install this locally using `python setup.py install --user`.

After installation, you can verify that you have the correct version using `ctupdate -v`.
