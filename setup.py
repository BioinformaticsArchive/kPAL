import sys
from setuptools import setup

if sys.version_info < (2, 6):
    raise Exception('kMer requires Python 2.6 or higher.')

# Todo: How does this play with pip freeze requirement files?
requires = ['Bio']

# Python 2.6 does not include the argparse module.
try:
    import argparse
except ImportError:
    requires.append('argparse')

import kMer as distmeta

setup(
    name='kMer',
    version=distmeta.__version__,
    description='k-mer analysis toolkit and programming library.',
    long_description=distmeta.__doc__,
    author=distmeta.__author__,
    author_email=distmeta.__contact__,
    url=distmeta.__homepage__,
    license='MIT License',
    platforms=['any'],
    packages=['kMer'],
    requires=requires,
    entry_points = {
        'console_scripts': ['kMer = kMer.kMer:main']
        },
    classifiers = [
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        ],
    keywords='bioinformatics'
)
