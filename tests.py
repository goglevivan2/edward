import edward

### TEST CASE ###

def test_001_simple():
    result = edward.Encryptor('files\\somefile.txt')
    assert result.return_decrypt_message() == 'edward'

def test_002_big_file():
    result = edward.Encryptor('files\\bigfile.txt')
    assert len(result.return_decrypt_message())==len('edward')*(100000//len('wweddaadwaffrdnn'))

def test_003_error_file_name():
    try:
        edward.Encryptor('files\\file_does_not_exist.txt') # ERROR
        assert False
    except:
        assert True

def test_004_empty_file():
    result = edward.Encryptor('files\\emptyfile.txt')
    assert result.return_decrypt_message() == ''

def test_005_normal_file():
    result = edward.Encryptor('files\\normalfile.txt')
    assert result.return_decrypt_message() == 'this file is not encrypted'

def test_006_three_identical_letters():
    result = edward.Encryptor('files\\file4tc6.txt')
    assert result.return_decrypt_message() == 'edward'