from importlib import import_module
import spacy
from errant.annotator import Annotator

# ERRANT version
__version__ = '2.3.0'

# Load an ERRANT Annotator object for a given language
# Assume english as the language
def load(spacy_model, nlp=None):

    # Load spacy
    nlp = nlp or spacy.load(spacy_model, disable=["ner"])

    # Load language edit merger
    merger = import_module("errant.en.merger")

    # Load language edit classifier
    classifier = import_module("errant.en.classifier")
    classifier.nlp = nlp
    # Return a configured ERRANT annotator
    return Annotator(lang, nlp, merger, classifier)
