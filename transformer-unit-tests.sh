#!/bin/sh

python -m unittest tests.transformer_tests.test_diagnosis_props
python -m unittest tests.transformer_tests.test_participant_props
python -m unittest tests.transformer_tests.test_reference_file_props
python -m unittest tests.transformer_tests.test_study_props
python -m unittest tests.transformer_tests.test_survival_props
