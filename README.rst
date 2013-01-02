
Sample Unittests
================

This is an example in code coverage.

Installation
============

Clone the repository ::

    git clone https://github.com/goodwillcoding/sample_unittests.git

Create a virtual environment for this project ::

    cd sample_unittests
    ./virtualenv.py --distribute --prompt=\(sample_unittests\) _venv

Install dependencies and the code in development mode ::

    source _venv/bin/activate
    ./makeme first_setup
    deactivate
    source activate
    me develop

Show coverage
=============

Run ::

    me cover

Coverage Output ::

    Name                                Stmts   Miss  Cover   Missing
    -----------------------------------------------------------------
    sample_unittests                        1      0   100%
    sample_unittests.tests                  1      0   100%
    sample_unittests.tests.test_utils      37      0   100%
    sample_unittests.utils                 23      0   100%
    -----------------------------------------------------------------
    TOTAL                                  62      0   100%
    -----------------------------------------------------------------

Examine the tests
=================

::

  less ./sample_unittests/tests/test_utils.py

As you can see the coverage is 100% even though test for `split_argument2`
do not test such cases as "a=b".
