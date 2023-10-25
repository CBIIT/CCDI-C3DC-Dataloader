import unittest
from transformer.nodes import Participant

class TestParticipantProps(unittest.TestCase):
    def setUp(self):
        pass

    # Participant.alternate_participant_id
    def test_participant_alternate_participant_id(self):
        test_msg = 'Testing Participant.alternate_participant_id being <{}>...'

        with self.assertRaisesRegex(TypeError, "Alternate Participant ID `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            Participant(
                alternate_participant_id = value,
                ethnicity = 'Not Hispanic or Latino',
                gender = 'Male',
                participant_id = 'FOO-BAR-123',
                race = 'Asian'
            )

    # Participant.ethnicity
    def test_participant_ethnicity(self):
        test_msg = 'Testing Participant.ethnicity being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Ethnicity is missing'):
            value = None
            print(test_msg.format(value))
            Participant(
                alternate_participant_id = None,
                ethnicity = value,
                gender = 'Male',
                participant_id = 'FOO-BAR-123',
                race = 'Asian'
            )
        with self.assertRaisesRegex(TypeError, 'Ethnicity is missing'):
            value = ''
            print(test_msg.format(value))
            Participant(
                alternate_participant_id = None,
                ethnicity = '',
                gender = 'Male',
                participant_id = 'FOO-BAR-123',
                race = 'Asian'
            )
        with self.assertRaisesRegex(ValueError, 'Ethnicity `3` must be one of the specified values'):
            value = 3
            print(test_msg.format(value))
            Participant(
                alternate_participant_id = None,
                ethnicity = value,
                gender = 'Male',
                participant_id = 'FOO-BAR-123',
                race = 'Asian'
            )
        with self.assertRaisesRegex(ValueError, 'Ethnicity `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            Participant(
                alternate_participant_id = None,
                ethnicity = value,
                gender = 'Male',
                participant_id = 'FOO-BAR-123',
                race = 'Asian'
            )

    # Participant.gender
    def test_participant_gender(self):
        test_msg = 'Testing Participant.gender being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Gender is missing'):
            value = None
            print(test_msg.format(value))
            Participant(
                alternate_participant_id = None,
                ethnicity = 'Not Hispanic or Latino',
                gender = value,
                participant_id = 'FOO-BAR-123',
                race = 'Asian'
            )
        with self.assertRaisesRegex(TypeError, 'Gender is missing'):
            value = ''
            print(test_msg.format(value))
            Participant(
                alternate_participant_id = None,
                ethnicity = 'Not Hispanic or Latino',
                gender = value,
                participant_id = 'FOO-BAR-123',
                race = 'Asian'
            )
        with self.assertRaisesRegex(ValueError, 'Gender `3` must be one of the specified values'):
            value = 3
            print(test_msg.format(value))
            Participant(
                alternate_participant_id = None,
                ethnicity = 'Not Hispanic or Latino',
                gender = value,
                participant_id = 'FOO-BAR-123',
                race = 'Asian'
            )
        with self.assertRaisesRegex(ValueError, 'Gender `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            Participant(
                alternate_participant_id = None,
                ethnicity = 'Not Hispanic or Latino',
                gender = value,
                participant_id = 'FOO-BAR-123',
                race = 'Asian'
            )

    # Participant.participant_id
    def test_participant_id(self):
        test_msg = 'Testing Participant.participant_id being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Participant ID is missing'):
            value = None
            print(test_msg.format(value))
            Participant(
                alternate_participant_id = None,
                ethnicity = 'Not Hispanic or Latino',
                gender = 'Male',
                participant_id = None,
                race = 'Asian'
            )
        with self.assertRaisesRegex(TypeError, 'Participant ID is missing'):
            value = ''
            print(test_msg.format(value))
            Participant(
                alternate_participant_id = None,
                ethnicity = 'Not Hispanic or Latino',
                gender = 'Male',
                participant_id = None,
                race = 'Asian'
            )
        with self.assertRaisesRegex(TypeError, "Participant ID `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            Participant(
                alternate_participant_id = None,
                ethnicity = 'Not Hispanic or Latino',
                gender = 'Male',
                participant_id = 3,
                race = 'Asian'
            )

    # Participant.race
    def test_participant_race(self):
        test_msg = 'Testing Participant.race being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Race is missing'):
            value = None
            print(test_msg.format(value))
            Participant(
                alternate_participant_id = None,
                ethnicity = 'Not Hispanic or Latino',
                gender = 'Male',
                participant_id = 'FOO-BAR-123',
                race = value
            )
        with self.assertRaisesRegex(TypeError, 'Race is missing'):
            value = ''
            print(test_msg.format(value))
            Participant(
                alternate_participant_id = None,
                ethnicity = 'Not Hispanic or Latino',
                gender = 'Male',
                participant_id = 'FOO-BAR-123',
                race = value
            )
        with self.assertRaisesRegex(ValueError, 'Race `3` must be one of the specified values'):
            value = 3
            print(test_msg.format(value))
            Participant(
                alternate_participant_id = None,
                ethnicity = 'Not Hispanic or Latino',
                gender = 'Male',
                participant_id = 'FOO-BAR-123',
                race = value
            )
        with self.assertRaisesRegex(ValueError, 'Race `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            Participant(
                alternate_participant_id = None,
                ethnicity = 'Not Hispanic or Latino',
                gender = 'Male',
                participant_id = 'FOO-BAR-123',
                race = value
            )

if __name__ == '__main__':
    unittest.main()
