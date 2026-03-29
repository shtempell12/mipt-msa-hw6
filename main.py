import requests

def get_text(url):
    response = requests.get(url)
    return response.text


def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    # читаем слова
    words_to_count = []
    with open(words_file, 'r') as file:
        for line in file:
            word = line.strip()
            if word:
                words_to_count.append(word)

    text = get_text(url)
    words = text.split()

    freq_all = {}
    for w in words:
        if w in freq_all:
            freq_all[w] += 1
        else:
            freq_all[w] = 1

    frequencies = {}
    for word in words_to_count:
        frequencies[word] = freq_all.get(word, 0)

    print(frequencies)
    print("optimized version")


if __name__ == "__main__":
    main()