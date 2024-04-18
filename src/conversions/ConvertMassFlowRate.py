from conversions.conversion_frame import ConversionFrame
import math

class ConvertMassFlowRate:
    units = [
            "kilogram_per_second",
            "gram_per_minute",
            "tonne_per_hour",
            "pound_per_hour",
        ]
    def __init__(self, value=None):
        self.value = value
        self.unit_symbols = {
            "kilogram_per_second": "kg/s",
            "gram_per_minute": "g/min",
            "tonne_per_hour": "t/h",
            "pound_per_hour": "lb/h",
        }
        self.conversions = {
            "kilogram_per_second": {
                "kilogram_per_second": lambda x: x,
                "gram_per_minute": lambda x: x * 60000,
                "tonne_per_hour": lambda x: x * 3600,
                "pound_per_hour": lambda x: x * 3600 * 0.453592,
            },
            "gram_per_minute": {
                "kilogram_per_second": lambda x: x / 60000,
                "gram_per_minute": lambda x: x,
                "tonne_per_hour": lambda x: x / 16.6667,
                "pound_per_hour": lambda x: x * 0.00220462,
            },
            "tonne_per_hour": {
                "kilogram_per_second": lambda x: x / 3600,
                "gram_per_minute": lambda x: x * 16.6667,
                "tonne_per_hour": lambda x: x,
                "pound_per_hour": lambda x: x * 2204.62,
            },
            "pound_per_hour": {
                "kilogram_per_second": lambda x: x / (3600 * 0.453592),
                "gram_per_minute": lambda x: x / 0.00220462,
                "tonne_per_hour": lambda x: x / 2204.62,
                "pound_per_hour": lambda x: x,
            },
        }

    def get_formula(self, source_unit: str, target_unit: str) -> str:
        source_unit = source_unit.lower()
        target_unit = target_unit.lower()

        formulas = {
            "kilogram_per_second": {
                "kilogram_per_second": "x",
                "gram_per_minute": "x * 60000",
                "tonne_per_hour": "x * 3600",
                "pound_per_hour": "x * 3600 * 0.453592",
            },
            "gram_per_minute": {
                "kilogram_per_second": "x / 60000",
                "gram_per_minute": "x",
                "tonne_per_hour": "x / 16.6667",
                "pound_per_hour": "x * 0.00220462",
            },
            "tonne_per_hour": {
                "kilogram_per_second": "x / 3600",
                "gram_per_minute": "x * 16.6667",
                "tonne_per_hour": "x",
                "pound_per_hour": "x * 2204.62",
            },
            "pound_per_hour": {
                "kilogram_per_second": "x / (3600 * 0.453592)",
                "gram_per_minute": "x / 0.00220462",
                "tonne_per_hour": "x / 2204.62",
                "pound_per_hour": "x",
            },
        }

        if source_unit in formulas and target_unit in formulas[source_unit]:
            formula = formulas[source_unit][target_unit]
            return formula
        else:
            return "Formule non disponible."

    def convert(self, massflowrate, original_unit, unit):
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
        
class MassFlowRateFrame(ConversionFrame):
    def __init__(self, parent, conversion_func, error_callback):
        super().__init__(parent, conversion_func, ConvertMassFlowRate.units, error_callback)
