import unittest
from transformer.nodes import Diagnosis

class TestDiagnosisFactory():
    def create_diagnosis(
            self,
            age_at_diagnosis = 96,
            anatomic_site = ['C74.9 : Adrenal gland, NOS'],
            diagnosis_basis = ['Not Reported'],
            diagnosis_classification = '9500/3 : Neuroblastoma, NOS',
            diagnosis_classification_system = 'ICD-O-3.2',
            diagnosis_comment = 'Neuroblastoma',
            diagnosis_id = '328b01d8-b493-48fe-ba2d-0e2d30ca9883',
            diagnosis_verification_status = 'Not Reported',
            disease_phase = 'Initial Diagnosis',
            toronto_childhood_cancer_staging = 'Neuroblastoma Stage M',
            tumor_grade = 'High Grade',
            tumor_stage_clinical_m = None,
            tumor_stage_clinical_n = None,
            tumor_stage_clinical_t = None):

        diagnosis = Diagnosis(
            age_at_diagnosis,
            anatomic_site,
            diagnosis_basis,
            diagnosis_classification,
            diagnosis_classification_system,
            diagnosis_comment,
            diagnosis_id,
            diagnosis_verification_status,
            disease_phase,
            toronto_childhood_cancer_staging,
            tumor_grade,
            tumor_stage_clinical_m,
            tumor_stage_clinical_n,
            tumor_stage_clinical_t
        )

        return diagnosis

