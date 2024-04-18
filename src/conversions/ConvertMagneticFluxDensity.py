from conversions.conversion_frame import ConversionFrame
import math

class ConvertMagneticFluxDensity:
    units = [
            "tesla",
            "gauss",
        ]
    def __init__(self, value=None):
        self.value = value
        self.unit_symbols = {
            "tesla": "T",
            "gauss": "G",
        }
        self.conversions = {
            "tesla": {
                "tesla": lambda x: x,
                "gauss": lambda x: x * 10000,
            },
            "gauss": {
                "tesla": lambda x: x / 10000,
                "gauss": lambda x: x,
            },
        }

    def get_formula(self, source_unit: str, target_unit: str) -> str:
        source_unit = source_unit.lower()
        target_unit = target_unit.lower()
        
        formulas = {
            "tesla": {
                "tesla": "x",
                "gauss": "x * 10000",
            },
            "gauss": {
                "tesla": "x / 10000",
                "gauss": "x",
            },
        }

        if source_unit in formulas and target_unit in formulas[source_unit]:
            formula = formulas[source_unit][target_unit]
            return formula
        else:
            return "Formule non disponible."

    def convert(self, magneticfluxdensity, original_unit, unit):
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

class MagneticFluxDensityFrame(ConversionFrame):
    def __init__(self, parent, conversion_func, error_callback):
        super().__init__(parent, conversion_func, ConvertMagneticFluxDensity.units, error_callback)

