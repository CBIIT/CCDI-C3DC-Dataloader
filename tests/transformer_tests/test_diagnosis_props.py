import unittest
import yaml
from transformer.nodes import Diagnosis

ERROR_MAP = {
    'type': TypeError,
    'value': ValueError
}

class TestDiagnosisFactory():
    def create_diagnosis(
            self,
            id = 'abc-123',
            age_at_diagnosis = 96,
            anatomic_site = 'C74.9 : Adrenal gland, NOS',
            diagnosis_basis = 'Not Reported',
            diagnosis = '9500/3 : Neuroblastoma, NOS',
            diagnosis_classification_system = 'ICD-O-3.2',
            diagnosis_comment = 'Neuroblastoma',
            diagnosis_id = '328b01d8-b493-48fe-ba2d-0e2d30ca9883',
            disease_phase = 'Initial Diagnosis',
            toronto_childhood_cancer_staging = 'Neuroblastoma Stage M',
            tumor_classification = 'Primary',
            tumor_grade = 'High Grade',
            tumor_stage_clinical_m = 'Not Reported',
            tumor_stage_clinical_n = 'Not Reported',
            tumor_stage_clinical_t = 'Not Reported'):
        diagnosis = Diagnosis(
            id,
            age_at_diagnosis,
            anatomic_site,
            diagnosis_basis,
            diagnosis,
            diagnosis_classification_system,
            diagnosis_comment,
            diagnosis_id,
            disease_phase,
            toronto_childhood_cancer_staging,
            tumor_classification,
            tumor_grade,
            tumor_stage_clinical_m,
            tumor_stage_clinical_n,
            tumor_stage_clinical_t
        )

        return diagnosis

class TestDiagnosisProps(unittest.TestCase):
    def setUp(self):
        self.diagnosis_factory = TestDiagnosisFactory()

        with open('tests/transformer_tests/test_cases/test_diagnosis_props.yml', 'r', encoding='utf8') as file:
            self.test_cases = yaml.safe_load(file)

    # Diagnosis.id
    def test_diagnosis_id(self):
        test_msg = 'Testing Diagnosis.id being <{}>...'

        for test_case in self.test_cases['id']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.diagnosis_factory.create_diagnosis(id=value)

    # Diagnosis.age_at_diagnosis
    def test_diagnosis_age_at_diagnosis(self):
        test_msg = 'Testing Diagnosis.age_at_diagnosis being <{}>...'

        for test_case in self.test_cases['age_at_diagnosis']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.diagnosis_factory.create_diagnosis(age_at_diagnosis=value)

    # Diagnosis.anatomic_site
    def test_diagnosis_anatomic_site(self):
        test_msg = 'Testing Diagnosis.anatomic_site being <{}>...'

        for test_case in self.test_cases['anatomic_site']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.diagnosis_factory.create_diagnosis(anatomic_site=value)

    # Diagnosis.diagnosis_basis
    def test_diagnosis_diagnosis_basis(self):
        test_msg = 'Testing Diagnosis.diagnosis_basis being <{}>...'

        for test_case in self.test_cases['diagnosis_basis']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.diagnosis_factory.create_diagnosis(diagnosis_basis=value)

    # Diagnosis.diagnosis
    def test_diagnosis_diagnosis(self):
        test_msg = 'Testing Diagnosis.diagnosis being <{}>...'

        for test_case in self.test_cases['diagnosis']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.diagnosis_factory.create_diagnosis(diagnosis=value)

    # Diagnosis.diagnosis_classification_system
    def test_diagnosis_diagnosis_classification_system(self):
        test_msg = 'Testing Diagnosis.diagnosis_classification_system being <{}>...'

        for test_case in self.test_cases['diagnosis_classification_system']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.diagnosis_factory.create_diagnosis(diagnosis_classification_system=value)

    # Diagnosis.diagnosis_comment
    def test_diagnosis_diagnosis_comment(self):
        test_msg = 'Testing Diagnosis.diagnosis_comment being <{}>...'

        for test_case in self.test_cases['diagnosis_comment']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.diagnosis_factory.create_diagnosis(diagnosis_comment=value)

    # Diagnosis.diagnosis_id
    def test_diagnosis_diagnosis_id(self):
        test_msg = 'Testing Diagnosis.diagnosis_id being <{}>...'

        for test_case in self.test_cases['diagnosis_id']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.diagnosis_factory.create_diagnosis(diagnosis_id=value)

    # Diagnosis.disease_phase
    def test_diagnosis_disease_phase(self):
        test_msg = 'Testing Diagnosis.disease_phase being <{}>...'

        for test_case in self.test_cases['disease_phase']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.diagnosis_factory.create_diagnosis(disease_phase=value)

    # Diagnosis.toronto_childhood_cancer_staging
    def test_diagnosis_toronto_childhood_cancer_staging(self):
        test_msg = 'Testing Diagnosis.toronto_childhood_cancer_staging being <{}>...'

        for test_case in self.test_cases['toronto_childhood_cancer_staging']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.diagnosis_factory.create_diagnosis(toronto_childhood_cancer_staging=value)

    # Diagnosis.tumor_classification
    def test_diagnosis_tumor_classification(self):
        test_msg = 'Testing Diagnosis.tumor_classification being <{}>...'

        for test_case in self.test_cases['tumor_classification']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.diagnosis_factory.create_diagnosis(tumor_classification=value)

    # Diagnosis.tumor_grade
    def test_diagnosis_tumor_grade(self):
        test_msg = 'Testing Diagnosis.tumor_grade being <{}>...'

        for test_case in self.test_cases['tumor_grade']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.diagnosis_factory.create_diagnosis(tumor_grade=value)

    # Diagnosis.tumor_stage_clinical_m
    def test_diagnosis_tumor_stage_clinical_m(self):
        test_msg = 'Testing Diagnosis.tumor_stage_clinical_m being <{}>...'

        for test_case in self.test_cases['tumor_stage_clinical_m']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.diagnosis_factory.create_diagnosis(tumor_stage_clinical_m=value)

    # Diagnosis.tumor_stage_clinical_n
    def test_diagnosis_tumor_stage_clinical_n(self):
        test_msg = 'Testing Diagnosis.tumor_stage_clinical_n being <{}>...'

        for test_case in self.test_cases['tumor_stage_clinical_n']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.diagnosis_factory.create_diagnosis(tumor_stage_clinical_n=value)

    # Diagnosis.tumor_stage_clinical_t
    def test_diagnosis_tumor_stage_clinical_t(self):
        test_msg = 'Testing Diagnosis.tumor_stage_clinical_t being <{}>...'

        for test_case in self.test_cases['tumor_stage_clinical_t']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.diagnosis_factory.create_diagnosis(tumor_stage_clinical_t=value)

if __name__ == '__main__':
    unittest.main()
