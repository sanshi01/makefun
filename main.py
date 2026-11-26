"""Copy entry.png to /output and verify that the file sizes match."""

from pathlib import Path
from shutil import copyfile


def main() -> None:
    source = Path(__file__).resolve().with_name("entry.png")
    destination = Path("/output/entry.png")
    destination.parent.mkdir(exist_ok=True)
    copyfile(source, destination)

    source_size = source.stat().st_size
    destination_size = destination.stat().st_size
    if destination_size != source_size:
        raise SystemExit(
            f"Size check failed for {destination}: "
            f"expected {source_size} bytes, found {destination_size} bytes."
        )
    print(f"Copied {destination} and verified its size ({destination_size} bytes).")


if __name__ == "__main__":
    main()
