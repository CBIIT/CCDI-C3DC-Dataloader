import unittest
from transformer.nodes import TreatmentResponse

class TestTreatmentResponseFactory():
    def create_treatment_response(
            self,
            id = 'abc-123',
            age_at_response = '1',
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

    # TreatmentResponse.id
    def test_treatment_id(self):
        test_msg = 'Testing TreatmentResponse.id being <{}>...'

        with self.assertRaisesRegex(TypeError, "ID `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.treatment_response_factory.create_treatment_response(id=value)

    # TreatmentResponse.age_at_response
    def test_treatment_response_age_at_response(self):
        test_msg = 'Testing TreatmentResponse.age_at_response being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Age at Response is missing'):
            value = None
            print(test_msg.format(value))
            self.treatment_response_factory.create_treatment_response(age_at_response=value)

        with self.assertRaisesRegex(TypeError, 'Age at Response is missing'):
            value = ''
            print(test_msg.format(value))
            self.treatment_response_factory.create_treatment_response(age_at_response=value)

        with self.assertRaisesRegex(TypeError, "Age at Response `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.treatment_response_factory.create_treatment_response(age_at_response=value)

    # TreatmentResponse.response
    def test_treatment_response_response(self):
        test_msg = 'Testing TreatmentResponse.response being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Response is missing'):
            value = None
            print(test_msg.format(value))
            self.treatment_response_factory.create_treatment_response(response=value)

        with self.assertRaisesRegex(TypeError, 'Response is missing'):
            value = ''
            print(test_msg.format(value))
            self.treatment_response_factory.create_treatment_response(response=value)

        with self.assertRaisesRegex(TypeError, "Response `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.treatment_response_factory.create_treatment_response(response=value)

        with self.assertRaisesRegex(ValueError, 'Response `foo` must be one of the specified values'):
            value = 'foo'
            print(test_msg.format(value))
            self.treatment_response_factory.create_treatment_response(response=value)

    # TreatmentResponse.response_category
    def test_treatment_response_response_category(self):
        test_msg = 'Testing TreatmentResponse.response_category being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Response Category is missing'):
            value = None
            print(test_msg.format(value))
            self.treatment_response_factory.create_treatment_response(response_category=value)

        with self.assertRaisesRegex(TypeError, 'Response Category is missing'):
            value = ''
            print(test_msg.format(value))
            self.treatment_response_factory.create_treatment_response(response_category=value)

        with self.assertRaisesRegex(TypeError, "Response Category `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.treatment_response_factory.create_treatment_response(response_category=value)

        with self.assertRaisesRegex(ValueError, 'Response Category `foo` must be one of the specified values'):
            value = 'foo'
            print(test_msg.format(value))
            self.treatment_response_factory.create_treatment_response(response_category=value)

    # TreatmentResponse.response_system
    def test_treatment_response_response_system(self):
        test_msg = 'Testing TreatmentResponse.response_system being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Response System is missing'):
            value = None
            print(test_msg.format(value))
            self.treatment_response_factory.create_treatment_response(response_system=value)

        with self.assertRaisesRegex(TypeError, 'Response System is missing'):
            value = ''
            print(test_msg.format(value))
            self.treatment_response_factory.create_treatment_response(response_system=value)

        with self.assertRaisesRegex(TypeError, "Response System `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.treatment_response_factory.create_treatment_response(response_system=value)

        with self.assertRaisesRegex(ValueError, 'Response System `foo` must be one of the specified values'):
            value = 'foo'
            print(test_msg.format(value))
            self.treatment_response_factory.create_treatment_response(response_system=value)

    # TreatmentResponse.treatment_response_id
    def test_treatment_response_treatment_response_id(self):
        test_msg = 'Testing TreatmentResponse.treatment_response_id being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Treatment Response ID is missing'):
            value = None
            print(test_msg.format(value))
            self.treatment_response_factory.create_treatment_response(treatment_response_id=value)

        with self.assertRaisesRegex(TypeError, 'Treatment Response ID is missing'):
            value = ''
            print(test_msg.format(value))
            self.treatment_response_factory.create_treatment_response(treatment_response_id=value)

        with self.assertRaisesRegex(TypeError, "Treatment Response ID `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.treatment_response_factory.create_treatment_response(treatment_response_id=value)

if __name__ == '__main__':
    unittest.main()
