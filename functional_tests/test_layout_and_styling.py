from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
	
	def test_layout_and_style(self):
		# Edith goes to the home page
		self.browser.get(self.server_url)
		self.browser.set_window_size(1024, 768)
		
		# She notices the inputbox is nicely centered
		inputbox = self.get_item_input_box()
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2,
			512,
			delta=5
		)
		
		# She starts a new list and notices the input is nicely centered
		# there too
		inputbox.send_keys('testing\n')
		inputbox = self.get_item_input_box()
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2,
			512,
			delta=5
		)
