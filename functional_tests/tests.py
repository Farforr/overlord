from django.test import LiveServerTestCase
from selenium import webdriver


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_make_a_minion_and_retrieve_it_later(self):
        # New user heads to the homepage of the myOverlord Site
        self.browser.get(self.live_server_url)

        # Overlord appears in the website title
        self.assertIn('overlord', self.browser.title)

        # The user clicks on the minions tab
        self.fail('Finish the test!')

        # The user is taken to a page which invites them to add a minion
        # It would list the existing minions present for the user, but the user
        # is new and haven't made any yet

        # The user gives a name to their new minion

        # The user confirms the submission

        # The user is redirected to a detail page of the minion that was just
        # created

        # The detail page includes the minion's name, and an empty section for
        # data

        # The user backs out to the listing page

        # The user sees the minion that they had created on the listing page
