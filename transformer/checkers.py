# Collection of foreign key checking functions for different node types

def check_diagnoses_for_participants():
    diagnosis_ids_to_remove = []

    for diagnosis_id in diagnoses.keys():
        if diagnosis_id not in diagnoses_to_participants.keys():
            logger.warning(f'Diagnosis {diagnosis_id} does not have a Participant!')
            logger.warning(f'Skipping Diagnosis {diagnosis_id}...')
            diagnosis_ids_to_remove.append(diagnosis_id)

    for diagnosis_id in diagnosis_ids_to_remove:
        del diagnoses[diagnosis_id]

def check_participants_for_studies():
    participant_ids_to_remove = []

    for participant_id in participants.keys():
        if participant_id not in participants_to_studies.keys():
            logger.warning(f'Participant {participant_id} does not have a Study!')
            logger.warning(f'Skipping Participant {participant_id}...')
            participant_ids_to_remove.append(participant_id)

    for participant_id in participant_ids_to_remove:
        del participants[participant_id]

def check_reference_files_for_studies():
    reference_file_ids_to_remove = []

    for reference_file_id in reference_files.keys():
        if reference_file_id not in reference_files_to_studies.keys():
            logger.warning(f'Reference File {reference_file_id} does not have a Study!')
            logger.warning(f'Skipping Reference File {reference_file_id}...')
            reference_file_ids_to_remove.append(reference_file_id)

    for reference_file_id in reference_file_ids_to_remove:
        del reference_files[reference_file_id]

def check_survivals_for_participants():
    survival_ids_to_remove = []

    for survival_id in survivals.keys():
        if survival_id not in survivals_to_participants.keys():
            logger.warning(f'Survival {survival_id} does not have a Participant!')
            logger.warning(f'Skipping Survival {survival_id}...')
            survival_ids_to_remove.append(survival_id)

    for survival_id in survival_ids_to_remove:
        del survivals[survival_id]