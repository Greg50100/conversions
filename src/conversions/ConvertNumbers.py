import tkinter as tk
from tkinter import ttk
from conversions.conversion_frame import ConversionFrame
from collections import OrderedDict
from num2words import num2words

class ConvertNumbers:
    units = ["binaire", "décimal", "hexadécimal", "octal", "ternaire", "quaternaire", "quinaire", "sénaire", "septénaire", "nonaire", "unidécimal", "duodécimal", "tridécimal", "quindécimal", "octodécimal", "vicésimal", "hexatrigésimal", "sexagésimal", "romain", "dén. littérale fr", "dén. littérale en", "dén. littérale de", "dén. littérale es"]
    base_prefixes = {
        "binaire": "0b",
        "décimal": "",
        "hexadécimal": "0x",
        "octal": "0o",
        "ternaire": "",
        "quaternaire": "",
        "quinaire": "",
        "sénaire": "",
        "septénaire": "",
        "nonaire": "",
        "unidécimal": "",
        "duodécimal": "",
        "tridécimal": "",
        "quindécimal": "",
        "octodécimal": "",
        "vicésimal": "",
        "hexatrigésimal": "",
        "sexagésimal": "",
        "romain": "",
        "dén. littérale fr": "",
        "dén. littérale en": "",
        "dén. littérale de": "",
        "dén. littérale es": "",
    }

    def __init__(self):
        self.conversions = {
            "binaire": OrderedDict([
                ("décimal", lambda x: str(int(x, 2))),
                ("hexadécimal", lambda x: hex(int(x, 2))[2:]),
                ("octal", lambda x: oct(int(x, 2))[2:]),
                ("ternaire", lambda x: self.to_ternary(int(x, 2))),
                ("quaternaire", lambda x: self.to_quaternary(int(x, 2))),
                ("quinaire", lambda x: self.to_quinary(int(x, 2))),
                ("sénaire", lambda x: self.to_senary(int(x, 2))),
                ("septénaire", lambda x: self.to_septenary(int(x, 2))),
                ("nonaire", lambda x: self.to_nonary(int(x, 2))),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 2))),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 2))),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 2))),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 2))),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 2))),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 2))),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 2))),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 2))),
                ("romain", lambda x: self.to_roman(int(x, 2))),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 2))),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 2))),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 2))),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 2))),
            ]),
            "décimal": OrderedDict([
                ("binaire", lambda x: bin(int(x))[2:]),
                ("hexadécimal", lambda x: hex(int(x))[2:]),
                ("octal", lambda x: oct(int(x))[2:]),
                ("ternaire", lambda x: self.to_ternary(int(x))),
                ("quaternaire", lambda x: self.to_quaternary(int(x))),
                ("quinaire", lambda x: self.to_quinary(int(x))),
                ("sénaire", lambda x: self.to_senary(int(x))),
                ("septénaire", lambda x: self.to_septenary(int(x))),
                ("nonaire", lambda x: self.to_nonary(int(x))),
                ("unidécimal", lambda x: self.to_undecimal(int(x))),
                ("duodécimal", lambda x: self.to_duodecimal(int(x))),
                ("tridécimal", lambda x: self.to_tridecimal(int(x))),
                ("quindécimal", lambda x: self.to_quindecimal(int(x))),
                ("octodécimal", lambda x: self.to_octodecimal(int(x))),
                ("vicésimal", lambda x: self.to_vigesimal(int(x))),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x))),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x))),
                ("romain", lambda x: self.to_roman(int(x))),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x))),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x))),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x))),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x))),
            ]),
            "hexadécimal": OrderedDict([
                ("binaire", lambda x: bin(int(x, 16))[2:] if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
                ("décimal", lambda x: str(int(x, 16)) if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
                ("octal", lambda x: oct(int(x, 16))[2:] if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
                ("ternaire", lambda x: self.to_ternary(int(x, 16)) if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
                ("quaternaire", lambda x: self.to_quaternary(int(x, 16)) if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
                ("quinaire", lambda x: self.to_quinary(int(x, 16)) if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
                ("sénaire", lambda x: self.to_senary(int(x, 16)) if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
                ("septénaire", lambda x: self.to_septenary(int(x, 16)) if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
                ("nonaire", lambda x: self.to_nonary(int(x, 16)) if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 16)) if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 16)) if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 16)) if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 16)) if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 16)) if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 16)) if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 16)) if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 16)) if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
                ("romain", lambda x: self.to_roman(int(x, 16)) if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 16)) if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 16)) if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 16)) if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 16)) if all(c in '0123456789abcdefABCDEF' for c in x) else "Invalid hexadecimal"),
            ]),
            "octal": OrderedDict([
                ("binaire", lambda x: bin(int(x, 8))[2:]),
                ("décimal", lambda x: str(int(x, 8))),
                ("hexadécimal", lambda x: hex(int(x, 8))[2:]),
                ("ternaire", lambda x: self.to_ternary(int(x, 8))),
                ("quaternaire", lambda x: self.to_quaternary(int(x, 8))),
                ("quinaire", lambda x: self.to_quinary(int(x, 8))),
                ("sénaire", lambda x: self.to_senary(int(x, 8))),
                ("septénaire", lambda x: self.to_septenary(int(x, 8))),
                ("nonaire", lambda x: self.to_nonary(int(x, 8))),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 8))),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 8))),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 8))),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 8))),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 8))),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 8))),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 8))),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 8))),
                ("romain", lambda x: self.to_roman(int(x, 8))),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 8))),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 8))),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 8))),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 8))),
            ]),
            "ternaire": OrderedDict([
                ("binaire", lambda x: bin(int(x, 3))[2:]),
                ("décimal", lambda x: str(int(x, 3))),
                ("hexadécimal", lambda x: hex(int(x, 3))[2:]),
                ("octal", lambda x: oct(int(x, 3))[2:]),
                ("quaternaire", lambda x: self.to_quaternary(int(x, 3))),
                ("quinaire", lambda x: self.to_quinary(int(x, 3))),
                ("sénaire", lambda x: self.to_senary(int(x, 3))),
                ("septénaire", lambda x: self.to_septenary(int(x, 3))),
                ("nonaire", lambda x: self.to_nonary(int(x, 3))),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 3))),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 3))),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 3))),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 3))),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 3))),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 3))),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 3))),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 3))),
                ("romain", lambda x: self.to_roman(int(x, 3))),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 3))),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 3))),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 3))),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 3))),
            ]),
            "quaternaire": OrderedDict([
                ("binaire", lambda x: bin(int(x, 4))[2:]),
                ("décimal", lambda x: str(int(x, 4))),
                ("hexadécimal", lambda x: hex(int(x, 4))[2:]),
                ("octal", lambda x: oct(int(x, 4))[2:]),
                ("ternaire", lambda x: self.to_ternary(int(x, 4))),
                ("quinaire", lambda x: self.to_quinary(int(x, 4))),
                ("sénaire", lambda x: self.to_senary(int(x, 4))),
                ("septénaire", lambda x: self.to_septenary(int(x, 4))),
                ("nonaire", lambda x: self.to_nonary(int(x, 4))),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 4))),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 4))),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 4))),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 4))),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 4))),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 4))),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 4))),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 4))),
                ("romain", lambda x: self.to_roman(int(x, 4))),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 4))),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 4))),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 4))),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 4))),
            ]),
            "quinaire": OrderedDict([
                ("binaire", lambda x: bin(int(x, 5))[2:]),
                ("décimal", lambda x: str(int(x, 5))),
                ("hexadécimal", lambda x: hex(int(x, 5))[2:]),
                ("octal", lambda x: oct(int(x, 5))[2:]),
                ("ternaire", lambda x: self.to_ternary(int(x, 5))),
                ("quaternaire", lambda x: self.to_quaternary(int(x, 5))),
                ("sénaire", lambda x: self.to_senary(int(x, 5))),
                ("septénaire", lambda x: self.to_septenary(int(x, 5))),
                ("nonaire", lambda x: self.to_nonary(int(x, 5))),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 5))),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 5))),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 5))),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 5))),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 5))),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 5))),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 5))),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 5))),
                ("romain", lambda x: self.to_roman(int(x, 5))),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 5))),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 5))),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 5))),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 5))),
            ]),
            "sénaire": OrderedDict([
                ("binaire", lambda x: bin(int(x, 6))[2:]),
                ("décimal", lambda x: str(int(x, 6))),
                ("hexadécimal", lambda x: hex(int(x, 6))[2:]),
                ("octal", lambda x: oct(int(x, 6))[2:]),
                ("ternaire", lambda x: self.to_ternary(int(x, 6))),
                ("quaternaire", lambda x: self.to_quaternary(int(x, 6))),
                ("quinaire", lambda x: self.to_quinary(int(x, 6))),
                ("sénaire", lambda x: self.to_senary(int(x, 6))),
                ("septénaire", lambda x: self.to_septenary(int(x, 6))),
                ("nonaire", lambda x: self.to_nonary(int(x, 6))),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 6))),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 6))),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 6))),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 6))),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 6))),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 6))),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 6))),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 6))),
                ("romain", lambda x: self.to_roman(int(x, 6))),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 6))),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 6))),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 6))),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 6))),
            ]),
            "septénaire": OrderedDict([
                ("binaire", lambda x: bin(int(x, 7))[2:]),
                ("décimal", lambda x: str(int(x, 7))),
                ("hexadécimal", lambda x: hex(int(x, 7))[2:]),
                ("octal", lambda x: oct(int(x, 7))[2:]),
                ("ternaire", lambda x: self.to_ternary(int(x, 7))),
                ("quaternaire", lambda x: self.to_quaternary(int(x, 7))),
                ("quinaire", lambda x: self.to_quinary(int(x, 7))),
                ("sénaire", lambda x: self.to_senary(int(x, 7))),
                ("septénaire", lambda x: self.to_septenary(int(x, 7))),
                ("nonaire", lambda x: self.to_nonary(int(x, 7))),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 7))),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 7))),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 7))),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 7))),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 7))),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 7))),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 7))),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 7))),
                ("romain", lambda x: self.to_roman(int(x, 7))),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 7))),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 7))),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 7))),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 7))),
            ]),
            "nonaire": OrderedDict([
                ("binaire", lambda x: bin(int(x, 9))[2:]),
                ("décimal", lambda x: str(int(x, 9))),
                ("hexadécimal", lambda x: hex(int(x, 9))[2:]),
                ("octal", lambda x: oct(int(x, 9))[2:]),
                ("ternaire", lambda x: self.to_ternary(int(x, 9))),
                ("quaternaire", lambda x: self.to_quaternary(int(x, 9))),
                ("quinaire", lambda x: self.to_quinary(int(x, 9))),
                ("sénaire", lambda x: self.to_senary(int(x, 9))),
                ("septénaire", lambda x: self.to_septenary(int(x, 9))),
                ("nonaire", lambda x: self.to_nonary(int(x, 9))),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 9))),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 9))),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 9))),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 9))),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 9))),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 9))),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 9))),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 9))),                
                ("romain", lambda x: self.to_roman(int(x, 9))),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 9))),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 9))),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 9))),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 9))),
            ]),
            "unidécimal": OrderedDict([
                ("binaire", lambda x: bin(int(x, 11))[2:]),
                ("décimal", lambda x: str(int(x, 11))),
                ("hexadécimal", lambda x: hex(int(x, 11))[2:]),
                ("octal", lambda x: oct(int(x, 11))[2:]),
                ("ternaire", lambda x: self.to_ternary(int(x, 11))),
                ("quaternaire", lambda x: self.to_quaternary(int(x, 11))),
                ("quinaire", lambda x: self.to_quinary(int(x, 11))),
                ("sénaire", lambda x: self.to_senary(int(x, 11))),
                ("septénaire", lambda x: self.to_septenary(int(x, 11))),
                ("nonaire", lambda x: self.to_nonary(int(x, 11))),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 11))),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 11))),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 11))),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 11))),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 11))),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 11))),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 11))),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 11))),
                ("romain", lambda x: self.to_roman(int(x, 11))),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 11))),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 11))),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 11))),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 11))),
            ]),
            "duodécimal": OrderedDict([
                ("binaire", lambda x: bin(int(x, 12))[2:]),
                ("décimal", lambda x: str(int(x, 12))),
                ("hexadécimal", lambda x: hex(int(x, 12))[2:]),
                ("octal", lambda x: oct(int(x, 12))[2:]),
                ("ternaire", lambda x: self.to_ternary(int(x, 12))),
                ("quaternaire", lambda x: self.to_quaternary(int(x, 12))),
                ("quinaire", lambda x: self.to_quinary(int(x, 12))),
                ("sénaire", lambda x: self.to_senary(int(x, 12))),
                ("septénaire", lambda x: self.to_septenary(int(x, 12))),
                ("nonaire", lambda x: self.to_nonary(int(x, 12))),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 12))),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 12))),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 12))),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 12))),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 12))),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 12))),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 12))),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 12))),
                ("romain", lambda x: self.to_roman(int(x, 12))),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 12))),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 12))),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 12))),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 12))),
            ]),
            "tridécimal": OrderedDict([
                ("binaire", lambda x: bin(int(x, 13))[2:]),
                ("décimal", lambda x: str(int(x, 13))),
                ("hexadécimal", lambda x: hex(int(x, 13))[2:]),
                ("octal", lambda x: oct(int(x, 13))[2:]),
                ("ternaire", lambda x: self.to_ternary(int(x, 13))),
                ("quaternaire", lambda x: self.to_quaternary(int(x, 13))),
                ("quinaire", lambda x: self.to_quinary(int(x, 13))),
                ("sénaire", lambda x: self.to_senary(int(x, 13))),
                ("septénaire", lambda x: self.to_septenary(int(x, 13))),
                ("nonaire", lambda x: self.to_nonary(int(x, 13))),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 13))),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 13))),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 13))),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 13))),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 13))),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 13))),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 13))),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 13))),
                ("romain", lambda x: self.to_roman(int(x, 13))),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 13))),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 13))),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 13))),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 13))),
            ]),
            "quindécimal": OrderedDict([
                ("binaire", lambda x: bin(int(x, 15))[2:]),
                ("décimal", lambda x: str(int(x, 15))),
                ("hexadécimal", lambda x: hex(int(x, 15))[2:]),
                ("octal", lambda x: oct(int(x, 15))[2:]),
                ("ternaire", lambda x: self.to_ternary(int(x, 15))),
                ("quaternaire", lambda x: self.to_quaternary(int(x, 15))),
                ("quinaire", lambda x: self.to_quinary(int(x, 15))),
                ("sénaire", lambda x: self.to_senary(int(x, 15))),
                ("septénaire", lambda x: self.to_septenary(int(x, 15))),
                ("nonaire", lambda x: self.to_nonary(int(x, 15))),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 15))),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 15))),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 15))),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 15))),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 15))),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 15))),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 15))),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 15))),
                ("romain", lambda x: self.to_roman(int(x, 15))),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 15))),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 15))),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 15))),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 15))),
            ]),
            "octodécimal": OrderedDict([
                ("binaire", lambda x: bin(int(x, 18))[2:]),
                ("décimal", lambda x: str(int(x, 18))),
                ("hexadécimal", lambda x: hex(int(x, 18))[2:]),
                ("octal", lambda x: oct(int(x, 18))[2:]),
                ("ternaire", lambda x: self.to_ternary(int(x, 18))),
                ("quaternaire", lambda x: self.to_quaternary(int(x, 18))),
                ("quinaire", lambda x: self.to_quinary(int(x, 18))),
                ("sénaire", lambda x: self.to_senary(int(x, 18))),
                ("septénaire", lambda x: self.to_septenary(int(x, 18))),
                ("nonaire", lambda x: self.to_nonary(int(x, 18))),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 18))),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 18))),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 18))),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 18))),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 18))),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 18))),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 18))),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 18))),
                ("romain", lambda x: self.to_roman(int(x, 18))),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 18))),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 18))),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 18))),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 18))),
            ]),
            "vicésimal": OrderedDict([
                ("binaire", lambda x: bin(int(x, 20))[2:]),
                ("décimal", lambda x: str(int(x, 20))),
                ("hexadécimal", lambda x: hex(int(x, 20))[2:]),
                ("octal", lambda x: oct(int(x, 20))[2:]),
                ("ternaire", lambda x: self.to_ternary(int(x, 20))),
                ("quaternaire", lambda x: self.to_quaternary(int(x, 20))),
                ("quinaire", lambda x: self.to_quinary(int(x, 20))),
                ("sénaire", lambda x: self.to_senary(int(x, 20))),
                ("septénaire", lambda x: self.to_septenary(int(x, 20))),
                ("nonaire", lambda x: self.to_nonary(int(x, 20))),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 20))),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 20))),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 20))),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 20))),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 20))),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 20))),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 20))),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 20))),
                ("romain", lambda x: self.to_roman(int(x, 20))),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 20))),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 20))),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 20))),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 20))),
            ]),
            "hexatrigésimal": OrderedDict([
                ("binaire", lambda x: bin(int(x, 36))[2:] if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
                ("décimal", lambda x: str(int(x, 36)) if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
                ("octal", lambda x: oct(int(x, 36))[2:] if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
                ("ternaire", lambda x: self.to_ternary(int(x, 36)) if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
                ("quaternaire", lambda x: self.to_quaternary(int(x, 36)) if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
                ("quinaire", lambda x: self.to_quinary(int(x, 36)) if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
                ("sénaire", lambda x: self.to_senary(int(x, 36)) if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
                ("septénaire", lambda x: self.to_septenary(int(x, 36)) if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
                ("nonaire", lambda x: self.to_nonary(int(x, 36)) if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 36)) if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 36)) if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 36)) if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 36)) if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 36)) if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 36)) if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 36)) if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 36)) if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
                ("romain", lambda x: self.to_roman(int(x, 36)) if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 36)) if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 36)) if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 36)) if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 36)) if all(c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in x) else "Invalid hexadecimal"),
            ]),
            "sexagésimal": OrderedDict([
                ("binaire", lambda x: bin(int(x, 60))[2:]),
                ("décimal", lambda x: str(int(x, 60))),
                ("hexadécimal", lambda x: hex(int(x, 60))[2:]),
                ("octal", lambda x: oct(int(x, 60))[2:]),
                ("ternaire", lambda x: self.to_ternary(int(x, 60))),
                ("quaternaire", lambda x: self.to_quaternary(int(x, 60))),
                ("quinaire", lambda x: self.to_quinary(int(x, 60))),
                ("sénaire", lambda x: self.to_senary(int(x, 60))),
                ("septénaire", lambda x: self.to_septenary(int(x, 60))),
                ("nonaire", lambda x: self.to_nonary(int(x, 60))),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 60))),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 60))),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 60))),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 60))),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 60))),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 60))),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 60))),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 60))),
                ("romain", lambda x: self.to_roman(int(x, 60))),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 60))),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 60))),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 60))),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 60))),
            ]),
            "romain": OrderedDict([
                ("binaire", lambda x: bin(int(x, 10))[2:]),
                ("décimal", lambda x: str(int(x, 10))),
                ("hexadécimal", lambda x: hex(int(x, 10))[2:]),
                ("octal", lambda x: oct(int(x, 10))[2:]),
                ("ternaire", lambda x: self.to_ternary(int(x, 10))),
                ("quaternaire", lambda x: self.to_quaternary(int(x, 10))),
                ("quinaire", lambda x: self.to_quinary(int(x, 10))),
                ("sénaire", lambda x: self.to_senary(int(x, 10))),
                ("septénaire", lambda x: self.to_septenary(int(x, 10))),
                ("nonaire", lambda x: self.to_nonary(int(x, 10))),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 10))),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 10))),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 10))),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 10))),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 10))),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 10))),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 10))),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 10))),
                ("romain", lambda x: self.to_roman(int(x, 10))),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 10))),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 10))),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 10))),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 10))),
            ]),
            "dén. littérale fr": OrderedDict([
                ("binaire", lambda x: bin(int(x, 11))[2:]),
                ("décimal", lambda x: str(int(x, 11))),
                ("hexadécimal", lambda x: hex(int(x, 11))[2:]),
                ("octal", lambda x: oct(int(x, 11))[2:]),
                ("ternaire", lambda x: self.to_ternary(int(x, 11))),
                ("quaternaire", lambda x: self.to_quaternary(int(x, 11))),
                ("quinaire", lambda x: self.to_quinary(int(x, 11))),
                ("sénaire", lambda x: self.to_senary(int(x, 11))),
                ("septénaire", lambda x: self.to_septenary(int(x, 11))),
                ("nonaire", lambda x: self.to_nonary(int(x, 11))),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 11))),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 11))),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 11))),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 11))),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 11))),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 11))),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 11))),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 11))),
                ("romain", lambda x: self.to_roman(int(x, 11))),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 11))),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 11))),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 11))),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 11))),
            ]),
            "dén. littérale en": OrderedDict([
                ("binaire", lambda x: bin(int(x, 12))[2:]),
                ("décimal", lambda x: str(int(x, 12))),
                ("hexadécimal", lambda x: hex(int(x, 12))[2:]),
                ("octal", lambda x: oct(int(x, 12))[2:]),
                ("ternaire", lambda x: self.to_ternary(int(x, 12))),
                ("quaternaire", lambda x: self.to_quaternary(int(x, 12))),
                ("quinaire", lambda x: self.to_quinary(int(x, 12))),
                ("sénaire", lambda x: self.to_senary(int(x, 12))),
                ("septénaire", lambda x: self.to_septenary(int(x, 12))),
                ("nonaire", lambda x: self.to_nonary(int(x, 12))),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 12))),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 12))),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 12))),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 12))),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 12))),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 12))),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 12))),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 12))),
                ("romain", lambda x: self.to_roman(int(x, 12))),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 12))),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 12))),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 12))),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 12))),
            ]),
            "dén. littérale de": OrderedDict([
                ("binaire", lambda x: bin(int(x, 13))[2:]),
                ("décimal", lambda x: str(int(x, 13))),
                ("hexadécimal", lambda x: hex(int(x, 13))[2:]),
                ("octal", lambda x: oct(int(x, 13))[2:]),
                ("ternaire", lambda x: self.to_ternary(int(x, 13))),
                ("quaternaire", lambda x: self.to_quaternary(int(x, 13))),
                ("quinaire", lambda x: self.to_quinary(int(x, 13))),
                ("sénaire", lambda x: self.to_senary(int(x, 13))),
                ("septénaire", lambda x: self.to_septenary(int(x, 13))),
                ("nonaire", lambda x: self.to_nonary(int(x, 13))),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 13))),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 13))),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 13))),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 13))),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 13))),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 13))),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 13))),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 13))),
                ("romain", lambda x: self.to_roman(int(x, 13))),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 13))),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 13))),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 13))),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 13))),
            ]),
            "dén. littérale es": OrderedDict([
                ("binaire", lambda x: bin(int(x, 13))[2:]),
                ("décimal", lambda x: str(int(x, 13))),
                ("hexadécimal", lambda x: hex(int(x, 13))[2:]),
                ("octal", lambda x: oct(int(x, 13))[2:]),
                ("ternaire", lambda x: self.to_ternary(int(x, 13))),
                ("quaternaire", lambda x: self.to_quaternary(int(x, 13))),
                ("quinaire", lambda x: self.to_quinary(int(x, 13))),
                ("sénaire", lambda x: self.to_senary(int(x, 13))),
                ("septénaire", lambda x: self.to_septenary(int(x, 13))),
                ("nonaire", lambda x: self.to_nonary(int(x, 13))),
                ("unidécimal", lambda x: self.to_undecimal(int(x, 13))),
                ("duodécimal", lambda x: self.to_duodecimal(int(x, 13))),
                ("tridécimal", lambda x: self.to_tridecimal(int(x, 13))),
                ("quindécimal", lambda x: self.to_quindecimal(int(x, 13))),
                ("octodécimal", lambda x: self.to_octodecimal(int(x, 13))),
                ("vicésimal", lambda x: self.to_vigesimal(int(x, 13))),
                ("hexatrigésimal", lambda x: self.to_hexatrigesimal(int(x, 13))),
                ("sexagésimal", lambda x: self.to_sexagesimal(int(x, 13))),
                ("romain", lambda x: self.to_roman(int(x, 13))),
                ("dén. littérale fr", lambda x: self.to_letters_fr(int(x, 13))),
                ("dén. littérale en", lambda x: self.to_letters_en(int(x, 13))),
                ("dén. littérale de", lambda x: self.to_letters_de(int(x, 13))),
                ("dén. littérale es", lambda x: self.to_letters_es(int(x, 13))),
            ]),
        }

    def to_ternary(self, num):
        """Convertit un nombre en base ternaire."""
        ternary = ''
        while num > 0:
            ternary = str(num % 3) + ternary
            num //= 3
        return ternary
    
    def to_quaternary(self, num):
        """Convertit un nombre en base quaternaire."""
        quaternary = ''
        while num > 0:
            quaternary = str(num % 4) + quaternary
            num //= 4
        return quaternary

    def to_quinary(self, num):
        """Convertit un nombre en base quinaire."""
        quinary = ''
        while num > 0:
            quinary = str(num % 5) + quinary
            num //= 5
        return quinary
    
    def to_senary(self, num):
        """Convertit un nombre en base sénaire."""
        senary = ''
        while num > 0:
            senary = str(num % 6) + senary
            num //= 6
        return senary
    
    def to_septenary(self, num):
        """Convertit un nombre en base septénaire."""
        septenary = ''
        while num > 0:
            septenary = str(num % 7) + septenary
            num //= 7
        return septenary
    
    def to_nonary(self, num):
        """Convertit un nombre en base nonaire."""
        nonary = ''
        while num > 0:
            nonary = str(num % 9) + nonary
            num //= 9
        return nonary

    def to_undecimal(self, num):
        """Convertit un nombre en base unidécimal."""
        undecimal = ''
        while num > 0:
            undecimal = str(num % 11) + undecimal
            num //= 11
        return undecimal
    
    def to_duodecimal(self, num):
        """Convertit un nombre en base duodécimal."""
        duodecimal = ''
        while num > 0:
            duodecimal = str(num % 12) + duodecimal
            num //= 12
        return duodecimal

    def to_tridecimal(self, num):
        """Convertit un nombre en base tridécimal."""
        tridecimal = ''
        while num > 0:
            tridecimal = str(num % 13) + tridecimal
            num //= 13
        return tridecimal
    
    def to_quindecimal(self, num):
        """Convertit un nombre en base quindécimal."""
        quindecimal = ''
        while num > 0:
            quindecimal = str(num % 15) + quindecimal
            num //= 15
        return quindecimal
    
    def to_octodecimal(self, num):
        """Convertit un nombre en base octodécimal."""
        octodecimal = ''
        while num > 0:
            octodecimal = str(num % 18) + octodecimal
            num //= 18
        return octodecimal

    def to_vigesimal(self, num):
        """Convertit un nombre en base vicésimal."""
        vigesimal = ''
        while num > 0:
            vigesimal = str(num % 20) + vigesimal
            num //= 20
        return vigesimal
    
    def to_hexatrigesimal(self, num):
        """Convertit un nombre en base hexatrigésimal."""
        hexatrigesimal = ''
        while num > 0:
            hexatrigesimal = str(num % 36) + hexatrigesimal
            num //= 36
        return hexatrigesimal

    def to_sexagesimal(self, num):
        """Convertit un nombre en base sexagésimal."""
        sexagesimal = ''
        while num > 0:
            sexagesimal = str(num % 17) + sexagesimal
            num //= 17
        return sexagesimal

    def to_roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
    
    def from_roman(self, roman):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integer = 0
        for i in range(len(roman)):
            if i > 0 and roman_numerals[roman[i]] > roman_numerals[roman[i - 1]]:
                integer += roman_numerals[roman[i]] - 2 * roman_numerals[roman[i - 1]]
            else:
                integer += roman_numerals[roman[i]]
        return integer


    def to_letters_fr(self, num):
        return num2words(num, lang='fr')

    def to_letters_en(self, num):
        return num2words(num, lang='en')

    def to_letters_de(self, num):
        return num2words(num, lang='de')

    def to_letters_es(self, num):
        return num2words(num, lang='es')

    
    def remove_prefix(self, number, unit):
        """Supprime le préfixe du nombre si nécessaire."""
        prefix = self.base_prefixes[unit]
        if number.startswith(prefix):
            number = number[len(prefix):]
        if unit == "hexadécimal":
            number = number.lower()
            if not all(c in '0123456789abcdef' for c in number):
                raise ValueError("Invalid hexadecimal")
        return number

    def add_prefix(self, number, unit):
        """Ajoute le préfixe au nombre si nécessaire."""
        prefix = self.base_prefixes[unit]
        if prefix and not number.startswith(prefix) and unit != "décimal":
            return prefix + number
        return number

    def convert(self, number, source_unit, target_unit):
        source_unit = source_unit.lower()
        target_unit = target_unit.lower()

        if source_unit == "romain":
            number = self.from_roman(number)
    
        if source_unit not in self.conversions or target_unit not in self.conversions[source_unit]:
            raise ValueError("Conversion entre les unités spécifiées n'est pas prise en charge.")
    
        try:
            number = self.remove_prefix(str(number), source_unit)
        except ValueError as e:
            if str(e) == "Invalid hexadecimal":
                raise ValueError("La valeur saisie n'est pas un nombre hexadécimal valide.")
            else:
                raise ValueError("La valeur saisie n'est pas un nombre valide ou n'a pas la bonne base.")
    
        conversion_func = self.conversions[source_unit][target_unit]
        converted_value = conversion_func(number)
    
        # Ajout du préfixe au résultat converti si nécessaire
        converted_value = self.add_prefix(converted_value, target_unit)
    
        return converted_value

class NumbersFrame(ConversionFrame):
    def __init__(self, parent, conversion_func, error_callback):
        super().__init__(parent, conversion_func, ConvertNumbers.units, error_callback)
        self.previous_values = {unit: "" for unit in self.units}

        for unit in self.units:
            if unit in conversion_func.base_prefixes:
                prefix = conversion_func.base_prefixes[unit]
            else:
                # Handle the case where the unit is not in the dictionary
                # For example, you could raise an error or set a default value for prefix
                raise KeyError(f"The unit '{unit}' is not supported.")

    def update_conversions(self, event=None):
        original_unit = self.unit_to_entry_widget[event.widget]
        value_str = self.entries[original_unit].get()
        try:
            # Utilise base=0 pour permettre la conversion automatique selon le préfixe
            value = int(value_str, base=0)  
        except ValueError:
            value = value_str  # conserve la valeur en tant que chaîne si elle n'est pas un nombre entier
        for unit in self.units:
            if unit != original_unit:
                try:
                    converted_value = self.conversion_func.convert(value_str, original_unit, unit)
                    self.entries[unit].set(f"{converted_value}")
                except ValueError as e:
                    self.entries[unit].set("Erreur")
        self.previous_values[original_unit] = self.entries[original_unit].get()