from conversions.conversion_frame import ConversionFrame
import math

class ConvertTime:
    units = [
            "secondes",
            "minutes",
            "heures",
            "jours",
            "semaines",
            "mois",
            "années",
        ]
    def __init__(self, value=None):
        self.value = value
        self.unit_symbols = {
            "secondes": "s",
            "minutes": "min",
            "heures": "h",
            "jours": "j",
            "semaines": "sem",
            "mois": "mois",
            "années": "an",
        }
        self.conversions = {
            "secondes": {
                "secondes": lambda x: x,
                "minutes": lambda x: x / 60,
                "heures": lambda x: x / 3600,
                "jours": lambda x: x / 86400,
                "semaines": lambda x: x / 604800,
                "mois": lambda x: x / (86400 * 30.44),
                "années": lambda x: x / (86400 * 365.25),
            },
            "minutes": {
                "secondes": lambda x: x * 60,
                "minutes": lambda x: x,
                "heures": lambda x: x / 60,
                "jours": lambda x: x / (24 * 60),
                "semaines": lambda x: x / (24 * 60 * 7),
                "mois": lambda x: x / (24 * 60 * 30.44),
                "années": lambda x: x / (24 * 60 * 365.25),
            },
            "heures": {
                "secondes": lambda x: x * 3600,
                "minutes": lambda x: x * 60,
                "heures": lambda x: x,
                "jours": lambda x: x / 24,
                "semaines": lambda x: x / (24 * 7),
                "mois": lambda x: x / (24 * 30.44),
                "années": lambda x: x / (24 * 365.25),
            },
            "jours": {
                "secondes": lambda x: x * 86400,
                "minutes": lambda x: x * (24 * 60),
                "heures": lambda x: x * 24,
                "jours": lambda x: x,
                "semaines": lambda x: x / 7,
                "mois": lambda x: x / 30.44,
                "années": lambda x: x / 365.25,
            },
            "semaines": {
                "secondes": lambda x: x * 604800,
                "minutes": lambda x: x * (7 * 24 * 60),
                "heures": lambda x: x * (7 * 24),
                "jours": lambda x: x * 7,
                "semaines": lambda x: x,
                "mois": lambda x: x / 4.34524,
                "années": lambda x: x / 52.1429,
            },
            "mois": {
                "secondes": lambda x: x * (86400 * 30.44),
                "minutes": lambda x: x * (24 * 60 * 30.44),
                "heures": lambda x: x * (24 * 30.44),
                "jours": lambda x: x * 30.44,
                "semaines": lambda x: x * 4.34524,
                "mois": lambda x: x,
                "années": lambda x: x / 12,
            },
            "années": {
                "secondes": lambda x: x * (86400 * 365.25),
                "minutes": lambda x: x * (24 * 60 * 365.25),
                "heures": lambda x: x * (24 * 365.25),
                "jours": lambda x: x * 365.25,
                "semaines": lambda x: x * 52.1429,
                "mois": lambda x: x * 12,
                "années": lambda x: x,
            },
        }

    def get_formula(self, source_unit: str, target_unit: str) -> str:
        source_unit = source_unit.lower()
        target_unit = target_unit.lower()

        formulas = {
            "secondes": {
                "secondes": "x",
                "minutes": "x / 60",
                "heures": "x / 3600",
                "jours": "x / 86400",
                "semaines": "x / 604800",
                "mois": "x / (86400 * 30.44)",
                "années": "x / (86400 * 365.25)",
            },
            "minutes": {
                "secondes": "x * 60",
                "minutes": "x",
                "heures": "x / 60",
                "jours": "x / (24 * 60)",
                "semaines": "x / (24 * 60 * 7)",
                "mois": "x / (24 * 60 * 30.44)",
                "années": "x / (24 * 60 * 365.25)",
            },
            "heures": {
                "secondes": "x * 3600",
                "minutes": "x * 60",
                "heures": "x",
                "jours": "x / 24",
                "semaines": "x / (24 * 7)",
                "mois": "x / (24 * 30.44)",
                "années": "x / (24 * 365.25)",
            },
            "jours": {
                "secondes": "x * 86400",
                "minutes": "x * (24 * 60)",
                "heures": "x * 24",
                "jours": "x",
                "semaines": "x / 7",
                "mois": "x / 30.44",
                "années": "x / 365.25",
            },
            "semaines": {
                "secondes": "x * 604800",
                "minutes": "x * (7 * 24 * 60)",
                "heures": "x * (7 * 24)",
                "jours": "x * 7",
                "semaines": "x",
                "mois": "x / 4.34524",
                "années": "x / 52.1429",
            },
            "mois": {
                "secondes": "x * (86400 * 30.44)",
                "minutes": "x * (24 * 60 * 30.44)",
                "heures": "x * (24 * 30.44)",
                "jours": "x * 30.44",
                "semaines": "x * 4.34524",
                "mois": "x",
                "années": "x / 12",
            },
            "années": {
                "secondes": "x * (86400 * 365.25)",
                "minutes": "x * (24 * 60 * 365.25)",
                "heures": "x * (24 * 365.25)",
                "jours": "x * 365.25",
                "semaines": "x * 52.1429",
                "mois": "x * 12",
                "années": "x",
            },
        }
        
        if source_unit in formulas and target_unit in formulas[source_unit]:
            formula = formulas[source_unit][target_unit]
            return formula
        else:
            return "Formule non disponible."

    def convert(self, time, original_unit, unit):
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
        
class TimeFrame(ConversionFrame):
    def __init__(self, parent, conversion_func, error_callback):
        super().__init__(parent, conversion_func, ConvertTime.units, error_callback)

