#!/usr/bin/env python3
"""
Interactieve CLI-app om Nederlandse werkwoordvervoegingen te trainen.

Functies:
- Oefen o.t.t. (tegenwoordige tijd), o.v.t. (onvoltooid verleden tijd),
  v.t.t. (voltooid tegenwoordige tijd) en v.v.t. (voltooid verleden tijd).
- Gebruikt een dataset met veel voorkomende en onregelmatige werkwoorden.
- Biedt een voorbereide zin aan, vermeldt het te vervoegen werkwoord en de gevraagde tijd.
- Controleert je invoer en geeft directe feedback en uitleg.

Gebruik:
- Start de app: `python -m Werkwoorden.src.main` of `python Werkwoorden/src/main.py`
- Volg de prompts in de terminal.
"""

from __future__ import annotations

import random
import re
from dataclasses import dataclass
from typing import List, Tuple, Optional, cast

# Dataset met werkwoorden, tijden en zinnen (+ gedeelde Literal-typen voor type-checking)
try:
    # Uitvoer via module (aanbevolen): python -m Werkwoorden.src.main
    from .verbs_data import (
        TENSES,
        VERBS,
        AUX_CONJUGATION,
        get_finite_form,
        list_templates_for_tense,
        TenseCode,
        Pronoun,
    )
except Exception:
    # Fallback voor directe uitvoer als script: python Werkwoorden/src/main.py
    from verbs_data import (  # type: ignore
        TENSES,
        VERBS,
        AUX_CONJUGATION,
        get_finite_form,
        list_templates_for_tense,
        TenseCode,
        Pronoun,
    )


@dataclass
class Question:
    template_id: str
    template_text: str
    tense: TenseCode
    pronoun: Pronoun
    verb_infinitive: str
    expected_answers: List[str]  # genormaliseerde correcte antwoorden
    display_answers: List[str]  # nette weergave voor feedback
    explanation: str  # korte uitleg
    hint: str  # bijv. 'o.t.t.'


def normalize_answer(s: str) -> str:
    """
    Normaliseer een antwoord voor robuuste vergelijking:
    - lowercase
    - trimmen
    - samenvouwen van whitespace
    - verwijderen van eenvoudige eind-interpunctie
    """
    s = s.strip().lower()
    s = re.sub(r"[.,;:!?]+$", "", s)
    s = re.sub(r"\s+", " ", s)
    return s


def build_expected_answers(verb: str, tense: TenseCode, pronoun: Pronoun) -> Tuple[List[str], List[str]]:
    """
    Bouw alle acceptabele antwoorden voor een vraag:
    - Voor o.t.t./o.v.t.: exacte vervoeging van het gekozen werkwoord.
    - Voor v.t.t./v.v.t.: alle combinaties van juiste hulpwerkwoord(en) + voltooid deelwoord.
      Als een werkwoord beide hulpwerkwoorden kan hebben (bijv. 'lopen'), accepteer beide.
    Retourneert (genormaliseerde_varianten, nette_weergave_varianten).
    """
    entry = VERBS[verb]
    display_variants: List[str] = []
    normalized_variants: List[str] = []

    if tense in ("o.t.t.", "o.v.t."):
        finite = get_finite_form(verb, tense, pronoun)
        display_variants.append(finite)
        normalized_variants.append(normalize_answer(finite))
        return normalized_variants, display_variants

    # Perfecte tijden: v.t.t. / v.v.t.
    aux_time_value = cast(Optional[str], TENSES[tense].get("aux_time"))
    assert aux_time_value in ("o.t.t.", "o.v.t.")
    aux_time = cast(TenseCode, aux_time_value)

    aux_val = entry.get("aux")
    if aux_val is None:
        raise KeyError(f"Verb-entry mist 'aux' voor {verb}")
    past_participle = entry.get("past_participle")
    if past_participle is None:
        raise KeyError(f"Verb-entry mist 'past_participle' voor {verb}")

    aux_list = aux_val if isinstance(aux_val, list) else [aux_val]
    for aux_name in aux_list:
        aux_form = AUX_CONJUGATION[aux_name][aux_time][pronoun]
        phrase = f"{aux_form} {past_participle}"
        display_variants.append(phrase)
        normalized_variants.append(normalize_answer(phrase))

    # Uniek maken (sommige combinaties kunnen gelijk zijn)
    seen = set()
    unique_norm: List[str] = []
    unique_disp: List[str] = []
    for n, d in zip(normalized_variants, display_variants):
        if n not in seen:
            seen.add(n)
            unique_norm.append(n)
            unique_disp.append(d)

    return unique_norm, unique_disp


