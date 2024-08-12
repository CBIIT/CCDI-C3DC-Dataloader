# Collection of writing functions for different node types

import csv
import logging
from node_types import NODE_TYPES
from tsv_headers import (
    DIAGNOSIS_HEADERS,
    PARTICIPANT_HEADERS,
    REFERENCE_FILE_HEADERS,
    STUDY_HEADERS,
    SURVIVAL_HEADERS,
    TREATMENT_HEADERS,
    TREATMENT_RESPONSE_HEADERS,
)
logger = logging.getLogger(__name__)

# Save Diagnosis records to a TSV file
def write_diagnoses(records, associations):
    # Obtain single study
    study = list(records.get(NODE_TYPES.STUDY.value).values())[0]
    dbgap_accession = study.dbgap_accession

    with open(f'data/{dbgap_accession} diagnoses.tsv', 'w', encoding='utf-8', newline='') as diagnoses_file:
        tsv_writer = csv.writer(diagnoses_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(DIAGNOSIS_HEADERS)

        # Write each Diagnosis record to a TSV row
        for diagnosis_id, diagnosis in records.get(NODE_TYPES.DIAGNOSIS.value).items():
            row = diagnosis.to_list()
            participant_id = associations.get('diagnoses_to_participants').get(diagnosis_id)

            if participant_id is not None:
                participant = records.get(NODE_TYPES.PARTICIPANT.value).get(participant_id)

                if participant is not None:
                    # Append foreign key to Participant record
                    row.append(participant.id)

            tsv_writer.writerow(row)

        diagnoses_file.close()

# Save Participant records to a TSV file
def write_participants(records, associations):
    # Obtain single study
    study = list(records.get(NODE_TYPES.STUDY.value).values())[0]
    dbgap_accession = study.dbgap_accession

    with open(f'data/{dbgap_accession} participants.tsv', 'w', encoding='utf-8', newline='') as participants_file:
        tsv_writer = csv.writer(participants_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(PARTICIPANT_HEADERS)

        # Write each Participant record to a TSV row
        for participant_id, participant in records.get(NODE_TYPES.PARTICIPANT.value).items():
            row = participant.to_list()
            participant_study_id = associations.get('participants_to_studies').get(participant_id)

            if participant_study_id is not None:
                participant_study = records.get(NODE_TYPES.STUDY.value).get(participant_study_id)

                if participant_study is not None:
                    # Append foreign key to Study record
                    row.append(participant_study.id)

            tsv_writer.writerow(row)

        participants_file.close()

# Save Reference File records to a TSV file
def write_reference_files(records, associations):
    # Obtain single study
    study = list(records.get(NODE_TYPES.STUDY.value).values())[0]
    dbgap_accession = study.dbgap_accession

    with open(f'data/{dbgap_accession} reference_files.tsv', 'w', encoding='utf-8', newline='') as reference_files_file:
        tsv_writer = csv.writer(reference_files_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(REFERENCE_FILE_HEADERS)

        # Write each Reference File record to a TSV row
        for reference_file_id, reference_file in records.get(NODE_TYPES.REFERENCE_FILE.value).items():
            row = reference_file.to_list()
            reference_file_study_id = associations.get('reference_files_to_studies').get(reference_file_id)

            if reference_file_study_id is not None:
                reference_file_study = records.get(NODE_TYPES.STUDY.value).get(reference_file_study_id)

                if reference_file_study is not None:
                    # Append foreign key to Study record
                    row.append(reference_file_study.id)

            tsv_writer.writerow(row)

        reference_files_file.close()

# Save Study records to a TSV file
def write_studies(records, associations):
    # Obtain single study
    study = list(records.get(NODE_TYPES.STUDY.value).values())[0]
    dbgap_accession = study.dbgap_accession

    with open(f'data/{dbgap_accession} studies.tsv', 'w', encoding='utf-8', newline='') as studies_file:
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
    dbgap_accession = study.dbgap_accession

    with open(f'data/{dbgap_accession} survivals.tsv', 'w', encoding='utf-8', newline='') as survivals_file:
        tsv_writer = csv.writer(survivals_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(SURVIVAL_HEADERS)

        # Write each Survival record to a TSV row
        for survival_id, survival in records.get(NODE_TYPES.SURVIVAL.value).items():
            row = survival.to_list()
            participant_id = associations.get('survivals_to_participants').get(survival_id)

            if participant_id is not None:
                participant = records.get(NODE_TYPES.PARTICIPANT.value).get(participant_id)

                if participant is not None:
                    # Append foreign key to Participant record
                    row.append(participant.id)

            tsv_writer.writerow(row)

        survivals_file.close()

# Save Treatment records to a TSV file
def write_treatments(records, associations):
    # Obtain single study
    study = list(records.get(NODE_TYPES.STUDY.value).values())[0]
    dbgap_accession = study.dbgap_accession

    with open(f'data/{dbgap_accession} treatments.tsv', 'w', encoding='utf-8', newline='') as treatments_file:
        tsv_writer = csv.writer(treatments_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(TREATMENT_HEADERS)

        # Write each Treatment record to a TSV row
        for treatment_id, treatment in records.get(NODE_TYPES.TREATMENT.value).items():
            row = treatment.to_list()
            participant_id = associations.get('treatments_to_participants').get(treatment_id)

            if participant_id is not None:
                participant = records.get(NODE_TYPES.PARTICIPANT.value).get(participant_id)

                if participant is not None:
                    # Append foreign key to Participant record
                    row.append(participant.id)

            tsv_writer.writerow(row)

        treatments_file.close()

# Save Treatment Response records to a TSV file
def write_treatment_responses(records, associations):
    # Obtain single study
    study = list(records.get(NODE_TYPES.STUDY.value).values())[0]
    dbgap_accession = study.dbgap_accession

    with open(f'data/{dbgap_accession} treatment_responses.tsv', 'w', encoding='utf-8', newline='') as treatment_responses_file:
        tsv_writer = csv.writer(treatment_responses_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(TREATMENT_RESPONSE_HEADERS)

        # Write each Treatment Response record to a TSV row
        for treatment_response_id, treatment_response in records.get(NODE_TYPES.TREATMENT_RESPONSE.value).items():
            row = treatment_response.to_list()
            participant_id = associations.get('treatment_responses_to_participants').get(treatment_response_id)

            if participant_id is not None:
                participant = records.get(NODE_TYPES.PARTICIPANT.value).get(participant_id)

                if participant is not None:
                    # Append foreign key to Participant record
                    row.append(participant.id)

            tsv_writer.writerow(row)

        treatment_responses_file.close()
