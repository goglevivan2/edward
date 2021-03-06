import argparse
import re

class Encryptor:
    def __init__(self,file_name):
        self.context=self.read_file(filename=file_name)
        self.data =  self.delete_double_letters(self.context)

    def return_decrypt_message(self)->str:
        """
        this function returns a decrypted message
        :return: decrypted message
        """
        return self.data

    def read_file(self,filename:str)->str:
        """
        [EN] This function returns the content of the file.
        [RU] Эта функция возвращает содержимое файла. filename - имя чтиаемого файла
        :param filename: name of file
        :return: content of file
        """
        try:
            with open(filename,'r') as file:
                content = file.read()
            return content
        except Exception as e:
            return str(e)+'\a'

    def delete_double_letters(self,sometext:str)->str:
        """
        [EN] This function removes combinations of two identical letters
        [RU] Данная функция удаляет сочетания из двух одинаковых букв
        :param sometext: some string
        :return: result string
        """
        return re.sub(r"((\w)\2)*",'',sometext) # this regex are used to remove combinations of two identical letters

class Main:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Message Decoder [for Edward :)]')
        parser.add_argument('file',type=str,help='write path or file name')
        args = parser.parse_args()
        result = Encryptor(args.file)
        print(result.return_decrypt_message())

if __name__=='__main__':
    Main()