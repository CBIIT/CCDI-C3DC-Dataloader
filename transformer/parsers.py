# Collection of parsing functions for different node types

import logging
from make_uuid import make_uuid
from node_types import NODE_TYPES
from nodes import Diagnosis, Participant, ReferenceFile, Study, Survival
logger = logging.getLogger(__name__)

# Reads Diagnosis records from JSON and saves them to a dict
def parse_diagnoses(data, records, associations):
    all_diagnosis_data = data.get('diagnoses', [])
    study_id = records.get(NODE_TYPES.STUDY.value).study_id

    if len(all_diagnosis_data) == 0:
        logger.info(f'No {NODE_TYPES.DIAGNOSIS.value} records to parse. Skipping...\n')
        return

    # Save each Diagnosis record as a Diagnosis object
    for diagnosis_data in all_diagnosis_data:
        diagnosis_id = diagnosis_data.get('diagnosis_id', None)
        diagnosis_uuid = make_uuid(
            NODE_TYPES.DIAGNOSIS.value,
            study_id,
            diagnosis_id
        )
        participant_id = diagnosis_data.get('participant.participant_id', None)

        # Don't consider duplicate diagnosis ID as an error yet
        if diagnosis_id in records.get(NODE_TYPES.DIAGNOSIS.value):
            logger.warning(f'Diagnosis {diagnosis_id} exists!')
            logger.warning(f'Skipping Diagnosis {diagnosis_id}...')

        # Map diagnosis ID to participant ID
        if participant_id is None:
            logger.warning(f'Diagnosis {diagnosis_id} does not have a Participant ID!')
        elif participant_id not in records.get(NODE_TYPES.PARTICIPANT.value).keys():
            raise ValueError(f'Diagnosis {diagnosis_id} references nonexistent Participant {participant_id}!')
        else:
            associations['diagnoses_to_participants'][diagnosis_id] = participant_id

        try:
            diagnosis = Diagnosis(
                id = diagnosis_uuid,
                age_at_diagnosis = diagnosis_data.get('age_at_diagnosis', None),
                anatomic_site = diagnosis_data.get('anatomic_site', None),
                diagnosis_basis = diagnosis_data.get('diagnosis_basis', None),
                diagnosis = diagnosis_data.get('diagnosis', None),
                diagnosis_classification_system = diagnosis_data.get('diagnosis_classification_system', None),
                diagnosis_comment = diagnosis_data.get('diagnosis_comment', None),
                diagnosis_id = diagnosis_id,
                disease_phase = diagnosis_data.get('disease_phase', None),
                toronto_childhood_cancer_staging = diagnosis_data.get('toronto_childhood_cancer_staging', None),
                tumor_classification= diagnosis_data.get('tumor_classification', None),
                tumor_grade = diagnosis_data.get('tumor_grade', None),
                tumor_stage_clinical_m = diagnosis_data.get('tumor_stage_clinical_m', None),
                tumor_stage_clinical_n = diagnosis_data.get('tumor_stage_clinical_n', None),
                tumor_stage_clinical_t = diagnosis_data.get('tumor_stage_clinical_t', None)
            )
            records[NODE_TYPES.DIAGNOSIS.value][diagnosis_id] = diagnosis
        except TypeError as e:
            logger.error('Wrong data type for Diagnosis %s: %s', diagnosis_id, e)
        except ValueError as e:
            logger.error('Invalid value for Diagnosis %s: %s', diagnosis_id, e)

# Reads Participant records from JSON and saves them to a dict
def parse_participants(data, records, associations):
    all_participant_data = data.get('participants', [])

    if len(all_participant_data) == 0:
        logger.info(f'No {NODE_TYPES.PARTICIPANT.value} records to parse. Skipping...\n')
        return

    # Save each Participant record as a Participant object
    for participant_data in all_participant_data:
        participant_id = participant_data.get('participant_id', None)

        # Study ID read from the Participant record
        participant_study_id = participant_data.get('study.study_id', None)

        # Study ID from a previously read study
        # Should be the same as the one read from the Participant record
        study_id = records[NODE_TYPES.STUDY.value].study_id
        participant_uuid = make_uuid(
            NODE_TYPES.PARTICIPANT.value,
            study_id,
            participant_id
        )

        # Don't consider duplicate participant ID as an error yet
        if participant_id in records.get(NODE_TYPES.PARTICIPANT.value):
            logger.warning(f'Participant {participant_id} exists!')
            logger.warning(f'Skipping Participant {participant_id}...')

        # Map participant ID to study ID
        if participant_study_id is None:
            logger.error(f'Participant {participant_id} has no Study ID! Skipping...')
            continue
        elif participant_study_id != study_id:
            raise ValueError(f'Participant {participant_id} references nonexistent Study {participant_study_id}!')
        else:
            associations['participants_to_studies'][participant_id] = participant_study_id

        try:
            participant = Participant(
                id = participant_uuid,
                ethnicity = participant_data.get('ethnicity', None),
                participant_id = participant_id,
                race = participant_data.get('race', None),
                sex_at_birth = participant_data.get('sex_at_birth', None)
            )
            records[NODE_TYPES.PARTICIPANT.value][participant_id] = participant
        except TypeError as e:
            logger.error('Wrong data type for Participant %s: %s', participant_id, e)
        except ValueError as e:
            logger.error('Invalid value for Participant %s: %s', participant_id, e)

