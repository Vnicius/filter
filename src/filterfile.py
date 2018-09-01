# -*- coding: utf-8 -*-

'''
  @author: Vinícius Veríssimo
  @email: vinicius.matheus@lavid.ufpb.br
'''


class FilterFile:
    def __init__(self, fileName):
        self.fileName = fileName
        self.words = []
        self.count = []

    def load(self):
        with open(self.fileName, 'r') as fl:
            try:
                while True:
                    word = fl.readline().replace('\n', '')

                    if word:
                        self.words.append(word)
                        self.count.append(0)
                    else:
                        break

            except EOFError:
                pass

    def has_word(self, word):

        has = word in self.words
        hasw = False
        index = []

        if has:
            index = self.words.index(word)
            self.count[index] += 1
        else:
            index = []
            for i, w in enumerate(self.words):
                tem = w in word.lower()
                if tem:
                    hasw = True
                    index.append(i)

            if index:
                for i in index:
                    self.count[i] += 1

        return has or hasw
