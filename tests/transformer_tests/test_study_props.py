import unittest
from transformer.nodes import Study

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

    # Study.id
    def test_study_id(self):
        test_msg = 'Testing Study.id being <{}>...'

        with self.assertRaisesRegex(TypeError, "ID `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.study_factory.create_study(id=value)

    # Study.consent
    def test_study_consent(self):
        test_msg = 'Testing Study.consent being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Consent is missing'):
            value = None
            print(test_msg.format(value))
            self.study_factory.create_study(consent=value)

        with self.assertRaisesRegex(TypeError, 'Consent is missing'):
            value = ''
            print(test_msg.format(value))
            self.study_factory.create_study(consent=value)

        with self.assertRaisesRegex(TypeError, "Consent `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.study_factory.create_study(consent=value)

    # Study.consent_number
    def test_study_consent_number(self):
        test_msg = 'Testing Study.consent_number being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Consent Number is missing'):
            value = None
            print(test_msg.format(value))
            self.study_factory.create_study(consent_number=value)

        with self.assertRaisesRegex(TypeError, "Consent Number `` must be of type <class 'int'>"):
            value = ''
            print(test_msg.format(value))
            self.study_factory.create_study(consent_number=value)

        with self.assertRaisesRegex(TypeError, "Consent Number `foo` must be of type <class 'int'>"):
            value = 'foo'
            print(test_msg.format(value))
            self.study_factory.create_study(consent_number=value)

    # Study.external_url
    def test_study_external_url(self):
        test_msg = 'Testing Study.external_url being <{}>...'

        with self.assertRaisesRegex(TypeError, 'External URL is missing'):
            value = None
            print(test_msg.format(value))
            self.study_factory.create_study(external_url=value)

        with self.assertRaisesRegex(TypeError, 'External URL is missing'):
            value = ''
            print(test_msg.format(value))
            self.study_factory.create_study(external_url=value)

        with self.assertRaisesRegex(TypeError, "External URL `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.study_factory.create_study(external_url=value)

    # Study.dbgap_accession
    def test_study_dbgap_accession(self):
        test_msg = 'Testing Study.dbgap_accession being <{}>...'

        with self.assertRaisesRegex(TypeError, 'dbGaP Accession is missing'):
            value = None
            print(test_msg.format(value))
            self.study_factory.create_study(dbgap_accession=value)

        with self.assertRaisesRegex(TypeError, 'dbGaP Accession is missing'):
            value = ''
            print(test_msg.format(value))
            self.study_factory.create_study(dbgap_accession=value)

        with self.assertRaisesRegex(TypeError, "dbGaP Accession `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.study_factory.create_study(dbgap_accession=value)

    # Study.study_description
    def test_study_study_description(self):
        test_msg = 'Testing Study.study_description being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Study Description is missing'):
            value = None
            print(test_msg.format(value))
            self.study_factory.create_study(study_description=value)

        with self.assertRaisesRegex(TypeError, 'Study Description is missing'):
            value = ''
            print(test_msg.format(value))
            self.study_factory.create_study(study_description=value)

        with self.assertRaisesRegex(TypeError, "Study Description `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.study_factory.create_study(study_description=value)

    # Study.study_id
    def test_study_study_id(self):
        test_msg = 'Testing Study.study_id being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Study ID is missing'):
            value = None
            print(test_msg.format(value))
            self.study_factory.create_study(study_id=value)

        with self.assertRaisesRegex(TypeError, 'Study ID is missing'):
            value = ''
            print(test_msg.format(value))
            self.study_factory.create_study(study_id=value)

        with self.assertRaisesRegex(TypeError, "Study ID `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.study_factory.create_study(study_id=value)

    # Study.study_name
    def test_study_study_name(self):
        test_msg = 'Testing Study.study_name being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Study Name is missing'):
            value = None
            print(test_msg.format(value))
            self.study_factory.create_study(study_name=value)

        with self.assertRaisesRegex(TypeError, 'Study Name is missing'):
            value = ''
            print(test_msg.format(value))
            self.study_factory.create_study(study_name=value)

        with self.assertRaisesRegex(TypeError, "Study Name `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.study_factory.create_study(study_name=value)

if __name__ == '__main__':
    unittest.main()
