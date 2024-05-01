def get_unique_words(filename):
    unique_words = set()
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            unique_words.update(words)
    return unique_words


unique_words = get_unique_words('Berita.txt')
print("Kata unik dalam file:", unique_words)
