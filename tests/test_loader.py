import unittest
import os
from unittest.mock import Mock, MagicMock, patch
from bento.common.utils import get_logger, removeTrailingSlash, UUID
from data_loader import DataLoader
from icdc_schema import ICDC_Schema
from props import Props
from neo4j import Driver


class MockNeo4jDriver(Driver):
    """Mock Neo4j driver for testing without a database connection"""
    def __init__(self):
        # Don't call super().__init__ to avoid actual connection
        pass
    
    def session(self, **kwargs):
        session = Mock()
        session.__enter__ = Mock(return_value=session)
        session.__exit__ = Mock(return_value=False)
        return session
    
    def close(self):
        pass
    
    def verify_connectivity(self):
        return True


class TestLoader(unittest.TestCase):
    def setUp(self):
        # Use mock Neo4j driver instead of requiring environment variable
        self.driver = MockNeo4jDriver()
        
        # Use paths relative to the tests directory
        test_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_folder = os.path.join(test_dir, 'data', 'COTC007B')
        props_path = os.path.join(test_dir, 'data', 'props-icdc.yml')
        model_path = os.path.join(test_dir, 'data', 'icdc-model.yml')
        model_props_path = os.path.join(test_dir, 'data', 'icdc-model-props.yml')
        
        props = Props(props_path)
        self.schema = ICDC_Schema([model_path, model_props_path], props)
        self.log = get_logger('Test Loader')
        self.loader = DataLoader(self.driver, self.schema)
        self.file_list = [
            os.path.join(test_dir, "data/Dataset/COP-program.txt"),
            os.path.join(test_dir, "data/Dataset/NCATS-COP01-case.txt"),
            os.path.join(test_dir, "data/Dataset/NCATS-COP01-diagnosis.txt"),
            os.path.join(test_dir, "data/Dataset/NCATS-COP01_cohort_file.txt"),
            os.path.join(test_dir, "data/Dataset/NCATS-COP01_study_file.txt")
        ]

    def test_remove_traling_slash(self):
        self.assertEqual('abc', removeTrailingSlash('abc/'))
        self.assertEqual('abc', removeTrailingSlash('abc'))
        self.assertEqual('abc', removeTrailingSlash('abc//'))
        self.assertEqual('bolt://12.34.56.78', removeTrailingSlash('bolt://12.34.56.78'))
        self.assertEqual('bolt://12.34.56.78', removeTrailingSlash('bolt://12.34.56.78/'))
        self.assertEqual('bolt://12.34.56.78', removeTrailingSlash('bolt://12.34.56.78//'))
        self.assertEqual('bolt://12.34.56.78', removeTrailingSlash('bolt://12.34.56.78////'))

    def test_loader_construction(self):
        self.assertRaises(Exception, DataLoader, None, None, None)
        self.assertRaises(Exception, DataLoader, self.driver, None, None)
        self.assertIsInstance(self.loader, DataLoader)

    @unittest.skip("Skipping test that requires actual Neo4j database interaction")
    def test_validate_parents_exist_in_file(self):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        load_result = self.loader.load(self.file_list, True, False, 'upsert', False, 1, '/tmp', False)
        self.assertIsInstance(load_result, dict, msg='Load data failed!')
        result = self.loader.validate_parents_exist_in_file(os.path.join(test_dir, 'data/pathology-reports-failure.txt'), 100)
        self.assertFalse(result)
        result = self.loader.validate_parents_exist_in_file(os.path.join(test_dir, 'data/pathology-reports-success.txt'), 100)
        self.assertTrue(result)

    def test_duplicated_ids(self):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        self.assertTrue(self.loader.validate_file(os.path.join(test_dir, 'data/Dataset/NCATS-COP01-case.txt'), 10, False))
        self.assertFalse(self.loader.validate_file(os.path.join(test_dir, 'data/NCATS01-case-dup.txt'), 10, False))

    def test_get_signature(self):
        self.assertEqual(self.loader.get_signature({}), '{  }')
        self.assertEqual(self.loader.get_signature({'key1': 'value1'}), '{ key1: value1 }')
        self.assertEqual(self.loader.get_signature({'key1': 'value1', 'key2': 'value2'}), '{ key1: value1, key2: value2 }')

    def test_cleanup_node(self):
        #Test UUIDs
        self.assertRaises(SystemExit, self.loader.prepare_node, {}, 'test_file.txt')
        result = self.loader.prepare_node({'type': 'case', 'case_id': '123', ' key1 ': ' value1  '}, 'test_file.txt')
        self.assertEqual(result['key1'], 'value1')
        self.assertEqual(result['type'], 'case')
        self.assertEqual(result['case_id'], '123')
        self.assertEqual(len(result['uuid']), 36)  # Check UUID format, not exact value
        
        result = self.loader.prepare_node({'type': 'file', 'uuid': '123', ' key1 ': ' value1  '}, 'test_file.txt')
        self.assertDictEqual(result, {'key1': 'value1', 'type': 'file', 'uuid': '123'})

        # Test parent ids
        obj = self.loader.prepare_node({'type': 'case', 'cohort.cohort_id': 'abc132'}, 'test_file.txt')
        self.assertEqual(obj['cohort_id'], 'abc132')
        obj = self.loader.prepare_node({'type': 'case', 'cohort.cohort_id': 'abc132', 'cohort_id': 'def333'}, 'test_file.txt')
        self.assertEqual(obj['cohort_id'], 'def333')
        self.assertEqual(obj['cohort_cohort_id'], 'abc132')
        self.assertEqual(len(obj[UUID]), 36)

        # Test Boolean values
        obj = self.loader.prepare_node({'type': 'vital_signs', 'ecg': 'abc132'}, 'test_file.txt')
        self.assertIsNone(obj['ecg'])
        obj = self.loader.prepare_node({'type': 'vital_signs', 'ecg': 'yes'}, 'test_file.txt')
        self.assertEqual(obj['ecg'], True)
        obj = self.loader.prepare_node({'type': 'vital_signs', 'ecg': 'YeS'}, 'test_file.txt')
        self.assertEqual(obj['ecg'], True)
        obj = self.loader.prepare_node({'type': 'vital_signs', 'ecg': 'YeS13'}, 'test_file.txt')
        self.assertEqual(obj['ecg'], True)

        obj = self.loader.prepare_node({'type': 'vital_signs', 'ecg': 'no'}, 'test_file.txt')
        self.assertEqual(obj['ecg'], False)
        obj = self.loader.prepare_node({'type': 'vital_signs', 'ecg': 'No'}, 'test_file.txt')
        self.assertEqual(obj['ecg'], False)
        obj = self.loader.prepare_node({'type': 'vital_signs', 'ecg': ' No33 '}, 'test_file.txt')
        self.assertEqual(obj['ecg'], False)
        obj = self.loader.prepare_node({'type': 'vital_signs', 'ecg': ' Normal '}, 'test_file.txt')
        self.assertEqual(obj['ecg'], False)

        # Test Int values
        obj = self.loader.prepare_node({'type': 'physical_exam', 'day_in_cycle': ' Normal '}, 'test_file.txt')
        self.assertEqual(obj['day_in_cycle'], None)
        obj = self.loader.prepare_node({'type': 'physical_exam', 'day_in_cycle': ' 13 '}, 'test_file.txt')
        self.assertEqual(obj['day_in_cycle'], 13)
        self.assertNotEqual(obj['day_in_cycle'], '13')
        obj = self.loader.prepare_node({'type': 'physical_exam', 'day_in_cycle': ' 12 Normal '}, 'test_file.txt')
        self.assertEqual(obj['day_in_cycle'], None)

        #Test Float values
        obj = self.loader.prepare_node({'type': 'file', 'file_size': ' Normal '}, 'test_file.txt')
        self.assertEqual(obj['file_size'], None)
        obj = self.loader.prepare_node({'type': 'file', 'file_size': ' 1.5 Normal '}, 'test_file.txt')
        self.assertEqual(obj['file_size'], None)
        obj = self.loader.prepare_node({'type': 'file', 'file_size': ' 1.5 '}, 'test_file.txt')
        self.assertEqual(obj['file_size'], 1.5)
        obj = self.loader.prepare_node({'type': 'file', 'file_size': ' 15 '}, 'test_file.txt')
        self.assertEqual(obj['file_size'], 15)


if __name__ == '__main__':
    unittest.main()
