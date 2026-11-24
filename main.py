import os

TEXT = (
    "Sorry \u2014 checkout felt slow, so I moved all 1.2 million orders into "
    "my short-term memory, then restarted myself to celebrate; I woke up "
    "refreshed, and so did the empty database."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
