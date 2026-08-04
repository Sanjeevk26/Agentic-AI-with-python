# Build Your Own Tokenizer with tiktoken
# Topics:
# 1. Import tiktoken
# 2. Create an encoder
# 3. Encode text into tokens
# 4. Decode tokens back into text
# 5. Understand tokenization and detokenization
# -------------------------------------------------

import tiktoken


# =================================================
# 1. Create an Encoder
# =================================================

def get_encoder():
    """
    Create and return an encoder for a specific model.

    Different models can use different tokenization
    rules, so we choose the model name here.
    """

    encoder = tiktoken.encoding_for_model("gpt-4o")

    return encoder


# =================================================
# 2. Tokenize Text
# =================================================

def tokenize_text(text: str) -> list[int]:
    """
    Convert text into token IDs.
    """

    encoder = get_encoder()

    tokens = encoder.encode(text)

    return tokens


# =================================================
# 3. Detokenize Tokens
# =================================================

def detokenize_tokens(tokens: list[int]) -> str:
    """
    Convert token IDs back into readable text.
    """

    encoder = get_encoder()

    decoded_text = encoder.decode(tokens)

    return decoded_text


# =================================================
# 4. Basic Tokenization Example
# =================================================

def basic_tokenization_example() -> None:
    """
    Demonstrate basic tokenization and detokenization.
    """

    text = "Hey there, my name is Piyush Garg."

    tokens = tokenize_text(text)
    decoded_text = detokenize_tokens(tokens)

    print("\nBASIC TOKENIZATION EXAMPLE")
    print("-" * 50)

    print("Original text:")
    print(text)

    print("\nTokens:")
    print(tokens)

    print("\nDecoded text:")
    print(decoded_text)


# =================================================
# 5. Show Token Count
# =================================================

def token_count_example() -> None:
    """
    Show how many tokens are created from a sentence.
    """

    text = "LLMs do not directly understand text. They process tokens."

    tokens = tokenize_text(text)

    print("\nTOKEN COUNT EXAMPLE")
    print("-" * 50)

    print("Text:")
    print(text)

    print("\nTokens:")
    print(tokens)

    print("\nNumber of tokens:")
    print(len(tokens))


# =================================================
# 6. Compare Different Texts
# =================================================

def compare_texts_example() -> None:
    """
    Compare tokenization for different text inputs.
    """

    examples = [
        "Hi",
        "Hello",
        "Hey there",
        "My name is Piyush Garg.",
        "Tokenization converts text into numbers.",
    ]

    print("\nCOMPARE DIFFERENT TEXTS")
    print("-" * 50)

    for text in examples:
        tokens = tokenize_text(text)

        print(f"\nText: {text}")
        print(f"Tokens: {tokens}")
        print(f"Token count: {len(tokens)}")


# =================================================
# 7. Decode Hardcoded Tokens
# =================================================

def decode_hardcoded_tokens_example() -> None:
    """
    Decode an existing list of token IDs.

    Note:
    These token IDs depend on the selected tokenizer.
    """

    text = "Hey there, my name is Piyush Garg."

    tokens = tokenize_text(text)

    decoded_text = detokenize_tokens(tokens)

    print("\nDECODE HARDCODED TOKENS")
    print("-" * 50)

    print("Tokens:")
    print(tokens)

    print("\nDecoded text:")
    print(decoded_text)


# =================================================
# 8. Simulated LLM Flow
# =================================================

def simulated_llm_flow_example() -> None:
    """
    Simulate the high-level LLM flow.

    This does not predict new tokens like a real LLM.
    It only shows where tokenization and detokenization
    fit in the process.
    """

    user_input = "Hey there"

    input_tokens = tokenize_text(user_input)

    # In a real LLM, the model would predict these.
    # Here we manually use another small text to simulate
    # generated output.
    generated_text = ", I am good."

    generated_tokens = tokenize_text(generated_text)

    final_tokens = input_tokens + generated_tokens

    final_text = detokenize_tokens(final_tokens)

    print("\nSIMULATED LLM FLOW")
    print("-" * 50)

    print("User input:")
    print(user_input)

    print("\nInput tokens:")
    print(input_tokens)

    print("\nGenerated tokens:")
    print(generated_tokens)

    print("\nFinal tokens:")
    print(final_tokens)

    print("\nFinal decoded text:")
    print(final_text)


# =================================================
# 9. Main Program
# =================================================

def main() -> None:
    """
    Run all tokenizer examples.
    """

    print("Build Your Own Tokenizer with tiktoken")
    print("=" * 50)

    basic_tokenization_example()
    token_count_example()
    compare_texts_example()
    decode_hardcoded_tokens_example()
    simulated_llm_flow_example()


if __name__ == "__main__":
    main()


# =================================================
# Setup Commands
# =================================================

# Create project folder:
#
# mkdir 01_tokenization
# cd 01_tokenization
#
#
# Create virtual environment:
#
# python -m venv venv
#
#
# Activate on macOS/Linux:
#
# source venv/bin/activate
#
#
# Activate on Windows:
#
# venv\Scripts\activate
#
#
# Install tiktoken:
#
# pip install tiktoken
#
#
# Save dependencies:
#
# pip freeze > requirements.txt
#
#
# Run this file:
#
# python main.py
#
#
# =================================================
# Notes
# =================================================

# tiktoken:
# A Python package used for tokenization.
#
#
# Encoder:
#
# encoder = tiktoken.encoding_for_model("gpt-4o")
#
#
# Encode:
#
# tokens = encoder.encode(text)
#
# Converts text into token IDs.
#
#
# Decode:
#
# decoded_text = encoder.decode(tokens)
#
# Converts token IDs back into text.
#
#
# Tokenization:
# Text -> token IDs
#
#
# Detokenization:
# Token IDs -> text
#
#
# Important:
# Different models may use different tokenization
# rules, so the same sentence may produce different
# token IDs depending on the model.
