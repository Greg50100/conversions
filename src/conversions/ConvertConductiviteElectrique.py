from conversions.conversion_frame import ConversionFrame
import math

class ConvertConductiviteElectrique:
    units = ["siemens_per_meter", "mho_per_meter", "ohm_inverse_meter"]

    def __init__(self, value=None):
        self.value = value
        self.unit_symbols = {
            "siemens_per_meter": "S/m",
            "mho_per_meter": "mho/m",
            "ohm_inverse_meter": "Ω⁻¹·m",
        }
        self.conversions = {
            "siemens_per_meter": {
                "siemens_per_meter": lambda x: x,
                "mho_per_meter": lambda x: x,
                "ohm_inverse_meter": lambda x: 1 / x,
            },
            "mho_per_meter": {
                "siemens_per_meter": lambda x: x,
                "mho_per_meter": lambda x: x,
                "ohm_inverse_meter": lambda x: 1 / x,
            },
            "ohm_inverse_meter": {
                "siemens_per_meter": lambda x: 1 / x,
                "mho_per_meter": lambda x: 1 / x,
                "ohm_inverse_meter": lambda x: x,
            },
        }

    def get_formula(self, source_unit: str, target_unit: str) -> str:
        source_unit = source_unit.lower()
        target_unit = target_unit.lower()

        formulas = {
            "siemens_per_meter": {
                "siemens_per_meter": "x",
                "mho_per_meter": "x",
                "ohm_inverse_meter": "1 / x",
            },
            "mho_per_meter": {
                "siemens_per_meter": "x",
                "mho_per_meter": "x",
                "ohm_inverse_meter": "1 / x",
            },
            "ohm_inverse_meter": {
                "siemens_per_meter": "1 / x",
                "mho_per_meter": "1 / x",
                "ohm_inverse_meter": "x",
            },
        }

        if source_unit in formulas and target_unit in formulas[source_unit]:
            formula = formulas[source_unit][target_unit]
            return formula
        else:
            return "Formule non disponible."


    def convert(self, conductiviteelectrique, original_unit, unit):
        source_unit = original_unit.lower()
        target_unit = unit.lower()

        if (
            source_unit in self.conversions
            and target_unit in self.conversions[source_unit]
        ):
            conversion_func = self.conversions[source_unit][target_unit]
            return conversion_func(conductiviteelectrique)
        else:
            raise ValueError("Unité cible non prise en charge.")

class ConductiviteElectriqueFrame(ConversionFrame):
    def __init__(self, parent, conversion_func, error_callback):
        super().__init__(parent, conversion_func, ConvertConductiviteElectrique.units, error_callback)