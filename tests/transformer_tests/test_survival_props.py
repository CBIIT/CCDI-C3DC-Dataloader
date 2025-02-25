import unittest
import yaml
from transformer.nodes import Survival

ERROR_MAP = {
    'type': TypeError,
    'value': ValueError
}

class TestSurvivalFactory():
    def create_survival(
            self,
            id = 'abc-123',
            age_at_event_free_survival_status = 3429,
            age_at_last_known_survival_status = 3429,
            cause_of_death = 'Due to other cause',
            event_free_survival_status = 'Censored',
            first_event = "Not Applicable",
            last_known_survival_status = 'Alive',
            survival_id = 'fcf081e4-3485-46f5-8988-a6feb67d06a7'):
        survival = Survival(
            id,
            age_at_event_free_survival_status,
            age_at_last_known_survival_status,
            cause_of_death,
            event_free_survival_status,
            first_event,
            last_known_survival_status,
            survival_id
        )

        return survival

class TestSurvivalProps(unittest.TestCase):
    def setUp(self):
        self.survival_factory = TestSurvivalFactory()

        with open('tests/transformer_tests/test_cases/test_survival_props.yml', 'r', encoding='utf8') as file:
            self.test_cases = yaml.safe_load(file)

    # Survival.id
    def test_survival_id(self):
        test_msg = 'Testing Survival.id being <{}>...'

        for test_case in self.test_cases['id']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.survival_factory.create_survival(id=value)

    # Survival.age_at_event_free_survival_status
    def test_survival_age_at_event_free_survival_status(self):
        test_msg = 'Testing Survival.age_at_event_free_survival_status being <{}>...'

        for test_case in self.test_cases['age_at_event_free_survival_status']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.survival_factory.create_survival(age_at_event_free_survival_status=value)

    # Survival.age_at_last_known_survival_status
    def test_survival_age_at_last_known_survival_status(self):
        test_msg = 'Testing Survival.age_at_last_known_survival_status being <{}>...'

        for test_case in self.test_cases['age_at_last_known_survival_status']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.survival_factory.create_survival(age_at_last_known_survival_status=value)

    # Survival.cause_of_death
    def test_survival_cause_of_death(self):
        test_msg = 'Testing Survival.cause_of_death being <{}>...'

        for test_case in self.test_cases['cause_of_death']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.survival_factory.create_survival(cause_of_death=value)

    # Survival.event_free_survival_status
    def test_survival_event_free_survival_status(self):
        test_msg = 'Testing Survival.event_free_survival_status being <{}>...'

        for test_case in self.test_cases['event_free_survival_status']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.survival_factory.create_survival(event_free_survival_status=value)

    # Survival.first_event
    def test_survival_first_event(self):
        test_msg = 'Testing Survival.first_event being <{}>...'

        for test_case in self.test_cases['first_event']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.survival_factory.create_survival(first_event=value)

    # Survival.last_known_survival_status
    def test_survival_last_known_survival_status(self):
        test_msg = 'Testing Survival.last_known_survival_status being <{}>...'

        for test_case in self.test_cases['last_known_survival_status']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.survival_factory.create_survival(last_known_survival_status=value)

    # Survival.survival_id
    def test_survival_survival_id(self):
        test_msg = 'Testing Survival.survival_id being <{}>...'

        for test_case in self.test_cases['survival_id']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.survival_factory.create_survival(survival_id=value)

if __name__ == '__main__':
    unittest.main()
