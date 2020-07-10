import unittest
import edward

class MyTestCase(unittest.TestCase):
    def test_case_001_simple(self):
        result = edward.Encryptor('files\\somefile.txt')
        self.assertTrue(result.return_decrypt_message() == 'edward')

if __name__ == '__main__':
    unittest.main()
