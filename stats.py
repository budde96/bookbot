def get_num_words(book):
    return len(book.split())
def get_num_chars(book):
    chars = {}
    for text in book:
        if text in chars:
            chars[text] += 1
        else:
            chars[text] = 1
    return chars
def sort_on(d):
    return d["amount"]
def sort_chars(num_chars):
    sorted_chars = []
    for char in num_chars:
        sorted_chars.append({"char": char, "amount": num_chars[char]})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars
