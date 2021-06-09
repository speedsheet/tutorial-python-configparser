from shared import *

from configparser import ConfigParser
from unittest import TestCase

CONFIG_CONTENTS = '''[test-section]
test-1 = value-1'''

class TestConfigParser(TestCase):

	def setUp(self):
		self.config = ConfigParser()
		self.config.read_string(CONFIG_CONTENTS)

	def test_has_option_for_test_1_should_return_true(self):
		self.assertTrue(
			self.config.has_option('test-section', 'test-1'))
