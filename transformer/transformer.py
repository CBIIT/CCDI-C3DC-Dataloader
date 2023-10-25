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

participants_to_studies = {} # Map of participant ids to study ids
participants = {}
studies = {}

def transform():
    print('Parsing Participants from JSON...')
    parse_participants()
    print('Finished parsing Participants\n')

    print('Parsing Studies from JSON...')
    parse_studies()
    print('Finished parsing Studies\n')

    print('Verifying that each Participant has a Study...')
    check_participants_for_studies()
    print('Finished verifying that each Participant has a Study\n')

    print('Writing Participants TSV...')
    write_participants()
    print('Finished writing Participants TSV\n')

    print('Writing Studies TSV...')
    write_studies()
    print('Finished writing Studies TSV')

def parse_participants():
    all_participant_data = discovery_data['participants'] + validation_data['participants']

    for participant_data in all_participant_data:
        participant_id = participant_data['participant_id']

        # Don't consider duplicate participant ID as an error yet
        if participant_id in participants:
            print(f'Participant {participant_id} exists!')
            print(f'Skipping Participant {participant_id}...')

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

def check_participants_for_studies():
    participant_ids_to_remove = []

    for participant_id in participants.keys():
        if participant_id not in participants_to_studies.keys():
            print(f'Participant {participant_id} does not have a study!')
            print(f'Skipping Participant {participant_id}...')
            participant_ids_to_remove.append(participant_id)

    for participant_id in participant_ids_to_remove:
        del participants[participant_id]

def write_participants():
    with open('data/participants.tsv', 'w', newline='') as participants_file:
        tsv_writer = csv.writer(participants_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(PARTICIPANT_HEADERS)

        for participant in participants.values():
            participant_row = participant.to_list()
            for study_id in participants_to_studies[participant.participant_id]:
                row = participant_row + [study_id]
                tsv_writer.writerow(row)

        participants_file.close()

# Log any duplicate participants
def parse_studies():
    all_study_data = discovery_data['studies'] + validation_data['studies']

    for study_data in all_study_data:
        participant_ids = study_data['participant.participant_id']
        study_id = study_data['study_id']

        # Don't consider duplicate study ID as an error yet
        if study_id in studies:
            print(f'Study {study_id} exists!')

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

        # Add mappings of participant ID's to study ID's
        for participant_id in participant_ids:
            if participant_id not in participants.keys():
                raise ValueError(f'Study {study_id} references nonexistent Participant {participant_id}!')

            # Don't consider it an error for a participant to be associated to multiple studies
            if participant_id in participants_to_studies.keys():
                print(f'Participant {participant_id} already matched to {participants_to_studies[participant_id]}!')
                print(f'Mapping participant {participant_id} to another study: {study_id}...')

            participants_to_studies[participant_id] = [study_id]

def write_studies():
    with open('data/studies.tsv', 'w', newline='') as studies_file:
        tsv_writer = csv.writer(studies_file, delimiter='\t', dialect='unix')
        tsv_writer.writerow(STUDY_HEADERS)

        for study in studies.values():
            tsv_writer.writerow(study.to_list())

        studies_file.close()

transform()

discovery_file.close()
validation_file.close()
