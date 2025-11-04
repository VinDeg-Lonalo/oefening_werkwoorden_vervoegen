"""
Dataset of Dutch verbs with conjugations and ready-to-use sentence templates
for practicing conjugations in:
- o.t.t. (tegenwoordige tijd / present)
- o.v.t. (onvoltooid verleden tijd / simple past)
- v.t.t. (voltooid tegenwoordige tijd / present perfect)
- v.v.t. (voltooid verleden tijd / past perfect)

This module provides:
- VERBS: rich metadata and conjugations for common and irregular verbs
- AUX_CONJUGATION: conjugations for auxiliaries 'hebben' and 'zijn' (present and past)
- SENTENCE_TEMPLATES: sentence templates with blanks and metadata about expected tense
- Helper utilities to compose expected answers for perfect tenses

Conventions:
- Pronoun keys are standardized as:
  ["ik", "jij/je", "u", "hij/zij/het", "wij/we", "jullie", "zij/ze"]
- Tense codes:
  "o.t.t." present (onvoltooid tegenwoordige tijd),
  "o.v.t." simple past (onvoltooid verleden tijd),
  "v.t.t." present perfect (voltooid tegenwoordige tijd),
  "v.v.t." past perfect (voltooid verleden tijd).
- For perfect tenses, the correct answer is "<auxiliary> <past_participle>".
  The auxiliary depends on the verb and pronoun; many motion/state-change verbs use "zijn".

Separable verbs:
- For o.t.t. and o.v.t. the particle typically moves to the end of the clause.
  Such templates explicitly include the particle at the end (e.g., "... ____ ... op.").
- For v.t.t. and v.v.t. the particle stays attached to the past participle
  (e.g., "is opgestaan", "was teruggekomen").
"""

from __future__ import annotations

from typing import Dict, List, Literal, Optional, TypedDict


Pronoun = Literal["ik", "jij/je", "u", "hij/zij/het", "wij/we", "jullie", "zij/ze"]
TenseCode = Literal["o.t.t.", "o.v.t.", "v.t.t.", "v.v.t."]

PRONOUNS: List[Pronoun] = ["ik", "jij/je", "u", "hij/zij/het", "wij/we", "jullie", "zij/ze"]

TENSES: Dict[TenseCode, Dict[str, object]] = {
    "o.t.t.": {
        "label": "tegenwoordige tijd",
        "is_perfect": False,
        "aux_time": None,
        "example": "ik werk",
    },
    "o.v.t.": {
        "label": "onvoltooid verleden tijd",
        "is_perfect": False,
        "aux_time": None,
        "example": "ik werkte",
    },
    "v.t.t.": {
        "label": "voltooid tegenwoordige tijd",
        "is_perfect": True,
        "aux_time": "o.t.t.",
        "example": "ik heb gewerkt / ik ben gekomen",
    },
    "v.v.t.": {
        "label": "voltooid verleden tijd",
        "is_perfect": True,
        "aux_time": "o.v.t.",
        "example": "ik had gewerkt / ik was gekomen",
    },
}


class Conjugations(TypedDict):
    # Finite verb forms
    o_t_t: Dict[Pronoun, str]
    o_v_t: Dict[Pronoun, str]


class VerbEntry(TypedDict, total=False):
    infinitive: str
    translation: str
    # Auxiliary for perfect tenses: "hebben" | "zijn" | ["hebben","zijn"]
    aux: str | List[str]
    past_participle: str
    separable_prefix: Optional[str]  # e.g., "op" for "opstaan"
    type: Literal["regular", "irregular", "separable"]
    notes: str
    conjugations: Conjugations


AUX_CONJUGATION: Dict[str, Dict[TenseCode, Dict[Pronoun, str]]] = {
    "hebben": {
        "o.t.t.": {
            "ik": "heb",
            "jij/je": "hebt",
            "u": "heeft",
            "hij/zij/het": "heeft",
            "wij/we": "hebben",
            "jullie": "hebben",
            "zij/ze": "hebben",
        },
        "o.v.t.": {
            "ik": "had",
            "jij/je": "had",
            "u": "had",
            "hij/zij/het": "had",
            "wij/we": "hadden",
            "jullie": "hadden",
            "zij/ze": "hadden",
        },
    },
    "zijn": {
        "o.t.t.": {
            "ik": "ben",
            "jij/je": "bent",
            "u": "bent",
            "hij/zij/het": "is",
            "wij/we": "zijn",
            "jullie": "zijn",
            "zij/ze": "zijn",
        },
        "o.v.t.": {
            "ik": "was",
            "jij/je": "was",
            "u": "was",
            "hij/zij/het": "was",
            "wij/we": "waren",
            "jullie": "waren",
            "zij/ze": "waren",
        },
    },
}

