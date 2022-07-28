import random

num1k_2k = random.randint(1000, 2000)

# fmt: off
def split_lines(text):
    lines = text.split("\n")
    for l in enumerate(lines):
        print(l)


def A44():
    # A44"
    text = (
            "line1" "\n"
            f"line2 with number: {num1k_2k}"
)
    split_lines(text)

A44()
