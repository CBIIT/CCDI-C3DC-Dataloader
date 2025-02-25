import unittest
import yaml
from transformer.nodes import Treatment

ERROR_MAP = {
    'type': TypeError,
    'value': ValueError
}

class TestTreatmentFactory():
    def create_treatment(
            self,
            id = 'abc-123',
            age_at_treatment_end = 419,
            age_at_treatment_start = 68,
            treatment_agent = ['Treatment Agent Value'],
            treatment_id = 'abc-123',
            treatment_type = 'Immunotherapy'):
        treatment = Treatment(
            id,
            age_at_treatment_end,
            age_at_treatment_start,
            treatment_agent,
            treatment_id,
            treatment_type
        )

        return treatment

class TestTreatmentProps(unittest.TestCase):
    def setUp(self):
        self.treatment_factory = TestTreatmentFactory()

        with open('tests/transformer_tests/test_cases/test_treatment_props.yml', 'r', encoding='utf8') as file:
            self.test_cases = yaml.safe_load(file)

    # Treatment.id
    def test_treatment_id(self):
        test_msg = 'Testing Treatment.id being <{}>...'

        for test_case in self.test_cases['id']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.treatment_factory.create_treatment(id=value)

    # Treatment.age_at_treatment_end
    def test_treatment_age_at_treatment_end(self):
        test_msg = 'Testing Treatment.age_at_treatment_end being <{}>...'

        for test_case in self.test_cases['age_at_treatment_end']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.treatment_factory.create_treatment(age_at_treatment_end=value)

    # Treatment.age_at_treatment_start
    def test_treatment_age_at_treatment_start(self):
        test_msg = 'Testing Treatment.age_at_treatment_start being <{}>...'

        for test_case in self.test_cases['age_at_treatment_start']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.treatment_factory.create_treatment(age_at_treatment_start=value)

    # Treatment.treatment_agent
    def test_treatment_treatment_agent(self):
        test_msg = 'Testing Treatment.treatment_agent being <{}>...'

        for test_case in self.test_cases['treatment_agent']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.treatment_factory.create_treatment(treatment_agent=value)

    # Treatment.treatment_id
    def test_treatment_treatment_id(self):
        test_msg = 'Testing Treatment.treatment_id being <{}>...'

        for test_case in self.test_cases['treatment_id']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.treatment_factory.create_treatment(treatment_id=value)

    # Treatment.treatment_type
    def test_treatment_treatment_type(self):
        test_msg = 'Testing Treatment.treatment_type being <{}>...'

        for test_case in self.test_cases['treatment_type']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.treatment_factory.create_treatment(treatment_type=value)

if __name__ == '__main__':
    unittest.main()
