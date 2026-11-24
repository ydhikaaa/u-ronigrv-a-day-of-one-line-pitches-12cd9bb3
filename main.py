import os

# Round 4 (final): mirror the round-3 winners — a CONCRETE everyday
# idea (mum's recipe app) instead of the generic "that app idea",
# keeping the round-2 winner's bones: plain words, tonight, first
# version on your phone, no coding, ten-minute worst case.
SENTENCE = (
    "That recipe app your mum keeps asking for? Type it into make.fun "
    "in your own words tonight — an AI agent builds a first version "
    "you can open on your phone. No coding, you approve every change, "
    "and worst case it costs you ten minutes."
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
