import unittest
from transformer.nodes import ReferenceFile

class TestReferenceFileFactory():
    def create_reference_file(
            self,
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

    # ReferenceFile.dcf_indexd_guid
    def test_reference_file_dcf_indexd_guid(self):
        test_msg = 'Testing ReferenceFile.dcf_indexd_guid being <{}>...'

        with self.assertRaisesRegex(TypeError, 'DCF Index GUID is missing'):
            value = None
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(dcf_indexd_guid=value)

        with self.assertRaisesRegex(TypeError, 'DCF Index GUID is missing'):
            value = ''
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(dcf_indexd_guid=value)

        with self.assertRaisesRegex(TypeError, "DCF Index GUID `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(dcf_indexd_guid=value)

    # ReferenceFile.file_category
    def test_reference_file_file_category(self):
        test_msg = 'Testing ReferenceFile.file_category being <{}>...'

        with self.assertRaisesRegex(TypeError, 'File Category is missing'):
            value = None
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(file_category=value)

        with self.assertRaisesRegex(TypeError, 'File Category is missing'):
            value = ''
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(file_category=value)

        with self.assertRaisesRegex(TypeError, "File Category `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(file_category=value)

        with self.assertRaisesRegex(ValueError, 'File Category `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(file_category=value)

    # ReferenceFile.file_description
    def test_reference_file_file_description(self):
        test_msg = 'Testing ReferenceFile.file_description being <{}>...'

        with self.assertRaisesRegex(TypeError, 'File Description is missing'):
            value = None
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(file_description=value)

        with self.assertRaisesRegex(TypeError, 'File Description is missing'):
            value = ''
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(file_desription=value)

        with self.assertRaisesRegex(TypeError, "File Description `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(file_description=value)

    # ReferenceFile.file_name
    def test_reference_file_file_name(self):
        test_msg = 'Testing ReferenceFile.file_name being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Filename is missing'):
            value = None
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(file_name=value)

        with self.assertRaisesRegex(TypeError, 'Filename is missing'):
            value = ''
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(file_name=value)

        with self.assertRaisesRegex(TypeError, "Filename `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(file_name=value)

    # ReferenceFile.file_size
    def test_reference_file_file_size(self):
        test_msg = 'Testing ReferenceFile.file_size being <{}>...'

        with self.assertRaisesRegex(TypeError, 'File Size is missing'):
            value = None
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(file_size=value)

        with self.assertRaisesRegex(TypeError, "File Size `` must be of type <class 'int'>"):
            value = ''
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(file_size=value)

        with self.assertRaisesRegex(TypeError, "File Size `Foo` must be of type <class 'int'>"):
            value = 'Foo'
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(file_size=value)

    # ReferenceFile.file_type
    def test_reference_file_file_type(self):
        test_msg = 'Testing ReferenceFile.file_type being <{}>...'

        with self.assertRaisesRegex(TypeError, 'File Type is missing'):
            value = None
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(file_type=value)

        with self.assertRaisesRegex(TypeError, 'File Type is missing'):
            value = ''
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(file_type=value)

        with self.assertRaisesRegex(TypeError, "File Type `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(file_type=value)

        with self.assertRaisesRegex(ValueError, 'File Type `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(file_type=value)

    # ReferenceFile.md5sum
    def test_reference_file_md5sum(self):
        test_msg = 'Testing ReferenceFile.md5sum being <{}>...'

        with self.assertRaisesRegex(TypeError, 'MD5 Checksum is missing'):
            value = None
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(md5sum=value)

        with self.assertRaisesRegex(TypeError, 'MD5 Checksum is missing'):
            value = ''
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(md5sum=value)

        with self.assertRaisesRegex(TypeError, "MD5 Checksum `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(md5sum=value)

    # ReferenceFile.reference_file_id
    def test_reference_file_reference_file_id(self):
        test_msg = 'Testing ReferenceFile.reference_file_id being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Reference File ID is missing'):
            value = None
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(reference_file_id=value)

        with self.assertRaisesRegex(TypeError, 'Reference File ID is missing'):
            value = ''
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(reference_file_id=value)

        with self.assertRaisesRegex(TypeError, "Reference File ID `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(reference_file_id=value)

    # ReferenceFile.reference_file_url
    def test_reference_file_reference_file_url(self):
        test_msg = 'Testing ReferenceFile.reference_file_url being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Reference File URL is missing'):
            value = None
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(reference_file_url=value)

        with self.assertRaisesRegex(TypeError, 'Reference File URL is missing'):
            value = ''
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(reference_file_url=value)

        with self.assertRaisesRegex(TypeError, "Reference File URL `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.reference_file_factory.create_reference_file(reference_file_url=value)

if __name__ == '__main__':
    unittest.main()
