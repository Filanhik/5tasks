def find_words_with_count(text, n):
    words = text.split()
    result = []
    for word in words:
        if words.count(word) == n and word not in result:
            result.append(word)
    return result