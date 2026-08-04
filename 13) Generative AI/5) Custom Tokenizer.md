# Build Your Own Tokenizer with `tiktoken`

## Overview

In this lesson, we build a simple tokenizer and detokenizer using Python.

We use the `tiktoken` package, which helps us convert text into tokens and convert tokens back into text.

This process is important because LLMs do not directly work with raw English text.

They work with tokens.

---

# 1. What We Are Building

We are building a small Python program that can:

* Take normal text input
* Convert the text into tokens
* Print the token IDs
* Decode the token IDs back into text
* Show how tokenization and detokenization work

---

# 2. Project Folder

Create a folder:

```text
01_tokenization
```

Inside it, create a Python file:

```text
main.py
```

Final structure:

```text
01_tokenization/
│
├── main.py
└── requirements.txt
```

---

# 3. Create a Virtual Environment

A virtual environment keeps project dependencies separate from the global Python installation.

Run:

```bash
python -m venv venv
```

This creates a folder named:

```text
venv
```

---

# 4. Activate the Virtual Environment

## macOS / Linux

```bash
source venv/bin/activate
```

## Windows

```bash
venv\Scripts\activate
```

After activation, the terminal usually shows something like:

```text
(venv)
```

This means the virtual environment is active.

---

# 5. Install `tiktoken`

Install the tokenizer package:

```bash
pip install tiktoken
```

Important spelling:

```text
Package name: tiktoken
Import name: tiktoken
```

Not:

```text
tick token
```

---

# 6. Save Dependencies

After installing the package, create a `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

This saves all installed packages into:

```text
requirements.txt
```

Later, someone else can install the same dependencies using:

```bash
pip install -r requirements.txt
```

---

# 7. Import `tiktoken`

In `main.py`, import the package:

```python
import tiktoken
```

---

# 8. Create an Encoder

To tokenize text, first create an encoder for a specific model.

Example:

```python
encoder = tiktoken.encoding_for_model("gpt-4o")
```

This creates a tokenizer suitable for the selected model.

Different models may use different tokenization rules.

---

# 9. Text to Tokenize

Create a text variable:

```python
text = "Hey there, my name is Piyush Garg."
```

This is the text we want to tokenize.

---

# 10. Encode Text into Tokens

Use:

```python
tokens = encoder.encode(text)
```

This converts the text into token IDs.

Example output may look like:

```python
[10850, 1354, 11, 922, 1308, 382, 543, 1518, 182942, 13]
```

The exact token IDs can vary depending on the model and tokenizer.

---

# 11. Print Tokens

```python
print("Tokens:", tokens)
```

This prints the tokenized form of the text.

The text:

```text
Hey there, my name is Piyush Garg.
```

becomes a list of numbers.

These numbers are what the model can process.

---

# 12. Decode Tokens Back into Text

To convert token IDs back into text, use:

```python
decoded_text = encoder.decode(tokens)
```

This is called detokenization.

It converts the tokens back into human-readable text.

---

# 13. Print Decoded Text

```python
print("Decoded text:", decoded_text)
```

The output should be close to the original text:

```text
Hey there, my name is Piyush Garg.
```

---

# 14. Tokenization and Detokenization Flow

```text
Original text
     ↓
Tokenization
     ↓
Token IDs
     ↓
Sent to LLM
     ↓
LLM predicts next token IDs
     ↓
Detokenization
     ↓
Readable response
```

---

# 15. Complete Concept

When we send text to an LLM:

```text
Hey there
```

The text is first converted into tokens.

Example:

```text
Hey there → [token IDs]
```

These token IDs are passed to the model.

The model predicts the next token.

Then the new token is added to the sequence.

This process repeats until the full response is generated.

Finally, the generated tokens are decoded back into text.

---

# 16. Encode vs Decode

| Method     | Meaning                           |
| ---------- | --------------------------------- |
| `encode()` | Converts text into token IDs      |
| `decode()` | Converts token IDs back into text |

Example:

```python
tokens = encoder.encode(text)
decoded_text = encoder.decode(tokens)
```

---

# 17. Running the File

From inside the project folder, run:

```bash
python main.py
```

Example output:

```text
Original text: Hey there, my name is Piyush Garg.
Tokens: [10850, 1354, 11, 922, 1308, 382, 543, 1518, 182942, 13]
Decoded text: Hey there, my name is Piyush Garg.
```

The token IDs may be different depending on the model and tokenizer version.

---

# 18. Why This Matters

Tokenization is one of the first steps in how LLMs work.

LLMs do not directly process text like humans do.

They process numerical token IDs.

So this:

```text
Hey there, my name is Piyush Garg.
```

becomes something like:

```text
[10850, 1354, 11, 922, ...]
```

The model then uses these numbers to predict the next token.

---

# 19. Important Reminder

Every model may have its own tokenizer.

The same text may produce different tokens for different models.

For example:

```python
tiktoken.encoding_for_model("gpt-4o")
```

may tokenize differently from another model tokenizer.

So tokenization is model-specific.

---

# Key Takeaways

* Tokenization converts text into token IDs.
* Detokenization converts token IDs back into readable text.
* LLMs process token IDs, not raw text directly.
* `tiktoken` can be used to tokenize text in Python.
* `encoder.encode(text)` converts text into tokens.
* `encoder.decode(tokens)` converts tokens back into text.
* Different models may tokenize the same text differently.
* Tokenization is a key step in understanding how LLMs work.
