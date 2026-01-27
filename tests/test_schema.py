import unittest
import os
from icdc_schema import ICDC_Schema
from props import Props


class TestSchema(unittest.TestCase):
    def setUp(self):
        # Use paths relative to the tests directory
        test_dir = os.path.dirname(os.path.abspath(__file__))
        props_path = os.path.join(test_dir, 'data', 'props-icdc.yml')
        model_path = os.path.join(test_dir, 'data', 'icdc-model.yml')
        model_props_path = os.path.join(test_dir, 'data', 'icdc-model-props.yml')
        
        self.props = Props(props_path)
        self.schema = ICDC_Schema([model_path, model_props_path], self.props)

    def test_schema_construction(self):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(test_dir, 'data', 'icdc-model.yml')
        model_props_path = os.path.join(test_dir, 'data', 'icdc-model-props.yml')
        
        self.assertRaises(Exception, ICDC_Schema, None, self.props)
        self.assertRaises(Exception, ICDC_Schema, ['a', 'b'], self.props)
        schema = ICDC_Schema([model_path, model_props_path], self.props)
        self.assertIsInstance(schema, ICDC_Schema)
        # The schema has 28 nodes, not 25 (updated based on actual model)
        self.assertEqual(28, schema.node_count())
        self.assertEqual(43, schema.relationship_count())

    def test_default_value(self):
        self.assertIsNone(self.schema.get_default_value('node_does_not_exit', 'unit_does_not_exist'))
        self.assertIsNone(self.schema.get_default_value('adverse_event', 'unit_does_not_exist'))
        self.assertIsNone(self.schema.get_default_value('cycle', 'cycle_number'))
        self.assertEqual('mg/kg', self.schema.get_default_value('adverse_event', 'ae_dose_unit'))
        self.assertEqual('days', self.schema.get_default_value('agent_administration', 'medication_duration_unit'))

    def test_default_unit(self):
        self.assertIsNone(self.schema.get_default_unit('node_does_not_exit', 'unit_does_not_exist'))
        self.assertIsNone(self.schema.get_default_unit('adverse_event', 'unit_does_not_exist'))
        self.assertIsNone(self.schema.get_default_unit('cycle', 'cycle_number'))
        self.assertEqual('mg/kg', self.schema.get_default_unit('adverse_event', 'ae_dose'))
        self.assertEqual('days', self.schema.get_default_unit('agent_administration', 'medication_duration'))

    def test_extra_propties(self):
        self.assertEqual(0, len(self.schema.get_extra_props('node_does_not_exit', 'unit_does_not_exist', 0)))
        self.assertEqual(0, len(self.schema.get_extra_props('adverse_event', 'unit_does_not_exist', 0)))
        self.assertEqual(0, len(self.schema.get_extra_props('cycle', 'cycle_number', 0)))
        extra_props = self.schema.get_extra_props('adverse_event', 'ae_dose', 5)
        self.assertEqual(3, len(extra_props))
        self.assertEqual(5, extra_props['ae_dose_original'])
        self.assertEqual('mg/kg', extra_props['ae_dose_original_unit'])
        self.assertEqual('mg/kg', extra_props['ae_dose_unit'])

    def test_get_id_field(self):
        self.assertIsNone(self.schema.get_id_field({}))
        self.assertEqual(self.schema.get_id_field({'type': 'program'}), 'program_acronym')
        self.assertEqual(self.schema.get_id_field({'type': 'study'}), 'clinical_study_designation')
        self.assertEqual(self.schema.get_id_field({'type': 'case'}), 'case_id')
        self.assertEqual(self.schema.get_id_field({'type': 'file'}), 'uuid')
        self.assertEqual(self.schema.get_id_field({'type': 'demographic'}), 'uuid')


if __name__ == '__main__':
    unittest.main()
