#!/usr/bin/env python
# This is a setuptools plugin that adds a 'trial' command which uses the
# trial script from Twisted to run unit tests instead of pyunit.
# The functionality of this plugin was contributed from
# the Elisa project: http://elisa.fluendo.com/.

import os, re, sys

from setuptools import find_packages, setup
from setuptools_trial.setuptools_trial import TrialTest

trove_classifiers=[
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: BSD License",
    "License :: DFSG approved",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Natural Language :: English",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.4",
    "Programming Language :: Python :: 2.5",
    "Programming Language :: Python :: 2.6",
    "Topic :: Utilities",
    "Topic :: Software Development :: Libraries",
    "Framework :: Setuptools Plugin",
    ]

PKG='setuptools_trial'
VERSIONFILE = os.path.join(PKG, "_version.py")
verstr = "unknown"
try:
    verstrline = open(VERSIONFILE, "rt").read()
except EnvironmentError:
    pass # Okay, there is no version file.
else:
    VSRE = r"^verstr = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        verstr = mo.group(1)
    else:
        print "unable to find version in %s" % (VERSIONFILE,)
        raise RuntimeError("If %s.py exists, it is required to be well-formed." % (VERSIONFILE,))

setup_requires = []

# darcsver is needed only if you want "./setup.py darcsver" to write a new
# version stamp in setuptools_trial/_version.py, with a version number derived from
# darcs history.  http://pypi.python.org/pypi/darcsver
if 'darcsver' in sys.argv[1:]:
    setup_requires.append('darcsver >= 1.0.0')

# setuptools_darcs is required to produce complete distributions (such as with
# "sdist" or "bdist_egg"), unless there is a setuptools_trial.egg-info/SOURCE.txt file
# present which contains a complete list of files that should be included.
# http://pypi.python.org/pypi/setuptools_darcs
setup_requires.append('setuptools_darcs >= 1.1.0')


data_fnames=[ 'README.txt', 'COPYING.SPL.txt' ]

# In case we are building for a .deb with stdeb's sdist_dsc command, we put the
# docs in "share/doc/python-$PKG".
PKG='setuptools_trial'
doc_loc = "share/doc/python-" + PKG
data_files = [(doc_loc, data_fnames)]

setup(
    name=PKG,
    version=verstr,
    author = "Chris Galvan",
    author_email = "cgalvan@enthought.com",
    url='http://allmydata.org/trac/' + PKG,
    description = "Setuptools plugin that makes unit tests execute with trial instead of pyunit.",
    entry_points = {
        'distutils.commands': [
            'trial = setuptools_trial.setuptools_trial:TrialTest',
        ],
    },
    install_requires = ["Twisted >= 2.4.0"],
    setup_requires = setup_requires,
    keywords = "distutils setuptools trial setuptools_plugin",
    license = "BSD",
    packages = find_packages(),
    include_package_data=True,
    data_files=data_files,
    classifiers=trove_classifiers,
    zip_safe = False, # We prefer unzipped for easier access.
    )
