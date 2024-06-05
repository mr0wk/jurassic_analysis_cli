import unittest

from utils.read_utils import read_dinosaurs, read_dinosaurs_by_properties


class TestReadUtils(unittest.TestCase):
    def test_read_dinosaurs_returns_data(self):
        dinosaurs = read_dinosaurs()
        self.assertIsNotNone(dinosaurs)
        self.assertNotEqual(len(dinosaurs), 0)

    def test_read_dinosaurs_by_properties_returns_dinosaurs_with_carnivore_diet(self):
        dinosaurs = read_dinosaurs_by_properties({"diet": "carnivorous"})
        self.assertIsNotNone(dinosaurs)
        self.assertNotEqual(len(dinosaurs), 0)
