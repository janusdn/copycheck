# Copyright 2016 Janus Friis Nielsen. All rights reserved.

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import unittest

import copycheck


class BasicTestCase(unittest.TestCase):

    def test_no_ignore(self):
        # copycheck.is_verbose = True
        # copycheck.is_debug = True
        no_files = copycheck.find_missing_copyright(['samples/no_ignore'])
        self.assertEqual(10, len(no_files))

    def test_ignore(self):
        # copycheck.is_verbose = True
        # copycheck.is_debug = True
        no_files = copycheck.find_missing_copyright(['samples/ignore'])
        self.assertEqual(10, len(no_files))

    def test_both(self):
        # copycheck.is_verbose = True
        # copycheck.is_debug = True
        no_files = copycheck.find_missing_copyright(['samples/ignore', 'samples/no_ignore'])
        self.assertEqual(20, len(no_files))

    def test_double_globbing(self):
        # copycheck.is_verbose = True
        # copycheck.is_debug = True
        no_files = copycheck.find_missing_copyright(['samples/double_globbing'])
        self.assertEqual(0, len(no_files))


if __name__ == '__main__':
    unittest.main()
