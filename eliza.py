import re
import random
from english import *
from indonesia import *
# based on Study group artificial intelligence laboratory 2020


class Eliza:
    def __init__(self, lang='en'):
        if lang == 'en':
            self.reflections = en_reflections
            self.dictionaries = en_dictionaries
            self.default_responses = en_default_responses
        elif lang == 'id':
            self.reflections = id_reflections
            self.dictionaries = id_dictionaries
            self.default_responses = id_default_responses
        self.regex = [re.compile(dictionary[0], re.IGNORECASE)
                      for dictionary in self.dictionaries]
        self.answers = [response[1]
                        for response in self.dictionaries]

    def translate(self, text):
        words = text.lower().split()
        keys = self.reflections.keys()
        for i in range(0, len(words)):
            if words[i] in keys:
                words[i] = self.reflections[words[i]]
        return ' '.join(words)

    def respond(self, text):
        text = text.lower()
        for i in range(len(self.regex)):
            match = self.regex[i].match(text)  # melakukan regex di kalimat
            if match:  # jika regex sesuai
                # dapatkan respon secara random dari list jawaban
                respon = random.choice(self.answers[i])
                # cari tahu info lalu gabungkan dengan respon jika respon perlu info
                if (respon.find('%') != -1):
                    respon = respon.split('%')
                    try:
                        group = match.group(2)
                    except IndexError:
                        group = match.group(1)
                    print(group)
                    respon.insert(1, self.translate(group))
                    return ''.join(respon)
                return respon
        # jika tidak ada di kamus, keluarkan kata random
        return random.choice(self.default_responses)
