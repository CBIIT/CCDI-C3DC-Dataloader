import unittest
import yaml
from transformer.nodes import TreatmentResponse

ERROR_MAP = {
    'type': TypeError,
    'value': ValueError
}

class TestTreatmentResponseFactory():
    def create_treatment_response(
            self,
            id = 'abc-123',
            age_at_response = 1,
            response = 'Complete Remission',
            response_category = 'Bone Marrow Response',
            response_system = 'iRANO',
            treatment_response_id = 'abc-123'):
        treatment_response = TreatmentResponse(
            id,
            age_at_response,
            response,
            response_category,
            response_system,
            treatment_response_id
        )

        return treatment_response

class TestTreatmentResponseProps(unittest.TestCase):
    def setUp(self):
        self.treatment_response_factory = TestTreatmentResponseFactory()

        with open('tests/transformer_tests/test_cases/test_treatment_response_props.yml', 'r', encoding='utf8') as file:
            self.test_cases = yaml.safe_load(file)

    # TreatmentResponse.id
    def test_treatment_id(self):
        test_msg = 'Testing TreatmentResponse.id being <{}>...'

        for test_case in self.test_cases['id']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.treatment_response_factory.create_treatment_response(id=value)

    # TreatmentResponse.age_at_response
    def test_treatment_response_age_at_response(self):
        test_msg = 'Testing TreatmentResponse.age_at_response being <{}>...'

        for test_case in self.test_cases['age_at_response']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.treatment_response_factory.create_treatment_response(age_at_response=value)

    # TreatmentResponse.response
    def test_treatment_response_response(self):
        test_msg = 'Testing TreatmentResponse.response being <{}>...'

        for test_case in self.test_cases['response']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.treatment_response_factory.create_treatment_response(response=value)

    # TreatmentResponse.response_category
    def test_treatment_response_response_category(self):
        test_msg = 'Testing TreatmentResponse.response_category being <{}>...'

        for test_case in self.test_cases['response_category']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.treatment_response_factory.create_treatment_response(response_category=value)

    # TreatmentResponse.response_system
    def test_treatment_response_response_system(self):
        test_msg = 'Testing TreatmentResponse.response_system being <{}>...'

        for test_case in self.test_cases['response_system']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.treatment_response_factory.create_treatment_response(response_system=value)

    # TreatmentResponse.treatment_response_id
    def test_treatment_response_treatment_response_id(self):
        test_msg = 'Testing TreatmentResponse.treatment_response_id being <{}>...'

        for test_case in self.test_cases['treatment_response_id']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.treatment_response_factory.create_treatment_response(treatment_response_id=value)

if __name__ == '__main__':
    unittest.main()
