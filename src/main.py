import spacy, sys
import matplotlib.pyplot as plt

def calculate_new_words(fname, use_spacy=False):
    with open(fname, 'r') as f:
        content = f.read().splitlines()
    if use_spacy:
        nlp = spacy.load("xx_ent_wiki_sm")
        for i in range(len(content)):
            doc = nlp(content[i])
            n = ""
            for t in doc:
                if (not t.is_stop) and not t.is_punct:
                    n += " " + t.lemma_
            content[i] = n

    fraction_size = len(content)//100
    last_size = len(content)-99*(len(content)//100)
    words = set()
    new_words = [0] * 100
    for i in range(100):
        new_words[i] = 0
        r_max = (i+1)*fraction_size if i < 99 else 99*fraction_size+last_size
        for row in range(i*fraction_size, r_max):
            for word in content[row].split(' '):
                if word not in words:
                    new_words[i] += 1
                    words.add(word)
    return new_words


if __name__ == "__main__":
    f = sys.argv[1]
    w = calculate_new_words(f)
    plt.plot([i+1 for i in range(0, 100)], w)
    plt.xlim([1, 100])
    plt.title("New words after completing each % of the book")
    plt.xlabel("Percentage of the book")
    plt.ylabel("Number of new words")
    plt.show()
