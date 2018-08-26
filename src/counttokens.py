import sys
import re

if __name__ == "__main__":
    file_name = sys.argv[1]
    acc = []
    punc = re.compile('([\.,\?!])')

    with open(file_name, 'r', encoding="utf-8") as f:
        while True:
            sentence = f.readline().replace('\n', '')
            if sentence:
                sentence = punc.sub(r' \1', sentence)
                words = sentence.split(' ')

                for word in words:
                    if not word.lower() in acc:
                        acc.append(word.lower())
            else:
                break

        print(len(acc))
