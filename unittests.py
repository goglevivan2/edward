import unittest
import edward

class MyTestCase(unittest.TestCase):
    def test_case_001_simple(self):
        result = edward.Encryptor('files\\somefile.txt')
        self.assertTrue(result.return_decrypt_message() == 'edward')

    def test_case_002_big_file(self):
        result = edward.Encryptor('files\\bigfile.txt')
        self.assertTrue(len(result.return_decrypt_message()) == len('edward') * (100000 // len('wweddaadwaffrdnn')))



if __name__ == '__main__':
    unittest.main()
