import os
import unittest
import main

class FunctionalTest(unittest.TestCase):

    def setUp(self):
        test_dir = os.path.dirname(os.path.realpath(__file__))
        test_data_dir = os.path.join(test_dir, 'data')
        term_path = os.path.join(test_data_dir, 'test-terms.csv')
        dataset_path = os.path.join(test_data_dir, 'test-dataset.csv')

        self.term_file = main.get_data_from_csv(term_path)
        self.terms = [line['Term'] for line in self.term_file]
        self.dataset = main.get_data_from_csv(dataset_path)


    def test_terms_loaded(self):
        self.assertEqual(len(self.terms), 8)
        self.assertEqual("mantrip", self.terms[3])
        self.assertEqual("hang", self.term_file[3]['Category'])

    def test_terms_connected(self):
        edges = main.get_term_edges(self.terms, self.dataset)
        expected = {'source': 'jimble',
                    'target': 'bang'}
        self.assertIn(expected, edges)

    def test_no_self_loops(self):
        edges = main.get_term_edges(self.terms, self.dataset)
        excluded = {'source': 'bang',
                    'target': 'bang'}
        self.assertNotIn(excluded, edges)

    def test_users_and_terms_connected(self):
        user_edges = main.get_term_edges(self.terms, self.dataset,
                                         data_userfield="User-id")
        expected = {'source': '1',
                    'target': 'jimble'}
        self.assertIn(expected, user_edges)


