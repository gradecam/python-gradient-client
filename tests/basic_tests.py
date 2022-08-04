import unittest

from gradient import factory

base_url = 'https://app-int.gradecam.com'
id = 'DEMO'
token = 'cacd79fbb7524fbc93c468f51f7564b5'

class TestClient(unittest.TestCase):
    def test_get_sub_details(self):
        client = factory( base_url, id, token )
        resp = client.get()
        self.assertEqual( resp.status_code, 200, 'Should have retrieved sub details' )

    def test_create_update_terms(self):
        client = factory( base_url, id, token )
        terms = [
            {"id": "1", "name": "Fall 2022-2023", "start_date": "2022-08-01", "end_date": "2022-12-20" },
            {"id": "2", "name": "Winter 2022-2023", "start_date": "2023-01-04", "end_date": "2023-04-15" },
        ]
        resp = client.post( terms, 'terms' )
        self.assertIn( resp.status_code, [ 200, 201 ], 'Should have created/updated terms')


if __name__ == '__main__':
    unittest.main()
