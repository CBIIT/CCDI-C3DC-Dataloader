import unittest
from transformer.nodes import Participant

class TestParticipantFactory():
    def create_participant(
            self,
            alternate_participant_id = None,
            ethnicity = ['Not Hispanic or Latino'],
            gender = 'Male',
            participant_id = 'FOO-BAR-123',
            race = ['Asian']):
        participant = Participant(
            alternate_participant_id,
            ethnicity,
            gender,
            participant_id,
            race
        )

        return participant

class TestParticipantProps(unittest.TestCase):
    def setUp(self):
        self.participant_factory = TestParticipantFactory()

    # Participant.alternate_participant_id
    def test_participant_alternate_participant_id(self):
        test_msg = 'Testing Participant.alternate_participant_id being <{}>...'

        with self.assertRaisesRegex(TypeError, "Alternate Participant ID `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.participant_factory.create_participant(alternate_participant_id=value)

    # Participant.ethnicity
    def test_participant_ethnicity(self):
        test_msg = 'Testing Participant.ethnicity being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Ethnicity is missing'):
            value = None
            print(test_msg.format(value))
            self.participant_factory.create_participant(ethnicity=value)

        with self.assertRaisesRegex(TypeError, 'Ethnicity is missing'):
            value = ''
            print(test_msg.format(value))
            self.participant_factory.create_participant(ethnicity=value)

        with self.assertRaisesRegex(TypeError, "Ethnicity `3` must be of type <class 'list'>"):
            value = 3
            print(test_msg.format(value))
            self.participant_factory.create_participant(ethnicity=value)

        with self.assertRaisesRegex(ValueError, "Ethnicity `\['Foo'\]` must be a subset of the specified values"):
            value = ['Foo']
            print(test_msg.format(value))
            self.participant_factory.create_participant(ethnicity=value)

    # Participant.gender
    def test_participant_gender(self):
        test_msg = 'Testing Participant.gender being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Gender is missing'):
            value = None
            print(test_msg.format(value))
            self.participant_factory.create_participant(gender=value)

        with self.assertRaisesRegex(TypeError, 'Gender is missing'):
            value = ''
            print(test_msg.format(value))
            self.participant_factory.create_participant(gender=value)

        with self.assertRaisesRegex(TypeError, "Gender `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.participant_factory.create_participant(gender=value)

        with self.assertRaisesRegex(ValueError, 'Gender `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            self.participant_factory.create_participant(gender=value)

    # Participant.participant_id
    def test_participant_id(self):
        test_msg = 'Testing Participant.participant_id being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Participant ID is missing'):
            value = None
            print(test_msg.format(value))
            self.participant_factory.create_participant(participant_id=value)

        with self.assertRaisesRegex(TypeError, 'Participant ID is missing'):
            value = ''
            print(test_msg.format(value))
            self.participant_factory.create_participant(participant_id=value)

        with self.assertRaisesRegex(TypeError, "Participant ID `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.participant_factory.create_participant(participant_id=value)

    # Participant.race
    def test_participant_race(self):
        test_msg = 'Testing Participant.race being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Race is missing'):
            value = None
            print(test_msg.format(value))
            self.participant_factory.create_participant(race=value)

        with self.assertRaisesRegex(TypeError, 'Race is missing'):
            value = ''
            print(test_msg.format(value))
            self.participant_factory.create_participant(race=value)

        with self.assertRaisesRegex(TypeError, "Race `3` must be of type <class 'list'>"):
            value = 3
            print(test_msg.format(value))
            self.participant_factory.create_participant(race=value)

        with self.assertRaisesRegex(TypeError, "Race `Foo` must be of type <class 'list'>"):
            value = 'Foo'
            print(test_msg.format(value))
            self.participant_factory.create_participant(race=value)

        with self.assertRaisesRegex(ValueError, "Race `\['Foo'\]` must be a subset of the specified values"):
            value = ['Foo']
            print(test_msg.format(value))
            self.participant_factory.create_participant(race=value)

if __name__ == '__main__':
    unittest.main()
