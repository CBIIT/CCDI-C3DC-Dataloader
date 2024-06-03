# Enum of node types in the datamodel

from enum import Enum

class NODE_TYPES(Enum):
    DIAGNOSIS = "Diagnosis"
    PARTICIPANT = "Participant"
    REFERENCE_FILE = "Reference File"
    STUDY = "Study"
    SURVIVAL = "Survival"
    TREATMENT = "Treatment"
    TREATMENT_RESPONSE = "Treatment Response"
