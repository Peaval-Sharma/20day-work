# 📊 File Statistics Program

A simple Python program that reads a text file and calculates the **number of lines, words, and characters** present in the file.

## 🎯 Objective

The objective of this program is to practice:

* File handling in Python
* Reading files using `open()`
* Using `with open()`
* Counting lines, words, and characters
* Exception handling using `try-except`

## 🛠️ Technologies Used

* **Python 3**
* File Handling
* Exception Handling

## 📌 Features

* Takes the file name from the user.
* Opens the file in read mode.
* Counts the total number of lines.
* Counts the total number of words.
* Counts the total number of characters.
* Handles missing files using `FileNotFoundError`.
* Handles other unexpected errors using `Exception`.

## 💻 Program

```python
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
```

## ▶️ How to Run

### Step 1: Create a Python file

Save the program as:

```text
file_statistics.py
```

### Step 2: Create a text file

For example:

```text
data.txt
```

Add some text inside the file.

### Step 3: Run the program

Open the terminal in the same folder and type:

```bash
python file_statistics.py
```

### Step 4: Enter the file name

```text
Enter file name: data.txt
```

## 🧪 Example Output

```text
Enter file name: data.txt

--- File Statistics ---
Number of lines     : 3
Number of words     : 12
Number of characters: 68
```

> **Note:** The exact character count depends on the content of your file. Spaces and newline characters are also counted as characters.

## 🔍 Concepts Used

### 1. `open()`

Used to open a file.

```python
open(filename, "r")
```

`"r"` means the file is opened in **read mode**.

### 2. `with open()`

```python
with open(filename, "r") as file:
```

It automatically closes the file after the operation is completed.

### 3. `split()`

```python
line.split()
```

Splits a line into words.

### 4. `len()`

Used to count the number of items.

```python
len(line.split())
```

Counts words, while:

```python
len(line)
```

Counts characters in the line.

### 5. Exception Handling

The program handles errors using:

```python
except FileNotFoundError:
```

and:

```python
except Exception as e:
```

This prevents the program from crashing when an error occurs.

## 📚 Learning Outcome

After completing this program, you will understand:

* How to read a text file in Python
* How to process file contents line by line
* How to count lines, words, and characters
* How to handle file-related errors
* How to use exception handling in real programs

## 👨‍💻 Author

**praval
**

---

⭐ If you found this project useful, consider giving the repository a star!
