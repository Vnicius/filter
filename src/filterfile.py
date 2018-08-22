# -*- coding: utf-8 -*-

'''
  @author: Vinícius Veríssimo
  @email: vinicius.matheus@lavid.ufpb.br
'''


class FilterFile:
    def __init__(self, fileName):
        self.fileName = fileName
        self.words = []

    def load(self):
        with open(self.fileName, 'r') as fl:
            try:
                while True:
                    word = fl.readline().replace('\n', '')

                    if word:
                        self.words.append(word)
                    else:
                        break

            except EOFError:
                pass

    def has_word(self, word):
        return word in self.words