def pick_question(tense: TenseCode) -> Question:
    """
    Kies willekeurig een sjabloon (zin) voor de gevraagde tijd en een passend werkwoord.
    """
    templates = list_templates_for_tense(tense)
    tmpl = random.choice(templates)

    allowed_verbs = cast(Optional[List[str]], tmpl.get("allowed_verbs"))
    if not allowed_verbs:
        allowed_verbs = list(VERBS.keys())
    verb = random.choice(allowed_verbs)

    tmpl_pronoun = cast(Optional[Pronoun], tmpl.get("pronoun"))
    if tmpl_pronoun is None:
        raise KeyError(f"Template '{tmpl.get('id','?')}' mist 'pronoun'")

    norm, disp = build_expected_answers(verb, tense, tmpl_pronoun)
    label = cast(str, TENSES[tense]["label"])
    hint = cast(str, tmpl.get("hint", tense))

    tmpl_id = cast(Optional[str], tmpl.get("id"))
    tmpl_text = cast(Optional[str], tmpl.get("template"))
    if tmpl_id is None or tmpl_text is None:
        raise KeyError("Template mist 'id' of 'template'")

    explanation = f"Tijd: {tense} ({label}). Onderwerp: {tmpl_pronoun}. Werkwoord: {verb}."

    return Question(
        template_id=tmpl_id,
        template_text=tmpl_text,
        tense=tense,
        pronoun=tmpl_pronoun,
        verb_infinitive=verb,
        expected_answers=norm,
        display_answers=disp,
        explanation=explanation,
        hint=hint,
    )


def ask_question(q: Question, question_number: int, total: int) -> bool:
    """
    Toon de vraag, vraag om invoer en geef feedback.
    Retourneert True bij goed antwoord, anders False.
    """
    print()
    print(f"[{question_number}/{total}] {q.explanation}")
    print(f"Zin ({q.hint}): {q.template_text}")
    print("Vul de juiste vervoeging in op de plek van de '____'.")
    print(f"Te vervoegen werkwoord: {q.verb_infinitive}")
    user = input("Jouw antwoord: ").strip()
    normalized_user = normalize_answer(user)

    correct = normalized_user in q.expected_answers
    if correct:
        print("✅ Correct!")
    else:
        print("❌ Niet correct.")
        # Toon alle mogelijke correcte antwoorden, netjes geformatteerd
        if len(q.display_answers) == 1:
            print(f"Correcte antwoord: {q.display_answers[0]}")
        else:
            print("Mogelijke correcte antwoorden:")
            for ans in q.display_answers:
                print(f" - {ans}")

        # Extra uitleg bij perfecte tijden
        if q.tense in ("v.t.t.", "v.v.t."):
            print("Let op: bij de voltooide tijden gebruik je het juiste hulpwerkwoord ('hebben' of 'zijn') plus het voltooid deelwoord.")
    return correct


def select_tenses_interactive() -> List[TenseCode]:
    """
    Laat de gebruiker kiezen welke tijden geoefend worden.
    """
    all_tenses: List[TenseCode] = ["o.t.t.", "o.v.t.", "v.t.t.", "v.v.t."]
    labels = {t: cast(str, TENSES[t]["label"]) for t in all_tenses}
    print("Welke tijden wil je oefenen? (meerdere keuzes toegestaan)")
    for idx, t in enumerate(all_tenses, start=1):
        print(f"{idx}. {t} ({labels[t]})")
    print("Kies nummers, gescheiden door komma. Voorbeeld: 1,3,4")
    choice = input("Jouw keuze [enter = alle]: ").strip()
    if not choice:
        return all_tenses

    nums = re.findall(r"\d+", choice)
    picked: List[TenseCode] = []
    for n in nums:
        i = int(n)
        if 1 <= i <= len(all_tenses):
            picked.append(all_tenses[i - 1])

    if not picked:
        print("Geen geldige keuze gedetecteerd. Alle tijden worden gebruikt.")
        return all_tenses
    return picked


def ask_int(prompt: str, default: int, min_value: int = 1, max_value: int = 1000) -> int:
    print(f"{prompt} (default: {default})")
    val = input("> ").strip()
    if not val:
        return default
    try:
        n = int(val)
        if n < min_value or n > max_value:
            print(f"Waarde buiten bereik [{min_value}-{max_value}]. Default {default} gebruikt.")
            return default
        return n
    except ValueError:
        print(f"Ongeldige invoer. Default {default} gebruikt.")
        return default


def run_session():
    print("Welkom bij de Werkwoorden Trainer!")
    print("Je gaat werkwoorden vervoegen in voorbereide zinnen.")
    print("We tonen steeds het werkwoord (infinitief) dat je moet vervoegen en de gevraagde tijd.\n")

    tenses = select_tenses_interactive()
    total = ask_int("Hoeveel vragen wil je?", default=10, min_value=1, max_value=500)
    print("\nPrima! We starten.\n")

    correct_count = 0
    asked = 0

    try:
        for i in range(1, total + 1):
            tense = random.choice(tenses)
            q = pick_question(tense)
            asked += 1
            if ask_question(q, i, total):
                correct_count += 1
    except KeyboardInterrupt:
        print("\nOnderbroken door gebruiker.")

    print("\nResultaat")
    print("---------")
    print(f"Goed: {correct_count} / {asked}")
    if asked > 0:
        pct = (correct_count / asked) * 100.0
        print(f"Score: {pct:.1f}%")
    print("\nBedankt voor het oefenen! Wil je opnieuw proberen, start de applicatie dan opnieuw.")


if __name__ == "__main__":
    run_session()