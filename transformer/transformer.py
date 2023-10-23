import csv
import json
from nodes import Participant, Study

PARTICIPANT_HEADERS = [
    'type',
    'participant_id',
    'race',
    'gender',
    'ethnicity',
    'alternate_participant_id',
    'id',
    'study.study_id',
]

STUDY_HEADERS = [
    'type',
    'study_id',
    'phs_accession',
    'acl',
    'study_name',
    'study_short_title',
    'study_acronym',
    'study_description',
    'consent',
    'consent_number',
    'external_url',
    'experimental_strategy_and_data_subtype',
    'study_data_types',
    'size_of_data_being_uploaded',
    'id',
]

discovery_file = open('data/TARGET_NBL_ClinicalData_Discovery_20220125.json')
validation_file = open('data/TARGET_NBL_ClinicalData_Validation_20220125.json')
discovery_data = json.load(discovery_file)
validation_data = json.load(validation_file)

def transform():
    participants = parse_participants()
    write_participants(participants)
    studies = parse_studies()
    write_studies(studies)

def parse_participants():
    all_participant_data = discovery_data['participants'] + validation_data['participants']
    participants = {}

    for participant_data in all_participant_data:
        participant_id = participant_data['participant_id']

        if participant_id in participants:
            print('Participant exists!')
        else:
            try:
                participant = Participant(
                    alternate_participant_id = None,
                    ethnicity = participant_data['ethnicity'][0],
                    gender = participant_data['gender'],
                    participant_id = participant_data['participant_id'],
                    race = participant_data['race'][0]
                )
                participants[participant_id] = participant
            except TypeError as e:
                print('Wrong data type!', e)
            except ValueError as e:
                print('Invalid value!', e)
    return participants

def write_participants(participants):
    with open('data/participants.tsv', 'w', newline='') as participants_file:
        tsv_writer = csv.writer(participants_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(PARTICIPANT_HEADERS)

        for participant in participants.values():
            tsv_writer.writerow(participant.to_list())

        participants_file.close()

# Log any duplicate participants
def parse_studies():
    all_study_data = discovery_data['studies'] + validation_data['studies']
    studies = {}

    for study_data in all_study_data:
        study_id = study_data['study_id']

        if study_id in studies:
            print('Study exists!')
        else:
            try:
                study = Study(
                    acl = study_data['acl'],
                    consent = study_data['consent'],
                    consent_number = study_data['consent_number'],
                    external_url = None,
                    phs_accession = study_data['phs_accession'],
                    study_acronym = study_data['study_acronym'],
                    study_description = study_data['study_description'],
                    study_id = study_data['study_id'],
                    study_name = study_data['study_name'],
                    study_short_title = study_data['study_short_title']
                )
                studies[study_id] = study
            except TypeError as e:
                print('Wrong data type!', e)
            except ValueError as e:
                print('Invalid value!', e)
    return studies

def write_studies(studies):
    with open('data/studies.tsv', 'w', newline='') as studies_file:
        tsv_writer = csv.writer(studies_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(STUDY_HEADERS)

        for study in studies.values():
            tsv_writer.writerow(study.to_list())

        studies_file.close()

transform()

discovery_file.close()
validation_file.close()
