from test_plus.test import TestCase
from ..models import (
    Minion,
    MinionData
)


class TestMinionModel(TestCase):

    def setUp(self):
        self.user = self.make_user()
        self.minion_parent = Minion(name='parent')
        self.minion_child = Minion(name='child', parent=self.minion_parent)
        self.minion_data = MinionData(
            pk=1,
            field_name='test_field_name',
            field_value='test_field_value',
            minion=self.minion_parent
        )

    def test_minion__str__(self):
        self.assertEqual(
            self.minion_parent.__str__(),
            "parent"  # This is the default username for self.make_user()
        )

    def test_minion_get_absolute_url(self):
        self.assertEqual(
            self.minion_parent.get_absolute_url(),
            '/minions/minion/' + self.minion_parent.name + '/'
        )

    def test_minion_is_top_level_negative(self):
        self.assertFalse(self.minion_child.is_top_level())

    def test_minion_is_top_level_positive(self):
        self.assertTrue(self.minion_parent.is_top_level())

    def test_minion_is_top_level_positive(self):
        self.assertTrue(self.minion_parent.is_top_level())

    def test_minionData_get_absolute_url(self):
        self.assertEqual(
            self.minion_data.get_absolute_url(),
            '/minions/data/' + str(self.minion_data.pk) + '/'
        )

    def test_minionData__str__(self):
        self.assertEqual(
            self.minion_data.__str__(),
            'test_field_name : test_field_value'
        )
