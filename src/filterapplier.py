# -*- coding: utf-8 -*-

'''
  @author: Vinicius Verissimo
  @email: vinicius.matheus@lavid.ufpb.br
'''
import re

PUNC = re.compile('([\.,\?!])')


class FilterApplier:
    def __init__(self, filters_list):
        self.filters_list = filters_list
        # self.classifier = WordCalssifier()

    def filter(self, file_source, file_prallel=""):
        filtred_sentences = []
        parallel_sentences = []

        with open(file_source, 'r') as source:
            try:
                while True:
                    parallel = ""
                    sentence = source.readline().replace('\n', '')

                    if(file_prallel):
                        parallel = file_prallel.readline().replace('\n', '')

                    filtred = False
                    if sentence:
                        for word in PUNC.sub(r' \1', sentence).split(' '):
                            if self.has_word(word.lower()):
                                # print(self.classifier.classify(sentence))
                                filtred = True

                        low = PUNC.sub(r' \1', sentence).lower()

                        if self.has_word(low):
                            filtred = True

                        if filtred:

                            filtred_sentences.append(sentence)
                            parallel_sentences.append(parallel)
                    else:
                        break
            except EOFError:
                pass

        return filtred_sentences, parallel_sentences

    def has_word(self, word):
        for f in self.filters_list:
            if f.has_word(word):
                return True

        return False

    def getCounts(self):
        for f in self.filters_list:
            file_name = f.fileName.split('/')[-1]

            with open('cont/contagem-' + file_name, 'w') as out:
                for index, value in enumerate(f.words):
                    out.write(f.words[index] +
                              " - " + str(f.count[index]) + "\n")
