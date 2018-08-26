# -*- coding: utf-8 -*-

'''
  @author: Vinicius Verissimo
  @email: vinicius.matheus@lavid.ufpb.br
'''

from wordclassifier import WordCalssifier


class FilterApplier:
    def __init__(self, filters_list):
        self.filters_list = filters_list
        self.classifier = WordCalssifier()

    def filter(self, file_source):
        filtred_sentences = []
        with open(file_source, 'r') as source:
            try:
                while True:
                    sentence = source.readline().replace('\n', '')
                    filtred = False
                    if sentence:
                        for word in sentence.split(' '):
                            if self.has_word(word.lower()):
                                # print(self.classifier.classify(sentence))
                                filtred = True

                        if filtred:
                            filtred_sentences.append(sentence)
                    else:
                        break
            except EOFError:
                pass

        return filtred_sentences

    def has_word(self, word):
        for f in self.filters_list:
            if f.has_word(word):
                return True

        return False