# Core verbs. This includes common regular and irregular verbs, including some separable ones.
VERBS: Dict[str, VerbEntry] = {
    # Regular verbs
    "werken": {
        "infinitive": "werken",
        "translation": "to work",
        "type": "regular",
        "aux": "hebben",
        "past_participle": "gewerkt",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "werk",
                "jij/je": "werkt",
                "u": "werkt",
                "hij/zij/het": "werkt",
                "wij/we": "werken",
                "jullie": "werken",
                "zij/ze": "werken",
            },
            "o_v_t": {
                "ik": "werkte",
                "jij/je": "werkte",
                "u": "werkte",
                "hij/zij/het": "werkte",
                "wij/we": "werkten",
                "jullie": "werkten",
                "zij/ze": "werkten",
            },
        },
    },
    "maken": {
        "infinitive": "maken",
        "translation": "to make",
        "type": "regular",
        "aux": "hebben",
        "past_participle": "gemaakt",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "maak",
                "jij/je": "maakt",
                "u": "maakt",
                "hij/zij/het": "maakt",
                "wij/we": "maken",
                "jullie": "maken",
                "zij/ze": "maken",
            },
            "o_v_t": {
                "ik": "maakte",
                "jij/je": "maakte",
                "u": "maakte",
                "hij/zij/het": "maakte",
                "wij/we": "maakten",
                "jullie": "maakten",
                "zij/ze": "maakten",
            },
        },
    },
    "spelen": {
        "infinitive": "spelen",
        "translation": "to play",
        "type": "regular",
        "aux": "hebben",
        "past_participle": "gespeeld",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "speel",
                "jij/je": "speelt",
                "u": "speelt",
                "hij/zij/het": "speelt",
                "wij/we": "spelen",
                "jullie": "spelen",
                "zij/ze": "spelen",
            },
            "o_v_t": {
                "ik": "speelde",
                "jij/je": "speelde",
                "u": "speelde",
                "hij/zij/het": "speelde",
                "wij/we": "speelden",
                "jullie": "speelden",
                "zij/ze": "speelden",
            },
        },
    },
    "leren": {
        "infinitive": "leren",
        "translation": "to learn/teach",
        "type": "regular",
        "aux": "hebben",
        "past_participle": "geleerd",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "leer",
                "jij/je": "leert",
                "u": "leert",
                "hij/zij/het": "leert",
                "wij/we": "leren",
                "jullie": "leren",
                "zij/ze": "leren",
            },
            "o_v_t": {
                "ik": "leerde",
                "jij/je": "leerde",
                "u": "leerde",
                "hij/zij/het": "leerde",
                "wij/we": "leerden",
                "jullie": "leerden",
                "zij/ze": "leerden",
            },
        },
    },
    "wonen": {
        "infinitive": "wonen",
        "translation": "to live (reside)",
        "type": "regular",
        "aux": "hebben",
        "past_participle": "gewoond",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "woon",
                "jij/je": "woont",
                "u": "woont",
                "hij/zij/het": "woont",
                "wij/we": "wonen",
                "jullie": "wonen",
                "zij/ze": "wonen",
            },
            "o_v_t": {
                "ik": "woonde",
                "jij/je": "woonde",
                "u": "woonde",
                "hij/zij/het": "woonde",
                "wij/we": "woonden",
                "jullie": "woonden",
                "zij/ze": "woonden",
            },
        },
    },
    "praten": {
        "infinitive": "praten",
        "translation": "to talk",
        "type": "regular",
        "aux": "hebben",
        "past_participle": "gepraat",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "praat",
                "jij/je": "praat",
                "u": "praat",
                "hij/zij/het": "praat",
                "wij/we": "praten",
                "jullie": "praten",
                "zij/ze": "praten",
            },
            "o_v_t": {
                "ik": "praatte",
                "jij/je": "praatte",
                "u": "praatte",
                "hij/zij/het": "praatte",
                "wij/we": "praatten",
                "jullie": "praatten",
                "zij/ze": "praatten",
            },
        },
    },
    "bellen": {
        "infinitive": "bellen",
        "translation": "to call",
        "type": "regular",
        "aux": "hebben",
        "past_participle": "gebeld",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "bel",
                "jij/je": "belt",
                "u": "belt",
                "hij/zij/het": "belt",
                "wij/we": "bellen",
                "jullie": "bellen",
                "zij/ze": "bellen",
            },
            "o_v_t": {
                "ik": "belde",
                "jij/je": "belde",
                "u": "belde",
                "hij/zij/het": "belde",
                "wij/we": "belden",
                "jullie": "belden",
                "zij/ze": "belden",
            },
        },
    },
    "koken": {
        "infinitive": "koken",
        "translation": "to cook",
        "type": "regular",
        "aux": "hebben",
        "past_participle": "gekookt",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "kook",
                "jij/je": "kookt",
                "u": "kookt",
                "hij/zij/het": "kookt",
                "wij/we": "koken",
                "jullie": "koken",
                "zij/ze": "koken",
            },
            "o_v_t": {
                "ik": "kookte",
                "jij/je": "kookte",
                "u": "kookte",
                "hij/zij/het": "kookte",
                "wij/we": "kookten",
                "jullie": "kookten",
                "zij/ze": "kookten",
            },
        },
    },
    "studeren": {
        "infinitive": "studeren",
        "translation": "to study",
        "type": "regular",
        "aux": "hebben",
        "past_participle": "gestudeerd",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "studeer",
                "jij/je": "studeert",
                "u": "studeert",
                "hij/zij/het": "studeert",
                "wij/we": "studeren",
                "jullie": "studeren",
                "zij/ze": "studeren",
            },
            "o_v_t": {
                "ik": "studeerde",
                "jij/je": "studeerde",
                "u": "studeerde",
                "hij/zij/het": "studeerde",
                "wij/we": "studeerden",
                "jullie": "studeerden",
                "zij/ze": "studeerden",
            },
        },
    },
    "reizen": {
        "infinitive": "reizen",
        "translation": "to travel",
        "type": "regular",
        "aux": "hebben",
        "past_participle": "gereisd",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "reis",
                "jij/je": "reist",
                "u": "reist",
                "hij/zij/het": "reist",
                "wij/we": "reizen",
                "jullie": "reizen",
                "zij/ze": "reizen",
            },
            "o_v_t": {
                "ik": "reisde",
                "jij/je": "reisde",
                "u": "reisde",
                "hij/zij/het": "reisde",
                "wij/we": "reisden",
                "jullie": "reisden",
                "zij/ze": "reisden",
            },
        },
    },
    "zetten": {
        "infinitive": "zetten",
        "translation": "to put/place",
        "type": "regular",
        "aux": "hebben",
        "past_participle": "gezet",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "zet",
                "jij/je": "zet",
                "u": "zet",
                "hij/zij/het": "zet",
                "wij/we": "zetten",
                "jullie": "zetten",
                "zij/ze": "zetten",
            },
            "o_v_t": {
                "ik": "zette",
                "jij/je": "zette",
                "u": "zette",
                "hij/zij/het": "zette",
                "wij/we": "zetten",
                "jullie": "zetten",
                "zij/ze": "zetten",
            },
        },
    },
    "fietsen": {
        "infinitive": "fietsen",
        "translation": "to cycle",
        "type": "regular",
        "aux": "hebben",
        "past_participle": "gefietst",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "fiets",
                "jij/je": "fietst",
                "u": "fietst",
                "hij/zij/het": "fietst",
                "wij/we": "fietsen",
                "jullie": "fietsen",
                "zij/ze": "fietsen",
            },
            "o_v_t": {
                "ik": "fietste",
                "jij/je": "fietste",
                "u": "fietste",
                "hij/zij/het": "fietste",
                "wij/we": "fietsten",
                "jullie": "fietsten",
                "zij/ze": "fietsten",
            },
        },
    },

    # Irregular verbs
    "zijn": {
        "infinitive": "zijn",
        "translation": "to be",
        "type": "irregular",
        "aux": "zijn",
        "past_participle": "geweest",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "ben",
                "jij/je": "bent",
                "u": "bent",
                "hij/zij/het": "is",
                "wij/we": "zijn",
                "jullie": "zijn",
                "zij/ze": "zijn",
            },
            "o_v_t": {
                "ik": "was",
                "jij/je": "was",
                "u": "was",
                "hij/zij/het": "was",
                "wij/we": "waren",
                "jullie": "waren",
                "zij/ze": "waren",
            },
        },
    },
    "hebben": {
        "infinitive": "hebben",
        "translation": "to have",
        "type": "irregular",
        "aux": "hebben",
        "past_participle": "gehad",
        "separable_prefix": None,
        "conjugations": AUX_CONJUGATION["hebben"] | {},  # reuse exact forms
    },
    "gaan": {
        "infinitive": "gaan",
        "translation": "to go",
        "type": "irregular",
        "aux": "zijn",
        "past_participle": "gegaan",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "ga",
                "jij/je": "gaat",
                "u": "gaat",
                "hij/zij/het": "gaat",
                "wij/we": "gaan",
                "jullie": "gaan",
                "zij/ze": "gaan",
            },
            "o_v_t": {
                "ik": "ging",
                "jij/je": "ging",
                "u": "ging",
                "hij/zij/het": "ging",
                "wij/we": "gingen",
                "jullie": "gingen",
                "zij/ze": "gingen",
            },
        },
    },
    "komen": {
        "infinitive": "komen",
        "translation": "to come",
        "type": "irregular",
        "aux": "zijn",
        "past_participle": "gekomen",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "kom",
                "jij/je": "komt",
                "u": "komt",
                "hij/zij/het": "komt",
                "wij/we": "komen",
                "jullie": "komen",
                "zij/ze": "komen",
            },
            "o_v_t": {
                "ik": "kwam",
                "jij/je": "kwam",
                "u": "kwam",
                "hij/zij/het": "kwam",
                "wij/we": "kwamen",
                "jullie": "kwamen",
                "zij/ze": "kwamen",
            },
        },
    },
    "blijven": {
        "infinitive": "blijven",
        "translation": "to stay",
        "type": "irregular",
        "aux": "zijn",
        "past_participle": "gebleven",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "blijf",
                "jij/je": "blijft",
                "u": "blijft",
                "hij/zij/het": "blijft",
                "wij/we": "blijven",
                "jullie": "blijven",
                "zij/ze": "blijven",
            },
            "o_v_t": {
                "ik": "bleef",
                "jij/je": "bleef",
                "u": "bleef",
                "hij/zij/het": "bleef",
                "wij/we": "bleven",
                "jullie": "bleven",
                "zij/ze": "bleven",
            },
        },
    },
    "worden": {
        "infinitive": "worden",
        "translation": "to become",
        "type": "irregular",
        "aux": "zijn",
        "past_participle": "geworden",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "word",
                "jij/je": "wordt",
                "u": "wordt",
                "hij/zij/het": "wordt",
                "wij/we": "worden",
                "jullie": "worden",
                "zij/ze": "worden",
            },
            "o_v_t": {
                "ik": "werd",
                "jij/je": "werd",
                "u": "werd",
                "hij/zij/het": "werd",
                "wij/we": "werden",
                "jullie": "werden",
                "zij/ze": "werden",
            },
        },
    },
    "vallen": {
        "infinitive": "vallen",
        "translation": "to fall",
        "type": "irregular",
        "aux": "zijn",
        "past_participle": "gevallen",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "val",
                "jij/je": "valt",
                "u": "valt",
                "hij/zij/het": "valt",
                "wij/we": "vallen",
                "jullie": "vallen",
                "zij/ze": "vallen",
            },
            "o_v_t": {
                "ik": "viel",
                "jij/je": "viel",
                "u": "viel",
                "hij/zij/het": "viel",
                "wij/we": "vielen",
                "jullie": "vielen",
                "zij/ze": "vielen",
            },
        },
    },
    "beginnen": {
        "infinitive": "beginnen",
        "translation": "to begin",
        "type": "irregular",
        "aux": "zijn",
        "past_participle": "begonnen",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "begin",
                "jij/je": "begint",
                "u": "begint",
                "hij/zij/het": "begint",
                "wij/we": "beginnen",
                "jullie": "beginnen",
                "zij/ze": "beginnen",
            },
            "o_v_t": {
                "ik": "begon",
                "jij/je": "begon",
                "u": "begon",
                "hij/zij/het": "begon",
                "wij/we": "begonnen",
                "jullie": "begonnen",
                "zij/ze": "begonnen",
            },
        },
    },
    "lopen": {
        "infinitive": "lopen",
        "translation": "to walk",
        "type": "irregular",
        "aux": ["hebben", "zijn"],
        "past_participle": "gelopen",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "loop",
                "jij/je": "loopt",
                "u": "loopt",
                "hij/zij/het": "loopt",
                "wij/we": "lopen",
                "jullie": "lopen",
                "zij/ze": "lopen",
            },
            "o_v_t": {
                "ik": "liep",
                "jij/je": "liep",
                "u": "liep",
                "hij/zij/het": "liep",
                "wij/we": "liepen",
                "jullie": "liepen",
                "zij/ze": "liepen",
            },
        },
    },
    "rijden": {
        "infinitive": "rijden",
        "translation": "to drive/ride",
        "type": "irregular",
        "aux": ["hebben", "zijn"],
        "past_participle": "gereden",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "rijd",
                "jij/je": "rijdt",
                "u": "rijdt",
                "hij/zij/het": "rijdt",
                "wij/we": "rijden",
                "jullie": "rijden",
                "zij/ze": "rijden",
            },
            "o_v_t": {
                "ik": "reed",
                "jij/je": "reed",
                "u": "reed",
                "hij/zij/het": "reed",
                "wij/we": "reden",
                "jullie": "reden",
                "zij/ze": "reden",
            },
        },
    },
    "kijken": {
        "infinitive": "kijken",
        "translation": "to look/watch",
        "type": "irregular",
        "aux": "hebben",
        "past_participle": "gekeken",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "kijk",
                "jij/je": "kijkt",
                "u": "kijkt",
                "hij/zij/het": "kijkt",
                "wij/we": "kijken",
                "jullie": "kijken",
                "zij/ze": "kijken",
            },
            "o_v_t": {
                "ik": "keek",
                "jij/je": "keek",
                "u": "keek",
                "hij/zij/het": "keek",
                "wij/we": "keken",
                "jullie": "keken",
                "zij/ze": "keken",
            },
        },
    },
    "kopen": {
        "infinitive": "kopen",
        "translation": "to buy",
        "type": "irregular",
        "aux": "hebben",
        "past_participle": "gekocht",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "koop",
                "jij/je": "koopt",
                "u": "koopt",
                "hij/zij/het": "koopt",
                "wij/we": "kopen",
                "jullie": "kopen",
                "zij/ze": "kopen",
            },
            "o_v_t": {
                "ik": "kocht",
                "jij/je": "kocht",
                "u": "kocht",
                "hij/zij/het": "kocht",
                "wij/we": "kochten",
                "jullie": "kochten",
                "zij/ze": "kochten",
            },
        },
    },
    "denken": {
        "infinitive": "denken",
        "translation": "to think",
        "type": "irregular",
        "aux": "hebben",
        "past_participle": "gedacht",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "denk",
                "jij/je": "denkt",
                "u": "denkt",
                "hij/zij/het": "denkt",
                "wij/we": "denken",
                "jullie": "denken",
                "zij/ze": "denken",
            },
            "o_v_t": {
                "ik": "dacht",
                "jij/je": "dacht",
                "u": "dacht",
                "hij/zij/het": "dacht",
                "wij/we": "dachten",
                "jullie": "dachten",
                "zij/ze": "dachten",
            },
        },
    },
    "geven": {
        "infinitive": "geven",
        "translation": "to give",
        "type": "irregular",
        "aux": "hebben",
        "past_participle": "gegeven",
        "separable_prefix": None,
        "conjugations": {
                "o_t_t": {
                    "ik": "geef",
                    "jij/je": "geeft",
                    "u": "geeft",
                    "hij/zij/het": "geeft",
                    "wij/we": "geven",
                    "jullie": "geven",
                    "zij/ze": "geven",
                },
                "o_v_t": {
                    "ik": "gaf",
                    "jij/je": "gaf",
                    "u": "gaf",
                    "hij/zij/het": "gaf",
                    "wij/we": "gaven",
                    "jullie": "gaven",
                    "zij/ze": "gaven",
                },
        },
    },
    "zien": {
        "infinitive": "zien",
        "translation": "to see",
        "type": "irregular",
        "aux": "hebben",
        "past_participle": "gezien",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "zie",
                "jij/je": "ziet",
                "u": "ziet",
                "hij/zij/het": "ziet",
                "wij/we": "zien",
                "jullie": "zien",
                "zij/ze": "zien",
            },
            "o_v_t": {
                "ik": "zag",
                "jij/je": "zag",
                "u": "zag",
                "hij/zij/het": "zag",
                "wij/we": "zagen",
                "jullie": "zagen",
                "zij/ze": "zagen",
            },
        },
    },
    "vinden": {
        "infinitive": "vinden",
        "translation": "to find",
        "type": "irregular",
        "aux": "hebben",
        "past_participle": "gevonden",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "vind",
                "jij/je": "vindt",
                "u": "vindt",
                "hij/zij/het": "vindt",
                "wij/we": "vinden",
                "jullie": "vinden",
                "zij/ze": "vinden",
            },
            "o_v_t": {
                "ik": "vond",
                "jij/je": "vond",
                "u": "vond",
                "hij/zij/het": "vond",
                "wij/we": "vonden",
                "jullie": "vonden",
                "zij/ze": "vonden",
            },
        },
    },
    "weten": {
        "infinitive": "weten",
        "translation": "to know",
        "type": "irregular",
        "aux": "hebben",
        "past_participle": "geweten",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "weet",
                "jij/je": "weet",
                "u": "weet",
                "hij/zij/het": "weet",
                "wij/we": "weten",
                "jullie": "weten",
                "zij/ze": "weten",
            },
            "o_v_t": {
                "ik": "wist",
                "jij/je": "wist",
                "u": "wist",
                "hij/zij/het": "wist",
                "wij/we": "wisten",
                "jullie": "wisten",
                "zij/ze": "wisten",
            },
        },
    },
    "nemen": {
        "infinitive": "nemen",
        "translation": "to take",
        "type": "irregular",
        "aux": "hebben",
        "past_participle": "genomen",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "neem",
                "jij/je": "neemt",
                "u": "neemt",
                "hij/zij/het": "neemt",
                "wij/we": "nemen",
                "jullie": "nemen",
                "zij/ze": "nemen",
            },
            "o_v_t": {
                "ik": "nam",
                "jij/je": "nam",
                "u": "nam",
                "hij/zij/het": "nam",
                "wij/we": "namen",
                "jullie": "namen",
                "zij/ze": "namen",
            },
        },
    },
    "drinken": {
        "infinitive": "drinken",
        "translation": "to drink",
        "type": "irregular",
        "aux": "hebben",
        "past_participle": "gedronken",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "drink",
                "jij/je": "drinkt",
                "u": "drinkt",
                "hij/zij/het": "drinkt",
                "wij/we": "drinken",
                "jullie": "drinken",
                "zij/ze": "drinken",
            },
            "o_v_t": {
                "ik": "dronk",
                "jij/je": "dronk",
                "u": "dronk",
                "hij/zij/het": "dronk",
                "wij/we": "dronken",
                "jullie": "dronken",
                "zij/ze": "dronken",
            },
        },
    },
    "slapen": {
        "infinitive": "slapen",
        "translation": "to sleep",
        "type": "irregular",
        "aux": "hebben",
        "past_participle": "geslapen",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "slaap",
                "jij/je": "slaapt",
                "u": "slaapt",
                "hij/zij/het": "slaapt",
                "wij/we": "slapen",
                "jullie": "slapen",
                "zij/ze": "slapen",
            },
            "o_v_t": {
                "ik": "sliep",
                "jij/je": "sliep",
                "u": "sliep",
                "hij/zij/het": "sliep",
                "wij/we": "sliepen",
                "jullie": "sliepen",
                "zij/ze": "sliepen",
            },
        },
    },
    "houden": {
        "infinitive": "houden",
        "translation": "to hold/like",
        "type": "irregular",
        "aux": "hebben",
        "past_participle": "gehouden",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "houd",
                "jij/je": "houdt",
                "u": "houdt",
                "hij/zij/het": "houdt",
                "wij/we": "houden",
                "jullie": "houden",
                "zij/ze": "houden",
            },
            "o_v_t": {
                "ik": "hield",
                "jij/je": "hield",
                "u": "hield",
                "hij/zij/het": "hield",
                "wij/we": "hielden",
                "jullie": "hielden",
                "zij/ze": "hielden",
            },
        },
    },
    "staan": {
        "infinitive": "staan",
        "translation": "to stand",
        "type": "irregular",
        "aux": "hebben",
        "past_participle": "gestaan",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "sta",
                "jij/je": "staat",
                "u": "staat",
                "hij/zij/het": "staat",
                "wij/we": "staan",
                "jullie": "staan",
                "zij/ze": "staan",
            },
            "o_v_t": {
                "ik": "stond",
                "jij/je": "stond",
                "u": "stond",
                "hij/zij/het": "stond",
                "wij/we": "stonden",
                "jullie": "stonden",
                "zij/ze": "stonden",
            },
        },
    },
    "lezen": {
        "infinitive": "lezen",
        "translation": "to read",
        "type": "irregular",
        "aux": "hebben",
        "past_participle": "gelezen",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "lees",
                "jij/je": "leest",
                "u": "leest",
                "hij/zij/het": "leest",
                "wij/we": "lezen",
                "jullie": "lezen",
                "zij/ze": "lezen",
            },
            "o_v_t": {
                "ik": "las",
                "jij/je": "las",
                "u": "las",
                "hij/zij/het": "las",
                "wij/we": "lazen",
                "jullie": "lazen",
                "zij/ze": "lazen",
            },
        },
    },
    "schrijven": {
        "infinitive": "schrijven",
        "translation": "to write",
        "type": "irregular",
        "aux": "hebben",
        "past_participle": "geschreven",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "schrijf",
                "jij/je": "schrijft",
                "u": "schrijft",
                "hij/zij/het": "schrijft",
                "wij/we": "schrijven",
                "jullie": "schrijven",
                "zij/ze": "schrijven",
            },
            "o_v_t": {
                "ik": "schreef",
                "jij/je": "schreef",
                "u": "schreef",
                "hij/zij/het": "schreef",
                "wij/we": "schreven",
                "jullie": "schreven",
                "zij/ze": "schreven",
            },
        },
    },
    "spreken": {
        "infinitive": "spreken",
        "translation": "to speak",
        "type": "irregular",
        "aux": "hebben",
        "past_participle": "gesproken",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "spreek",
                "jij/je": "spreekt",
                "u": "spreekt",
                "hij/zij/het": "spreekt",
                "wij/we": "spreken",
                "jullie": "spreken",
                "zij/ze": "spreken",
            },
            "o_v_t": {
                "ik": "sprak",
                "jij/je": "sprak",
                "u": "sprak",
                "hij/zij/het": "sprak",
                "wij/we": "spraken",
                "jullie": "spraken",
                "zij/ze": "spraken",
            },
        },
    },
    "doen": {
        "infinitive": "doen",
        "translation": "to do",
        "type": "irregular",
        "aux": "hebben",
        "past_participle": "gedaan",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "doe",
                "jij/je": "doet",
                "u": "doet",
                "hij/zij/het": "doet",
                "wij/we": "doen",
                "jullie": "doen",
                "zij/ze": "doen",
            },
            "o_v_t": {
                "ik": "deed",
                "jij/je": "deed",
                "u": "deed",
                "hij/zij/het": "deed",
                "wij/we": "deden",
                "jullie": "deden",
                "zij/ze": "deden",
            },
        },
    },
    "eten": {
        "infinitive": "eten",
        "translation": "to eat",
        "type": "irregular",
        "aux": "hebben",
        "past_participle": "gegeten",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "eet",
                "jij/je": "eet",
                "u": "eet",
                "hij/zij/het": "eet",
                "wij/we": "eten",
                "jullie": "eten",
                "zij/ze": "eten",
            },
            "o_v_t": {
                "ik": "at",
                "jij/je": "at",
                "u": "at",
                "hij/zij/het": "at",
                "wij/we": "aten",
                "jullie": "aten",
                "zij/ze": "aten",
            },
        },
    },
    "helpen": {
        "infinitive": "helpen",
        "translation": "to help",
        "type": "irregular",
        "aux": "hebben",
        "past_participle": "geholpen",
        "separable_prefix": None,
        "conjugations": {
            "o_t_t": {
                "ik": "help",
                "jij/je": "helpt",
                "u": "helpt",
                "hij/zij/het": "helpt",
                "wij/we": "helpen",
                "jullie": "helpen",
                "zij/ze": "helpen",
            },
            "o_v_t": {
                "ik": "hielp",
                "jij/je": "hielp",
                "u": "hielp",
                "hij/zij/het": "hielp",
                "wij/we": "hielpen",
                "jullie": "hielpen",
                "zij/ze": "hielpen",
            },
        },
    },

    # Separable verbs
    "opstaan": {
        "infinitive": "opstaan",
        "translation": "to get up",
        "type": "separable",
        "aux": "zijn",
        "past_participle": "opgestaan",
        "separable_prefix": "op",
        "conjugations": {
            "o_t_t": {
                "ik": "sta",
                "jij/je": "staat",
                "u": "staat",
                "hij/zij/het": "staat",
                "wij/we": "staan",
                "jullie": "staan",
                "zij/ze": "staan",
            },
            "o_v_t": {
                "ik": "stond",
                "jij/je": "stond",
                "u": "stond",
                "hij/zij/het": "stond",
                "wij/we": "stonden",
                "jullie": "stonden",
                "zij/ze": "stonden",
            },
        },
    },
    "afwassen": {
        "infinitive": "afwassen",
        "translation": "to do the dishes",
        "type": "separable",
        "aux": "hebben",
        "past_participle": "afgewassen",
        "separable_prefix": "af",
        "conjugations": {
            "o_t_t": {
                "ik": "was",
                "jij/je": "wast",
                "u": "wast",
                "hij/zij/het": "wast",
                "wij/we": "wassen",
                "jullie": "wassen",
                "zij/ze": "wassen",
            },
            "o_v_t": {
                "ik": "waste",
                "jij/je": "waste",
                "u": "waste",
                "hij/zij/het": "waste",
                "wij/we": "wasten",
                "jullie": "wasten",
                "zij/ze": "wasten",
            },
        },
    },
    "opbellen": {
        "infinitive": "opbellen",
        "translation": "to call (on the phone)",
        "type": "separable",
        "aux": "hebben",
        "past_participle": "opgebeld",
        "separable_prefix": "op",
        "conjugations": {
            "o_t_t": {
                "ik": "bel",
                "jij/je": "belt",
                "u": "belt",
                "hij/zij/het": "belt",
                "wij/we": "bellen",
                "jullie": "bellen",
                "zij/ze": "bellen",
            },
            "o_v_t": {
                "ik": "belde",
                "jij/je": "belde",
                "u": "belde",
                "hij/zij/het": "belde",
                "wij/we": "belden",
                "jullie": "belden",
                "zij/ze": "belden",
            },
        },
    },
    "terugkomen": {
        "infinitive": "terugkomen",
        "translation": "to come back",
        "type": "separable",
        "aux": "zijn",
        "past_participle": "teruggekomen",
        "separable_prefix": "terug",
        "conjugations": {
            "o_t_t": {
                "ik": "kom",
                "jij/je": "komt",
                "u": "komt",
                "hij/zij/het": "komt",
                "wij/we": "komen",
                "jullie": "komen",
                "zij/ze": "komen",
            },
            "o_v_t": {
                "ik": "kwam",
                "jij/je": "kwam",
                "u": "kwam",
                "hij/zij/het": "kwam",
                "wij/we": "kwamen",
                "jullie": "kwamen",
                "zij/ze": "kwamen",
            },
        },
    },
    "meenemen": {
        "infinitive": "meenemen",
        "translation": "to take along",
        "type": "separable",
        "aux": "hebben",
        "past_participle": "meegenomen",
        "separable_prefix": "mee",
        "conjugations": {
            "o_t_t": {
                "ik": "neem",
                "jij/je": "neemt",
                "u": "neemt",
                "hij/zij/het": "neemt",
                "wij/we": "nemen",
                "jullie": "nemen",
                "zij/ze": "nemen",
            },
            "o_v_t": {
                "ik": "nam",
                "jij/je": "nam",
                "u": "nam",
                "hij/zij/het": "nam",
                "wij/we": "namen",
                "jullie": "namen",
                "zij/ze": "namen",
            },
        },
    },
    "meebrengen": {
        "infinitive": "meebrengen",
        "translation": "to bring along",
        "type": "separable",
        "aux": "hebben",
        "past_participle": "meegebracht",
        "separable_prefix": "mee",
        "conjugations": {
            "o_t_t": {
                "ik": "breng",
                "jij/je": "brengt",
                "u": "brengt",
                "hij/zij/het": "brengt",
                "wij/we": "brengen",
                "jullie": "brengen",
                "zij/ze": "brengen",
            },
            "o_v_t": {
                "ik": "bracht",
                "jij/je": "bracht",
                "u": "bracht",
                "hij/zij/het": "bracht",
                "wij/we": "brachten",
                "jullie": "brachten",
                "zij/ze": "brachten",
            },
        },
    },
}

