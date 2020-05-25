"""
Test cases for code in src/punits/__init__.py
"""

import argparse

import pytest

import punits.app


@pytest.fixture
def parser():
    """
    Fixture returning an argparse.ArgumentParser
    """
    return punits.app.create_parser()


class TestCreateParser:
    def test_valid(self, parser):
        """
        Test cases with valid input
        """
        args = parser.parse_args('mass kg g 2.41 412 0.25'.split())
        assert args.measure == 'mass'
        assert args.src_unit == 'kg'
        assert args.target_unit == 'g'
        assert args.values == [2.41, 412, 0.25]
        assert args.precision == 2

    def test_valid_with_dpi(self, parser):
        """
        Test with --dpi option
        """
        args = parser.parse_args('length cm px 412 -p4 --dpi 400'.split())
        assert args.measure == 'length'
        assert args.src_unit == 'cm'
        assert args.target_unit == 'px'
        assert args.values == [412]
        assert args.precision == 4
        assert args.dpi == 400


class TestMain:
    def test_valid(self):
        args = argparse.Namespace(measure='mass',
                                  src_unit='kg',
                                  target_unit='g',
                                  values=[2, 24.12], dpi=None,
                                  precision=2, verbose=False)
        assert punits.app.main(args) == 0

    def test_valid_with_dpi(self, parser):
        args = argparse.Namespace(measure='mass',
                                  src_unit='kg',
                                  target_unit='g',
                                  values=[2, 24.12],
                                  precision=2, verbose=False,
                                  dpi=200)
        assert punits.app.main(args) == 0

    def test_valid_with_verbose(self, parser):
        args = argparse.Namespace(measure='mass',
                                  src_unit='kg',
                                  target_unit='g',
                                  values=[2, 24.12],
                                  precision=2, verbose=True,
                                  dpi=200)
        assert punits.app.main(args) == 0

    def test_valid_non_linear(self, parser):
        args = argparse.Namespace(measure='temperature',
                                  src_unit='C',
                                  target_unit='F',
                                  values=[24.12],
                                  precision=2, verbose=True,
                                  dpi=None)
        assert punits.app.main(args) == 0

    def test_invalid(self):
        args = argparse.Namespace(measure='mass',
                                  src_unit='dunno',
                                  target_unit='g',
                                  values=[2, 24.12],
                                  precision=2, verbose=False,
                                  dpi=200)
        assert punits.app.main(args) == 1
