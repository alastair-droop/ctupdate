#!/usr/bin/env python
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

version = '1.1 (2016-07-01)'

import sys
import os
import os.path
import time
import argparse

# Get the version from the installed version.py file:
version = {}
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'version.py')) as f: exec(f.read(), version)

def error(msg):
    sys.stderr.write('ERROR: {0}\n'.format(msg))
    sys.exit(1)

def message(msg):
    if args.silent != True:
        print(msg)

def main():
    # Make sure we have an input function even in old python:
    try: input = raw_input
    except NameError: pass

    parser = argparse.ArgumentParser(description = 'Update file ctimes')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s {0}'.format(version['__version__']))
    parser.add_argument('-s', '--silent', action='store_true', help='Do not provide output')
    action_group = parser.add_mutually_exclusive_group(required=False)
    action_group.add_argument('-l', '--list', action='store_true', help='List files without updating')
    action_group.add_argument('-i', '--interactive', action='store_true', help='Ask before updating each file')
    parser.add_argument(dest='file_list', metavar='<file list>', type=argparse.FileType('rt'), help='File list to update')
    args = parser.parse_args()

    for line in args.file_list.readlines():
        fname = line.strip()
        if os.path.exists(fname) == False:
            message('{0} does not exist'.format(fname))
            continue
        try:
            old_ctime = os.path.getctime(fname)
            fstat = os.stat(fname)
            if args.list == True: print('[{0}] {1}'.format(time.ctime(old_ctime), fname))
            else:
                if args.interactive == True:
                    while True:
                        res = input('update {0}?: '.format(fname)).lower().strip()
                        if res == '': res = 'n'
                        if res in 'ynca': break
                    if res == 'c': raise KeyboardInterrupt()
                    if res == 'n': continue
                    if res == 'a': args.interactive = False
                os.utime(fname, (fstat.st_atime, fstat.st_mtime))
                new_ctime = os.path.getctime(fname)
                message('[{0} -> {1}] {2}'.format(time.ctime(old_ctime), time.ctime(new_ctime), fname))
        except KeyboardInterrupt: sys.exit(0)
        except: error('could not set ctime for "{0}"'.format(fname))
