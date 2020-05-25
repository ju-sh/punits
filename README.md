# punits

<a href="https://pypi.org/project/punits"><img alt="PyPI" src="https://img.shields.io/pypi/v/punits"></a>
<a href="https://travis-ci.com/ju-sh/punits"><img alt="Build Status" src="https://api.travis-ci.com/ju-sh/punits.svg?branch=master"></a>
<a href="https://github.com/ju-sh/punits/blob/master/LICENSE.md"><img alt="License: MIT" src="https://img.shields.io/pypi/l/punits"></a>

A simple utility to convert values between different units.

<h2>Installation</h2>

You need Python>=3.6 to use punits.

It can be installed from PyPI with pip using

    pip install punits

<h2>Command line usage</h2>

    python3 -m punits <choice> <source-unit> <target-unit> <value-list>

where choice is the kind of units. Allowed values for <choice> are:
 - mass
 - length
 - volume
 - data
 - temperature.

For example, you can use

    python3 -m punits mass lb kg 23 46.2 12.46

to get

    10.43 20.96 5.65

Use `python3 -m punits --help` for more information.

<h2>Usage as module</h2>

The `punits()` function can be used.

Its signature is:

    def punits(measure: str,
               src_unit: str,
               target_unit: str,
               values: List[float],
               params: Optional[dict] = None) -> List[float]

where the `params` argument can be used to pass additional parameters that may be needed (like `dpi` value when conversion is from or to pixesl).

For example,

    >>> punits.punits('temperature', 'K', 'C', [235, 123.2])
    [-38.14999999999998, -149.95]

or

    >>> punits.punits('length', 'px', 'mm', [235, 123.2], {'dpi': 200})
    [29.844999999999995, 15.646400000000002]

