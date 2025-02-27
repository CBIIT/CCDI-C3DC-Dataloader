import unittest
import yaml
from transformer.nodes import ReferenceFile

ERROR_MAP = {
    'type': TypeError,
    'value': ValueError
}

class TestReferenceFileFactory():
    def create_reference_file(
            self,
            id = 'abc-123',
            dcf_indexd_guid = '7c2abf1c-3d3e-45fb-94e4-99e705242bbf',
            file_category = 'programmatic source code',
            file_description = 'foo',
            file_name = 'c3dc_etl.py',
            file_size = 37950,
            file_type = 'py',
            md5sum = '315e7ab85a82186b8aca5d1eafcc737a',
            reference_file_id = '9d35fb29-72f6-4d52-a13c-50fe10dbe2b1',
            reference_file_url = 'https://github.com/chicagopcdc/c3dc_etl/blob/main/etl/c3dc_etl.py'):
        reference_file = ReferenceFile(
            id,
            dcf_indexd_guid,
            file_category,
            file_description,
            file_name,
            file_size,
            file_type,
            md5sum,
            reference_file_id,
            reference_file_url
        )

        return reference_file

class TestReferenceFileProps(unittest.TestCase):
    def setUp(self):
        self.reference_file_factory = TestReferenceFileFactory()

        with open('tests/transformer_tests/test_cases/test_reference_file_props.yml', 'r', encoding='utf8') as file:
            self.test_cases = yaml.safe_load(file)

    # ReferenceFile.dcf_indexd_guid
    def test_reference_file_dcf_indexd_guid(self):
        test_msg = 'Testing ReferenceFile.dcf_indexd_guid being <{}>...'

        for test_case in self.test_cases['dcf_indexd_guid']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.reference_file_factory.create_reference_file(dcf_indexd_guid=value)

    # ReferenceFile.file_category
    def test_reference_file_file_category(self):
        test_msg = 'Testing ReferenceFile.file_category being <{}>...'

        for test_case in self.test_cases['file_category']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.reference_file_factory.create_reference_file(file_category=value)

    # ReferenceFile.file_description
    def test_reference_file_file_description(self):
        test_msg = 'Testing ReferenceFile.file_description being <{}>...'

        for test_case in self.test_cases['file_description']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.reference_file_factory.create_reference_file(file_description=value)

    # ReferenceFile.file_name
    def test_reference_file_file_name(self):
        test_msg = 'Testing ReferenceFile.file_name being <{}>...'

        for test_case in self.test_cases['file_name']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.reference_file_factory.create_reference_file(file_name=value)

    # ReferenceFile.file_size
    def test_reference_file_file_size(self):
        test_msg = 'Testing ReferenceFile.file_size being <{}>...'

        for test_case in self.test_cases['file_size']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.reference_file_factory.create_reference_file(file_size=value)

    # ReferenceFile.file_type
    def test_reference_file_file_type(self):
        test_msg = 'Testing ReferenceFile.file_type being <{}>...'

        for test_case in self.test_cases['file_type']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.reference_file_factory.create_reference_file(file_type=value)

    # ReferenceFile.md5sum
    def test_reference_file_md5sum(self):
        test_msg = 'Testing ReferenceFile.md5sum being <{}>...'

        for test_case in self.test_cases['md5sum']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.reference_file_factory.create_reference_file(md5sum=value)

    # ReferenceFile.reference_file_id
    def test_reference_file_reference_file_id(self):
        test_msg = 'Testing ReferenceFile.reference_file_id being <{}>...'

        for test_case in self.test_cases['reference_file_id']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.reference_file_factory.create_reference_file(reference_file_id=value)

    # ReferenceFile.reference_file_url
    def test_reference_file_reference_file_url(self):
        test_msg = 'Testing ReferenceFile.reference_file_url being <{}>...'

        for test_case in self.test_cases['reference_file_url']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.reference_file_factory.create_reference_file(reference_file_url=value)

if __name__ == '__main__':
    unittest.main()
