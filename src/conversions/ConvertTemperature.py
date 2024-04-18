from conversions.conversion_frame import ConversionFrame
import math

class ConvertTemperature:
    units = ["celsius", "kelvin", "fahrenheit", "reaumur",
             "rankine", "delisle", "newton", "romer"]

    def __init__(self, value=None):
        self.value = value
        self.unit_symbols = {
            "celsius": "°C",
            "kelvin": "K",
            "fahrenheit": "°F",
            "reaumur": "°Ré",
            "rankine": "°Ra",
            "delisle": "°De",
            "newton": "°N",
            "romer": "°Ro",
        }
        self.conversions = {
            "celsius": {
                "celsius": lambda x: x,
                "kelvin": lambda x: x + 273.15,
                "fahrenheit": lambda x: (x * 9 / 5) + 32,
                "reaumur": lambda x: x * 4 / 5,
                "rankine": lambda x: (x + 273.15) * 9 / 5,
                "delisle": lambda x: (100 - x) * 3 / 2,
                "newton": lambda x: x * 33 / 100,
                "romer": lambda x: x * 21 / 40 + 7.5,
            },
            "kelvin": {
                "celsius": lambda x: x - 273.15,
                "kelvin": lambda x: x,
                "fahrenheit": lambda x: (x - 273.15) * 9 / 5 + 32,
                "reaumur": lambda x: (x - 273.15) * 4 / 5,
                "rankine": lambda x: x * 9 / 5,
                "delisle": lambda x: (373.15 - x) * 3 / 2,
                "newton": lambda x: (x - 273.15) * 33 / 100,
                "romer": lambda x: (x - 273.15) * 21 / 40 + 7.5,
            },
            "fahrenheit": {
                "celsius": lambda x: (x - 32) * 5 / 9,
                "kelvin": lambda x: (x - 32) * 5 / 9 + 273.15,
                "fahrenheit": lambda x: x,
                "reaumur": lambda x: (x - 32) * 4 / 9,
                "rankine": lambda x: x + 459.67,
                "delisle": lambda x: (212 - x) * 5 / 6,
                "newton": lambda x: (x - 32) * 11 / 60,
                "romer": lambda x: (x - 32) * 7 / 24 + 7.5,
            },
            "reaumur": {
                "celsius": lambda x: x * 5 / 4,
                "kelvin": lambda x: x * 5 / 4 + 273.15,
                "fahrenheit": lambda x: x * 9 / 4 + 32,
                "reaumur": lambda x: x,
                "rankine": lambda x: (x * 9 / 4 + 273.15) * 9 / 5,
                "delisle": lambda x: (80 - x) * 15 / 8,
                "newton": lambda x: x * 35 / 22,
                "romer": lambda x: x * 21 / 32 + 7.5,
            },
            "rankine": {
                "celsius": lambda x: (x - 491.67) * 5 / 9,
                "kelvin": lambda x: x * 5 / 9,
                "fahrenheit": lambda x: x - 459.67,
                "reaumur": lambda x: (x - 491.67) * 4 / 9,
                "rankine": lambda x: x,
                "delisle": lambda x: (671.67 - x) * 5 / 6,
                "newton": lambda x: (x - 491.67) * 11 / 60,
                "romer": lambda x: (x - 491.67) * 7 / 24 + 7.5,
            },
            "delisle": {
                "celsius": lambda x: 100 - x * 2 / 3,
                "kelvin": lambda x: 373.15 - x * 2 / 3,
                "fahrenheit": lambda x: 212 - x * 6 / 5,
                "rankine": lambda x: (671.67 - x * 6 / 5) * 5 / 9,
                "reaumur": lambda x: (80 - x) * 8 / 15,
                "delisle": lambda x: x,
                "newton": lambda x: 33 - x * 20 / 11,
                "romer": lambda x: 60 - (x - 7.5) * 40 / 21,
            },
            "newton": {
                "celsius": lambda x: x * 33 / 100,
                "kelvin": lambda x: (x - 273.15) * 33 / 100,
                "fahrenheit": lambda x: (x - 32) * 11 / 60,
                "reaumur": lambda x: x * 33 / 80,
                "rankine": lambda x: (x - 491.67) * 11 / 60,
                "delisle": lambda x: 33 - x * 11 / 50,
                "newton": lambda x: x,
                "romer": lambda x: (x - 7.5) * 22 / 35,
            },
            "romer": {
                "celsius": lambda x: (x * 21 / 40) + 7.5,
                "kelvin": lambda x: ((x - 273.15) * 21 / 40) + 7.5,
                "fahrenheit": lambda x: ((x - 32) * 7 / 24) + 7.5,
                "reaumur": lambda x: (x * 21 / 32) + 7.5,
                "rankine": lambda x: (((x + 459.67) - 491.67) * 21 / 40) + 7.5,
                "delisle": lambda x: (100 - x) * 7 / 20,
                "newton": lambda x: (x * 35 / 22) + 7.5,
                "romer": lambda x: x,
            },
        }

    def get_formula(self, source_unit: str, target_unit: str) -> str:
        source_unit = source_unit.lower()
        target_unit = target_unit.lower()

        formulas = {
            "celsius": {
                "celsius": "x",
                "kelvin": "x + 273.15",
                "fahrenheit": "(x * 9/5) + 32",
                "reaumur": "x * 4/5",
                "rankine": "(x + 273.15) * 9/5",
                "delisle": "(100 - x) * 3/2",
                "newton": "x * 33/100",
                "romer": "x * 21/40 + 7.5",
            },
            "kelvin": {
                "celsius": "x - 273.15",
                "kelvin": "x",
                "fahrenheit": "(x - 273.15) * 9/5 + 32",
                "reaumur": "(x - 273.15) * 4/5",
                "rankine": "x * 9/5",
                "delisle": "(373.15 - x) * 3/2",
                "newton": "(x - 273.15) * 33/100",
                "romer": "(x - 273.15) * 21/40 + 7.5",
            },
            # ... (autres formules)
        }

        if source_unit in formulas and target_unit in formulas[source_unit]:
            formula = formulas[source_unit][target_unit]
            return formula
        else:
            return "Formule non disponible."

    def convert(self, temperature, original_unit, unit):
        source_unit = original_unit.lower()
        target_unit = unit.lower()

        if (
            source_unit in self.conversions
            and target_unit in self.conversions[source_unit]
        ):
            conversion_func = self.conversions[source_unit][target_unit]
            try:
                return conversion_func(temperature)
            except Exception as e:
                raise ValueError(f"Erreur lors de la conversion : {e}")
        else:
            raise ValueError("Unité cible non prise en charge.")


class TemperatureFrame(ConversionFrame):
    def __init__(self, parent, conversion_func, error_callback):
        super().__init__(parent, conversion_func, ConvertTemperature.units, error_callback)

