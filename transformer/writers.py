# Collection of writing functions for different node types

import csv
import logging
from node_types import NODE_TYPES
from tsv_headers import DIAGNOSIS_HEADERS, PARTICIPANT_HEADERS, REFERENCE_FILE_HEADERS, STUDY_HEADERS, SURVIVAL_HEADERS
logger = logging.getLogger(__name__)

def write_diagnoses(records, associations):
    study = records[NODE_TYPES.STUDY.value]
    study_acronym = study.study_acronym

    with open(f'data/{study_acronym} diagnoses.tsv', 'w', newline='') as diagnoses_file:
        tsv_writer = csv.writer(diagnoses_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(DIAGNOSIS_HEADERS)

        for diagnosis_id, diagnosis in records[NODE_TYPES.DIAGNOSIS.value].items():
            diagnosis_row = diagnosis.to_list()
            participant_id = associations['diagnoses_to_participants'][diagnosis_id]
            participant = records[NODE_TYPES.PARTICIPANT.value][participant_id]

            row = [
                *diagnosis_row,
                participant.id,
            ]
            tsv_writer.writerow(row)

        diagnoses_file.close()

def write_participants(records, associations):
    study = records[NODE_TYPES.STUDY.value]
    study_acronym = study.study_acronym

    with open(f'data/{study_acronym} participants.tsv', 'w', newline='') as participants_file:
        tsv_writer = csv.writer(participants_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(PARTICIPANT_HEADERS)

        for participant_id, participant in records[NODE_TYPES.PARTICIPANT.value].items():
            participant_row = participant.to_list()
            row = [
                *participant_row,
                study.id,
            ]
            tsv_writer.writerow(row)

        participants_file.close()

def write_reference_files(records, associations):
    study = records[NODE_TYPES.STUDY.value]
    study_acronym = study.study_acronym

    with open(f'data/{study_acronym} reference_files.tsv', 'w', newline='') as reference_files_file:
        tsv_writer = csv.writer(reference_files_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(REFERENCE_FILE_HEADERS)

        for reference_file_id, reference_file in records[NODE_TYPES.REFERENCE_FILE.value].items():
            reference_file_row = reference_file.to_list()
            row = [
                *reference_file_row,
                study.id,
            ]
            tsv_writer.writerow(row)

        reference_files_file.close()

def write_studies(records, associations):
    study = records[NODE_TYPES.STUDY.value]
    study_acronym = study.study_acronym

    with open(f'data/{study_acronym} studies.tsv', 'w', encoding='utf-8', newline='') as studies_file:
        tsv_writer = csv.writer(studies_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(STUDY_HEADERS)

        row = study.to_list()
        tsv_writer.writerow(row)

        studies_file.close()

def write_survivals(records, associations):
    study = records[NODE_TYPES.STUDY.value]
    study_acronym = study.study_acronym

    with open(f'data/{study_acronym} survivals.tsv', 'w', newline='') as survivals_file:
        tsv_writer = csv.writer(survivals_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(SURVIVAL_HEADERS)

        for survival_id, survival in records[NODE_TYPES.SURVIVAL.value].items():
            survival_row = survival.to_list()
            participant_id = associations['survivals_to_participants'][survival_id]
            participant = records[NODE_TYPES.PARTICIPANT.value][participant_id]

            row = [
                *survival_row,
                participant.id,
            ]
            tsv_writer.writerow(row)

        survivals_file.close()
