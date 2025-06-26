# Name to Alphabet Number Converter

# This script converts each letter in a name to its alphabetical position (A=1, B=2, ..., Z=26).
# It demonstrates string methods, loops, and functions in Python.

def name_to_numbers(name):
    """Convert a name to a list of numbers based on alphabetical order."""
    numbers = []
    for char in name.upper():
        if char.isalpha():
            numbers.append(ord(char) - ord('A') + 1)
    return numbers

def number_to_alphabet(numbers):
    """Convert a list of numbers (1-26) to corresponding uppercase letters."""
    result = ''
    for num in numbers:
        if 1 <= num <= 26:
            result += chr(num + ord('A') - 1)
        else:
            result += '?'  # Placeholder for invalid numbers
    return result

def main():
    print("Name to Alphabet Number Converter")
    user_name = input("Enter a name: ")
    result = name_to_numbers(user_name)
    print("Alphabet positions:", result)

    # New feature: convert numbers to alphabet
    num_input = input("Enter numbers separated by spaces to convert to letters (or press Enter to skip): ")
    if num_input.strip():
        try:
            num_list = [int(n) for n in num_input.split()]
            letters = number_to_alphabet(num_list)
            print("Letters:", letters)
        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()
