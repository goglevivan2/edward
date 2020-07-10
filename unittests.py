import unittest
import edward

class EdwardTestCase(unittest.TestCase):

    def test_001_simple(self):
        result = edward.Encryptor('files\\somefile.txt')
        self.assertTrue(result.return_decrypt_message() == 'edward')

    def test_002_big_file(self):
        result = edward.Encryptor('files\\bigfile.txt')
        self.assertTrue(len(result.return_decrypt_message()) == len('edward') * (100000 // len('wweddaadwaffrdnn')))

    def test_003_error_file_name(self):
        try:
            edward.Encryptor('files\\file_does_not_exist.txt')  # ERROR
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_004_empty_file(self):
        result = edward.Encryptor('files\\emptyfile.txt')
        self.assertTrue(result.return_decrypt_message() == '')

    def test_005_normal_file(self):
        result = edward.Encryptor('files\\normalfile.txt')
        self.assertTrue(result.return_decrypt_message() == 'this file is not encrypted')

    def test_006_three_identical_letters(self):
        result = edward.Encryptor('files\\file4tc6.txt')
        self.assertTrue(result.return_decrypt_message() == 'edward')




if __name__ == '__main__':
    unittest.main()
