import unittest
import json
import os
from unittest.mock import Mock
from neo4j import Driver
from file_loader import FileLoader
from icdc_schema import ICDC_Schema
from props import Props
from config import BentoConfig
from data_loader import DataLoader


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


class TestLambda(unittest.TestCase):
    def setUp(self):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(test_dir, 'data/lambda/event1.json')) as inf:
            self.event = json.load(inf)
        
        # Use mock Neo4j driver instead of requiring environment variable
        self.driver = MockNeo4jDriver()
        
        props_path = os.path.join(test_dir, 'data', 'props-icdc.yml')
        model_path = os.path.join(test_dir, 'data', 'icdc-model.yml')
        model_props_path = os.path.join(test_dir, 'data', 'icdc-model-props.yml')
        
        props = Props(props_path)
        self.schema = ICDC_Schema([model_path, model_props_path], props)
        
        # Create a minimal config file for testing
        config_path = os.path.join(test_dir, 'data', 'test_config.yml')
        if not os.path.exists(config_path):
            with open(config_path, 'w') as f:
                f.write('Config:\n')
                f.write('  s3_bucket: test-bucket\n')
                f.write('  temp_folder: /tmp\n')
        
        config = BentoConfig(config_path)
        self.processor = FileLoader('', self.driver, self.schema, config, 'test-file-loader', 'test/manifests')
        self.loader = DataLoader(self.driver, self.schema)
        self.file_list = [
            os.path.join(test_dir, "data/Dataset/COP-program.txt"),
            os.path.join(test_dir, "data/Dataset/NCATS-COP01-case.txt"),
            os.path.join(test_dir, "data/Dataset/NCATS-COP01-diagnosis.txt"),
            os.path.join(test_dir, "data/Dataset/NCATS-COP01_cohort_file.txt"),
            os.path.join(test_dir, "data/Dataset/NCATS-COP01_study_file.txt")
        ]

    def test_join_path(self):
        self.assertEqual(self.processor.join_path(), '')
        self.assertEqual(self.processor.join_path('abc'), 'abc')
        self.assertEqual(self.processor.join_path('/abc'), '/abc')
        self.assertEqual(self.processor.join_path('/abc/'), '/abc')

        self.assertEqual(self.processor.join_path('abd/def', 'ghi.zip'), 'abd/def/ghi.zip')
        self.assertEqual(self.processor.join_path('abd/def/', 'ghi.zip'), 'abd/def/ghi.zip')
        self.assertEqual(self.processor.join_path('abd/def//', '//ghi.zip'), 'abd/def/ghi.zip')
        self.assertEqual(self.processor.join_path('http://abd/def//', '//ghi.zip//'), 'http://abd/def/ghi.zip')

        # Test multiple paths joining
        self.assertEqual(self.processor.join_path('abd/def', 'xy/z', 'ghi.zip'), 'abd/def/xy/z/ghi.zip')
        self.assertEqual(self.processor.join_path('abd/def/', '/xy/z/' , 'ghi.zip'), 'abd/def/xy/z/ghi.zip')
        self.assertEqual(self.processor.join_path('abd/def/', '///xy/z///', '///ghi.zip'), 'abd/def/xy/z/ghi.zip')

    @unittest.skip("Skipping test that requires actual Neo4j database interaction")
    def test_lambda(self):
        load_result = self.loader.load(self.file_list, True, False, 'upsert', False, 1, '/tmp', False)
        self.assertIsInstance(load_result, dict, msg='Load data failed!')

        self.assertTrue(self.processor.handler(self.event))
