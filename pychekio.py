# def bigger_price(limit: int, data: list[dict]) -> list[dict]:
#     """
#     Returns the TOP most expensive goods
#     """
#     sorting = sorted(data, key=lambda x: x['price'], reverse=True)
#     return sorting[:limit]
def words_order(text: str, words: list) -> bool:
    """
    Checks if the words in the given list appear in the same order in the text.
    """
    indices = []
    last_index = -1
    if words[-1] not in text:
        return False

    for word in words:
        index = text.find(word, last_index + 1)
        if index == -1:
            return False
        indices.append(index)
        last_index = index

    for i in range(len(indices) - 1):
        if indices[i] + len(words[i]) >= indices[i + 1]:
            return False

    return True

print("Example:")
print(words_order("hi world im here", ["world", "here"]))

# These "asserts" are used for self-checking
assert words_order("hi world im here", ["world", "here"]) == True
assert words_order("hi world im here", ["here", "world"]) == False
assert words_order("hi world im here", ["world"]) == True
assert words_order("hi world im here", ["world", "here", "hi"]) == False
assert words_order("hi world im here", ["world", "im", "here"]) == True
assert words_order("hi world im here", ["world", "hi", "here"]) == False
assert words_order("hi world im here", ["world", "world"]) == False
assert words_order("hi world im here", ["country", "world"]) == False
assert words_order("hi world im here", ["wo", "rld"]) == False
assert words_order("", ["world", "here"]) == False
assert words_order("hi world world im here", ["world", "world"]) == False
assert (
    words_order("hi world world im here hi world world im here", ["world", "here"])
    == True
)

print("The mission is done! Click 'Check Solution' to earn rewards!")

