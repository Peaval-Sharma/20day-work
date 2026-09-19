try:
    filename = input("Enter file name: ")

    with open(filename, "r") as file:
        line_count = 0
        word_count = 0
        char_count = 0

        for line in file:
            line_count += 1
            word_count += len(line.split())
            char_count += len(line)

    print("\n--- File Statistics ---")
    print("Number of lines     :", line_count)
    print("Number of words     :", word_count)
    print("Number of characters:", char_count)

except FileNotFoundError:
    print("Error: File not found.")

except Exception as e:
    print("An error occurred:", e)