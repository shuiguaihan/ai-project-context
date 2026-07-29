#!/usr/bin/env python3
"""Build a read-only metadata and SHA256 inventory for project evidence files."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


DEFAULT_EXCLUDES = {".git", ".svn", "node_modules", "__pycache__"}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_files(inputs: Iterable[Path], excludes: set[str]) -> list[Path]:
    found: dict[str, Path] = {}

    def raise_walk_error(error: OSError) -> None:
        raise error

    for input_path in inputs:
        resolved = input_path.resolve(strict=True)
        if resolved.is_file():
            found[os.path.normcase(str(resolved))] = resolved
            continue
        if not resolved.is_dir():
            raise ValueError(f"Unsupported input type: {input_path}")
        for current_root, dir_names, file_names in os.walk(
            resolved, followlinks=False, onerror=raise_walk_error
        ):
            dir_names[:] = sorted(
                name for name in dir_names if name not in excludes
            )
            root_path = Path(current_root)
            for name in sorted(file_names):
                candidate = root_path / name
                if candidate.is_symlink() or not candidate.is_file():
                    continue
                candidate = candidate.resolve(strict=True)
                found[os.path.normcase(str(candidate))] = candidate
    return sorted(found.values(), key=lambda item: str(item).casefold())


def display_path(path: Path, root: Path | None) -> str:
    if root is not None:
        try:
            return path.relative_to(root).as_posix()
        except ValueError:
            pass
    return str(path)


def build_inventory(
    files: list[Path], root: Path | None, received_date: str | None, source: str | None
) -> dict[str, object]:
    records: list[dict[str, object]] = []
    for path in files:
        stat = path.stat()
        records.append(
            {
                "path": display_path(path, root),
                "name": path.name,
                "extension": path.suffix.lower(),
                "size_bytes": stat.st_size,
                "modified_utc": datetime.fromtimestamp(
                    stat.st_mtime, timezone.utc
                ).isoformat(),
                "sha256": sha256_file(path),
            }
        )
    return {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "root": str(root) if root else None,
        "received_date": received_date,
        "source": source,
        "file_count": len(records),
        "files": records,
    }


def escape_markdown(value: object) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace(
        "\n", " "
    )


def render_markdown(inventory: dict[str, object]) -> str:
    lines = [
        "# Evidence Inventory",
        "",
        f"- Generated (UTC): {inventory['generated_at_utc']}",
        f"- Root: {inventory['root'] or ''}",
        f"- Received date: {inventory['received_date'] or ''}",
        f"- Source: {inventory['source'] or ''}",
        f"- File count: {inventory['file_count']}",
        "",
        "| Path | Size (bytes) | Modified (UTC) | SHA256 |",
        "| --- | ---: | --- | --- |",
    ]
    for record in inventory["files"]:
        assert isinstance(record, dict)
        lines.append(
            "| {path} | {size_bytes} | {modified_utc} | `{sha256}` |".format(
                **{key: escape_markdown(value) for key, value in record.items()}
            )
        )
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Inventory exact project evidence files or directories. The command is "
            "read-only unless --output names a file that does not yet exist."
        )
    )
    parser.add_argument("paths", nargs="+", type=Path, help="Files or directories")
    parser.add_argument(
        "--root", type=Path, help="Render paths relative to this project root when possible"
    )
    parser.add_argument(
        "--format", choices=("json", "markdown"), default="json", help="Output format"
    )
    parser.add_argument("--received-date", help="Project received date, usually YYYY-MM-DD")
    parser.add_argument("--source", help="Sender, system, or evidence source description")
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Additional directory name to exclude; may be repeated",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Write to a new file; existing files are never overwritten",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        root = args.root.resolve(strict=True) if args.root else None
        if root is not None and not root.is_dir():
            raise ValueError(f"Root is not a directory: {args.root}")
        files = iter_files(args.paths, DEFAULT_EXCLUDES | set(args.exclude))
        inventory = build_inventory(files, root, args.received_date, args.source)
        rendered = (
            json.dumps(inventory, ensure_ascii=False, indent=2) + "\n"
            if args.format == "json"
            else render_markdown(inventory)
        )
        if args.output:
            output = args.output.resolve(strict=False)
            output.parent.mkdir(parents=True, exist_ok=True)
            with output.open("x", encoding="utf-8", newline="\n") as handle:
                handle.write(rendered)
        else:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stdout.write(rendered)
        return 0
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
