def titlize(sentence):
    words = sentence.split()
    new_words = []

    for word in words:
        if len(word) > 2:
            capitalized = word.capitalize()
            new_words.append(capitalized)
        else:
            new_words.append(word)

    return ' '.join(new_words)

title = 'hello world of programming'
print(titlize(title))
