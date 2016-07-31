from unittest.mock import patch, MagicMock
from django.core.urlresolvers import reverse
from django.test import RequestFactory
from test_plus.test import TestCase
from ..models import (
    Minion,
    MinionData
)

from ..views import(
    MinionCreateView,
    MinionDetailView
)


class TestMinionCreateView(TestCase):

    def setUp(self):
        self.user = self.make_user()
        self.factory = RequestFactory()

    def test_get(self):
        request = self.factory.get(reverse('minions:minion-create'))
        request.user = self.user
        response = MinionCreateView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.context_data['user'], self.data)
        # self.assertEqual(response.context_data['request'], request)

    @patch('Minion.save', MagicMock(name="save"))
    def test_post(self):
        data = {
            'name': 'test_minion'
        }

        request = self.factory.post(reverse('minions:minion-create'), data)
        request.user = self.user

        response = MinionCreateView.as_view()(request)
        self.assertEqual(response.status_code, 302)

        self.assertTrue(Minion.save.called)
        self.assertEqual(Minion.save.call_count, 1)
