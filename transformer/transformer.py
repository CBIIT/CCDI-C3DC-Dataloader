# Reads harmonized JSON files and produces TSV files

import json
import logging
import os
import sys
import time
from checkers import (
    check_diagnoses_for_participants,
    check_participants_for_studies,
    check_reference_files_for_studies,
    check_survivals_for_participants,
    check_treatments_for_participants,
    check_treatment_responses_for_participants,
)
from parsers import (
    parse_diagnoses,
    parse_participants,
    parse_reference_files,
    parse_studies,
    parse_survivals,
)
from node_types import NODE_TYPES
from writers import (
    write_diagnoses,
    write_participants,
    write_reference_files,
    write_studies,
    write_survivals,
)
logger = logging.getLogger(__name__)

def main():
    # Set up logging
    timestr = time.strftime('%Y%m%d-%H%M%S')
    log_targets = logging.StreamHandler(sys.stdout), logging.FileHandler('tmp/transformer-' + timestr + '.log')
    logging.basicConfig(format='%(message)s', level=logging.INFO, handlers=log_targets)

    # Node names we expect from the JSON files
    node_names = [
        'diagnoses',
        'participants',
        'reference_files',
        'studies',
        'survivals',
        'treatments',
        'treatment_responses',
    ]
    dir_paths = []

    # Find data subdirectories
    for dirname in os.listdir('data/'):
        dir_path = 'data/' + dirname

        # Add directory to visit later
        if os.path.isdir(dir_path):
            dir_paths.append(dir_path)

    logger.info(f'Found {len(dir_paths)} subdirectories\n')

    # Look at all the files in the data directory, grouping files within a subdirectory into a single study
    for dir_path in dir_paths:
        all_json_data = dict.fromkeys(node_names, [])
        file_paths = []

        # Look in this subdirectory for individual JSON files to group into a single study
        for filename in os.listdir(dir_path):
            # Add JSON file to parse later
            if filename.endswith('.json'):
                file_paths.append('/'.join([dir_path, filename]))
        
        # Skip if no JSON files in subdirectory
        if len(file_paths) == 0:
            continue
        
        logger.info(f'Found {len(file_paths)} JSON file(s) in subdirectory {dir_path}\n')

        for file_path in file_paths:
            logger.info('Reading data from ' + file_path + '...')

            json_file = open(file_path)
            json_data = json.load(json_file)

            for node_name in node_names:
                if node_name not in json_data:
                    continue

                all_json_data[node_name] = all_json_data.get(node_name) + json_data.get(node_name)

            json_file.close()
            logger.info('Finished reading data from ' + file_path + '...\n')

        processJsonData(all_json_data)

# Runs the parsers, checkers, and writers
def processJsonData(data):
    # Big dict in which we save all the objects before writing them to TSV
    records = {node_type.value: {} for node_type in NODE_TYPES}

    # TODO crosscheck foreign keys (eg: check each participant's study ID consistent with study's participant ID's)
    associations = {
        'diagnoses_to_participants': {}, # Map of diagnosis_id to participant_id
        'participants_to_studies': {}, # Map of participant_id to study_id
        'reference_files_to_studies': {}, # Map of reference_file_id to study_id
        'survivals_to_participants': {}, # Map of survival_id to participant_id
        'treatments_to_participants': {}, # Map of treatment_id to participant_id
        'treatment_responses_to_participants': {}, # Map of treatment_response_id to participant_id
    }
    node_funcs = {
        NODE_TYPES.STUDY.value: {
            'parser': parse_studies,
            'writer': write_studies,
        },
        NODE_TYPES.PARTICIPANT.value: {
            'checker': check_participants_for_studies,
            'parser': parse_participants,
            'writer': write_participants,
        },
        NODE_TYPES.SURVIVAL.value: {
            'checker': check_survivals_for_participants,
            'parser': parse_survivals,
            'writer': write_survivals,
        },
        NODE_TYPES.DIAGNOSIS.value: {
            'checker': check_diagnoses_for_participants,
            'parser': parse_diagnoses,
            'writer': write_diagnoses,
        },
        NODE_TYPES.REFERENCE_FILE.value: {
            'checker': check_reference_files_for_studies,
            'parser': parse_reference_files,
            'writer': write_reference_files,
        },
        NODE_TYPES.TREATMENT.value: {
            'checker': check_treatments_for_participants,
            'parser': parse_reference_files,
            'writer': write_reference_files,
        },
        NODE_TYPES.TREATMENT_RESPONSE.value: {
            'checker': check_treatment_responses_for_participants,
            'parser': parse_reference_files,
            'writer': write_reference_files,
        },
    }

    # Run the parsers
    for node_name, node_func in node_funcs.items():
        parser = node_func.get('parser')

        # Error if there is no parser for this node
        if parser is None:
            raise Exception(f'Node type {node_name} has no parser!')

        logger.info(f'Parsing {node_name} records from JSON...')
        parser(data, records, associations)
        logger.info(f'Finished parsing {node_name} records\n')

    # Run the checkers
    for node_name, node_func in node_funcs.items():
        checker = node_func.get('checker')

        # Parent nodes (Study, for C3DC) don't have foreign keys to other nodes
        if checker is None:
            continue

        logger.info(f'Checking each {node_name} record\'s foreign keys...')
        checker(records, associations)
        logger.info(f'Finished checking each {node_name} record\'s foreign keys\n')

    # Run the writers
    for node_name, node_func in node_funcs.items():
        writer = node_func.get('writer')

        if node_name != NODE_TYPES.STUDY.value and len(records.get(node_name)) == 0:
            logger.info(f'No {node_name} records. Skipping TSV...\n')
            continue

        # Error if there is no writer for this node
        if writer is None:
            raise Exception(f'Node type {node_name} has no writer!')

        logger.info(f'Writing {node_name} records to TSV...')
        writer(records, associations)
        logger.info(f'Finished writing {node_name} records to TSV\n')

if __name__ == '__main__':
    main()
