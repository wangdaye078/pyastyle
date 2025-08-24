#!/usr/bin/env python
import os
import sys

from setuptools import setup, Extension

import version

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    long_description = f.read()

astyle_sources = [
    'astyle/src/' + basename + '.cpp'
    for basename in ('ASBeautifier', 'ASEnhancer', 'ASFormatter', 'ASResource',
                     'astyle_main')
]

sources = ['src/pyastyle.cc']
sources.extend(astyle_sources)

if sys.platform != 'win32':
    extra_compile_args = '-W -Wall -fno-rtti -fno-exceptions'.split()
else:
    extra_compile_args = []

if sys.platform == 'win32':
    extra_compile_args.extend(['/EHsc', '/std:c++17'])


module = Extension(
    'pyastyle',
    define_macros=[('ASTYLE_LIB', 1), ('ASTYLE_STATIC', 1),
                   ('ASTYLE_NO_EXPORTS', 1)],
    include_dirs=['astyle/src'],
    sources=sources,
    language='c++',
    extra_compile_args=extra_compile_args,
)


setup(
    name="pyastyle",
    version=version.get_version(),

    description='Python wrapper extension for Artistic Style',
    long_description=long_description,

    author="Timon Wong",
    author_email="timon86.wang@gmail.com",
    url="https://github.com/timonwong/pyastyle",

    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
    ],

    zip_safe=False,
    ext_modules=[module],
)
