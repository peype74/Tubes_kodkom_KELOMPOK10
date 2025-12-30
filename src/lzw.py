def lzw_compress(text):
    dictionary = {chr(i): i for i in range(256)}
    current_string = ""
    result = []
    dict_size = 256

    for char in text:
        combined = current_string + char
        if combined in dictionary:
            current_string = combined
        else:
            result.append(dictionary[current_string])
            dictionary[combined] = dict_size
            dict_size += 1
            current_string = char

    if current_string:
        result.append(dictionary[current_string])

    return result
