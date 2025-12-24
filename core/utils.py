import pickle
import spacy
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

nlp = spacy.load("en_core_web_sm")

with open(BASE_DIR / "best_model.pkl", "rb") as f:
    tone_model = pickle.load(f)

def detect_tone(sentence):
    return tone_model.predict([sentence])[0]

def extract_intent(sentence):
    doc = nlp(sentence)
    verb = None
    obj = None

    for token in doc:
        if token.dep_ == "ROOT" and token.pos_ == "VERB":
            verb = token.lemma_
        if token.dep_ in ("dobj", "pobj"):
            obj = token.text

    if verb and obj:
        return f"{verb} the {obj}"
    return sentence.lower()

TEMPLATES = {
    "polite": [
        "Could you please {intent}?",
        "Please {intent} when you have time."
    ],
    "professional": [
        "Kindly {intent} at your convenience.",
        "I would appreciate it if you could {intent}."
    ],
    "friendly": [
        "Hey, could you {intent}?",
        "Just checking if you can {intent}."
    ]
}

def generate_suggestions(sentence):
    detected = detect_tone(sentence)
    intent = extract_intent(sentence)

    suggestions = {}
    for tone, templates in TEMPLATES.items():
        suggestions[tone] = [
            t.format(intent=intent) for t in templates
        ]

    return detected, suggestions
