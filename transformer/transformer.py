# Run this script once per study

import csv
import json
import logging
import os
import sys
import time
import uuid
from enum import Enum
from nodes import Diagnosis, Participant, ReferenceFile, Study, Survival

class NODE_TYPES(Enum):
    DIAGNOSIS = "Diagnosis"
    PARTICIPANT = "Participant"
    REFERENCE_FILE = "Reference File"
    STUDY = "Study"
    SURVIVAL = "Survival"

DIAGNOSIS_HEADERS = [
    'type',
    'id',
    'diagnosis_id',
    'diagnosis',
    'diagnosis_classification_system',
    'diagnosis_basis',
    'diagnosis_comment',
    'disease_phase',
    'anatomic_site',
    'age_at_diagnosis',
    'toronto_childhood_cancer_staging',
    'tumor_classification',
    'tumor_grade',
    'tumor_stage_clinical_t',
    'tumor_stage_clinical_n',
    'tumor_stage_clinical_m',
    'participant.id',
]

PARTICIPANT_HEADERS = [
    'type',
    'id',
    'participant_id',
    'race',
    'sex_at_birth',
    'ethnicity',
    'study.id',
]

REFERENCE_FILE_HEADERS = [
    'type',
    'id',
    'reference_file_id',
    'file_category',
    'file_name',
    'file_type',
    'file_description',
    'file_size',
    'md5sum',
    'reference_file_url',
    'dcf_indexd_guid',
    'study.id',
]

STUDY_HEADERS = [
    'type',
    'id',
    'study_id',
    'phs_accession',
    'acl',
    'study_short_title',
    'study_acronym',
    'study_description',
    'consent',
    'consent_number',
    'external_url',
]

SURVIVAL_HEADERS = [
    'type',
    'id',
    'survival_id',
    'last_known_survival_status',
    'event_free_survival_status',
    'first_event',
    'age_at_last_known_survival_status',
    'age_at_event_free_survival_status',
    'participant.id',
]

node_names = [
    'diagnoses',
    'participants',
    'reference_files',
    'studies',
    'survivals',
]
all_json_data = dict.fromkeys(node_names, [])
timestr = time.strftime('%Y%m%d-%H%M%S')
log_targets = logging.StreamHandler(sys.stdout), logging.FileHandler('tmp/transformer-' + timestr + '.log')
logging.basicConfig(format='%(message)s', level=logging.INFO, handlers=log_targets)

# Look at all the files in the data directory
for filename in os.listdir('data/'):
    # Skip non-JSON files
    if not filename.endswith('.json'):
        continue

    path = 'data/' + filename

    logging.info('Reading data from ' + path + '...')
    json_file = open(path)
    json_data = json.load(json_file)

    for node_name in node_names:
        if node_name not in json_data:
            continue

        all_json_data[node_name] = all_json_data[node_name] + json_data[node_name]
    json_file.close()
    logging.info('Finished reading data from ' + path + '...')

# TODO crosscheck foreign keys (eg: check each participant's study ID consistent with study's participant ID's)
diagnoses = {}
diagnoses_to_participants = {} # Map of diagnosis ids to participant ids
participants_to_studies = {} # Map of participant ids to study ids
participants = {}
reference_files = {}
reference_files_to_studies = {} # Map of reference file ids to study ids
study_id = None # There should be only one Study record
study = None # There should be only one Study record
survivals = {}
survivals_to_participants = {} # Map of survival ids to participant ids

