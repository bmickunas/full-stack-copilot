import unittest
from unittest.mock import MagicMock
from thing_service import ThingService

class TestThingService(unittest.TestCase):
    def setUp(self):
        self.mock_dao = MagicMock()
        self.thing_service = ThingService(self.mock_dao)

    def test_get_thing_success(self):
        # Arrange
        thing_id = '123'
        expected_thing = {'id': thing_id, 'name': 'Test Thing'}
        self.mock_dao.get_thing.return_value = expected_thing

        # Act
        result = self.thing_service.get_thing(thing_id)

        # Assert
        self.assertEqual(result, expected_thing)
        self.mock_dao.get_thing.assert_called_once_with(thing_id)

    def test_get_thing_not_found(self):
        # Arrange
        thing_id = '123'
        self.mock_dao.get_thing.return_value = None

        # Act
        result = self.thing_service.get_thing(thing_id)

        # Assert
        self.assertIsNone(result)
        self.mock_dao.get_thing.assert_called_once_with(thing_id)

if __name__ == '__main__':
    unittest.main()