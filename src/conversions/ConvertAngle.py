from conversions.conversion_frame import ConversionFrame
import math

class ConvertAngle:
    units = ["radian", "degree", "gradian", "minute", "second", "revolution", "mil", "arcsecond"]

    def __init__(self, value=None):
        self.value = value
        self.unit_symbols = {
            "radian": "rad", "degree": "°", "gradian": "grad", "minute": "'", "second": "''",
            "revolution": "rev", "mil": "mil", "arcsecond": "arcsec"
        }
        self.conversions = {
            "radian": {
                "radian": lambda x: x,
                "degree": lambda x: math.degrees(x),
                "gradian": lambda x: x * 200 / math.pi,
                "minute": lambda x: math.degrees(x) * 60,
                "second": lambda x: math.degrees(x) * 3600,
                "revolution": lambda x: x / (2 * math.pi),
                "mil": lambda x: x * (6400 / (2 * math.pi)),
                "arcsecond": lambda x: math.degrees(x) * 3600,
            },
            "degree": {
                "radian": lambda x: math.radians(x),
                "degree": lambda x: x,
                "gradian": lambda x: x * 10 / 9,
                "minute": lambda x: x * 60,
                "second": lambda x: x * 3600,
                "revolution": lambda x: x / 360,
                "mil": lambda x: x * (6400 / 360),
                "arcsecond": lambda x: x * 3600,
            },
            "gradian": {
                "radian": lambda x: x * 200 / math.pi,
                "degree": lambda x: x * 9 / 10,
                "gradian": lambda x: x,
                "minute": lambda x: x * 200 / 9,
                "second": lambda x: x * 200 * 60 / 9,
                "revolution": lambda x: x / 400,
                "mil": lambda x: x * (6400 / 400),
                "arcsecond": lambda x: x * 3600,
            },
            "minute": {
                "radian": lambda x: x * 180 * 60 / math.pi,
                "degree": lambda x: x * 60,
                "gradian": lambda x: x * 9 / (200 * 60),
                "minute": lambda x: x,
                "second": lambda x: x * 60,
                "revolution": lambda x: x / (360 * 60),
                "mil": lambda x: x * (6400 / (360 * 60)),
                "arcsecond": lambda x: x * 3600,
            },
            "second": {
                "radian": lambda x: x * 180 * 3600 / math.pi,
                "degree": lambda x: x * 3600,
                "gradian": lambda x: x * 9 / (200 * 3600),
                "minute": lambda x: x / 60,
                "second": lambda x: x,
                "revolution": lambda x: x / (360 * 3600),
                "mil": lambda x: x * (6400 / (360 * 3600)),
                "arcsecond": lambda x: x,
            },
        }

    def get_formula(self, source_unit: str, target_unit: str) -> str:
        source_unit = source_unit.lower()
        target_unit = target_unit.lower()

        formulas = {
            "radian": {
                "radian": "x",
                "degree": "x * 180 / 3",
                "gradian": "x * 200 / π",
                "minute": "x * 180 * 60 / π",
                "second": "x * 180 * 3600 / π",
                "revolution": "x / (2 * π)",
                "mil": "x * (6400 / (2 * π))",
                "arcsecond": "x * 180 * 3600 / π",
            },
            "degree": {
                "radian": "x * π / 180",
                "degree": "x",
                "gradian": "x * 10 / 9",
                "minute": "x * 60",
                "second": "x * 3600",
                "revolution": "x / 360",
                "mil": "x * (6400 / 360)",
                "arcsecond": "x * 3600",
            },
            "gradian": {
                "radian": "x * π / 200",
                "degree": "x * 9 / 10",
                "gradian": "x",
                "minute": "x * 200 / 9",
                "second": "x * 200 * 60 / 9",
                "revolution": "x / 400",
                "mil": "x * (6400 / 400)",
                "arcsecond": "x * 3600",
            },
            "minute": {
                "radian": "x * π / (180 * 60)",
                "degree": "x / 60",
                "gradian": "x * 9 / (200 * 60)",
                "minute": "x",
                "second": "x * 60",
                "revolution": "x / (360 * 60)",
                "mil": "x * (6400 / (360 * 60))",
                "arcsecond": "x * 3600",
            },
            "second": {
                "radian": "x * π / (180 * 3600)",
                "degree": "x / 3600",
                "gradian": "x * 9 / (200 * 3600)",
                "minute": "x / 60",
                "second": "x",
                "revolution": "x / (360 * 3600)",
                "mil": "x * (6400 / (360 * 3600))",
                "arcsecond": "x",
            },
        }

        if source_unit in formulas and target_unit in formulas[source_unit]:
            formula = formulas[source_unit][target_unit]
            return formula
        else:
            return "Formule non disponible."

    def convert(self, angle, original_unit, unit):
        source_unit = original_unit.lower()
        target_unit = unit.lower()

        if (
            source_unit in self.conversions
            and target_unit in self.conversions[source_unit]
        ):
            conversion_func = self.conversions[source_unit][target_unit]
            try:
                return conversion_func(angle)
            except Exception as e:
                raise ValueError(f"Erreur lors de la conversion : {e}")
        else:
            raise ValueError("Unité cible non prise en charge.")


class AngleFrame(ConversionFrame):
    def __init__(self, parent, conversion_func, error_callback):
        super().__init__(parent, conversion_func, ConvertAngle.units, error_callback)

