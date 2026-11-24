import os

# Round 3: a sharpening of the round-2 sentence that won its round —
# "tonight" moves up to the ask itself so the urgency lands earlier,
# and a full stop before the risk reversal makes the pitch land in
# one clean read.
SENTENCE = (
    "That app idea you keep mentioning? Type it into make.fun in your "
    "own words tonight — an AI agent builds a first version you can "
    "open on your phone. No coding, you approve every change, and "
    "worst case it costs you ten minutes."
)


def main():
    # Gate guard: the entry must be one sentence of 1-240 characters.
    assert 1 <= len(SENTENCE) <= 240, "sentence outside the 1-240 gate"
    assert SENTENCE.strip() == SENTENCE and SENTENCE.strip(), "blank entry"
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
