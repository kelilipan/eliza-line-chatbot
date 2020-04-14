import re
import random
from english import *
from indonesia import *


class Eliza:
    def __init__(self, lang='en'):
        if lang == 'en':
            self.dictionaries = en_dictionaries
            self.default_responses = en_default_responses
        elif lang == 'id':
            self.dictionaries = id_dictionaries
            self.default_responses = id_default_responses
        self.regex = [re.compile(dictionary[0], re.IGNORECASE)
                      for dictionary in self.dictionaries]
        self.answers = [response[1]
                        for response in self.dictionaries]

    def respond(self, text):
        for i in range(len(self.regex)):
            match = self.regex[i].match(text)  # melakukan regex di kalimat
            if match:  # jika regex sesuai
                # dapatkan respon secara random dari list jawaban
                respon = random.choice(self.answers[i])
                # cari tahu info lalu gabungkan dengan respon jika respon perlu info
                if (respon.find('%') != -1):
                    respon = respon.split('%')
                    print(respon.insert(1, match.group(1)))
                    return ''.join(respon)
                return respon
        # jika tidak ada di kamus, keluarkan kata random
        return random.choice(self.default_responses)
