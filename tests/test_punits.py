import pytest

import punits


class TestFindUnitCode:
    def test_known_unit(self):
        test_data = [
            ("mass", "lbs", "lb"),
            ("length", "inch", "in"),
            ("length", "metre", "m"),
            ("length", "meter", "m"),
            ("volume", "fl. oz.", "oz"),
            ("volume", "imp. cups", "imp cup"),
            ("data", "bits", "b"),
            ("data", "kB", "kB"),
        ]
        for measure, unit, expected in test_data:
            assert punits.find_unit_code(measure, unit) == expected

    def test_unknown_unit(self):
        test_data = [
            ('length', 'inche'),
            ('volume', 'lit'),
            ('mass', 'pond'),
            ('data', 'vB'),
        ]
        for measure, unit in test_data:
            with pytest.raises(punits.UnknownUnitException):
                punits.find_unit_code(measure, unit)


class TestPunits:
    def test_valid(self):
        # Invocations with required parameters
        test_data = [
            ('length', 'in', 'ft', [32], {}, [2.666666666666667]),
            ('length', 'mi', 'm', [0.25], {}, [402.336]),
            ('length', 'cm', 'yd', [78.4], {}, [0.8573928258967629]),

            # px conversion
            ('length', 'px', 'cm', [208], {'dpi': 300}, [1.7610666666666666]),
            ('length', 'px', 'cm', [562], {'dpi': 720}, [1.982611111111111]),
            ('length', 'cm', 'px', [1.761067], {'dpi': 300},
             [208.00003937007872]),

            ('data', 'KiB', 'nibble', [287.8], {}, [589414.4]),
            ('volume', 'imp gal', 'tbsp', [4.23], {}, [1300.4846553306973]),
            ('mass', 'oz', 'mg', [8.1], {}, [229631.13731249998]),
        ]
        for (measure, src_unit_code, target_unit_code, values,
             params, expected) in test_data:
            assert punits.punits(measure, src_unit_code, target_unit_code,
                                 values, params) == expected

    def test_missing_param(self):
        # Invocations that raise exception due to missing parameters
        test_data = [
            ('length', 'px', 'm', [562], {'no_dpi': 720}),
        ]
        for (measure, src_unit_code, target_unit_code,
             values, params) in test_data:
            with pytest.raises(punits.MissingParameterException):
                punits.punits(measure, src_unit_code, target_unit_code,
                              values, params)


class TestGetFactor:
    def test_linear_units(self):
        # For units that have a linear relationship
        test_data = [
            ('length', 'm', 'cm', 0.01),
        ]
        for measure, src_unit_code, target_unit_code, expected in test_data:
            assert punits.get_factor(measure, src_unit_code,
                                     target_unit_code) == expected

    def test_non_linear_units(self):
        # For units that do not have a linear relationship
        test_data = [
            ('temperature', 'C', 'F'),
        ]
        for measure, src_unit_code, target_unit_code in test_data:
            assert punits.get_factor(measure, src_unit_code,
                                     target_unit_code) is None


def test_to_from_base():
    test_data = [
        ('length', 'mm', 'to', 123, {}, 0.123),
    ]
    for measure, unit_code, to_from, value, params, expected in test_data:
        assert punits.to_from_base(measure, unit_code, to_from,
                                   value, params) == expected
