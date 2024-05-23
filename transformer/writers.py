# Collection of writing functions for different node types

import csv
import logging
from node_types import NODE_TYPES
from tsv_headers import DIAGNOSIS_HEADERS, PARTICIPANT_HEADERS, REFERENCE_FILE_HEADERS, STUDY_HEADERS, SURVIVAL_HEADERS
logger = logging.getLogger(__name__)

# Save Diagnosis records to a TSV file
def write_diagnoses(records, associations):
    # Obtain single study
    study = list(records.get(NODE_TYPES.STUDY.value).values())[0]
    study_acronym = study.study_acronym

    with open(f'data/{study_acronym} diagnoses.tsv', 'w', encoding='utf-8', newline='') as diagnoses_file:
        tsv_writer = csv.writer(diagnoses_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(DIAGNOSIS_HEADERS)

        # Write each Diagnosis record to a TSV row
        for diagnosis_id, diagnosis in records.get(NODE_TYPES.DIAGNOSIS.value).items():
            diagnosis_row = diagnosis.to_list()
            participant_id = associations.get('diagnoses_to_participants').get(diagnosis_id)
            participant = records.get(NODE_TYPES.PARTICIPANT.value).get(participant_id)

            # Append foreign key to Participant record
            row = [
                *diagnosis_row,
                participant.id,
            ]
            tsv_writer.writerow(row)

        diagnoses_file.close()

# Save Participant records to a TSV file
def write_participants(records, associations):
    # Obtain single study
    study = list(records.get(NODE_TYPES.STUDY.value).values())[0]
    study_acronym = study.study_acronym

    with open(f'data/{study_acronym} participants.tsv', 'w', encoding='utf-8', newline='') as participants_file:
        tsv_writer = csv.writer(participants_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(PARTICIPANT_HEADERS)

        # Write each Participant record to a TSV row
        for participant_id, participant in records.get(NODE_TYPES.PARTICIPANT.value).items():
            participant_row = participant.to_list()
            participant_study_id = associations.get('participants_to_studies').get(participant_id)
            participant_study = records.get(NODE_TYPES.STUDY.value).get(participant_study_id)

            # Append foreign key to Study record
            row = [
                *participant_row,
                participant_study.id,
            ]
            tsv_writer.writerow(row)

        participants_file.close()

# Save Reference File records to a TSV file
def write_reference_files(records, associations):
    # Obtain single study
    study = list(records.get(NODE_TYPES.STUDY.value).values())[0]
    study_acronym = study.study_acronym

    with open(f'data/{study_acronym} reference_files.tsv', 'w', encoding='utf-8', newline='') as reference_files_file:
        tsv_writer = csv.writer(reference_files_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(REFERENCE_FILE_HEADERS)

        # Write each Reference File record to a TSV row
        for reference_file_id, reference_file in records.get(NODE_TYPES.REFERENCE_FILE.value).items():
            reference_file_row = reference_file.to_list()
            reference_file_study_id = associations.get('reference_files_to_studies').get(reference_file_id)
            reference_file_study = records.get(NODE_TYPES.STUDY.value).get(reference_file_study_id)

            # Append foreign key to Study record
            row = [
                *reference_file_row,
                reference_file_study.id,
            ]
            tsv_writer.writerow(row)

        reference_files_file.close()

# Save Study records to a TSV file
def write_studies(records, associations):
    # Obtain single study
    study = list(records.get(NODE_TYPES.STUDY.value).values())[0]
    study_acronym = study.study_acronym

    with open(f'data/{study_acronym} studies.tsv', 'w', encoding='utf-8', newline='') as studies_file:
        tsv_writer = csv.writer(studies_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(STUDY_HEADERS)

        # Should only be one study
        for study in records.get(NODE_TYPES.STUDY.value).values():
            row = study.to_list()
            tsv_writer.writerow(row)

        studies_file.close()

# Save Survival records to a TSV file
def write_survivals(records, associations):
    # Obtain single study
    study = list(records.get(NODE_TYPES.STUDY.value).values())[0]
    study_acronym = study.study_acronym

    with open(f'data/{study_acronym} survivals.tsv', 'w', encoding='utf-8', newline='') as survivals_file:
        tsv_writer = csv.writer(survivals_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(SURVIVAL_HEADERS)

        # Write each Survival record to a TSV row
        for survival_id, survival in records.get(NODE_TYPES.SURVIVAL.value).items():
            survival_row = survival.to_list()
            participant_id = associations.get('survivals_to_participants').get(survival_id)
            participant = records.get(NODE_TYPES.PARTICIPANT.value).get(participant_id)

            # Append foreign key to Participant record
            row = [
                *survival_row,
                participant.id,
            ]
            tsv_writer.writerow(row)

        survivals_file.close()
