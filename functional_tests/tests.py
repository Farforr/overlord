from django.test import LiveServerTestCase
from selenium import webdriver
from allauth.account.models import EmailAddress


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_create_an_account_and_login(self):
        # New user heads to the homepage of the myOverlord Site
        self.browser.get(self.live_server_url)

        # Overlord appears in the website title
        self.assertIn('overlord', self.browser.title)

        # is invited to Sign Up
        navbar_links = self.browser.find_elements_by_xpath(
            "//div[@id='bs-navbar-collapse-1']/nav/a"
        )

        self.verify_navbar_links(navbar_links)

        # navigates to the sign up page by clicking the Sign Up button
        for link in navbar_links:
            if (link.text == "Sign Up"):
                link.click()
                break

        # The sign up page includes a form with the following fields:
        # Username, E-mail, Password, Password (again)
        username_field = self.browser.find_element_by_id("id_username")
        email_field = self.browser.find_element_by_id("id_email")
        password_field = self.browser.find_element_by_id("id_password1")
        password_again_field = self.browser.find_element_by_id("id_password2")

        self.assertEqual(
            "Username",
            username_field.get_attribute('placeholder')
        )
        self.assertEqual(
            "E-mail address",
            email_field.get_attribute('placeholder')
        )
        self.assertEqual(
            "Password",
            password_field.get_attribute('placeholder')
        )
        self.assertEqual(
            "Password (again)",
            password_again_field.get_attribute('placeholder')
        )

        # There is also a submit button
        buttons = self.browser.find_elements_by_class_name("btn-primary")
        self.assertIn("Sign Up »", [button.text for button in buttons])

        username = "some_user"
        email = "some_email@fake.com"
        password = "some_password"

        # fills out the form
        username_field.send_keys(username)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_again_field.send_keys(password)

        # clicks the submit button
        self.click_button_with_text_from_list("Sign Up »", buttons)

        # a request for email verification appears

        # verifies email address
        # (This is a bit of a hack to avoid having to actually send the email
        # confirmation for now)
        email = EmailAddress.objects.get(email=email)
        email.verified = True
        email.save()

        # navigates back to home page
        self.browser.get(self.live_server_url)

        # the user is not yet logged in
        navbar_links = self.browser.find_elements_by_xpath(
            "//div[@id='bs-navbar-collapse-1']/nav/a"
        )

        self.verify_navbar_links(navbar_links)

        # navigates to the sign up page by clicking the Sign Up button
        self.click_button_with_text_from_list("Log In", navbar_links)

        # logs in by filling out the login form
        username_field = self.browser.find_element_by_id("id_login")
        password_field = self.browser.find_element_by_id("id_password")
        buttons = self.browser.find_elements_by_class_name(
            "btn-primary"
        )

        username_field.send_keys(username)
        password_field.send_keys(password)

        self.click_button_with_text_from_list("Sign In", buttons)

        # The Sign Up and Log In links have been replaced by 3 new ones:
        # My Minions, My Profile, and Logout
        navbar_links = self.browser.find_elements_by_xpath(
            "//div[@id='bs-navbar-collapse-1']/nav/a"
        )
        self.verify_navbar_links(navbar_links, True)
        # clicks on the minions tab

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
        self.fail('Finish the test!')

    def verify_navbar_links(self, navbar_links, logged_in=False):
        navbar_links = [link.text for link in navbar_links]
        self.assertIn('Home', navbar_links)
        self.assertIn('About', navbar_links)

        if (logged_in == True):
            self.assertIn('My Minions', navbar_links)
            self.assertIn('My Profile', navbar_links)
            self.assertIn('Logout', navbar_links)
            self.assertNotIn('Sign Up', navbar_links)
            self.assertNotIn('Log In', navbar_links)
        else:
            self.assertIn('Sign Up', navbar_links)
            self.assertIn('Log In', navbar_links)
            self.assertNotIn('My Minions', navbar_links)
            self.assertNotIn('My Profile', navbar_links)
            self.assertNotIn('Logout', navbar_links)

    def click_button_with_text_from_list(self, text, buttons):
        for button in buttons:
            if (button.text == text):
                button.click()
                break
