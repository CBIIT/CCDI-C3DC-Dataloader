import unittest
from transformer.nodes import Study

class TestStudyFactory():
    def create_study(
            self,
            id = 'abc-123',
            acl = 'phs000467.v22.p8',
            consent = 'DS-PEDCR',
            consent_number = 1,
            external_url = 'foo',
            phs_accession = "['phs000467']",
            study_acronym = 'TARGET_NBL',
            study_description = 'foo',
            study_id = 'phs000467.v22.p8',
            study_short_title = 'TARGET NBL'):
        study = Study(
            id,
            acl,
            consent,
            consent_number,
            external_url,
            phs_accession,
            study_acronym,
            study_description,
            study_id,
            study_short_title
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

    # Study.acl
    def test_study_acl(self):
        test_msg = 'Testing Study.acl being <{}>...'

        with self.assertRaisesRegex(TypeError, 'ACL is missing'):
            value = None
            print(test_msg.format(value))
            self.study_factory.create_study(acl=value)

        with self.assertRaisesRegex(TypeError, 'ACL is missing'):
            value = ''
            print(test_msg.format(value))
            self.study_factory.create_study(acl=value)

        with self.assertRaisesRegex(TypeError, "ACL `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.study_factory.create_study(acl=value)

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

    # Study.phs_accession
    def test_study_phs_accession(self):
        test_msg = 'Testing Study.phs_accession being <{}>...'

        with self.assertRaisesRegex(TypeError, 'PHS Accession is missing'):
            value = None
            print(test_msg.format(value))
            self.study_factory.create_study(phs_accession=value)

        with self.assertRaisesRegex(TypeError, 'PHS Accession is missing'):
            value = ''
            print(test_msg.format(value))
            self.study_factory.create_study(phs_accession=value)

        with self.assertRaisesRegex(TypeError, "PHS Accession `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.study_factory.create_study(phs_accession=value)

    # Study.study_acronym
    def test_study_study_acronym(self):
        test_msg = 'Testing Study.study_acronym being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Study Acronym is missing'):
            value = None
            print(test_msg.format(value))
            self.study_factory.create_study(study_acronym=value)

        with self.assertRaisesRegex(TypeError, 'Study Acronym is missing'):
            value = ''
            print(test_msg.format(value))
            self.study_factory.create_study(study_acronym=value)

        with self.assertRaisesRegex(TypeError, "Study Acronym `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.study_factory.create_study(study_acronym=value)

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

    # Study.study_short_title
    def test_study_study_short_title(self):
        test_msg = 'Testing Study.study_short_title being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Study Short Title is missing'):
            value = None
            print(test_msg.format(value))
            self.study_factory.create_study(study_short_title=value)

        with self.assertRaisesRegex(TypeError, 'Study Short Title is missing'):
            value = ''
            print(test_msg.format(value))
            self.study_factory.create_study(study_short_title=value)

        with self.assertRaisesRegex(TypeError, "Study Short Title `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.study_factory.create_study(study_short_title=value)

if __name__ == '__main__':
    unittest.main()
