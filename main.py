from pathlib import Path
from shutil import copyfile


def main() -> None:
    source = Path(__file__).resolve().with_name("entry.png")
    destination = Path("/output/entry.png")
    destination.parent.mkdir(parents=True, exist_ok=True)
    copyfile(source, destination)


if __name__ == "__main__":
    main()
