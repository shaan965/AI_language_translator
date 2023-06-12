import unittest

from translator import englishToFrench, frenchToEnglish


class TestEnglishToFrench(unittest.TestCase):

    def testE2F(self):
        self.assertEqual(englishToFrench('Hello'), "Bonjour")
        self.assertNotEqual(englishToFrench('Hello'), 'Hello')


class TestFrenchToEnglish(unittest.TestCase):
    def testF2E(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertNotEqual(frenchToEnglish("Bonjour"), "Bonjour")


if __name__ == '__main__':
    unittest.main()