# Reads Reference File records from JSON and saves them to a dict
def parse_reference_files(data, records, associations):
    all_reference_file_data = data.get('reference_files', [])

    if len(all_reference_file_data) == 0:
        logger.info(f'No {NODE_TYPES.REFERENCE_FILE.value} records to parse. Skipping...\n')
        return

    # Save each Reference File record as a Reference File object
    for reference_file_data in all_reference_file_data:
        reference_file_id = reference_file_data['reference_file_id']

        # Study ID read from the Reference File record
        reference_file_study_id = reference_file_data.get('study.study_id', None)

        # Study ID from a previously read study
        # Should be the same as the one read from the Reference File record
        study_id = records[NODE_TYPES.STUDY.value].study_id
        reference_file_uuid = make_uuid(
            NODE_TYPES.REFERENCE_FILE.value,
            study_id,
            reference_file_id
        )

        # Don't consider duplicate reference file ID as an error yet
        if reference_file_id in records.get(NODE_TYPES.REFERENCE_FILE.value):
            logger.warning(f'Reference File {reference_file_id} exists!')
            logger.warning(f'Skipping Reference File {reference_file_id}...')

        # Skip reference file if it doesn't have a study
        if reference_file_study_id is None:
            logger.warning(f'Reference File {reference_file_id} has no Study ID! Skipping...')
            continue
        elif reference_file_study_id != study_id:
            raise ValueError(f'Reference File {reference_file_id} references nonexistent Study {reference_file_study_id}!')
        else:
            associations['reference_files_to_studies'][reference_file_id] = reference_file_study_id

        try:
            reference_file = ReferenceFile(
                id = reference_file_uuid,
                dcf_indexd_guid = reference_file_data.get('dcf_indexd_guid', None),
                file_category = reference_file_data.get('file_category', None),
                file_description = reference_file_data.get('file_description', None),
                file_name = reference_file_data.get('file_name', None),
                file_size = reference_file_data.get('file_size', None),
                file_type = reference_file_data.get('file_type', None),
                md5sum = reference_file_data.get('md5sum', None),
                reference_file_id = reference_file_id,
                reference_file_url = reference_file_data.get('reference_file_url', None)
            )
            records[NODE_TYPES.REFERENCE_FILE.value][reference_file_id] = reference_file
        except TypeError as e:
            logger.error('Wrong data type for Reference File %s: %s', reference_file_id, e)
        except ValueError as e:
            logger.error('Invalid value for Reference File %s: %s', reference_file_id, e)

# Reads Study records from JSON and saves them to a dict
def parse_study(data, records, associations):
    all_study_data = data.get('studies', [])

    if len(all_study_data) == 0:
        raise Exception(f'No {NODE_TYPES.STUDY.value} records to parse!')

    study_data = all_study_data[0]
    study_id = study_data.get('study_id', None)
    study_uuid = make_uuid(
        NODE_TYPES.STUDY.value,
        study_id,
        study_id
    )

    try:
        study = Study(
            id = study_uuid,
            acl = study_data.get('acl', None),
            consent = study_data.get('consent', None),
            consent_number = study_data.get('consent_number', None),
            external_url = study_data.get('external_url', None),
            phs_accession = study_data.get('phs_accession', None),
            study_acronym = study_data.get('study_acronym', None),
            study_description = study_data.get('study_description', None),
            study_id = study_id,
            study_short_title = study_data.get('study_short_title', None),
        )

        if records[NODE_TYPES.STUDY.value] is not None and study.id != records[NODE_TYPES.STUDY.value].id:
            raise Exception(f'More than one unique {NODE_TYPES.STUDY.value} record found: {[study_json["study_id"] for study_json in all_study_data]}')

        records[NODE_TYPES.STUDY.value] = study

    except TypeError as e:
        logger.error('Wrong data type for Study %s: %s', study, e)
    except ValueError as e:
        logger.error('Invalid value for Study %s: %s', study, e)

# Reads Survival records from JSON and saves them to a dict
def parse_survivals(data, records, associations):
    all_survival_data = data.get('survivals', [])
    study_id = records.get(NODE_TYPES.STUDY.value).study_id

    if len(all_survival_data) == 0:
        logger.info(f'No {NODE_TYPES.SURVIVAL.value} records to parse. Skipping...\n')
        return

    # Save each Survival record as a Survival object
    for survival_data in all_survival_data:
        participant_id = survival_data.get('participant.participant_id', None)
        survival_id = survival_data.get('survival_id')
        survival_uuid = make_uuid(
            NODE_TYPES.SURVIVAL.value,
            study_id,
            survival_id,
        )

        # Don't consider duplicate survival ID as an error yet
        if survival_id in records.get(NODE_TYPES.SURVIVAL.value):
            logger.warning(f'Survival {survival_id} exists!')
            logger.warning(f'Skipping Survival {survival_id}...')

        # Map survival ID to participant ID
        if participant_id is None:
            logger.warning(f'Survival {survival_id} does not have a Participant ID!')
        elif participant_id not in records.get(NODE_TYPES.PARTICIPANT.value).keys():
            raise ValueError(f'Survival {survival_id} references nonexistent Participant {participant_id}!')
        else:
            associations['survivals_to_participants'][survival_id] = participant_id

        try:
            survival = Survival(
                id = survival_uuid,
                age_at_event_free_survival_status = survival_data.get('age_at_event_free_survival_status', None),
                age_at_last_known_survival_status = survival_data.get('age_at_last_known_survival_status', None),
                event_free_survival_status = survival_data.get('event_free_survival_status', None),
                first_event = survival_data.get('first_event', None),
                last_known_survival_status = survival_data.get('last_known_survival_status', None),
                survival_id = survival_data.get('survival_id', None)
            )
            records[NODE_TYPES.SURVIVAL.value][survival_id] = survival
        except TypeError as e:
            logger.error('Wrong data type for Survival %s: %s', survival_id, e)
        except ValueError as e:
            logger.error('Invalid value for Survival %s: %s', survival_id, e)
