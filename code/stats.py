def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    count = {}
    text = text.lower()

    for char in text:
        count[char] = count.get(char, 0) + 1
    return count 

def sorted_char(count):
    items = [{"char": ch, "num": num} for ch, num in count.items()]

    def by_num(d):
        return d["num"]
    
    items.sort(key=by_num, reverse=True)
    return items

