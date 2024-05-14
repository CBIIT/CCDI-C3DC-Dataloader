# Collection of writing functions for different node types

import csv
import logging
from tsv_headers import DIAGNOSIS_HEADERS, PARTICIPANT_HEADERS, REFERENCE_FILE_HEADERS, STUDY_HEADERS, SURVIVAL_HEADERS
logger = logging.getLogger(__name__)

def write_diagnoses():
    with open('data/diagnoses.tsv', 'w', newline='') as diagnoses_file:
        tsv_writer = csv.writer(diagnoses_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(DIAGNOSIS_HEADERS)

        for diagnosis_id, diagnosis in diagnoses.items():
            diagnosis_row = diagnosis.to_list()
            participant_id = diagnoses_to_participants[diagnosis_id]
            participant = participants[participant_id]

            row = [
                *diagnosis_row,
                participant.id,
            ]
            tsv_writer.writerow(row)

        diagnoses_file.close()

def write_participants():
    with open('data/participants.tsv', 'w', newline='') as participants_file:
        tsv_writer = csv.writer(participants_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(PARTICIPANT_HEADERS)

        for participant_id, participant in participants.items():
            participant_row = participant.to_list()
            row = [
                *participant_row,
                study.id,
            ]
            tsv_writer.writerow(row)

        participants_file.close()

def write_reference_files():
    with open('data/reference_files.tsv', 'w', newline='') as reference_files_file:
        tsv_writer = csv.writer(reference_files_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(REFERENCE_FILE_HEADERS)

        for reference_file_id, reference_file in reference_files.items():
            reference_file_row = reference_file.to_list()
            row = [
                *reference_file_row,
                study.id,
            ]
            tsv_writer.writerow(row)

        reference_files_file.close()

def write_studies():
    with open('data/studies.tsv', 'w', newline='') as studies_file:
        tsv_writer = csv.writer(studies_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(STUDY_HEADERS)

        row = study.to_list()
        tsv_writer.writerow(row)

        studies_file.close()

def write_survivals():
    with open('data/survivals.tsv', 'w', newline='') as survivals_file:
        tsv_writer = csv.writer(survivals_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(SURVIVAL_HEADERS)

        for survival_id, survival in survivals.items():
            survival_row = survival.to_list()
            participant_id = survivals_to_participants[survival_id]
            participant = participants[participant_id]

            row = [
                *survival_row,
                participant.id,
            ]
            tsv_writer.writerow(row)

        survivals_file.close()
