from conversions.conversion_frame import ConversionFrame
import math

class ConvertEnergy:
    units = [
            "joule",
            "calorie",
            "watt_hour",
            "electronvolt",
            "british_thermal_unit",
            "foot_pound",
            "erg",
        ]
    def __init__(self, value=None):
        self.value = value
        self.unit_symbols = {
            "joule": "J",
            "calorie": "cal",
            "watt_hour": "Wh",
            "electronvolt": "eV",
            "british_thermal_unit": "BTU",
            "foot_pound": "ft.lb",
            "erg": "erg",
        }
        self.conversions = {
            "joule": {
                "joule": lambda x: x,
                "calorie": lambda x: x / 4.184,
                "watt_hour": lambda x: x / 3600,
                "electronvolt": lambda x: x / 1.60218e-19,
                "british_thermal_unit": lambda x: x / 1055.06,
                "foot_pound": lambda x: x / 1.35582,
                "erg": lambda x: x * 1e7,
            },
            "calorie": {
                "joule": lambda x: x * 4.184,
                "calorie": lambda x: x,
                "watt_hour": lambda x: x / 860,
                "electronvolt": lambda x: x * 3.8293e-20,
                "british_thermal_unit": lambda x: x / 252.164,
                "foot_pound": lambda x: x / 3.086,
                "erg": lambda x: x * 418685.28,
            },
            "watt_hour": {
                "joule": lambda x: x * 3600,
                "calorie": lambda x: x * 860,
                "watt_hour": lambda x: x,
                "electronvolt": lambda x: x * 2.247e+22,
                "british_thermal_unit": lambda x: x * 3.41214,
                "foot_pound": lambda x: x * 2655.22,
                "erg": lambda x: x * 3.6e+6,
            },
            "electronvolt": {
                "joule": lambda x: x * 1.60218e-19,
                "calorie": lambda x: x * 2.61145e+19,
                "watt_hour": lambda x: x * 4.45049e-23,
                "electronvolt": lambda x: x,
                "british_thermal_unit": lambda x: x * 3.82673e-20,
                "foot_pound": lambda x: x * 1.1817e-19,
                "erg": lambda x: x * 1.60218e-12,
            },
            "british_thermal_unit": {
                "joule": lambda x: x * 1055.06,
                "calorie": lambda x: x * 252.164,
                "watt_hour": lambda x: x / 3.41214,
                "electronvolt": lambda x: x * 2.61145e+19,
                "british_thermal_unit": lambda x: x,
                "foot_pound": lambda x: x * 778.169,
                "erg": lambda x: x * 1.05506e+10,
            },
            "foot_pound": {
                "joule": lambda x: x * 1.35582,
                "calorie": lambda x: x * 3.086,
                "watt_hour": lambda x: x / 2655.22,
                "electronvolt": lambda x: x * 8.46235e+18,
                "british_thermal_unit": lambda x: x / 778.169,
                "foot_pound": lambda x: x,
                "erg": lambda x: x * 1.35582e+7,
            },
            "erg": {
                "joule": lambda x: x * 1e-7,
                "calorie": lambda x: x * 2.38846e-8,
                "watt_hour": lambda x: x * 2.77778e-11,
                "electronvolt": lambda x: x * 6.242e+11,
                "british_thermal_unit": lambda x: x * 9.4782e-11,
                "foot_pound": lambda x: x * 7.37562e-8,
                "erg": lambda x: x,
            },
        }

    def get_formula(self, source_unit: str, target_unit: str) -> str:
        source_unit = source_unit.lower()
        target_unit = target_unit.lower()
        formulas = {
            "joule": {
                "joule": "x",
                "calorie": "x / 4.184",
                "watt_hour": "(x / 3600) * 1000",
                "electronvolt": "x / 1.60218e-19",
                "british_thermal_unit": "x / 1055.06",
                "foot_pound": "x / 1.35582",
                "erg": "x * 1e7",
            },
            "calorie": {
                "joule": "x * 4.184",
                "calorie": "x",
                "watt_hour": "(x / 860) * 1000",
                "electronvolt": "x * 3.8293e-20",
                "british_thermal_unit": "x / 252.164",
                "foot_pound": "x / 3.086",
                "erg": "x * 418685.28",
            },
            "watt_hour": {
                "joule": "x * 3600",
                "calorie": "(x * 860) / 1000",
                "watt_hour": "x",
                "electronvolt": "x * 2.247e+22",
                "british_thermal_unit": "x * 3.41214",
                "foot_pound": "x * 2655.22",
                "erg": "x * 3.6e+6",
            },
            "electronvolt": {
                "joule": "x * 1.60218e-19",
                "calorie": "x * 2.61145e+19",
                "watt_hour": "x * 4.45049e-23",
                "electronvolt": "x",
                "british_thermal_unit": "x * 3.82673e-20",
                "foot_pound": "x * 1.1817e-19",
                "erg": "x * 1.60218e-12",
            },
            "british_thermal_unit": {
                "joule": "x * 1055.06",
                "calorie": "x * 252.164",
                "watt_hour": "x / 3.41214",
                "electronvolt": "x * 2.61145e+19",
                "british_thermal_unit": "x",
                "foot_pound": "x * 778.169",
                "erg": "x * 1.05506e+10",
            },
            "foot_pound": {
                "joule": "x * 1.35582",
                "calorie": "x * 3.086",
                "watt_hour": "(x / 2655.22) * 1000",
                "electronvolt": "x * 8.46235e+18",
                "british_thermal_unit": "x / 778.169",
                "foot_pound": "x",
                "erg": "x * 1.35582e+7",
            },
            "erg": {
                "joule": "x * 1e-7",
                "calorie": "x * 2.38846e-8",
                "watt_hour": "x * 2.77778e-11",
                "electronvolt": "x * 6.242e+11",
                "british_thermal_unit": "x * 9.4782e-11",
                "foot_pound": "x * 7.37562e-8",
                "erg": "x",
            },
        }

        if source_unit in formulas and target_unit in formulas[source_unit]:
            formula = formulas[source_unit][target_unit]
            return formula
        else:
            return "Formule non disponible."

    def convert(self, energy, original_unit, unit):
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
class EnergyFrame(ConversionFrame):
    def __init__(self, parent, conversion_func, error_callback):
        super().__init__(parent, conversion_func, ConvertEnergy.units, error_callback)

