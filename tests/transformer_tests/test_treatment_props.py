import unittest
from transformer.nodes import Treatment

class TestTreatmentFactory():
    def create_treatment(
            self,
            id = 'abc-123',
            age_at_treatment_end = 419,
            age_at_treatment_start = 68,
            treatment_agent = 'Treatment Agent Value',
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

    # Treatment.id
    def test_treatment_id(self):
        test_msg = 'Testing Treatment.id being <{}>...'

        with self.assertRaisesRegex(TypeError, "ID `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.treatment_factory.create_treatment(id=value)

    # Treatment.age_at_treatment_end
    def test_treatment_age_at_treatment_end(self):
        test_msg = 'Testing Treatment.age_at_treatment_end being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Age at Treatment End is missing'):
            value = None
            print(test_msg.format(value))
            self.treatment_factory.create_treatment(age_at_treatment_end=value)

        with self.assertRaisesRegex(TypeError, "Age at Treatment End `` must be of type <class 'int'>"):
            value = ''
            print(test_msg.format(value))
            self.treatment_factory.create_treatment(age_at_treatment_end=value)

        with self.assertRaisesRegex(TypeError, "Age at Treatment End `foo` must be of type <class 'int'>"):
            value = 'foo'
            print(test_msg.format(value))
            self.treatment_factory.create_treatment(age_at_treatment_end=value)

    # Treatment.age_at_treatment_start
    def test_treatment_age_at_treatment_start(self):
        test_msg = 'Testing Treatment.age_at_treatment_start being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Age at Treatment Start is missing'):
            value = None
            print(test_msg.format(value))
            self.treatment_factory.create_treatment(age_at_treatment_start=value)

        with self.assertRaisesRegex(TypeError, "Age at Treatment Start `` must be of type <class 'int'>"):
            value = ''
            print(test_msg.format(value))
            self.treatment_factory.create_treatment(age_at_treatment_start=value)

        with self.assertRaisesRegex(TypeError, "Age at Treatment Start `foo` must be of type <class 'int'>"):
            value = 'foo'
            print(test_msg.format(value))
            self.treatment_factory.create_treatment(age_at_treatment_start=value)

    # Treatment.treatment_agent
    def test_treatment_treatment_agent(self):
        test_msg = 'Testing Treatment.treatment_agent being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Treatment Agent is missing'):
            value = None
            print(test_msg.format(value))
            self.treatment_factory.create_treatment(treatment_agent=value)

        with self.assertRaisesRegex(TypeError, 'Treatment Agent is missing'):
            value = ''
            print(test_msg.format(value))
            self.treatment_factory.create_treatment(treatment_agent=value)

        with self.assertRaisesRegex(TypeError, "Treatment Agent `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.treatment_factory.create_treatment(treatment_agent=value)

    # Treatment.treatment_id
    def test_treatment_treatment_id(self):
        test_msg = 'Testing Treatment.treatment_id being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Treatment ID is missing'):
            value = None
            print(test_msg.format(value))
            self.treatment_factory.create_treatment(treatment_id=value)

        with self.assertRaisesRegex(TypeError, 'Treatment ID is missing'):
            value = ''
            print(test_msg.format(value))
            self.treatment_factory.create_treatment(treatment_id=value)

        with self.assertRaisesRegex(TypeError, "Treatment ID `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.treatment_factory.create_treatment(treatment_id=value)

    # Treatment.treatment_type
    def test_treatment_treatment_type(self):
        test_msg = 'Testing Treatment.treatment_type being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Treatment Type is missing'):
            value = None
            print(test_msg.format(value))
            self.treatment_factory.create_treatment(treatment_type=value)

        with self.assertRaisesRegex(TypeError, 'Treatment Type is missing'):
            value = ''
            print(test_msg.format(value))
            self.treatment_factory.create_treatment(treatment_type=value)

        with self.assertRaisesRegex(TypeError, "Treatment Type `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.treatment_factory.create_treatment(treatment_type=value)

        with self.assertRaisesRegex(ValueError, 'Treatment Type `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            self.treatment_factory.create_treatment(treatment_type=value)

if __name__ == '__main__':
    unittest.main()
