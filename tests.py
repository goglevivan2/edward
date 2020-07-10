import edward

### TEST CASES ###

def test_case_001_simple():
    result = edward.Encryptor('somefile.txt')
    assert result.return_decrypt_message() == 'edward'

def test_case_002_big_file():
    result = edward.Encryptor('bigfile.txt')
    assert len(result.return_decrypt_message())==len('edward')*(100000//len('wweddaadwaffrdnn'))

def test_case_003_error_file_name():
    try:
        edward.Encryptor('file_does_not_exist.txt') # ERROR
        assert False
    except:
        assert True

def test_case_004_empty_file():
    result = edward.Encryptor('emptyfile.txt')
    assert result.return_decrypt_message() == ''