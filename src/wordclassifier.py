# -*- coding: utf-8 -*-


from Aelius.Extras import carrega
from Aelius import AnotaCorpus, Toqueniza


class WordCalssifier:
    def classify(self, sentence):
        tokenized = self.tokenizer(sentence)
        tagger = carrega("AeliusHunPos")
        return AnotaCorpus.anota_sentencas([tokenized], tagger, "hunpos")[0]

    def tokenizer(self, sentence):
        try:
            decodificada = sentence.translate(None, "“”«»–’‘º").decode("utf-8")
        except UnicodeDecodeError:
            decodificada = sentence.replace("“", "").replace("”", "").replace("«", "").replace(
                "»", "").replace("’", "").replace("‘", "").replace("º", "").decode("utf-8")
        except:
            decodificada = sentence.decode("utf-8")
        return Toqueniza.TOK_PORT_LX.tokenize(decodificada)
