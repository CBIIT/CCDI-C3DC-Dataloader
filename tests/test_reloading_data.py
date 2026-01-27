import unittest
import os
from unittest.mock import Mock, patch
from bento.common.utils import get_logger, NODES_CREATED, RELATIONSHIP_CREATED, NODES_DELETED, RELATIONSHIP_DELETED
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


class TestLoaderReload(unittest.TestCase):
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
            "data/Dataset/COP-program.txt",
            "data/Dataset/COTC007B-case.txt",
            "data/Dataset/COTC007B-cohort.txt",
            "data/Dataset/COTC007B-cycle.txt",
            "data/Dataset/COTC007B-demographic.txt",
            "data/Dataset/COTC007B-diagnostic.txt",
            "data/Dataset/COTC007B-enrollment.txt",
            "data/Dataset/COTC007B-extent_of_disease.txt",
            "data/Dataset/COTC007B-physical_exam.txt",
            "data/Dataset/COTC007B-principal_investigator.txt",
            "data/Dataset/COTC007B-prior_surgery.txt",
            "data/Dataset/COTC007B-study.txt",
            "data/Dataset/COTC007B-study_arm.txt",
            "data/Dataset/COTC007B-vital_signs.txt",
            "data/Dataset/NCATS-COP01-blood_samples.txt",
            "data/Dataset/NCATS-COP01-case.txt",
            "data/Dataset/NCATS-COP01-demographic.txt",
            "data/Dataset/NCATS-COP01-diagnosis.txt",
            "data/Dataset/NCATS-COP01-enrollment.txt",
            "data/Dataset/NCATS-COP01-normal_samples.txt",
            "data/Dataset/NCATS-COP01-tumor_samples.txt",
            "data/Dataset/NCATS-COP01_20170228-GSL-079A-PE-Breen-NCATS-MEL-Rep1-Lane3.tar-file_neo4j.txt",
            "data/Dataset/NCATS-COP01_GSL-076A-Breen-NCATS-MEL-Rep1-Lane1.tar-file_neo4j.txt",
            "data/Dataset/NCATS-COP01_GSL-076A-Breen-NCATS-MEL-Rep1-Lane2.tar-file_neo4j.txt",
            "data/Dataset/NCATS-COP01_GSL-076A-Breen-NCATS-MEL-Rep2-Lane1.tar-file_neo4j.txt",
            "data/Dataset/NCATS-COP01_GSL-076A-Breen-NCATS-MEL-Rep3-Lane1.tar-file_neo4j.txt",
            "data/Dataset/NCATS-COP01_GSL-079A-Breen-NCATS-MEL-Rep2-Lane2.tar-file_neo4j.txt",
            "data/Dataset/NCATS-COP01_GSL-079A-Breen-NCATS-MEL-Rep2-Lane3.tar-file_neo4j.txt",
            "data/Dataset/NCATS-COP01_GSL-079A-Breen-NCATS-MEL-Rep3-Lane2.tar-file_neo4j.txt",
            "data/Dataset/NCATS-COP01_GSL-079A-Breen-NCATS-MEL-Rep3-Lane3.tar-file_neo4j.txt",
            "data/Dataset/NCATS-COP01_cohort_file.txt",
            "data/Dataset/NCATS-COP01_path_report_file_neo4j.txt",
            "data/Dataset/NCATS-COP01_study_file.txt"
        ]
        self.file_list_unique = [
            "data/Dataset/COP-program.txt",
            "data/Dataset/COTC007B-case.txt",
            "data/Dataset/COTC007B-cohort.txt",
            "data/Dataset/COTC007B-cycle.txt",
            "data/Dataset/COTC007B-demographic.txt",
            "data/Dataset/COTC007B-diagnostic.txt",
            "data/Dataset/COTC007B-enrollment.txt",
            "data/Dataset/COTC007B-extent_of_disease.txt",
            "data/Dataset/COTC007B-physical_exam.txt",
            "data/Dataset/COTC007B-principal_investigator.txt",
            "data/Dataset/COTC007B-prior_surgery.txt",
            "data/Dataset/COTC007B-study.txt",
            "data/Dataset/COTC007B-study_arm.txt",
            "data/Dataset/COTC007B-vital_signs_unique.txt",
            "data/Dataset/NCATS-COP01-blood_samples.txt",
            "data/Dataset/NCATS-COP01-case.txt",
            "data/Dataset/NCATS-COP01-demographic.txt",
            "data/Dataset/NCATS-COP01-diagnosis.txt",
            "data/Dataset/NCATS-COP01-enrollment.txt",
            "data/Dataset/NCATS-COP01-normal_samples.txt",
            "data/Dataset/NCATS-COP01-tumor_samples.txt",
            "data/Dataset/NCATS-COP01_20170228-GSL-079A-PE-Breen-NCATS-MEL-Rep1-Lane3.tar-file_neo4j.txt",
            "data/Dataset/NCATS-COP01_GSL-076A-Breen-NCATS-MEL-Rep1-Lane1.tar-file_neo4j.txt",
            "data/Dataset/NCATS-COP01_GSL-076A-Breen-NCATS-MEL-Rep1-Lane2.tar-file_neo4j.txt",
            "data/Dataset/NCATS-COP01_GSL-076A-Breen-NCATS-MEL-Rep2-Lane1.tar-file_neo4j.txt",
            "data/Dataset/NCATS-COP01_GSL-076A-Breen-NCATS-MEL-Rep3-Lane1.tar-file_neo4j.txt",
            "data/Dataset/NCATS-COP01_GSL-079A-Breen-NCATS-MEL-Rep2-Lane2.tar-file_neo4j.txt",
            "data/Dataset/NCATS-COP01_GSL-079A-Breen-NCATS-MEL-Rep2-Lane3.tar-file_neo4j.txt",
            "data/Dataset/NCATS-COP01_GSL-079A-Breen-NCATS-MEL-Rep3-Lane2.tar-file_neo4j.txt",
            "data/Dataset/NCATS-COP01_GSL-079A-Breen-NCATS-MEL-Rep3-Lane3.tar-file_neo4j.txt",
            "data/Dataset/NCATS-COP01_cohort_file.txt",
            "data/Dataset/NCATS-COP01_path_report_file_neo4j.txt",
            "data/Dataset/NCATS-COP01_study_file.txt"
        ]


    @unittest.skip("Skipping test that requires actual Neo4j database interaction")
    def test_load_detect_duplicate(self):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        self.assertRaises(Exception, self.loader.load([os.path.join(test_dir, "data/COTC007B/COTC007B-vital_signs.txt")], True, False, 'new', True, 1, '/tmp', False))


    @unittest.skip("Skipping test that requires actual Neo4j database interaction")
    def test_reload_with_new_and_delete_cohorts(self):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        file_list_unique = [os.path.join(test_dir, f) for f in self.file_list_unique]
        load_result = self.loader.load(file_list_unique, True, False, 'new', True, 1, '/tmp', False)
        self.assertIsInstance(load_result, dict, msg='Load data failed!')
        self.assertEqual(1832, load_result[NODES_CREATED])
        self.assertEqual(1974, load_result[RELATIONSHIP_CREATED])
        result = self.loader.load([os.path.join(test_dir, 'data/Dataset/COTC007B-cohort.txt')], True, False, 'delete', False, 1, '/tmp', False)
        self.assertEqual(result[NODES_DELETED], 18)
        self.assertEqual(result[RELATIONSHIP_DELETED], 101)

    @unittest.skip("Skipping test that requires actual Neo4j database interaction")
    def test_reload_with_new_and_delete_study(self):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        file_list_unique = [os.path.join(test_dir, f) for f in self.file_list_unique]
        load_result = self.loader.load(file_list_unique, True, False, 'new', True, 1, '/tmp', False)
        self.assertIsInstance(load_result, dict, msg='Load data failed!')
        self.assertEqual(1832, load_result[NODES_CREATED])
        self.assertEqual(1974, load_result[RELATIONSHIP_CREATED])
        result = self.loader.load([os.path.join(test_dir, 'data/Dataset/COTC007B-study.txt')], True, False, 'delete', False, 1, '/tmp', False)
        self.assertEqual(result[NODES_DELETED], 1118)
        self.assertEqual(result[RELATIONSHIP_DELETED], 1201)

        result = self.loader.load([os.path.join(test_dir, 'data/Dataset/NCATS-COP01_study_file.txt')], True, False, 'delete', False, 1, '/tmp', False)
        self.assertEqual(result[NODES_DELETED], 713)
        self.assertEqual(result[RELATIONSHIP_DELETED], 773)

    @unittest.skip("Skipping test that requires actual Neo4j database interaction")
    def test_reload_with_new_and_delete_program(self):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        file_list_unique = [os.path.join(test_dir, f) for f in self.file_list_unique]
        load_result = self.loader.load(file_list_unique, True, False, 'new', True, 1, '/tmp', False)
        self.assertIsInstance(load_result, dict, msg='Load data failed!')
        self.assertEqual(1832, load_result[NODES_CREATED])
        self.assertEqual(1974, load_result[RELATIONSHIP_CREATED])
        result = self.loader.load([os.path.join(test_dir, 'data/Dataset/COP-program.txt')], True, False, 'delete', False, 1, '/tmp', False)
        self.assertEqual(result[NODES_DELETED], 1832)
        self.assertEqual(result[RELATIONSHIP_DELETED], 1974)


    @unittest.skip("Skipping test that requires actual Neo4j database interaction")
    def test_reload_upsert(self):
        test_dir = os.path.dirname(os.path.abspath(__file__))
        file_list = [os.path.join(test_dir, f) for f in self.file_list]
        load_result = self.loader.load(file_list, True, False, 'upsert', True, 1, '/tmp', False)
        self.assertIsInstance(load_result, dict, msg='Load data failed!')
        self.assertEqual(1832, load_result[NODES_CREATED])
        self.assertEqual(1974, load_result[RELATIONSHIP_CREATED])



if __name__ == '__main__':
    unittest.main()
