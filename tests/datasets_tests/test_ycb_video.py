import unittest

import pytest

from objslampp.datasets.ycb_video import YCBVideoDataset
from objslampp.datasets.ycb_video import class_names


@pytest.mark.heavy
class TestYCBVideoDataset(unittest.TestCase):

    def setUp(self):
        self.dataset = YCBVideoDataset('val')

    def test_init(self):
        assert self.dataset.split == 'val'

    def test_get_example(self):
        example = self.dataset.get_example(0)
        assert set(example.keys()) == {'meta', 'color', 'depth', 'label'}


def test_class_names():
    assert isinstance(class_names, tuple)
    assert len(class_names) == 22