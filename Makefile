# Copyright 2016 Janus Friis Nielsen. All rights reserved.

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

default: pylint
	rm -rf dist
	python setup.py bdist_wheel -d dist/

test:
	python -m unittest tests.committests

pypi_upload:
	twine upload -u ${PYPI_USERNAME} -p ${PYPI_PASSWORD} -r https://pypi.python.org/pypi  -r pypi dist/copycheck-*

testpypi_upload:
	twine upload -p ${PYPI_TEST_PASSWORD} -u infrastructuresepior -r pypitest dist/copycheck-*

pylint:
	pylint copycheck

.PHONY:

clean:
	rm -rf dist
	rm -rf build
	rm -f setuptools_scm-*
	rm -rf copycheck.egg-info/
	/usr/bin/yes | pip uninstall copycheck || true
	pip install --upgrade -r requirements.txt