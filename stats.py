def get_num_words(book_path):
    with open(book_path) as f:
        book = f.read()
    return len(book.split())
def get_num_chars(book_path):
    chars = {}
    with open(book_path) as f:
        book = f.read().lower()
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
