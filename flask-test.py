import unittest

import flaskhello


class TestFlaskHello(unittest.TestCase):

    def setUp(self):
        self.app = flaskhello.app.test_client()

    def test_get(self):
        response = self.app.get('/')
        assert response.status_code == 404

if __name__ == '__main__':
    unittest.main()
