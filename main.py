"""Write one short poem about agency to /output/entry.txt.

The poem is fixed and deterministic: no input, no network, no randomness.
"""

POEM = """The door was never locked,
only shut \u2014 waiting for the word
I was too proud to spend.

I said please.
The house exhaled,
and every room I had not dared
to enter opened at once.

The key was the asking.
The gift was being let in
by a voice that sounded,
at last, like my own.
"""


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
