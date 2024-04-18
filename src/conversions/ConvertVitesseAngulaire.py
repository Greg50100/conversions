from conversions.conversion_frame import ConversionFrame
import math

class ConvertVitesseAngulaire:
    units = [
            "radian_per_second",
            "revolution_per_minute",
            "degree_per_second",
            "hertz",
            "turn_per_minute",
            "angular_velocity",
        ]
    def __init__(self, value=None):
        self.value = value
        self.conversions = {
            "radian_per_second": {
                "radian_per_second": lambda x: x,
                "revolution_per_minute": lambda x: x * 9.54929658551,
                "degree_per_second": lambda x: x * 57.2957795131,
                "hertz": lambda x: x / (2 * 3.14159265359),
                "turn_per_minute": lambda x: x / (2 * 3.14159265359) * 60,
                "angular_velocity": lambda x: x * 180 / 3.14159265359,
            },
            "revolution_per_minute": {
                "radian_per_second": lambda x: x * 0.10471975512,
                "revolution_per_minute": lambda x: x,
                "degree_per_second": lambda x: x * 6,
                "hertz": lambda x: x / 60,
                "turn_per_minute": lambda x: x,
                "angular_velocity": lambda x: x * 180 / 3.14159265359 / 60,
            },
            "degree_per_second": {
                "radian_per_second": lambda x: x * 0.01745329252,
                "revolution_per_minute": lambda x: x / 6,
                "degree_per_second": lambda x: x,
                "hertz": lambda x: x / 360,
                "turn_per_minute": lambda x: x / 360,
                "angular_velocity": lambda x: x * 180 / 360,
            },
            "hertz": {
                "radian_per_second": lambda x: x * (2 * 3.14159265359),
                "revolution_per_minute": lambda x: x * 60,
                "degree_per_second": lambda x: x * 360,
                "hertz": lambda x: x,
                "turn_per_minute": lambda x: x * 60,
                "angular_velocity": lambda x: x * 180,
            },
            "turn_per_minute": {
                "radian_per_second": lambda x: x * (2 * 3.14159265359) / 60,
                "revolution_per_minute": lambda x: x,
                "degree_per_second": lambda x: x * 360 / 60,
                "hertz": lambda x: x / 60,
                "turn_per_minute": lambda x: x,
                "angular_velocity": lambda x: x * 180 / 60,
            },
            "angular_velocity": {
                "radian_per_second": lambda x: x * 3.14159265359 / 180,
                "revolution_per_minute": lambda x: x * 60 / 180 * 3.14159265359,
                "degree_per_second": lambda x: x * 360 / 180,
                "hertz": lambda x: x / 180,
                "turn_per_minute": lambda x: x * 60 / 180,
                "angular_velocity": lambda x: x,
            },
        }

    def get_formula(self, source_unit: str, target_unit: str) -> str:
        source_unit = source_unit.lower()
        target_unit = target_unit.lower()

        formulas = {
            "radian_per_second": {
                "radian_per_second": "x",
                "revolution_per_minute": "x * 9.54929658551",
                "degree_per_second": "x * 57.2957795131",
                "hertz": "x / (2 * π)",
                "turn_per_minute": "x / (2 * π) * 60",
                "angular_velocity": "x * 180 / π",
            },
            "revolution_per_minute": {
                "radian_per_second": "x * 0.10471975512",
                "revolution_per_minute": "x",
                "degree_per_second": "x * 6",
                "hertz": "x / 60",
                "turn_per_minute": "x",
                "angular_velocity": "x * 180 / π / 60",
            },
            "degree_per_second": {
                "radian_per_second": "x * 0.01745329252",
                "revolution_per_minute": "x / 6",
                "degree_per_second": "x",
                "hertz": "x / 360",
                "turn_per_minute": "x / 360",
                "angular_velocity": "x * 180 / 360",
            },
            "hertz": {
                "radian_per_second": "x * (2 * π)",
                "revolution_per_minute": "x * 60",
                "degree_per_second": "x * 360",
                "hertz": "x",
                "turn_per_minute": "x * 60",
                "angular_velocity": "x * 180",
            },
            "turn_per_minute": {
                "radian_per_second": "x * (2 * π) / 60",
                "revolution_per_minute": "x",
                "degree_per_second": "x * 360 / 60",
                "hertz": "x / 60",
                "turn_per_minute": "x",
                "angular_velocity": "x * 180 / 60",
            },
            "angular_velocity": {
                "radian_per_second": "x * π / 180",
                "revolution_per_minute": "x * 60 / 180 * π",
                "degree_per_second": "x * 360 / 180",
                "hertz": "x / 180",
                "turn_per_minute": "x * 60 / 180",
                "angular_velocity": "x",
            },
        }

        if source_unit in formulas and target_unit in formulas[source_unit]:
            formula = formulas[source_unit][target_unit]
            return formula
        else:
            return "Formule non disponible."

    def convert(self, vitesseangulaire, original_unit, unit):
        source_unit = original_unit.lower()
        target_unit = unit.lower()

        if (
            source_unit in self.conversions
            and target_unit in self.conversions[source_unit]
        ):
            conversion_func = self.conversions[source_unit][target_unit]
            return conversion_func(self.value)
        else:
            raise ValueError("Unité cible non prise en charge.")
        
class VitesseAngulaireFrame(ConversionFrame):
    def __init__(self, parent, conversion_func, error_callback):
        super().__init__(parent, conversion_func, ConvertVitesseAngulaire.units, error_callback)

