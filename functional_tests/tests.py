from django.test import LiveServerTestCase
from selenium import webdriver
from allauth.account.models import EmailAddress


class AbstractTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def click_button_with_text_from_list(self, text, buttons):
        for button in buttons:
            if (button.text == text):
                button.click()
                break

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


class NewVisitorTest(AbstractTestCase):

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
        self.click_button_with_text_from_list("Sign Up", navbar_links)

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


class NewMinionTest(AbstractTestCase):

    def test_can_create_minion_and_view_it_later(self):
        self.username = "some_user"
        self.email = "some_email@fake.com"
        self.password = "some_password"
        self.first_minion_name = "some_minion_name"
        self.generate_new_user()
        self.login()

        # clicks on the minions tab
        navbar_links = self.browser.find_elements_by_xpath(
            "//div[@id='bs-navbar-collapse-1']/nav/a"
        )

        self.click_button_with_text_from_list("My Minions", navbar_links)

        # The user is taken to a page which invites them to add a minion
        create = self.browser.find_element_by_link_text("Create a new Minion")

        # It would list the existing minions present for the user, but the user
        # is new and haven't made any yet
        minion_list = self.browser.find_element_by_class_name("list-group")
        self.assertEqual(0, len(minion_list.find_elements_by_tag_name("div")))
        self.assertEqual(0, len(minion_list.find_elements_by_tag_name("a")))

        # clicks the "Create a new Minion link"
        create.click()

        # the user is taken to a form page to create the new minion
        # the form includes a Name field, a Parent field (with no options), and
        # a "Create" button
        form = self.browser.find_element_by_tag_name("form")
        inputs = form.find_elements_by_tag_name("input")
        parent_select = form.find_element_by_tag_name("select")
        self.assertEqual(3, len(inputs))

        self.assertEqual(
            "csrfmiddlewaretoken",
            inputs[0].get_attribute("name")
        )
        self.assertEqual("id_name", inputs[1].get_attribute("id"))
        name_input = inputs[1]
        self.assertEqual("id_parent", parent_select.get_attribute("id"))

        # There are no options available for parents yet (besides the default)
        parent_options = parent_select.find_elements_by_tag_name("option")
        self.assertEqual(
            1,
            len(parent_options)
        )
        self.assertEqual("", parent_options[0].get_attribute("value"))
        self.assertEqual("submit", inputs[2].get_attribute("type"))
        submit_button = inputs[2]

        # The user gives a name to their new minion
        name_input.send_keys(self.first_minion_name)

        # The user confirms the submission
        submit_button.click()

        # The user is redirected to a detail page of the minion that was just
        # created
        container = self.browser.find_element_by_class_name("col-sm-12")

        # the detail page begins with the name of the minion
        self.assertEqual(
            self.first_minion_name,
            container.find_element_by_tag_name("h2").text
        )

        # The rest of the page is broken up into 2 sections
        sections = container.find_elements_by_tag_name("div")
        headers = container.find_elements_by_tag_name("h4")
        self.assertEqual(2, len(sections))
        self.assertEqual(2, len(headers))

        # there is one section which lists any children the minion has
        self.assertEqual(
            "Minions",
            headers[0].text
        )
        # this section is currently empty
        self.assertEqual(0, len(sections[0].find_elements_by_tag_name("a")))
        self.assertEqual(0, len(sections[0].find_elements_by_tag_name("div")))
        # there is a final section with any data the minion has accumulated
        self.assertEqual(
            "Data",
            headers[1].text
        )
        # this section is also currently empty
        self.assertEqual(0, len(sections[1].find_elements_by_tag_name("a")))
        self.assertEqual(0, len(sections[1].find_elements_by_tag_name("div")))

        # The user backs out to the listing page
        navbar_links = self.browser.find_elements_by_xpath(
            "//div[@id='bs-navbar-collapse-1']/nav/a"
        )
        self.click_button_with_text_from_list("My Minions", navbar_links)

        # The user now sees the minion that they had created on the listing
        # page
        minion_list = self.browser.find_element_by_class_name("list-group")
        self.assertEqual(1, len(minion_list.find_elements_by_tag_name("a")))
        self.browser.find_element_by_link_text(self.first_minion_name)

    def generate_new_user(self):
        # Go to the signup page
        self.browser.get(self.live_server_url + "/accounts/signup/")

        # submit the form
        self.complete_and_submit_signup_form()

        # verify email address
        self.verify_email_address()

    def complete_and_submit_signup_form(self):
        username_field = self.browser.find_element_by_id("id_username")
        email_field = self.browser.find_element_by_id("id_email")
        password_field = self.browser.find_element_by_id("id_password1")
        password_again_field = self.browser.find_element_by_id("id_password2")

        username_field.send_keys(self.username)
        email_field.send_keys(self.email)
        password_field.send_keys(self.password)
        password_again_field.send_keys(self.password)

        # clicks the submit button
        buttons = self.browser.find_elements_by_class_name("btn-primary")
        self.click_button_with_text_from_list("Sign Up »", buttons)

    def verify_email_address(self):
        # verifies email address
        # (This is a bit of a hack to avoid having to actually send the email
        # confirmation for now)
        email = EmailAddress.objects.get(email=self.email)
        email.verified = True
        email.save()

    def login(self):
        # Go to the login page
        self.browser.get(self.live_server_url + "/accounts/login/")

        # logs in by filling out the login form
        username_field = self.browser.find_element_by_id("id_login")
        password_field = self.browser.find_element_by_id("id_password")
        buttons = self.browser.find_elements_by_class_name(
            "btn-primary"
        )

        username_field.send_keys(self.username)
        password_field.send_keys(self.password)

        self.click_button_with_text_from_list("Sign In", buttons)
