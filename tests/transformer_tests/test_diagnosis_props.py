import unittest
from transformer.nodes import Diagnosis

class TestDiagnosisProps(unittest.TestCase):
    def setUp(self):
        pass

    # Diagnosis.age_at_diagnosis
    def test_diagnosis_age_at_diagnosis(self):
        test_msg = 'Testing Diagnosis.age_at_diagnosis being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Age at Diagnosis is missing'):
            value = None
            print(test_msg.format(value))
            Diagnosis(
                age_at_diagnosis = value,
                anatomic_site = 'Adrenal gland, NOS',
                diagnosis_finer_resolution = 'Neuroblastoma',
                diagnosis_icd_cm = None,
                diagnosis_icd_o = ['9500/3 : Neuroblastoma, NOS'],
                diagnosis_id = '328b01d8-b493-48fe-ba2d-0e2d30ca9883',
                disease_phase = 'Initial Diagnosis',
                toronto_childhood_cancer_staging = 'Neuroblastoma Stage M',
                tumor_grade = 'High Grade',
                tumor_stage_clinical_m = None,
                tumor_stage_clinical_n = None,
                tumor_stage_clinical_t = None
            )

        with self.assertRaisesRegex(TypeError, 'Age at Diagnosis is missing'):
            value = ''
            print(test_msg.format(value))
            Diagnosis(
                age_at_diagnosis = value,
                anatomic_site = 'Adrenal gland, NOS',
                diagnosis_finer_resolution = 'Neuroblastoma',
                diagnosis_icd_cm = None,
                diagnosis_icd_o = ['9500/3 : Neuroblastoma, NOS'],
                diagnosis_id = '328b01d8-b493-48fe-ba2d-0e2d30ca9883',
                disease_phase = 'Initial Diagnosis',
                toronto_childhood_cancer_staging = 'Neuroblastoma Stage M',
                tumor_grade = 'High Grade',
                tumor_stage_clinical_m = None,
                tumor_stage_clinical_n = None,
                tumor_stage_clinical_t = None
            )

        with self.assertRaisesRegex(TypeError, "Age at Diagnosis `foo` must be of type <class 'int'>"):
            value = 'foo'
            print(test_msg.format(value))
            Diagnosis(
                age_at_diagnosis = value,
                anatomic_site = 'Adrenal gland, NOS',
                diagnosis_finer_resolution = 'Neuroblastoma',
                diagnosis_icd_cm = None,
                diagnosis_icd_o = ['9500/3 : Neuroblastoma, NOS'],
                diagnosis_id = '328b01d8-b493-48fe-ba2d-0e2d30ca9883',
                disease_phase = 'Initial Diagnosis',
                toronto_childhood_cancer_staging = 'Neuroblastoma Stage M',
                tumor_grade = 'High Grade',
                tumor_stage_clinical_m = None,
                tumor_stage_clinical_n = None,
                tumor_stage_clinical_t = None
            )

    # Diagnosis.anatomic_site
    def test_diagnosis_anatomic_site(self):
        test_msg = 'Testing Diagnosis.anatomic_site being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Anatomic Site is missing'):
            value = None
            print(test_msg.format(value))
            Diagnosis(
                age_at_diagnosis = 96,
                anatomic_site = value,
                diagnosis_finer_resolution = 'Neuroblastoma',
                diagnosis_icd_cm = None,
                diagnosis_icd_o = ['9500/3 : Neuroblastoma, NOS'],
                diagnosis_id = '328b01d8-b493-48fe-ba2d-0e2d30ca9883',
                disease_phase = 'Initial Diagnosis',
                toronto_childhood_cancer_staging = 'Neuroblastoma Stage M',
                tumor_grade = 'High Grade',
                tumor_stage_clinical_m = None,
                tumor_stage_clinical_n = None,
                tumor_stage_clinical_t = None
            )

        with self.assertRaisesRegex(TypeError, 'Anatomic Site is missing'):
            value = ''
            print(test_msg.format(value))
            Diagnosis(
                age_at_diagnosis = 96,
                anatomic_site = value,
                diagnosis_finer_resolution = 'Neuroblastoma',
                diagnosis_icd_cm = None,
                diagnosis_icd_o = ['9500/3 : Neuroblastoma, NOS'],
                diagnosis_id = '328b01d8-b493-48fe-ba2d-0e2d30ca9883',
                disease_phase = 'Initial Diagnosis',
                toronto_childhood_cancer_staging = 'Neuroblastoma Stage M',
                tumor_grade = 'High Grade',
                tumor_stage_clinical_m = None,
                tumor_stage_clinical_n = None,
                tumor_stage_clinical_t = None
            )

        with self.assertRaisesRegex(TypeError, "Anatomic Site `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            Diagnosis(
                age_at_diagnosis = 96,
                anatomic_site = value,
                diagnosis_finer_resolution = 'Neuroblastoma',
                diagnosis_icd_cm = None,
                diagnosis_icd_o = ['9500/3 : Neuroblastoma, NOS'],
                diagnosis_id = '328b01d8-b493-48fe-ba2d-0e2d30ca9883',
                disease_phase = 'Initial Diagnosis',
                toronto_childhood_cancer_staging = 'Neuroblastoma Stage M',
                tumor_grade = 'High Grade',
                tumor_stage_clinical_m = None,
                tumor_stage_clinical_n = None,
                tumor_stage_clinical_t = None
            )

        with self.assertRaisesRegex(ValueError, 'Anatomic Site `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            Diagnosis(
                age_at_diagnosis = 96,
                anatomic_site = value,
                diagnosis_finer_resolution = 'Neuroblastoma',
                diagnosis_icd_cm = None,
                diagnosis_icd_o = ['9500/3 : Neuroblastoma, NOS'],
                diagnosis_id = '328b01d8-b493-48fe-ba2d-0e2d30ca9883',
                disease_phase = 'Initial Diagnosis',
                toronto_childhood_cancer_staging = 'Neuroblastoma Stage M',
                tumor_grade = 'High Grade',
                tumor_stage_clinical_m = None,
                tumor_stage_clinical_n = None,
                tumor_stage_clinical_t = None
            )

if __name__ == '__main__':
    unittest.main()
