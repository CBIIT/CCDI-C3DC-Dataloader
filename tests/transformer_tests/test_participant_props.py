import unittest
from transformer.nodes import Participant

class TestParticipantFactory():
    def create_participant(
            self,
            id = 'abc-123',
            participant_id = 'FOO-BAR-123',
            race = ['Asian'],
            sex_at_birth = 'Male'):
        participant = Participant(
            id,
            participant_id,
            race,
            sex_at_birth
        )

        return participant

class TestParticipantProps(unittest.TestCase):
    def setUp(self):
        self.participant_factory = TestParticipantFactory()

    # Participant.id
    def test_participant_id(self):
        test_msg = 'Testing Participant.id being <{}>...'

        with self.assertRaisesRegex(TypeError, "ID `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.participant_factory.create_participant(id=value)

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

        with self.assertRaisesRegex(TypeError, "Race `` must be of type <class 'list'>"):
            value = ''
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

    # Participant.sex_at_birth
    def test_participant_sex_at_birth(self):
        test_msg = 'Testing Participant.sex_at_birth being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Sex at Birth is missing'):
            value = None
            print(test_msg.format(value))
            self.participant_factory.create_participant(sex_at_birth=value)

        with self.assertRaisesRegex(TypeError, 'Sex at Birth is missing'):
            value = ''
            print(test_msg.format(value))
            self.participant_factory.create_participant(sex_at_birth=value)

        with self.assertRaisesRegex(TypeError, "Sex at Birth `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.participant_factory.create_participant(sex_at_birth=value)

        with self.assertRaisesRegex(ValueError, 'Sex at Birth `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            self.participant_factory.create_participant(sex_at_birth=value)

if __name__ == '__main__':
    unittest.main()
