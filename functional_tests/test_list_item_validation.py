from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    @skip
    def test_cannot_add_empty_list_items(self):
        # Edith goes to hope page and tries to submit an empty list item
        # She hits ENTER on the box
        
        # Page refreshes, saying list item cannot be blank

        #She tries again with some text, which works

        #She again tries to submit a second blank list item
        #which again fails.

        self.fail('write me')
