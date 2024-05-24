# Collection of foreign key checking functions for different node types

import logging
from node_types import NODE_TYPES
logger = logging.getLogger(__name__)

# Each Diagnosis record should reference a Participant record
def check_diagnoses_for_participants(records, associations):
    # Keep track of Diagnosis records to remove
    diagnosis_ids_to_remove = []

    # Find Diagnosis records that lack a reference to a Participant record
    for diagnosis_id in records.get(NODE_TYPES.DIAGNOSIS.value).keys():
        if diagnosis_id not in associations['diagnoses_to_participants'].keys():
            logger.warning(f'Diagnosis {diagnosis_id} does not have a Participant!')
            logger.warning(f'Skipping Diagnosis {diagnosis_id}...')
            diagnosis_ids_to_remove.append(diagnosis_id)

    # Remove bad Diagnosis records
    for diagnosis_id in diagnosis_ids_to_remove:
        del records[NODE_TYPES.DIAGNOSIS.value][diagnosis_id]

# Each Participant record should reference a Study record
def check_participants_for_studies(records, associations):
    # Keep track of Participant records to remove
    participant_ids_to_remove = []

    # Find Participant records that lack a reference to a Study record
    for participant_id in records.get(NODE_TYPES.PARTICIPANT.value).keys():
        if participant_id not in associations['participants_to_studies'].keys():
            logger.warning(f'Participant {participant_id} does not have a Study!')
            logger.warning(f'Skipping Participant {participant_id}...')
            participant_ids_to_remove.append(participant_id)

    # Remove bad Participant records
    for participant_id in participant_ids_to_remove:
        del records[NODE_TYPES.PARTICIPANT.value][participant_id]

# Each Reference File record should reference a Study record
def check_reference_files_for_studies(records, associations):
    # Keep track of Reference File records to remove
    reference_file_ids_to_remove = []

    # Find Reference File records that lack a reference to a Study record
    for reference_file_id in records.get(NODE_TYPES.REFERENCE_FILE.value).keys():
        if reference_file_id not in associations['reference_files_to_studies'].keys():
            logger.warning(f'Reference File {reference_file_id} does not have a Study!')
            logger.warning(f'Skipping Reference File {reference_file_id}...')
            reference_file_ids_to_remove.append(reference_file_id)

    # Remove bad Reference File records
    for reference_file_id in reference_file_ids_to_remove:
        del records[NODE_TYPES.REFERENCE_FILE.value][reference_file_id]

# Each Survival record should reference a Participant record
def check_survivals_for_participants(records, associations):
    # Keep track of Survival records to remove
    survival_ids_to_remove = []

    # Find Survival records that lack a reference to a Participant record
    for survival_id in records.get(NODE_TYPES.SURVIVAL.value).keys():
        if survival_id not in associations['survivals_to_participants'].keys():
            logger.warning(f'Survival {survival_id} does not have a Participant!')
            logger.warning(f'Skipping Survival {survival_id}...')
            survival_ids_to_remove.append(survival_id)

    # Remove bad Survival records
    for survival_id in survival_ids_to_remove:
        del records[NODE_TYPES.SURVIVAL.value][survival_id]