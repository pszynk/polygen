"""
registered PaylodGenerators
"""

from polygen.payload.SymmiGenerator import SymmiGenerator
from polygen.payload.GupdGenerator import GupdGenerator
from polygen.payload.HawkEyeGenerator import HawkEyeGenerator
from polygen.payload.GhbnGenerator import GhbnGenerator
from polygen.payload.DcerpcGenerator import DcerpcGenerator
from polygen.payload.MadnessProGenerator import MadnessProGenerator

PAYLOAD_GENERATORS = [
    SymmiGenerator(),
    GupdGenerator(),
    HawkEyeGenerator(),
    GhbnGenerator(),
    DcerpcGenerator(),
    MadnessProGenerator(),
]
