from conversions.conversion_frame import ConversionFrame
import math

class ConvertPuissanceFluxLumineux:
    units = ["lumen", "candela"]

    def __init__(self, value=None):
        self.value = value
        self.unit_symbols = {"lumen": "lm", "candela": "cd"}
        self.conversions = {
            "lumen": {"lumen": lambda x: x, "candela": lambda x: x / 4 * 3.14159265359},
            "candela": {"lumen": lambda x: x * 4 * 3.14159265359, "candela": lambda x: x},
        }

    def get_formula(self, source_unit: str, target_unit: str) -> str:
        source_unit = source_unit.lower()
        target_unit = target_unit.lower()

        formulas = {
            "lumen": {"lumen": "x", "candela": "x / 4 * 3.14159265359"},
            "candela": {"lumen": "x * 4 * 3.14159265359", "candela": "x"},
        }

        if source_unit in formulas and target_unit in formulas[source_unit]:
            formula = formulas[source_unit][target_unit]
            return formula
        else:
            return "Formule non disponible."

    def convert(self, puissancefluxlumineux, original_unit, unit):
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

class PuissanceFluxLumineuxFrame(ConversionFrame):
    def __init__(self, parent, conversion_func, error_callback):
        super().__init__(parent, conversion_func, ConvertPuissanceFluxLumineux.units, error_callback)

