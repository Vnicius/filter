import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('data', help='Arquivo com as contagens das palavras')
parser.add_argument('title', help='Titulo do gráfico')
args = parser.parse_args()

image_name = args.title.lower().replace(' ', '_') + '.png'
words_freq = []
words = []
freq = []

plt.rcdefaults()
fig, ax = plt.subplots(figsize=(20, 10))

def read_words(data):
    with open(data, 'r') as words_file:
        try:
            while True:
                line = words_file.readline().replace('\n','')
                word, freq = line.split(' - ')
                yield (word, freq)
        except EOFError:
            pass
        except ValueError:
            pass

for w, f in read_words(args.data):
    words_freq.append((w, int(f)))

words_freq = sorted(words_freq, key=lambda x: x[0])
words = [wf[0] for wf in words_freq]
freq = [wf[1] for wf in words_freq]
position = np.arange(len(words))

ax.barh(position, freq, color='green')
ax.set_yticks(position)
ax.set_yticklabels(words)
ax.invert_yaxis()
ax.set_xlabel('Ocorrências')
ax.set_title(args.title)

for i, v in enumerate(freq):
    ax.text(v, i, str(v), color='black', va='center')

#plt.show()
plt.savefig(image_name)