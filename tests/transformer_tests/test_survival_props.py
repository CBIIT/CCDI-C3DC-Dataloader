import unittest
from transformer.nodes import Survival

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

    # Survival.id
    def test_survival_id(self):
        test_msg = 'Testing Survival.id being <{}>...'

        with self.assertRaisesRegex(TypeError, "ID `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.survival_factory.create_survival(id=value)

    # Survival.age_at_event_free_survival_status
    def test_survival_age_at_event_free_survival_status(self):
        test_msg = 'Testing Survival.age_at_event_free_survival_status being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Age at Event Free Survival Status is missing'):
            value = None
            print(test_msg.format(value))
            self.survival_factory.create_survival(age_at_event_free_survival_status=value)

        with self.assertRaisesRegex(TypeError, "Age at Event Free Survival Status `` must be of type <class 'int'>"):
            value = ''
            print(test_msg.format(value))
            self.survival_factory.create_survival(age_at_event_free_survival_status=value)

        with self.assertRaisesRegex(TypeError, "Age at Event Free Survival Status `Foo` must be of type <class 'int'>"):
            value = 'Foo'
            print(test_msg.format(value))
            self.survival_factory.create_survival(age_at_event_free_survival_status=value)

    # Survival.age_at_last_known_survival_status
    def test_survival_age_at_last_known_survival_status(self):
        test_msg = 'Testing Survival.age_at_last_known_survival_status being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Age at Last Known Survival Status is missing'):
            value = None
            print(test_msg.format(value))
            self.survival_factory.create_survival(age_at_last_known_survival_status=value)

        with self.assertRaisesRegex(TypeError, "Age at Last Known Survival Status `` must be of type <class 'int'>"):
            value = ''
            print(test_msg.format(value))
            self.survival_factory.create_survival(age_at_last_known_survival_status=value)

        with self.assertRaisesRegex(TypeError, "Age at Last Known Survival Status `Foo` must be of type <class 'int'>"):
            value = 'Foo'
            print(test_msg.format(value))
            self.survival_factory.create_survival(age_at_last_known_survival_status=value)

    # Survival.cause_of_death
    def test_survival_cause_of_death(self):
        test_msg = 'Testing Survival.cause_of_death being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Cause of Death is missing'):
            value = None
            print(test_msg.format(value))
            self.survival_factory.create_survival(cause_of_death=value)

        with self.assertRaisesRegex(TypeError, 'Cause of Death is missing'):
            value = ''
            print(test_msg.format(value))
            self.survival_factory.create_survival(cause_of_death=value)

        with self.assertRaisesRegex(TypeError, "Cause of Death `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.survival_factory.create_survival(cause_of_death=value)

        with self.assertRaisesRegex(ValueError, 'Cause of Death `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            self.survival_factory.create_survival(cause_of_death=value)

    # Survival.event_free_survival_status
    def test_survival_event_free_survival_status(self):
        test_msg = 'Testing Survival.event_free_survival_status being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Event Free Survival Status is missing'):
            value = None
            print(test_msg.format(value))
            self.survival_factory.create_survival(event_free_survival_status=value)

        with self.assertRaisesRegex(TypeError, 'Event Free Survival Status is missing'):
            value = ''
            print(test_msg.format(value))
            self.survival_factory.create_survival(event_free_survival_status=value)

        with self.assertRaisesRegex(TypeError, "Event Free Survival Status `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.survival_factory.create_survival(event_free_survival_status=value)

        with self.assertRaisesRegex(ValueError, 'Event Free Survival Status `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            self.survival_factory.create_survival(event_free_survival_status=value)

    # Survival.first_event
    def test_survival_first_event(self):
        test_msg = 'Testing Survival.first_event being <{}>...'

        with self.assertRaisesRegex(TypeError, 'First Event is missing'):
            value = None
            print(test_msg.format(value))
            self.survival_factory.create_survival(first_event=value)

        with self.assertRaisesRegex(TypeError, 'First Event is missing'):
            value = ''
            print(test_msg.format(value))
            self.survival_factory.create_survival(first_event=value)

        with self.assertRaisesRegex(TypeError, "First Event `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.survival_factory.create_survival(first_event=value)

        with self.assertRaisesRegex(ValueError, 'First Event `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            self.survival_factory.create_survival(first_event=value)

    # Survival.last_known_survival_status
    def test_survival_last_known_survival_status(self):
        test_msg = 'Testing Survival.last_known_survival_status being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Last Known Survival Status is missing'):
            value = None
            print(test_msg.format(value))
            self.survival_factory.create_survival(last_known_survival_status=value)

        with self.assertRaisesRegex(TypeError, 'Last Known Survival Status is missing'):
            value = ''
            print(test_msg.format(value))
            self.survival_factory.create_survival(last_known_survival_status=value)

        with self.assertRaisesRegex(TypeError, "Last Known Survival Status `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.survival_factory.create_survival(last_known_survival_status=value)

        with self.assertRaisesRegex(ValueError, 'Last Known Survival Status `Foo` must be one of the specified values'):
            value = 'Foo'
            print(test_msg.format(value))
            self.survival_factory.create_survival(last_known_survival_status=value)

    # Survival.survival_id
    def test_survival_survival_id(self):
        test_msg = 'Testing Survival.survival_id being <{}>...'

        with self.assertRaisesRegex(TypeError, 'Survival ID is missing'):
            value = None
            print(test_msg.format(value))
            self.survival_factory.create_survival(survival_id=value)

        with self.assertRaisesRegex(TypeError, 'Survival ID is missing'):
            value = ''
            print(test_msg.format(value))
            self.survival_factory.create_survival(survival_id=value)

        with self.assertRaisesRegex(TypeError, "Survival ID `3` must be of type <class 'str'>"):
            value = 3
            print(test_msg.format(value))
            self.survival_factory.create_survival(survival_id=value)

if __name__ == '__main__':
    unittest.main()
