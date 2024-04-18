from conversions.conversion_frame import ConversionFrame
import math

class ConvertPressure:
    units = [
            "pascal",
            "kilopascal",
            "megapascal",
            "bar",
            "millibar",
            "atmosphere",
            "torr",
            "pound_per_square_inch",
            "inch_of_mercury",
            "millimeter_of_mercury",
            "psi",
            "millimeter_of_water",
            "hectopascal",
            "millitorr",
        ]
    def __init__(self, value=None):
        self.value = value
        self.unit_symbols = {
            "pascal": "Pa",
            "kilopascal": "kPa",
            "megapascal": "MPa",
            "bar": "bar",
            "millibar": "mbar",
            "atmosphere": "atm",
            "torr": "Torr",
            "pound_per_square_inch": "psi",
            "inch_of_mercury": "inHg",
            "millimeter_of_mercury": "mmHg",
            "psi": "psi",
            "millimeter_of_water": "mmH2O",
            "hectopascal": "hPa",
            "millitorr": "mTorr",
        }
        self.conversions = {
            "pascal": {
                "pascal": lambda x: x,
                "kilopascal": lambda x: x * 0.001,
                "megapascal": lambda x: x * 1e-6,
                "bar": lambda x: x * 1e-5,
                "millibar": lambda x: x * 0.01,
                "atmosphere": lambda x: x * 9.8692e-6,
                "torr": lambda x: x * 0.00750062,
                "pound_per_square_inch": lambda x: x * 0.000145038,
                "inch_of_mercury": lambda x: x * 0.000295299,
                "millimeter_of_mercury": lambda x: x * 0.00750062,
                "psi": lambda x: x * 0.000145038,
                "millimeter_of_water": lambda x: x * 0.101972,
                "hectopascal": lambda x: x * 0.01,
                "millitorr": lambda x: x * 7.50062e-3,
            },
            "kilopascal": {
                "pascal": lambda x: x * 1000,
                "kilopascal": lambda x: x,
                "megapascal": lambda x: x * 0.001,
                "bar": lambda x: x * 0.01,
                "millibar": lambda x: x * 10,
                "atmosphere": lambda x: x * 0.00986923,
                "torr": lambda x: x * 7.50062,
                "pound_per_square_inch": lambda x: x * 0.145038,
                "inch_of_mercury": lambda x: x * 0.295299,
                "millimeter_of_mercury": lambda x: x * 7.50062,
                "psi": lambda x: x * 0.145038,
                "millimeter_of_water": lambda x: x * 101.972,
                "hectopascal": lambda x: x * 10,
                "millitorr": lambda x: x * 7500.62,
            },
            "megapascal": {
                "pascal": lambda x: x * 1e6,
                "kilopascal": lambda x: x * 1000,
                "megapascal": lambda x: x,
                "bar": lambda x: x * 10,
                "millibar": lambda x: x * 10000,
                "atmosphere": lambda x: x * 0.00986923,
                "torr": lambda x: x * 7500.62,
                "pound_per_square_inch": lambda x: x * 145.038,
                "inch_of_mercury": lambda x: x * 295.299,
                "millimeter_of_mercury": lambda x: x * 7500.62,
                "psi": lambda x: x * 145.038,
                "millimeter_of_water": lambda x: x * 101972,
                "hectopascal": lambda x: x * 10000,
                "millitorr": lambda x: x * 750062,
            },
            "bar": {
                "pascal": lambda x: x * 1e5,
                "kilopascal": lambda x: x * 100,
                "megapascal": lambda x: x * 0.1,
                "bar": lambda x: x,
                "millibar": lambda x: x * 1000,
                "atmosphere": lambda x: x * 0.987,
                "torr": lambda x: x * 750.062,
                "pound_per_square_inch": lambda x: x * 14.5038,
                "inch_of_mercury": lambda x: x * 29.5299,
                "millimeter_of_mercury": lambda x: x * 750.062,
                "psi": lambda x: x * 14.5038,
                "millimeter_of_water": lambda x: x * 10197.2,
                "hectopascal": lambda x: x * 1000,
                "millitorr": lambda x: x * 750062,
            },
            "millibar": {
                "pascal": lambda x: x * 100,
                "kilopascal": lambda x: x * 0.1,
                "megapascal": lambda x: x * 1e-4,
                "bar": lambda x: x * 0.001,
                "millibar": lambda x: x,
                "atmosphere": lambda x: x * 9.8692e-4,
                "torr": lambda x: x * 0.750062,
                "pound_per_square_inch": lambda x: x * 0.0145038,
                "inch_of_mercury": lambda x: x * 0.0295299,
                "millimeter_of_mercury": lambda x: x * 0.750062,
                "psi": lambda x: x * 0.0145038,
                "millimeter_of_water": lambda x: x * 10.1972,
                "hectopascal": lambda x: x * 0.1,
                "millitorr": lambda x: x * 75.0062,
            },
            "atmosphere": {
                "pascal": lambda x: x * 101325,
                "kilopascal": lambda x: x * 101.325,
                "megapascal": lambda x: x * 0.101325,
                "bar": lambda x: x * 1.01325,
                "millibar": lambda x: x * 1013.25,
                "atmosphere": lambda x: x,
                "torr": lambda x: x * 760,
                "pound_per_square_inch": lambda x: x * 14.6959,
                "inch_of_mercury": lambda x: x * 29.9213,
                "millimeter_of_mercury": lambda x: x * 760,
                "psi": lambda x: x * 14.6959,
                "millimeter_of_water": lambda x: x * 10332.3,
                "hectopascal": lambda x: x * 1013.25,
                "millitorr": lambda x: x * 760000,
            },
            "torr": {
                "pascal": lambda x: x * 133.322,
                "kilopascal": lambda x: x * 0.133322,
                "megapascal": lambda x: x * 1.33322e-4,
                "bar": lambda x: x * 0.00133322,
                "millibar": lambda x: x * 1.33322,
                "atmosphere": lambda x: x * 0.00131579,
                "torr": lambda x: x,
                "pound_per_square_inch": lambda x: x * 0.0193368,
                "inch_of_mercury": lambda x: x * 0.0393701,
                "millimeter_of_mercury": lambda x: x,
                "psi": lambda x: x * 0.0193368,
                "millimeter_of_water": lambda x: x * 13.5951,
                "hectopascal": lambda x: x * 1.33322,
                "millitorr": lambda x: x * 1,
            },
            "pound_per_square_inch": {
                "pascal": lambda x: x * 6894.76,
                "kilopascal": lambda x: x * 6.89476,
                "megapascal": lambda x: x * 0.00689476,
                "bar": lambda x: x * 0.0689476,
                "millibar": lambda x: x * 68.9476,
                "atmosphere": lambda x: x * 0.0680459,
                "torr": lambda x: x * 51.7149,
                "pound_per_square_inch": lambda x: x,
                "inch_of_mercury": lambda x: x * 2.03602,
                "millimeter_of_mercury": lambda x: x * 51.7149,
                "psi": lambda x: x,
                "millimeter_of_water": lambda x: x * 703.069,
                "hectopascal": lambda x: x * 68.9476,
                "millitorr": lambda x: x * 51714.9,
            },
            "inch_of_mercury": {
                "pascal": lambda x: x * 3386.39,
                "kilopascal": lambda x: x * 3.38639,
                "megapascal": lambda x: x * 0.00338639,
                "bar": lambda x: x * 0.0338639,
                "millibar": lambda x: x * 33.8639,
                "atmosphere": lambda x: x * 0.0334211,
                "torr": lambda x: x * 25.4,
                "pound_per_square_inch": lambda x: x * 0.491154,
                "inch_of_mercury": lambda x: x,
                "millimeter_of_mercury": lambda x: x * 25.4,
                "psi": lambda x: x * 0.491154,
                "millimeter_of_water": lambda x: x * 345.315,
                "hectopascal": lambda x: x * 33.8639,
                "millitorr": lambda x: x * 25400,
            },
            "millimeter_of_mercury": {
                "pascal": lambda x: x * 133.322,
                "kilopascal": lambda x: x * 0.133322,
                "megapascal": lambda x: x * 1.33322e-4,
                "bar": lambda x: x * 0.00133322,
                "millibar": lambda x: x * 1.33322,
                "atmosphere": lambda x: x * 0.00131579,
                "torr": lambda x: x,
                "pound_per_square_inch": lambda x: x * 0.0193368,
                "inch_of_mercury": lambda x: x * 0.0393701,
                "millimeter_of_mercury": lambda x: x,
                "psi": lambda x: x * 0.0193368,
                "millimeter_of_water": lambda x: x * 13.5951,
                "hectopascal": lambda x: x * 1.33322,
                "millitorr": lambda x: x * 1,
            },
            "psi": {
                "pascal": lambda x: x * 6894.76,
                "kilopascal": lambda x: x * 6.89476,
                "megapascal": lambda x: x * 0.00689476,
                "bar": lambda x: x * 0.0689476,
                "millibar": lambda x: x * 68.9476,
                "atmosphere": lambda x: x * 0.0680459,
                "torr": lambda x: x * 51.7149,
                "pound_per_square_inch": lambda x: x,
                "inch_of_mercury": lambda x: x * 2.03602,
                "millimeter_of_mercury": lambda x: x * 51.7149,
                "psi": lambda x: x,
                "millimeter_of_water": lambda x: x * 703.069,
                "hectopascal": lambda x: x * 68.9476,
                "millitorr": lambda x: x * 51714.9,
            },
            "millimeter_of_water": {
                "pascal": lambda x: x * 9.80665,
                "kilopascal": lambda x: x * 0.00980665,
                "megapascal": lambda x: x * 9.80665e-6,
                "bar": lambda x: x * 9.80665e-5,
                "millibar": lambda x: x * 0.0980665,
                "atmosphere": lambda x: x * 9.67841e-5,
                "torr": lambda x: x * 0.0735569,
                "pound_per_square_inch": lambda x: x * 0.00142233,
                "inch_of_mercury": lambda x: x * 0.002902,
                "millimeter_of_mercury": lambda x: x * 0.0735569,
                "psi": lambda x: x * 0.00142233,
                "millimeter_of_water": lambda x: x,
                "hectopascal": lambda x: x * 0.0980665,
                "millitorr": lambda x: x * 73.5569,
            },
            "hectopascal": {
                "pascal": lambda x: x * 100,
                "kilopascal": lambda x: x * 0.1,
                "megapascal": lambda x: x * 1e-4,
                "bar": lambda x: x * 0.001,
                "millibar": lambda x: x * 1,
                "atmosphere": lambda x: x * 0.000986923,
                "torr": lambda x: x * 0.750062,
                "pound_per_square_inch": lambda x: x * 0.0145038,
                "inch_of_mercury": lambda x: x * 0.0295299,
                "millimeter_of_mercury": lambda x: x * 0.750062,
                "psi": lambda x: x * 0.0145038,
                "millimeter_of_water": lambda x: x * 10.1972,
                "hectopascal": lambda x: x,
                "millitorr": lambda x: x * 7500.62,
            },
            "millitorr": {
                "pascal": lambda x: x * 0.133322,
                "kilopascal": lambda x: x * 1.33322e-4,
                "megapascal": lambda x: x * 1.33322e-7,
                "bar": lambda x: x * 1.33322e-6,
                "millibar": lambda x: x * 0.00133322,
                "atmosphere": lambda x: x * 1.31579e-6,
                "torr": lambda x: x * 0.00133322,
                "pound_per_square_inch": lambda x: x * 1.93368e-5,
                "inch_of_mercury": lambda x: x * 3.93701e-5,
                "millimeter_of_mercury": lambda x: x * 0.00133322,
                "psi": lambda x: x * 1.93368e-5,
                "millimeter_of_water": lambda x: x * 0.0135951,
                "hectopascal": lambda x: x * 0.00133322,
                "millitorr": lambda x: x,
            },
        }

    def get_formula(self, source_unit: str, target_unit: str) -> str:
        source_unit = source_unit.lower()
        target_unit = target_unit.lower()

        formulas = {
            "pascal": {
                "pascal": "x",
                "kilopascal": "x * 0.001",
                "megapascal": "x * 1e-6",
                "bar": "x * 1e-5",
                "millibar": "x * 0.01",
                "atmosphere": "x * 9.8692e-6",
                "torr": "x * 0.00750062",
                "pound_per_square_inch": "x * 0.000145038",
                "inch_of_mercury": "x * 0.000295299",
                "millimeter_of_mercury": "x * 0.00750062",
                "psi": "x * 0.000145038",
                "millimeter_of_water": "x * 0.101972",
                "hectopascal": "x * 0.01",
                "millitorr": "x * 7.50062e-3",
            },
            "kilopascal": {
                "pascal": "x * 1000",
                "kilopascal": "x",
                "megapascal": "x * 0.001",
                "bar": "x * 0.01",
                "millibar": "x * 10",
                "atmosphere": "x * 0.00986923",
                "torr": "x * 7.50062",
                "pound_per_square_inch": "x * 0.145038",
                "inch_of_mercury": "x * 0.295299",
                "millimeter_of_mercury": "x * 7.50062",
                "psi": "x * 0.145038",
                "millimeter_of_water": "x * 101.972",
                "hectopascal": "x * 10",
                "millitorr": "x * 7500.62",
            },
            "megapascal": {
                "pascal": "x * 1e6",
                "kilopascal": "x * 1000",
                "megapascal": "x",
                "bar": "x * 10",
                "millibar": "x * 10000",
                "atmosphere": "x * 0.00986923",
                "torr": "x * 7500.62",
                "pound_per_square_inch": "x * 145.038",
                "inch_of_mercury": "x * 295.299",
                "millimeter_of_mercury": "x * 7500.62",
                "psi": "x * 145.038",
                "millimeter_of_water": "x * 101972",
                "hectopascal": "x * 10000",
                "millitorr": "x * 750062",
            },
            "bar": {
                "pascal": "x * 1e5",
                "kilopascal": "x * 100",
                "megapascal": "x * 0.1",
                "bar": "x",
                "millibar": "x * 1000",
                "atmosphere": "x * 0.987",
                "torr": "x * 750.062",
                "pound_per_square_inch": "x * 14.5038",
                "inch_of_mercury": "x * 29.5299",
                "millimeter_of_mercury": "x * 750.062",
                "psi": "x * 14.5038",
                "millimeter_of_water": "x * 10197.2",
                "hectopascal": "x * 1000",
                "millitorr": "x * 750062",
            },
            "millibar": {
                "pascal": "x * 100",
                "kilopascal": "x * 0.1",
                "megapascal": "x * 1e-4",
                "bar": "x * 0.001",
                "millibar": "x",
                "atmosphere": "x * 9.8692e-4",
                "torr": "x * 0.750062",
                "pound_per_square_inch": "x * 0.0145038",
                "inch_of_mercury": "x * 0.0295299",
                "millimeter_of_mercury": "x * 0.750062",
                "psi": "x * 0.0145038",
                "millimeter_of_water": "x * 10.1972",
                "hectopascal": "x * 0.1",
                "millitorr": "x * 75.0062",
            },
            "atmosphere": {
                "pascal": "x * 101325",
                "kilopascal": "x * 101.325",
                "megapascal": "x * 0.101325",
                "bar": "x * 1.01325",
                "millibar": "x * 1013.25",
                "atmosphere": "x",
                "torr": "x * 760",
                "pound_per_square_inch": "x * 14.6959",
                "inch_of_mercury": "x * 29.9213",
                "millimeter_of_mercury": "x * 760",
                "psi": "x * 14.6959",
                "millimeter_of_water": "x * 10332.3",
                "hectopascal": "x * 1013.25",
                "millitorr": "x * 760000",
            },
            "torr": {
                "pascal": "x * 133.322",
                "kilopascal": "x * 0.133322",
                "megapascal": "x * 1.33322e-4",
                "bar": "x * 0.00133322",
                "millibar": "x * 1.33322",
                "atmosphere": "x * 0.00131579",
                "torr": "x",
                "pound_per_square_inch": "x * 0.0193368",
                "inch_of_mercury": "x * 0.0393701",
                "millimeter_of_mercury": "x",
                "psi": "x * 0.0193368",
                "millimeter_of_water": "x * 13.5951",
                "hectopascal": "x * 1.33322",
                "millitorr": "x",
            },
            "pound_per_square_inch": {
                "pascal": "x * 6894.76",
                "kilopascal": "x * 6.89476",
                "megapascal": "x * 0.00689476",
                "bar": "x * 0.0689476",
                "millibar": "x * 68.9476",
                "atmosphere": "x * 0.0680459",
                "torr": "x * 51.7149",
                "pound_per_square_inch": "x",
                "inch_of_mercury": "x * 2.03602",
                "millimeter_of_mercury": "x * 51.7149",
                "psi": "x",
                "millimeter_of_water": "x * 703.069",
                "hectopascal": "x * 68.9476",
                "millitorr": "x * 51714.9",
            },
            "inch_of_mercury": {
                "pascal": "x * 3386.39",
                "kilopascal": "x * 3.38639",
                "megapascal": "x * 0.00338639",
                "bar": "x * 0.0338639",
                "millibar": "x * 33.8639",
                "atmosphere": "x * 0.0334211",
                "torr": "x * 25.4",
                "pound_per_square_inch": "x * 0.491154",
                "inch_of_mercury": "x",
                "millimeter_of_mercury": "x * 25.4",
                "psi": "x * 0.491154",
                "millimeter_of_water": "x * 345.315",
                "hectopascal": "x * 33.8639",
                "millitorr": "x * 25400",
            },
            "millimeter_of_mercury": {
                "pascal": "x * 133.322",
                "kilopascal": "x * 0.133322",
                "megapascal": "x * 1.33322e-4",
                "bar": "x * 0.00133322",
                "millibar": "x * 1.33322",
                "atmosphere": "x * 0.00131579",
                "torr": "x",
                "pound_per_square_inch": "x * 0.0193368",
                "inch_of_mercury": "x * 0.0393701",
                "millimeter_of_mercury": "x",
                "psi": "x * 0.0193368",
                "millimeter_of_water": "x * 13.5951",
                "hectopascal": "x * 1.33322",
                "millitorr": "x",
            },
            "psi": {
                "pascal": "x * 6894.76",
                "kilopascal": "x * 6.89476",
                "megapascal": "x * 0.00689476",
                "bar": "x * 0.0689476",
                "millibar": "x * 68.9476",
                "atmosphere": "x * 0.0680459",
                "torr": "x * 51.7149",
                "pound_per_square_inch": "x",
                "inch_of_mercury": "x * 2.03602",
                "millimeter_of_mercury": "x * 51.7149",
                "psi": "x",
                "millimeter_of_water": "x * 703.069",
                "hectopascal": "x * 68.9476",
                "millitorr": "x * 51714.9",
            },
            "millimeter_of_water": {
                "pascal": "x * 9.80665",
                "kilopascal": "x * 0.00980665",
                "megapascal": "x * 9.80665e-6",
                "bar": "x * 9.80665e-5",
                "millibar": "x * 0.0980665",
                "atmosphere": "x * 9.67841e-5",
                "torr": "x * 0.0735569",
                "pound_per_square_inch": "x * 0.00142233",
                "inch_of_mercury": "x * 0.002902",
                "millimeter_of_mercury": "x * 0.0735569",
                "psi": "x * 0.00142233",
                "millimeter_of_water": "x",
                "hectopascal": "x * 0.0980665",
                "millitorr": "x * 73.5569",
            },
            "hectopascal": {
                "pascal": "x * 100",
                "kilopascal": "x * 0.1",
                "megapascal": "x * 1e-4",
                "bar": "x * 0.001",
                "millibar": "x * 1",
                "atmosphere": "x * 0.000986923",
                "torr": "x * 0.750062",
                "pound_per_square_inch": "x * 0.0145038",
                "inch_of_mercury": "x * 0.0295299",
                "millimeter_of_mercury": "x * 0.750062",
                "psi": "x * 0.0145038",
                "millimeter_of_water": "x * 10.1972",
                "hectopascal": "x",
                "millitorr": "x * 7500.62",
            },
            "millitorr": {
                "pascal": "x * 0.133322",
                "kilopascal": "x * 1.33322e-4",
                "megapascal": "x * 1.33322e-7",
                "bar": "x * 1.33322e-6",
                "millibar": "x * 0.00133322",
                "atmosphere": "x * 1.31579e-6",
                "torr": "x * 0.00133322",
                "pound_per_square_inch": "x * 1.93368e-5",
                "inch_of_mercury": "x * 3.93701e-5",
                "millimeter_of_mercury": "x * 0.00133322",
                "psi": "x * 1.93368e-5",
                "millimeter_of_water": "x * 0.0135951",
                "hectopascal": "x * 0.00133322",
                "millitorr": "x",
            },
        }
        
        if source_unit in formulas and target_unit in formulas[source_unit]:
            formula = formulas[source_unit][target_unit]
            return formula
        else:
            return "Formule non disponible."

    def convert(self, pressure, original_unit, unit):
        source_unit = original_unit.lower()
        target_unit = unit.lower()

        if (
            source_unit in self.conversions
            and target_unit in self.conversions[source_unit]
        ):
            conversion_func = self.conversions[source_unit][target_unit]
            return conversion_func(pressure)
        else:
            raise ValueError("Unité cible non prise en charge.")
        
class PressureFrame(ConversionFrame):
    def __init__(self, parent, conversion_func, error_callback):
        super().__init__(parent, conversion_func, ConvertPressure.units, error_callback)

