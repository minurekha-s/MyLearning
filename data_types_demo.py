# Data Types Demo: Tuples, Sets, Lists, and Dictionaries

# This script demonstrates how to use different data types in Python.

def demo_tuples():
    print("\nTuple Example:")
    my_tuple = (1, 2, 3, "apple")
    print("Tuple:", my_tuple)
    print("First element:", my_tuple[0])
    print("Length:", len(my_tuple))


def demo_sets():
    print("\nSet Example:")
    my_set = {1, 2, 3, 2, 1}
    print("Set (no duplicates):", my_set)
    my_set.add(4)
    print("After adding 4:", my_set)


def demo_lists():
    print("\nList Example:")
    my_list = [1, 2, 3, 2]
    print("List:", my_list)
    my_list.append(4)
    print("After appending 4:", my_list)
    print("Count of 2:", my_list.count(2))


def demo_dicts():
    print("\nDictionary Example:")
    my_dict = {"name": "Alice", "age": 25}
    print("Dictionary:", my_dict)
    print("Name:", my_dict["name"])
    my_dict["city"] = "New York"
    print("After adding city:", my_dict)


def main():
    print("Data Types Demo")
    demo_tuples()
    demo_sets()
    demo_lists()
    demo_dicts()

if __name__ == "__main__":
    main()