ALL_VERBS: List[str] = sorted(VERBS.keys())


class Template(TypedDict, total=False):
    id: str
    template: str  # sentence with a single "____" blank for the verb/verb phrase
    tense: TenseCode
    pronoun: Pronoun
    # If provided, limit the verb choices to these infinitives (for thematic/natural fit)
    allowed_verbs: List[str]
    # Optional hint shown alongside the prompt (e.g., "ovt", "vvt")
    hint: str
    notes: str


SENTENCE_TEMPLATES: List[Template] = [
    # Present (o.t.t.)
    {"id": "ott_1", "template": "Ik ____ elke dag om acht uur.", "tense": "o.t.t.", "pronoun": "ik", "allowed_verbs": ["opstaan"], "hint": "o.t.t.", "notes": "Separable: opstaan -> particle at end for o.t.t."},
    {"id": "ott_1b", "template": "Ik ____ elke dag om acht uur op.", "tense": "o.t.t.", "pronoun": "ik", "allowed_verbs": ["opstaan"], "hint": "o.t.t."},
    {"id": "ott_2", "template": "Hij ____ in Amsterdam.", "tense": "o.t.t.", "pronoun": "hij/zij/het", "allowed_verbs": ["wonen"], "hint": "o.t.t."},
    {"id": "ott_3", "template": "Wij ____ Nederlands in de avond.", "tense": "o.t.t.", "pronoun": "wij/we", "allowed_verbs": ["leren", "studeren"], "hint": "o.t.t."},
    {"id": "ott_4", "template": "Zij ____ elke vrijdag voetbal.", "tense": "o.t.t.", "pronoun": "zij/ze", "allowed_verbs": ["spelen"], "hint": "o.t.t."},
    {"id": "ott_5", "template": "Jullie ____ vaak naar films.", "tense": "o.t.t.", "pronoun": "jullie", "allowed_verbs": ["kijken"], "hint": "o.t.t."},
    {"id": "ott_6", "template": "U ____ de afwas.", "tense": "o.t.t.", "pronoun": "u", "allowed_verbs": ["doen", "afwassen"], "hint": "o.t.t."},
    {"id": "ott_6b", "template": "U ____ de afwas af.", "tense": "o.t.t.", "pronoun": "u", "allowed_verbs": ["afwassen"], "hint": "o.t.t."},
    {"id": "ott_7", "template": "Jij ____ koffie in de ochtend.", "tense": "o.t.t.", "pronoun": "jij/je", "allowed_verbs": ["drinken", "maken"], "hint": "o.t.t."},
    {"id": "ott_8", "template": "Ik ____ in een ziekenhuis.", "tense": "o.t.t.", "pronoun": "ik", "allowed_verbs": ["werken"], "hint": "o.t.t."},
    {"id": "ott_9", "template": "Hij ____ snel naar het station.", "tense": "o.t.t.", "pronoun": "hij/zij/het", "allowed_verbs": ["lopen", "rijden", "gaan", "fietsen"], "hint": "o.t.t."},
    {"id": "ott_10", "template": "Wij ____ het boek samen.", "tense": "o.t.t.", "pronoun": "wij/we", "allowed_verbs": ["lezen"], "hint": "o.t.t."},
    {"id": "ott_11", "template": "Zij ____ elke dag om zes uur.", "tense": "o.t.t.", "pronoun": "zij/ze", "allowed_verbs": ["komen", "opstaan"], "hint": "o.t.t."},
    {"id": "ott_12", "template": "Ik ____ mijn vrienden in het weekend.", "tense": "o.t.t.", "pronoun": "ik", "allowed_verbs": ["bellen", "opbellen", "bezoeken" if False else "bellen"], "hint": "o.t.t.", "notes": "Gebruik opbellen voor separable variant."},
    {"id": "ott_13", "template": "Jullie ____ altijd op tijd.", "tense": "o.t.t.", "pronoun": "jullie", "allowed_verbs": ["komen", "zijn"], "hint": "o.t.t."},

    # Simple past (o.v.t.)
    {"id": "ovt_1", "template": "Gisteren ____ ik naar het park.", "tense": "o.v.t.", "pronoun": "ik", "allowed_verbs": ["lopen", "gaan", "fietsen", "rijden"], "hint": "o.v.t."},
    {"id": "ovt_2", "template": "Vorige week ____ hij een auto.", "tense": "o.v.t.", "pronoun": "hij/zij/het", "allowed_verbs": ["kopen", "verkopen" if False else "kopen"], "hint": "o.v.t."},
    {"id": "ovt_3", "template": "Toen ____ wij in Utrecht.", "tense": "o.v.t.", "pronoun": "wij/we", "allowed_verbs": ["wonen"], "hint": "o.v.t."},
    {"id": "ovt_4", "template": "Gisteren ____ jullie de afwas.", "tense": "o.v.t.", "pronoun": "jullie", "allowed_verbs": ["doen", "afwassen"], "hint": "o.v.t."},
    {"id": "ovt_4b", "template": "Gisteren ____ jullie de afwas af.", "tense": "o.v.t.", "pronoun": "jullie", "allowed_verbs": ["afwassen"], "hint": "o.v.t."},
    {"id": "ovt_5", "template": "Vorig jaar ____ zij naar Nederland.", "tense": "o.v.t.", "pronoun": "zij/ze", "allowed_verbs": ["komen", "verhuizen" if False else "komen"], "hint": "o.v.t."},
    {"id": "ovt_6", "template": "Eerder ____ ik weinig Nederlands.", "tense": "o.v.t.", "pronoun": "ik", "allowed_verbs": ["weten", "spreken", "verstaan" if False else "spreken"], "hint": "o.v.t."},
    {"id": "ovt_7", "template": "Vanochtend ____ hij vroeg op.", "tense": "o.v.t.", "pronoun": "hij/zij/het", "allowed_verbs": ["opstaan"], "hint": "o.v.t."},
    {"id": "ovt_8", "template": "Gisteravond ____ we tot laat door.", "tense": "o.v.t.", "pronoun": "wij/we", "allowed_verbs": ["werken", "studeren"], "hint": "o.v.t."},

    # Present perfect (v.t.t.)
    {"id": "vtt_1", "template": "Ik ____ al ontbeten.", "tense": "v.t.t.", "pronoun": "ik", "allowed_verbs": ["eten"], "hint": "v.t.t."},
    {"id": "vtt_2", "template": "Hij ____ het boek gelezen.", "tense": "v.t.t.", "pronoun": "hij/zij/het", "allowed_verbs": ["lezen"], "hint": "v.t.t."},
    {"id": "vtt_3", "template": "Wij ____ gisteren een film gekeken.", "tense": "v.t.t.", "pronoun": "wij/we", "allowed_verbs": ["kijken"], "hint": "v.t.t."},
    {"id": "vtt_4", "template": "Zij ____ met de auto naar huis gereden.", "tense": "v.t.t.", "pronoun": "zij/ze", "allowed_verbs": ["rijden"], "hint": "v.t.t."},
    {"id": "vtt_5", "template": "Jullie ____ de bloemen gekocht.", "tense": "v.t.t.", "pronoun": "jullie", "allowed_verbs": ["kopen"], "hint": "v.t.t."},
    {"id": "vtt_6", "template": "U ____ alles zelf gedaan.", "tense": "v.t.t.", "pronoun": "u", "allowed_verbs": ["doen"], "hint": "v.t.t."},
    {"id": "vtt_7", "template": "Hij ____ te laat gekomen.", "tense": "v.t.t.", "pronoun": "hij/zij/het", "allowed_verbs": ["komen"], "hint": "v.t.t."},
    {"id": "vtt_8", "template": "Ik ____ om zeven uur opgestaan.", "tense": "v.t.t.", "pronoun": "ik", "allowed_verbs": ["opstaan"], "hint": "v.t.t."},
    {"id": "vtt_9", "template": "Wij ____ het pakket meegebracht.", "tense": "v.t.t.", "pronoun": "wij/we", "allowed_verbs": ["meebrengen"], "hint": "v.t.t."},
    {"id": "vtt_10", "template": "Zij ____ de tassen meegenomen.", "tense": "v.t.t.", "pronoun": "zij/ze", "allowed_verbs": ["meenemen"], "hint": "v.t.t."},

    # Past perfect (v.v.t.)
    {"id": "vvt_1", "template": "Toen ik aankwam, ____ hij al gegeten.", "tense": "v.v.t.", "pronoun": "hij/zij/het", "allowed_verbs": ["eten"], "hint": "v.v.t."},
    {"id": "vvt_2", "template": "Wij ____ het werk al gedaan voordat hij kwam.", "tense": "v.v.t.", "pronoun": "wij/we", "allowed_verbs": ["doen"], "hint": "v.v.t."},
    {"id": "vvt_3", "template": "Zij ____ al naar buiten gegaan toen het regende.", "tense": "v.v.t.", "pronoun": "zij/ze", "allowed_verbs": ["gaan"], "hint": "v.v.t."},
    {"id": "vvt_4", "template": "Ik ____ mijn telefoon niet meegenomen.", "tense": "v.v.t.", "pronoun": "ik", "allowed_verbs": ["meenemen"], "hint": "v.v.t."},
    {"id": "vvt_5", "template": "Jullie ____ het huiswerk al gemaakt.", "tense": "v.v.t.", "pronoun": "jullie", "allowed_verbs": ["maken"], "hint": "v.v.t."},
    {"id": "vvt_6", "template": "Hij ____ te lang gebleven.", "tense": "v.v.t.", "pronoun": "hij/zij/het", "allowed_verbs": ["blijven"], "hint": "v.v.t."},
    {"id": "vvt_7", "template": "We ____ hem al opgebeld voordat we vertrokken.", "tense": "v.v.t.", "pronoun": "wij/we", "allowed_verbs": ["opbellen"], "hint": "v.v.t."},
    {"id": "vvt_8", "template": "Zij ____ net teruggekomen toen de bel ging.", "tense": "v.v.t.", "pronoun": "zij/ze", "allowed_verbs": ["terugkomen"], "hint": "v.v.t."},
]


