import unittest
import yaml
from transformer.nodes import GeneticAnalysis

ERROR_MAP = {
    'type': TypeError,
    'value': ValueError
}

class TestGeneticAnalysisFactory():
    def create_genetic_analysis(
            self,
            id = 'abc-123',
            age_at_genetic_analysis = 200,
            allelic_ratio = 3.1,
            alteration = '11q Deletion',
            dna_index_numeric = 3.1,
            genetic_analysis_id = 'abc-123',
            hgvs_coding = 'Some coding here',
            hgvs_protein = 'Some protein here',
            iscn = 'Some words here',
            status = 'Present',
            vaf_numeric = 3.1):
        genetic_analysis = GeneticAnalysis(
            id,
            age_at_genetic_analysis,
            allelic_ratio,
            alteration,
            dna_index_numeric,
            genetic_analysis_id,
            hgvs_coding,
            hgvs_protein,
            iscn,
            status,
            vaf_numeric
        )

        return genetic_analysis

class TestGeneticAnalysisProps(unittest.TestCase):
    def setUp(self):
        self.genetic_analysis_factory = TestGeneticAnalysisFactory()

        with open('tests/transformer_tests/test_cases/test_genetic_analysis_props.yml', 'r', encoding='utf8') as file:
            self.test_cases = yaml.safe_load(file)

    # GeneticAnalysis.id
    def test_genetic_analysis_id(self):
        test_msg = 'Testing GeneticAnalysis.id being <{}>...'

        for test_case in self.test_cases['id']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.genetic_analysis_factory.create_genetic_analysis(id=value)

    # GeneticAnalysis.age_at_genetic_analysis
    def test_genetic_analysis_age_at_genetic_analysis(self):
        test_msg = 'Testing GeneticAnalysis.age_at_genetic_analysis being <{}>...'

        for test_case in self.test_cases['age_at_genetic_analysis']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.genetic_analysis_factory.create_genetic_analysis(age_at_genetic_analysis=value)

    # GeneticAnalysis.allelic_ratio
    def test_genetic_analysis_allelic_ratio(self):
        test_msg = 'Testing GeneticAnalysis.allelic_ratio being <{}>...'

        for test_case in self.test_cases['allelic_ratio']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.genetic_analysis_factory.create_genetic_analysis(allelic_ratio=value)

    # GeneticAnalysis.alteration
    def test_genetic_analysis_alteration(self):
        test_msg = 'Testing GeneticAnalysis.alteration being <{}>...'

        for test_case in self.test_cases['alteration']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.genetic_analysis_factory.create_genetic_analysis(alteration=value)

    # GeneticAnalysis.dna_index_numeric
    def test_genetic_analysis_result(self):
        test_msg = 'Testing GeneticAnalysis.dna_index_numeric being <{}>...'

        for test_case in self.test_cases['dna_index_numeric']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.genetic_analysis_factory.create_genetic_analysis(dna_index_numeric=value)

    # GeneticAnalysis.genetic_analysis_id
    def test_genetic_analysis_genetic_analysis_id(self):
        test_msg = 'Testing GeneticAnalysis.genetic_analysis_id being <{}>...'

        for test_case in self.test_cases['genetic_analysis_id']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.genetic_analysis_factory.create_genetic_analysis(genetic_analysis_id=value)

    # GeneticAnalysis.hgvs_coding
    def test_genetic_analysis_hgvs_coding(self):
        test_msg = 'Testing GeneticAnalysis.hgvs_coding being <{}>...'

        for test_case in self.test_cases['hgvs_coding']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.genetic_analysis_factory.create_genetic_analysis(hgvs_coding=value)

    # GeneticAnalysis.hgvs_protein
    def test_genetic_analysis_hgvs_protein(self):
        test_msg = 'Testing GeneticAnalysis.hgvs_protein being <{}>...'

        for test_case in self.test_cases['hgvs_protein']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.genetic_analysis_factory.create_genetic_analysis(hgvs_protein=value)

    # GeneticAnalysis.iscn
    def test_genetic_analysis_iscn(self):
        test_msg = 'Testing GeneticAnalysis.iscn being <{}>...'

        for test_case in self.test_cases['iscn']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.genetic_analysis_factory.create_genetic_analysis(iscn=value)

    # GeneticAnalysis.status
    def test_genetic_analysis_status(self):
        test_msg = 'Testing GeneticAnalysis.status being <{}>...'

        for test_case in self.test_cases['status']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.genetic_analysis_factory.create_genetic_analysis(status=value)

    # GeneticAnalysis.vaf_numeric
    def test_genetic_analysis_vaf_numeric(self):
        test_msg = 'Testing GeneticAnalysis.vaf_numeric being <{}>...'

        for test_case in self.test_cases['vaf_numeric']:
            if test_case['error_type'] == None:
                continue

            with self.assertRaisesRegex(ERROR_MAP[test_case['error_type']], test_case['error_msg']):
                value = test_case['test_value']
                print(test_msg.format(value))
                self.genetic_analysis_factory.create_genetic_analysis(vaf_numeric=value)

if __name__ == '__main__':
    unittest.main()
