def analyze_data(data):
    numbers = list(filter(lambda x: isinstance(x, (int, float)), data))
    strings = list(filter(lambda x: isinstance(x, str), data))
    tuples = list(filter(lambda x: isinstance(x, tuple), data))

    max_number = max(numbers) if numbers else None

    longest_string = max(strings, key=len) if strings else None

    largest_tuple = max(tuples, key=len) if tuples else None


    return max_number, longest_string, largest_tuple

data = [3, "fbfhgvxgbzdf", (1, 2, 3), 7.5, "zsdff", (4, 5), "rvdfvbdfb", (6, 7, 8, 9), 100, {"key": "value"}]

max_number, longest_string, largest_tuple = analyze_data(data)

print(f"Najwieksza liczba: {max_number}")
print(f"Najdluzszy napis: {longest_string}")
print(f"Krotka o najwiekszej liczbie elementow: {largest_tuple}")
