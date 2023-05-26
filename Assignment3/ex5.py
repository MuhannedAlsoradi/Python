from collections import Counter

def replace_spaces_with_least_frequent_char(my_str):
    # Step 1: Count the frequency of each character
    char_count = Counter(my_str)

    # Step 2: Find the least frequent character
    least_frequent_char = min(char_count, key=char_count.get)

    # Step 3: Replace spaces with the least frequent character
    replaced_str = my_str.replace(' ', least_frequent_char)

    return replaced_str

# Test with the given input
my_str = 'dbc deb abed ggade'
output = replace_spaces_with_least_frequent_char(my_str)
print(output)
