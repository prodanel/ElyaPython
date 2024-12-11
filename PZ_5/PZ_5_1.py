def horizontal_line(length, character='-'):
    return character * length
def vertical_line(length, character='|'):
    return [character for _ in range(length)]
def print_word_in_frame(word):
    frame_length = len(word) + 4
    top_bottom_line = horizontal_line(frame_length)
    print(top_bottom_line)
    print(f"| {word} |")
    print(top_bottom_line)
print_word_in_frame("Привет")





