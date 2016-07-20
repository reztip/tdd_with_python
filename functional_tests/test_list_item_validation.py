from unittest import skip
from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to hope page and tries to submit an empty list item
        # She hits ENTER on the box
        self.browser.get(self.server_url)
        self.browser.implicitly_wait(5)
        inputbox = self.get_item_input_box()
        self.browser.implicitly_wait(5)
        inputbox.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(5)

        
        # Page refreshes, with error saying list item cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        
        self.browser.implicitly_wait(5)
        #She tries again with some text, which works
        self.browser.implicitly_wait(5)
        inputbox = self.get_item_input_box()
        self.browser.implicitly_wait(5)
        inputbox.send_keys("Buy milk")
        self.browser.implicitly_wait(5)
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy milk')
        self.browser.implicitly_wait(5)


        #She again tries to submit a second blank list item
        #which again fails.
        inputbox = self.get_item_input_box()
        self.browser.implicitly_wait(5)
        inputbox.send_keys(Keys.ENTER)

        # She receives a similar warning as before
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # She corrects it by filling in text
        inputbox = self.get_item_input_box()
        inputbox.send_keys("Make tea")
        inputbox.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(5)
        self.check_for_row_in_list_table("1: Buy milk")
        self.browser.implicitly_wait(5)
        self.check_for_row_in_list_table("2: Make tea")

    def test_cannot_add_duplicate_items(self):
        # Edith goes to home page and starts a new list
        self.browser.get(self.server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys("Buy wellies")
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy wellies')

        # She accidentally enters in the same item again!!
        self.browser.get(self.browser.current_url)
        self.browser.implicitly_wait(5)
        inputbox = self.get_item_input_box()
        inputbox.send_keys("Buy wellies")
        inputbox.send_keys(Keys.ENTER)
        # self.browser.get(self.browser.current_url)
        # 
        # #She gets a good error msg
        self.browser.implicitly_wait(5)
        self.check_for_row_in_list_table('1: Buy wellies')
        self.browser.implicitly_wait(5)
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You've already got this in your list")


