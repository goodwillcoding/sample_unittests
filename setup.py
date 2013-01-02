# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (c) 2008-2011 Michael R.
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt.  A copy of the license should accompany
# this distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE
#
###############################################################################

import os
import sys

from setuptools import setup
from setuptools import find_packages


PACKAGE_NAME = u"sample_unittests"
PACKAGE_NAME_PRETTY = u"SampleUnittest"
PACKAGE_VERSION = u"0.1"
PACKAGE_VERSION_TAG = u"dev"
PACKAGE_VERSION_FULL = u"%s%s" % (PACKAGE_VERSION, PACKAGE_VERSION_TAG)
PACKAGE_DESC = u"Sample Unittests"
PACKAGE_URL = u"http://github.com/goodwillcoding/sample_unittests"
PACKAGE_LICENSE = u"BSD",
PACKAGE_AUTHOR = u"Michael R"


here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''

# install requires
install_requires = [
    'nose',
    'coverage',
    'nosexcover',
    ]

# testing requires
tests_require = [
    ]


# testing extras are used in a command
testing_extras = tests_require + [
    'ipython',
    'ipdb'
    ]

# documentation generation requires
docs_extras = [
    'docutils'
    ]


def main():

    setup(
        name=PACKAGE_NAME,
        version=PACKAGE_VERSION_FULL,
        description=PACKAGE_DESC,
        long_description=README + '\n\n' + CHANGES,
        classifiers=[
            "Intended Audience :: Developers",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.7",
            "Intended Audience :: Developers",
            "Environment :: Console",
            "Topic :: Software Development :: Testing",
            "License :: OSI Approved :: BSD License",
            ],
        keywords='unittests',
        author=PACKAGE_AUTHOR,
        author_email="me@example.com",
        url=PACKAGE_URL,
        license=PACKAGE_LICENSE,
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        install_requires=install_requires,
        extras_require={
            'testing': testing_extras,
            'docs': docs_extras,
            },
        tests_require=tests_require,
        test_suite="sample_unittests.tests",
        entry_points={}
        )

if __name__ == '__main__':
    main()