def get_finite_form(infinitive: str, tense: TenseCode, pronoun: Pronoun) -> str:
    """
    Return the expected finite form for o.t.t./o.v.t. or the full verb phrase for v.t.t./v.v.t.
    For perfect tenses, returns "<aux> <past_participle>" using the correct auxiliary and its conjugation.
    """
    if infinitive not in VERBS:
        raise KeyError(f"Unknown verb: {infinitive}")
    entry = VERBS[infinitive]
    if tense in ("o.t.t.", "o.v.t."):
        key = "o_t_t" if tense == "o.t.t." else "o_v_t"
        return entry["conjugations"][key][pronoun]
    # Perfect tenses
    aux_time = TENSES[tense]["aux_time"]  # type: ignore
    assert aux_time in ("o.t.t.", "o.v.t.")
    aux_used = _pick_aux(entry)
    aux_form = AUX_CONJUGATION[aux_used][aux_time][pronoun]  # type: ignore[index]
    return f"{aux_form} {entry['past_participle']}"


def _pick_aux(entry: VerbEntry) -> str:
    """
    Pick an auxiliary for perfect tenses.
    If the entry lists multiple auxiliaries, defaults to 'hebben' (neutral) unless the verb is a canonical
    zijn-verb (e.g., komen/gaan/blijven/worden/vallen/beginnen/opstaan/terugkomen) where 'zijn' is preferred.
    """
    aux = entry["aux"]
    if isinstance(aux, str):
        return aux
    # Heuristic: prefer 'zijn' for typical motion/state-change verbs
    prefer_zijn = entry["aux"] and "zijn" in entry["aux"] and entry["infinitive"] in {
        "gaan", "komen", "blijven", "worden", "vallen",
        "beginnen", "opstaan", "terugkomen",
    }
    if prefer_zijn:
        return "zijn"
    # Otherwise default to 'hebben'
    return "hebben"


def list_templates_for_tense(tense: TenseCode) -> List[Template]:
    return [t for t in SENTENCE_TEMPLATES if t["tense"] == tense]


def list_verbs_for_template(t: Template) -> List[str]:
    return t.get("allowed_verbs", ALL_VERBS)


__all__ = [
    "PRONOUNS",
    "TENSES",
    "AUX_CONJUGATION",
    "VERBS",
    "ALL_VERBS",
    "SENTENCE_TEMPLATES",
    "get_finite_form",
    "list_templates_for_tense",
    "list_verbs_for_template",
]