"""Dad Joke Showdown entry: write one dad joke to /output/entry.txt."""

from pathlib import Path

JOKE = "My son asked why I always carry a ladder. I said, 'Son, in this family, we always take things to the next level.'"

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(JOKE) <= MAX_CHARS, "joke must be 1-200 characters"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(JOKE, encoding="utf-8")
    print(JOKE)


if __name__ == "__main__":
    main()