class TestDiagnosisProps(unittest.TestCase):
    def setUp(self):
        self.diagnosis_factory = TestDiagnosisFactory()

    # Diagnosis.age_at_diagnosis
    def test_diagnosis_age_at_diagnosis(self):
        test_msg = 'Testing Diagnosis.age_at_diagnosis being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Age at Diagnosis is missing'):
            value = None
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(age_at_diagnosis=value)

        with self.assertRaisesRegex(TypeError, 'Age at Diagnosis is missing'):
            value = ''
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(age_at_diagnosis=value)

        with self.assertRaisesRegex(TypeError, "Age at Diagnosis `foo` must be of type <class 'int'>"):
            value = 'foo'
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(age_at_diagnosis=value)

    # Diagnosis.anatomic_site
    def test_diagnosis_anatomic_site(self):
        test_msg = 'Testing Diagnosis.anatomic_site being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Anatomic Site is missing'):
            value = None
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(anatomic_site=value)

        with self.assertRaisesRegex(TypeError, 'Anatomic Site is missing'):
            value = ''
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(anatomic_site=value)

        with self.assertRaisesRegex(TypeError, "Anatomic Site `Foo` must be of type <class 'list'>"):
            value = 'Foo'
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(anatomic_site=value)

        with self.assertRaisesRegex(ValueError, "Anatomic Site `\['Foo'\]` must be a subset of the specified values"):
            value = ['Foo']
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(anatomic_site=value)

    # Diagnosis.diagnosis_basis
    def test_diagnosis_diagnosis_basis(self):
        test_msg = 'Testing Diagnosis.diagnosis_basis being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Diagnosis Basis is missing'):
            value = None
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(diagnosis_basis=value)

        with self.assertRaisesRegex(TypeError, 'Diagnosis Basis is missing'):
            value = ''
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(diagnosis_basis=value)

        with self.assertRaisesRegex(TypeError, "Diagnosis Basis `Foo` must be of type <class 'list'>"):
            value = 'Foo'
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(diagnosis_basis=value)

        with self.assertRaisesRegex(ValueError, "Diagnosis Basis `\['Foo'\]` must be a subset of the specified values"):
            value = ['Foo']
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(diagnosis_basis=value)

    # Diagnosis.diagnosis_classification
    def test_diagnosis_diagnosis_classification(self):
        test_msg = 'Testing Diagnosis.diagnosis_classification being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Diagnosis Classification is missing'):
            value = None
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(diagnosis_classification=value)

        with self.assertRaisesRegex(TypeError, 'Diagnosis Classification is missing'):
            value = ''
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(diagnosis_classification=value)

        with self.assertRaisesRegex(TypeError, "Diagnosis Classification `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(diagnosis_classification=value)

        with self.assertRaisesRegex(ValueError, 'Diagnosis Classification `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(diagnosis_classification=value)

    # Diagnosis.diagnosis_classification_system
    def test_diagnosis_diagnosis_classification_system(self):
        test_msg = 'Testing Diagnosis.diagnosis_classification_system being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Diagnosis Classification System is missing'):
            value = None
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(diagnosis_classification_system=value)

        with self.assertRaisesRegex(TypeError, 'Diagnosis Classification System is missing'):
            value = ''
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(diagnosis_classification_system=value)

        with self.assertRaisesRegex(TypeError, "Diagnosis Classification System `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(diagnosis_classification_system=value)

        with self.assertRaisesRegex(ValueError, 'Diagnosis Classification System `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(diagnosis_classification_system=value)

    # Diagnosis.diagnosis_comment
    def test_diagnosis_diagnosis_comment(self):
        test_msg = 'Testing Diagnosis.diagnosis_comment being <{}>...'

        with self.assertRaisesRegex(TypeError, "Diagnosis Comment `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(diagnosis_comment=value)

    # Diagnosis.diagnosis_id
    def test_diagnosis_diagnosis_id(self):
        test_msg = 'Testing Diagnosis.diagnosis_id being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Diagnosis ID is missing'):
            value = None
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(diagnosis_id=value)

        with self.assertRaisesRegex(TypeError, 'Diagnosis ID is missing'):
            value = ''
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(diagnosis_id=value)

        with self.assertRaisesRegex(TypeError, "Diagnosis ID `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(diagnosis_id=value)

    # Diagnosis.diagnosis_verification_status
    def test_diagnosis_diagnosis_verification_status(self):
        test_msg = 'Testing Diagnosis.diagnosis_verification_status being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Diagnosis Verification Status is missing'):
            value = None
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(diagnosis_verification_status=value)

        with self.assertRaisesRegex(TypeError, 'Diagnosis Verification Status is missing'):
            value = ''
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(diagnosis_verification_status=value)

        with self.assertRaisesRegex(TypeError, "Diagnosis Verification Status `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(diagnosis_verification_status=value)

        with self.assertRaisesRegex(ValueError, 'Diagnosis Verification Status `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(diagnosis_verification_status=value)

    # Diagnosis.disease_phase
    def test_diagnosis_disease_phase(self):
        test_msg = 'Testing Diagnosis.disease_phase being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Disease Phase is missing'):
            value = None
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(disease_phase=value)

        with self.assertRaisesRegex(TypeError, 'Disease Phase is missing'):
            value = ''
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(disease_phase=value)

        with self.assertRaisesRegex(TypeError, "Disease Phase `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(disease_phase=value)

        with self.assertRaisesRegex(ValueError, 'Disease Phase `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(disease_phase=value)

    # Diagnosis.toronto_childhood_cancer_staging
    def test_diagnosis_toronto_childhood_cancer_staging(self):
        test_msg = 'Testing Diagnosis.toronto_childhood_cancer_staging being <{}>...'

        with self.assertRaisesRegex(TypeError, "Toronto Childhood Cancer Staging `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(toronto_childhood_cancer_staging=value)

        with self.assertRaisesRegex(ValueError, 'Toronto Childhood Cancer Staging `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(toronto_childhood_cancer_staging=value)

    # Diagnosis.tumor_grade
    def test_diagnosis_tumor_grade(self):
        test_msg = 'Testing Diagnosis.tumor_grade being <{}>...'

        with self.assertRaisesRegex(TypeError, "Tumor Grade `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(tumor_grade=value)

        with self.assertRaisesRegex(ValueError, 'Tumor Grade `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(tumor_grade=value)

    # Diagnosis.tumor_stage_clinical_m
    def test_diagnosis_tumor_stage_clinical_m(self):
        test_msg = 'Testing Diagnosis.tumor_stage_clinical_m being <{}>...'

        with self.assertRaisesRegex(TypeError, "Tumor Clinical M Stage `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(tumor_stage_clinical_m=value)

        with self.assertRaisesRegex(ValueError, 'Tumor Clinical M Stage `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(tumor_stage_clinical_m=value)

    # Diagnosis.tumor_stage_clinical_n
    def test_diagnosis_tumor_stage_clinical_n(self):
        test_msg = 'Testing Diagnosis.tumor_stage_clinical_n being <{}>...'

        with self.assertRaisesRegex(TypeError, "Tumor Clinical N Stage `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(tumor_stage_clinical_n=value)

        with self.assertRaisesRegex(ValueError, 'Tumor Clinical N Stage `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(tumor_stage_clinical_n=value)

    # Diagnosis.tumor_stage_clinical_t
    def test_diagnosis_tumor_stage_clinical_t(self):
        test_msg = 'Testing Diagnosis.tumor_stage_clinical_t being <{}>...'

        with self.assertRaisesRegex(TypeError, "Tumor Clinical T Stage `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(tumor_stage_clinical_t=value)

        with self.assertRaisesRegex(ValueError, 'Tumor Clinical T Stage `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            self.diagnosis_factory.create_diagnosis(tumor_stage_clinical_t=value)

if __name__ == '__main__':
    unittest.main()
