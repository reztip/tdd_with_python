from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to hope page and tries to submit an empty list item
        # She hits ENTER on the box
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys("\n")

        
        # Page refreshes, with error saying list item cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        
        #She tries again with some text, which works
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')
        self.check_for_row_in_list_table('1: Buy milk')


        #She again tries to submit a second blank list item
        #which again fails.
        self.browser.find_element_by_id('id_new_item').send_keys("\n")

        # She receives a similar warning as before
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # She corrects it by filling in text
        self.browser.find_element_by_id('id_new_item').send_keys("Make tea\n")
        self.check_for_row_in_list_table("1: Buy milk")
        self.check_for_row_in_list_table("2: Make tea")