def transform():
    logging.info('Parsing Study record from JSON...')
    parse_study()
    logging.info('Finished parsing Study record\n')

    logging.info('Parsing Participant records from JSON...')
    parse_participants()
    logging.info('Finished parsing Participant records\n')

    logging.info('Parsing Survival records from JSON...')
    parse_survivals()
    logging.info('Finished parsing Survival records\n')

    logging.info('Parsing Diagnose records from JSON...')
    parse_diagnoses()
    logging.info('Finished parsing Diagnose records\n')

    logging.info('Parsing Reference File records from JSON...')
    parse_reference_files()
    logging.info('Finished parsing Reference File records\n')

    logging.info('Verifying that each Participant record has a Study record...')
    check_participants_for_studies()
    logging.info('Finished verifying that each Participant record has a Study record\n')

    logging.info('Verifying that each Survival record has a Participant record...')
    check_survivals_for_participants()
    logging.info('Finished verifying that each Survival record has a Participant record\n')

    logging.info('Verifying that each Diagnosis record has a Participant record...')
    check_diagnoses_for_participants()
    logging.info('Finished verifying that each Diagnosis record has a Participant record\n')

    logging.info('Verifying that each Reference File record has a Study record...')
    check_reference_files_for_studies()
    logging.info('Finished verifying that each Reference File record has a Study record\n')

    if study is None:
        logging.info('No Study records. Skipping TSV...\n')
    else:
        logging.info('Writing Studies TSV...')
        write_studies()
        logging.info('Finished writing Studies TSV\n')

    if len(participants) == 0:
        logging.info('No Participant records. Skipping TSV...\n')
    else:
        logging.info('Writing Participants TSV...')
        write_participants()
        logging.info('Finished writing Participants TSV\n')

    if len(survivals) == 0:
        logging.info('No Survival records. Skipping TSV...\n')
    else:
        logging.info('Writing Survivals TSV...')
        write_survivals()
        logging.info('Finished writing Survivals TSV\n')

    if len(diagnoses) == 0:
        logging.info('No Diagnosis records. Skipping TSV...\n')
    else:
        logging.info('Writing Diagnoses TSV...')
        write_diagnoses()
        logging.info('Finished writing Diagnoses TSV\n')

    if len(reference_files) == 0:
        logging.info('No Reference File records. Skipping TSV...\n')
    else:
        logging.info('Writing Reference Files TSV...')
        write_reference_files()
        logging.info('Finished writing Reference Files TSV')

def parse_diagnoses():
    # Retrieve map of Diagnosis records
    all_diagnosis_data = all_json_data['diagnoses']

    for diagnosis_data in all_diagnosis_data:
        diagnosis_id = diagnosis_data.get('diagnosis_id', None)
        diagnosis_uuid = make_uuid(
            NODE_TYPES.DIAGNOSIS.value,
            study_id,
            diagnosis_id
        )

        # Don't consider duplicate diagnosis ID as an error yet
        if diagnosis_id in diagnoses:
            logging.warning(f'Diagnosis {diagnosis_id} exists!')
            logging.warning(f'Skipping Diagnosis {diagnosis_id}...')

        # Warning for not having a foreign key to Participant
        if 'participant.participant_id' not in diagnosis_data:
            logging.warning(f'Diagnosis {diagnosis_id} does not have a Participant ID!')
        else:
            diagnoses_to_participants[diagnosis_id] = diagnosis_data.get('participant.participant_id', None)

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
            diagnoses[diagnosis_id] = diagnosis
        except TypeError as e:
            logging.error('Wrong data type for Diagnosis %s: %s', diagnosis_id, e)
        except ValueError as e:
            logging.error('Invalid value for Diagnosis %s: %s', diagnosis_id, e)

def check_diagnoses_for_participants():
    diagnosis_ids_to_remove = []

    for diagnosis_id in diagnoses.keys():
        if diagnosis_id not in diagnoses_to_participants.keys():
            logging.warning(f'Diagnosis {diagnosis_id} does not have a Participant!')
            logging.warning(f'Skipping Diagnosis {diagnosis_id}...')
            diagnosis_ids_to_remove.append(diagnosis_id)

    for diagnosis_id in diagnosis_ids_to_remove:
        del diagnoses[diagnosis_id]

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

def parse_participants():
    all_participant_data = all_json_data['participants']

    for participant_data in all_participant_data:
        participant_id = participant_data.get('participant_id', None)
        participant_study_id = participant_data.get('study.study_id', None)
        participant_uuid = make_uuid(
            NODE_TYPES.PARTICIPANT.value,
            study_id,
            participant_id
        )

        # Don't consider duplicate participant ID as an error yet
        if participant_id in participants:
            logging.warning(f'Participant {participant_id} exists!')
            logging.warning(f'Skipping Participant {participant_id}...')

        # Skip participant if it doesn't have a study
        if participant_study_id is None:
            logging.warning(f'Participant {participant_id} has no Study ID! Skipping...')
            continue

        try:
            participant = Participant(
                id = participant_uuid,
                ethnicity = participant_data.get('ethnicity', None),
                participant_id = participant_id,
                race = participant_data.get('race', None),
                sex_at_birth = participant_data.get('sex_at_birth', None)
            )
            participants[participant_id] = participant

            # Warn if the participant's study doesn't exist
            if participant_study_id != study_id:
                raise ValueError(f'Participant {participant_id} references Study {participant_study_id}, not Study {study_id}!')

            # Warn if the participant is already associated with a study
            if participant_id in participants_to_studies.keys():
                logging.warning(f'Participant {participant_id} already matched to {participants_to_studies[participant_id]}!')
                logging.warning(f'Mapping participant {participant_id} to another study: {study_id}...')

            participants_to_studies[participant_id] = study_id
        except TypeError as e:
            logging.error('Wrong data type for Participant %s: %s', participant_id, e)
        except ValueError as e:
            logging.error('Invalid value for Participant %s: %s', participant_id, e)

