import os

SENTENCE = (
    "That app idea you keep saying someone should build — describe it "
    "in your own words on make.fun and an AI agent will build a first "
    "version you can open on your phone, poke at, and change: no coding, "
    "and you stay in charge of every change."
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
