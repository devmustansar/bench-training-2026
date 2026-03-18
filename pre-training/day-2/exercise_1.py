# =============================================================
# Exercise 1 — Word Frequency Counter
# =============================================================

import string

def word_frequency(text: str) -> dict[str, int]:
    cleaned = text.lower().translate(str.maketrans("", "", string.punctuation))
    words = cleaned.split()

    frequency: dict[str, int] = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

paragraph = """
Python is a powerful programming language. Python is widely used in web development,
data science, and automation. Many developers love Python because Python is easy to
read and write. The Python community is large and supportive. If you learn Python,
you open the door to machine learning, web development, and much more. Python, Python,
Python — it's everywhere in the tech world!
"""
freq = word_frequency(paragraph)

top_5 = sorted(freq.items(), key=lambda item: item[1], reverse=True)[:5]

print("Top 5 most common words:")
print(f"  {'Word':<15} {'Count':>5}")
print(f"  {'─' * 15} {'─' * 5}")
for rank, (word, count) in enumerate(top_5, start=1):
    print(f"  {rank}. {word:<13} {count:>5}")
