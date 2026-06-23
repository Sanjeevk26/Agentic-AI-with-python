# Python Strings: Basics, Indexing, Slicing, Encoding and Decoding

## Overview

Strings are one of the most commonly used data types in Python.

A string is any text written inside quotes.

```python
chai_type = "Ginger Chai"
customer_name = "Priya"
```

Strings can contain:

* Words
* Sentences
* Numbers as text
* Special characters
* Non-English characters

## String Basics

A string can be stored in a variable.

```python
chai_type = "Ginger Chai"
customer_name = "Priya"
```

Strings can be printed using formatted strings.

```python
print(f"Order for {customer_name}: {chai_type} please!")
```

Output:

```text
Order for Priya: Ginger Chai please!
```

## Strings Are Immutable

Strings in Python are immutable.

This means once a string is created, it cannot be changed directly.

If we modify a string, Python creates a new string in memory.

## Indexing in Strings

Each character in a string has a position number called an index.

Indexing starts from `0`.

Example:

```python
chai_description = "Aromatic and bold"
```

Index positions:

```text
A r o m a t i c
0 1 2 3 4 5 6 7
```

To get a character:

```python
print(chai_description[0])
```

Output:

```text
A
```

## Slicing in Strings

Slicing is used to extract a part of a string.

Syntax:

```python
string[start:end:step]
```

Important rule:

The ending index is not included.

Example:

```python
chai_description = "Aromatic and bold"

first_word = chai_description[0:8]
print(first_word)
```

Output:

```text
Aromatic
```

Here, index `8` is not included.

## Slicing Without Start

If the start value is missing, Python starts from the beginning.

```python
first_word = chai_description[:8]
```

This gives the same result:

```text
Aromatic
```

## Slicing Without End

If the end value is missing, Python goes till the end of the string.

```python
last_word = chai_description[13:]
print(last_word)
```

Output:

```text
bold
```

## Step in Slicing

The step value decides how characters are picked.

```python
text = "Aromatic"

print(text[0:8:1])
```

Output:

```text
Aromatic
```

Step `1` means pick every character.

```python
print(text[0:8:2])
```

Output:

```text
Aoai
```

Step `2` means pick every second character.

## Reverse a String

A common Python trick to reverse a string is:

```python
reversed_text = chai_description[::-1]
print(reversed_text)
```

Output:

```text
dlob dna citamorA
```

Here, `-1` means move backward through the string.

## Encoding and Decoding Strings

Sometimes strings contain special characters or non-English characters.

Example:

```python
label_text = "Chai Spécial"
```

To safely store or transfer such text, we can encode it.

```python
encoded_label = label_text.encode("utf-8")
```

To convert it back to normal text, we decode it.

```python
decoded_label = encoded_label.decode("utf-8")
```

UTF-8 is a common encoding format used for handling text across different languages and systems.

## Key Takeaways

* Strings are text values in Python.
* Strings are written inside quotes.
* Strings are immutable.
* Indexing starts from `0`.
* Slicing extracts part of a string.
* The ending index is not included in slicing.
* `[::-1]` reverses a string.
* Encoding converts text into bytes.
* Decoding converts bytes back into text.
* UTF-8 is commonly used for special and multilingual characters.
