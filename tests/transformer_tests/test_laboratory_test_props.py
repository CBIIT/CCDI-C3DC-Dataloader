import unittest
import yaml
from transformer.nodes import LaboratoryTest

ERROR_MAP = {
    'type': TypeError,
    'value': ValueError
}

class TestLaboratoryTestFactory():
    def create_laboratory_test(
            self,
            id = 'abc-123',
            age_at_lab = 200,
            laboratory_test_id = 'abc-123',
            method = 'Cytology',
            result = 'Positive',
            result_modifier = 'Some modifier here',
            result_numeric = 3,
            result_text = 'Some text here',
            result_unit = '%',
            sensitivity = 3.1,
            specimen = 'Blood',
            test = '5 Prime Nucleotidase'):
        laboratory_test = LaboratoryTest(
            id,
            age_at_lab,
            laboratory_test_id,
            method,
            result,
            result_modifier,
            result_numeric,
            result_text,
            result_unit,
            sensitivity,
            specimen,
            test
        )

        return laboratory_test

class TestLaboratoryTestProps(unittest.TestCase):
    def setUp(self):
        self.laboratory_test_factory = TestLaboratoryTestFactory()

        with open('tests/transformer_tests/test_cases/test_laboratory_test_props.yml', 'r', encoding='utf8') as file:
            self.test_cases = yaml.safe_load(file)

    # LaboratoryTest.id
    def test_laboratory_test_id(self):
        test_msg = 'Testing LaboratoryTest.id being <{}>...'

        for test_case in self.test_cases['id']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.laboratory_test_factory.create_laboratory_test(id=value)

    # LaboratoryTest.age_at_lab
    def test_laboratory_test_age_at_lab(self):
        test_msg = 'Testing LaboratoryTest.age_at_lab being <{}>...'

        for test_case in self.test_cases['age_at_lab']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.laboratory_test_factory.create_laboratory_test(age_at_lab=value)

    # LaboratoryTest.laboratory_test_id
    def test_laboratory_test_laboratory_test_id(self):
        test_msg = 'Testing LaboratoryTest.laboratory_test_id being <{}>...'

        for test_case in self.test_cases['laboratory_test_id']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.laboratory_test_factory.create_laboratory_test(laboratory_test_id=value)

    # LaboratoryTest.method
    def test_laboratory_test_method(self):
        test_msg = 'Testing LaboratoryTest.method being <{}>...'

        for test_case in self.test_cases['method']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.laboratory_test_factory.create_laboratory_test(method=value)

    # LaboratoryTest.result
    def test_laboratory_test_result(self):
        test_msg = 'Testing LaboratoryTest.result being <{}>...'

        for test_case in self.test_cases['result']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.laboratory_test_factory.create_laboratory_test(result=value)

    # LaboratoryTest.result_modifier
    def test_laboratory_test_result_modifier(self):
        test_msg = 'Testing LaboratoryTest.result_modifier being <{}>...'

        for test_case in self.test_cases['result_modifier']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.laboratory_test_factory.create_laboratory_test(result_modifier=value)

    # LaboratoryTest.result_numeric
    def test_laboratory_test_result_numeric(self):
        test_msg = 'Testing LaboratoryTest.result_numeric being <{}>...'

        for test_case in self.test_cases['result_numeric']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.laboratory_test_factory.create_laboratory_test(result_numeric=value)

    # LaboratoryTest.result_text
    def test_laboratory_test_result_text(self):
        test_msg = 'Testing LaboratoryTest.result_text being <{}>...'

        for test_case in self.test_cases['result_text']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.laboratory_test_factory.create_laboratory_test(result_text=value)

    # LaboratoryTest.result_unit
    def test_laboratory_test_result_unit(self):
        test_msg = 'Testing LaboratoryTest.result_unit being <{}>...'

        for test_case in self.test_cases['result_unit']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.laboratory_test_factory.create_laboratory_test(result_unit=value)

    # LaboratoryTest.sensitivity
    def test_laboratory_test_sensitivity(self):
        test_msg = 'Testing LaboratoryTest.sensitivity being <{}>...'

        for test_case in self.test_cases['sensitivity']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.laboratory_test_factory.create_laboratory_test(sensitivity=value)

    # LaboratoryTest.specimen
    def test_laboratory_test_specimen(self):
        test_msg = 'Testing LaboratoryTest.specimen being <{}>...'

        for test_case in self.test_cases['specimen']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.laboratory_test_factory.create_laboratory_test(specimen=value)

    # LaboratoryTest.test
    def test_laboratory_test_test(self):
        test_msg = 'Testing LaboratoryTest.test being <{}>...'

        for test_case in self.test_cases['test']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.laboratory_test_factory.create_laboratory_test(test=value)

if __name__ == '__main__':
    unittest.main()
