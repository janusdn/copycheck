# Copyright 2016 Janus Friis Nielsen. All rights reserved.

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


import io
from setuptools import setup, find_packages

about = {}
with open('copycheck/__about__.py') as f:
    exec(f.read(), about)

packages = [
    about['__title__'],
]

# Read readme and changes files.
with io.open('README.rst', mode='r', encoding='UTF-8') as fh:
    readme = fh.read().strip()
with io.open('CHANGELOG.rst', mode='r', encoding='UTF-8') as fh:
    changes = fh.read().strip()

setup(
    name=about['__title__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    description=about['__description__'],
    long_description=readme + "\n\n" + changes,
    setup_requires=['setuptools_scm'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Utilities',
    ],
    license=about['__license__'],
    packages=find_packages(exclude=['samples', 'tests']),
    test_suite='tests',
    entry_points={
        'console_scripts': ['copycheck = copycheck.__init__:main'],
    },
    keywords=about['__keywords__'],
    install_requires=['pathspec'],
)


# # Always prefer setuptools over distutils
# from setuptools import setup, find_packages
# # To use a consistent encoding
# from codecs import open
# from os import path

# import sys
# if not sys.version_info[0] == 3:
#     sys.exit("Sorry, Python 2 is not supported (yet)")


# here = path.abspath(path.dirname(__file__))

# # Get the long description from the README file
# with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
#     long_description = f.read()

# about = {}
# with open('copycheck/__about__.py') as f:
#     exec(f.read(), about)

# packages = [
#     about['__title__'],
# ]

# setup(
#     name=about['__title__'],
#     version=about['__version__'],
#     license=about['__license__'],
#     description=about['__description__'],

#     use_scm_version=True,

#     setup_requires=['setuptools_scm'],

#     long_description=long_description,

#     url=about['__url__'],

#     # Author details.
#     author=about['__author__'],
#     author_email=about['__author_email__'],
#     maintainer=about['__maintainer__'],
#     maintainer_email=about['__maintainer_email__'],

#     entry_points={
#         'console_scripts': ['copycheck = copycheck.__init__:main'],
#     },

#     # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
#     classifiers=[
#         # How mature is this project? Common values are
#         #   3 - Alpha
#         #   4 - Beta
#         #   5 - Production/Stable
#         'Development Status :: 5 - Production/Stable',

#         # Indicate who your project is intended for
#         'Intended Audience :: Developers',
#         'Topic :: Software Development :: Build Tools',

#         # Pick your license as you wish (should match "license" above)
#         'License :: Other/Proprietary License',

#         # Specify the Python versions you support here. In particular, ensure
#         # that you indicate whether you support Python 2, Python 3 or both.
#         'Programming Language :: Python :: 3.5',
#     ],

#     # What does your project relate to?
#     keywords='Copyright check',

#     # You can just specify the packages manually here if your project is
#     # simple. Or you can use find_packages().
#     packages=find_packages(exclude=['contrib', 'docs', 'tests']),

#     # List run-time dependencies here.  These will be installed by pip when
#     # your project is installed. For an analysis of "install_requires" vs pip's
#     # requirements files see:
#     # https://packaging.python.org/en/latest/requirements.html
#     install_requires=['pathspec'],

# )
