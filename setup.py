"""
For instructions on how to put a package on PyPI:
http://peterdowns.com/posts/first-time-with-pypi.html

To upload a new version to PyPI:
1. Udate `VERSION` below. 
5. Create a tag for new version in git:
    % git tag 0.0.1 -m "Fixed some problems"
    % git tag -n # to verify that new tag is in list
    % git push --tags

6. Register and upload to PyPI Test:
% python setup.py register -r pypitest
% python setup.py sdist upload -r pypitest

7. Register and upload to PyPI Live:
% python setup.py register -r pypi
% python setup.py sdist upload -r pypi

"""

from setuptools import setup, find_packages

MAJOR   = 0
MINOR   = 0
MICRO   = 3
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ]

KEYWORDS = [
        "queue",
        "delay",
        "thread",
        ]

setup(
        name='delayqueue',
        packages=find_packages(),
        version=VERSION,
        description='Thread-safe delay queue class',
        author='Marshall Farrier',
        author_email='marshalldfarrier@gmail.com',
        url='https://github.com/aisthesis/delayqueue',
        download_url=('https://github.com/aisthesis/delayqueue/tarball/' + VERSION),
        keywords=' '.join(KEYWORDS),
        classifiers=CLASSIFIERS,
        )
