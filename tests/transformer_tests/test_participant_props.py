import unittest
import yaml
from transformer.nodes import Participant

ERROR_MAP = {
    'type': TypeError,
    'value': ValueError
}

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

        with open('tests/transformer_tests/test_cases/test_participant_props.yml', 'r', encoding='utf8') as file:
            self.test_cases = yaml.safe_load(file)

    # Participant.id
    def test_participant_id(self):
        test_msg = 'Testing Participant.id being <{}>...'

        for test_case in self.test_cases['id']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.participant_factory.create_participant(id=value)

    # Participant.participant_id
    def test_participant_participant_id(self):
        test_msg = 'Testing Participant.participant_id being <{}>...'

        for test_case in self.test_cases['participant_id']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.participant_factory.create_participant(participant_id=value)

    # Participant.race
    def test_participant_race(self):
        test_msg = 'Testing Participant.race being <{}>...'

        for test_case in self.test_cases['race']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.participant_factory.create_participant(race=value)

    # Participant.sex_at_birth
    def test_participant_sex_at_birth(self):
        test_msg = 'Testing Participant.sex_at_birth being <{}>...'

        for test_case in self.test_cases['sex_at_birth']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.participant_factory.create_participant(sex_at_birth=value)

if __name__ == '__main__':
    unittest.main()
