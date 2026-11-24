import os

# Round 2: shorter and more direct than round 1 — the friend is spoken
# to in the first five words, the payoff lands tonight, and the risk is
# priced honestly at ten minutes.
SENTENCE = (
    "That app idea you keep mentioning? Type it into make.fun in your "
    "own words — an AI agent builds a first version you can open on "
    "your phone tonight. No coding, you approve every change, and "
    "worst case you've spent ten minutes."
)


def main():
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
