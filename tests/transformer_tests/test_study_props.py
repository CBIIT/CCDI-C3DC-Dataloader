import unittest
import yaml
from transformer.nodes import Study

ERROR_MAP = {
    'type': TypeError,
    'value': ValueError
}

class TestStudyFactory():
    def create_study(
            self,
            id = 'abc-123',
            consent = 'DS-PEDCR',
            consent_number = 1,
            external_url = 'foo',
            dbgap_accession = "['phs000467']",
            study_description = 'foo',
            study_id = 'phs000467.v22.p8',
            study_name = 'TARGET NBL'):
        study = Study(
            id,
            consent,
            consent_number,
            external_url,
            dbgap_accession,
            study_description,
            study_id,
            study_name
        )

        return study

class TestStudyProps(unittest.TestCase):
    def setUp(self):
        self.study_factory = TestStudyFactory()

        with open('tests/transformer_tests/test_cases/test_study_props.yml', 'r', encoding='utf8') as file:
            self.test_cases = yaml.safe_load(file)

    # Study.id
    def test_study_id(self):
        test_msg = 'Testing Study.id being <{}>...'

        for test_case in self.test_cases['id']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.study_factory.create_study(id=value)

    # Study.consent
    def test_study_consent(self):
        test_msg = 'Testing Study.consent being <{}>...'

        for test_case in self.test_cases['consent']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.study_factory.create_study(consent=value)

    # Study.consent_number
    def test_study_consent_number(self):
        test_msg = 'Testing Study.consent_number being <{}>...'

        for test_case in self.test_cases['consent_number']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.study_factory.create_study(consent_number=value)

    # Study.external_url
    def test_study_external_url(self):
        test_msg = 'Testing Study.external_url being <{}>...'

        for test_case in self.test_cases['external_url']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.study_factory.create_study(external_url=value)

    # Study.dbgap_accession
    def test_study_dbgap_accession(self):
        test_msg = 'Testing Study.dbgap_accession being <{}>...'

        for test_case in self.test_cases['dbgap_accession']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.study_factory.create_study(dbgap_accession=value)

    # Study.study_description
    def test_study_study_description(self):
        test_msg = 'Testing Study.study_description being <{}>...'

        for test_case in self.test_cases['study_description']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.study_factory.create_study(study_description=value)

    # Study.study_id
    def test_study_study_id(self):
        test_msg = 'Testing Study.study_id being <{}>...'

        for test_case in self.test_cases['study_id']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.study_factory.create_study(study_id=value)

    # Study.study_name
    def test_study_study_name(self):
        test_msg = 'Testing Study.study_name being <{}>...'

        for test_case in self.test_cases['study_name']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.study_factory.create_study(study_name=value)

if __name__ == '__main__':
    unittest.main()