def check_participants_for_studies():
    participant_ids_to_remove = []

    for participant_id in participants.keys():
        if participant_id not in participants_to_studies.keys():
            logging.warning(f'Participant {participant_id} does not have a Study!')
            logging.warning(f'Skipping Participant {participant_id}...')
            participant_ids_to_remove.append(participant_id)

    for participant_id in participant_ids_to_remove:
        del participants[participant_id]

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

def parse_reference_files():
    all_reference_file_data = all_json_data['reference_files']

    for reference_file_data in all_reference_file_data:
        reference_file_id = reference_file_data['reference_file_id']
        reference_file_study_id = reference_file_data.get('study.study_id', None)
        reference_file_uuid = make_uuid(
            NODE_TYPES.REFERENCE_FILE.value,
            study_id,
            reference_file_id
        )

        # Don't consider duplicate reference file ID as an error yet
        if reference_file_id in reference_files:
            logging.warning(f'Reference File {reference_file_id} exists!')
            logging.warning(f'Skipping Reference File {reference_file_id}...')

        # Skip reference file if it doesn't have a study
        if reference_file_study_id is None:
            logging.warning(f'Reference File {reference_file_id} has no Study ID! Skipping...')
            continue

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
            reference_files[reference_file_id] = reference_file
            reference_files_to_studies[reference_file_id] = reference_file_study_id
        except TypeError as e:
            logging.error('Wrong data type for Reference File %s: %s', reference_file_id, e)
        except ValueError as e:
            logging.error('Invalid value for Reference File %s: %s', reference_file_id, e)

def check_reference_files_for_studies():
    reference_file_ids_to_remove = []

    for reference_file_id in reference_files.keys():
        if reference_file_id not in reference_files_to_studies.keys():
            logging.warning(f'Reference File {reference_file_id} does not have a Study!')
            logging.warning(f'Skipping Reference File {reference_file_id}...')
            reference_file_ids_to_remove.append(reference_file_id)

    for reference_file_id in reference_file_ids_to_remove:
        del reference_files[reference_file_id]

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

def parse_study():
    global study, study_id

    all_study_data = all_json_data['studies']

    # Check whether there exists a study
    if (len(all_study_data) == 0):
        error_msg = 'No study found!'
        logging.error(error_msg)
        raise Exception(error_msg)

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
    except TypeError as e:
        logging.error('Wrong data type for Study %s: %s', study, e)
    except ValueError as e:
        logging.error('Invalid value for Study %s: %s', study, e)

    return (study, study_id)

def write_studies():
    with open('data/studies.tsv', 'w', newline='') as studies_file:
        tsv_writer = csv.writer(studies_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(STUDY_HEADERS)

        row = study.to_list()
        tsv_writer.writerow(row)

        studies_file.close()

def parse_survivals():
    all_survival_data = all_json_data['survivals']

    for survival_data in all_survival_data:
        participant_id = survival_data.get('participant.participant_id', None)
        survival_id = survival_data.get('survival_id')
        survival_uuid = make_uuid(
            NODE_TYPES.SURVIVAL.value,
            study_id,
            survival_id,
        )

        # Don't consider duplicate survival ID as an error yet
        if survival_id in survivals:
            logging.warning(f'Survival {survival_id} exists!')

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
            survivals[survival_id] = survival
        except TypeError as e:
            logging.error('Wrong data type for Survival %s: %s', survival_id, e)
        except ValueError as e:
            logging.error('Invalid value for Survival %s: %s', survival_id, e)

        # Add mappings of participant ID's to survival ID's
        if participant_id not in participants.keys():
            raise ValueError(f'Survival {survival_id} references nonexistent Participant {participant_id}!')

        survivals_to_participants[survival_id] = participant_id

def check_survivals_for_participants():
    survival_ids_to_remove = []

    for survival_id in survivals.keys():
        if survival_id not in survivals_to_participants.keys():
            logging.warning(f'Survival {survival_id} does not have a Participant!')
            logging.warning(f'Skipping Survival {survival_id}...')
            survival_ids_to_remove.append(survival_id)

    for survival_id in survival_ids_to_remove:
        del survivals[survival_id]

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

def make_uuid(node_type, study_id, record_id):
    uuid_name = "".join([
        node_type,
        study_id,
        record_id
    ])

    return str(uuid.uuid5(uuid.NAMESPACE_URL, uuid_name))

transform()
