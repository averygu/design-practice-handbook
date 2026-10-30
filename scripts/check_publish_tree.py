#!/usr/bin/env python3
"""Check this draft's explicit publication boundary; never publish or modify files."""

from pathlib import Path
import re
import sys
from urllib.parse import parse_qsl, urlsplit


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "release-files.txt"
ALLOWED_SUFFIXES = {".md", ".json", ".txt", ".py", ".svg", ".mmd", ".yml", ".yaml"}
BLOCKED_PARTS = {"private", "raw", "downloads", "notion-exports", "media-audit"}
AUTH_QUERY_KEYS = {
    "token", "access_token", "auth", "authorization", "signature", "sig",
    "x-amz-signature", "x-amz-credential", "x-amz-security-token",
    "x-goog-signature", "x-goog-credential", "key-pair-id", "policy",
}


def main():
    errors = []
    if not MANIFEST.is_file():
        print("Missing release-files.txt")
        return 1

    declared = [line.strip() for line in MANIFEST.read_text().splitlines()
                if line.strip() and not line.lstrip().startswith("#")]
    if len(declared) != len(set(declared)):
        errors.append("Release list contains duplicate paths")
    allowlist = set(declared)

    for rel in allowlist:
        p = Path(rel)
        if p.is_absolute() or ".." in p.parts:
            errors.append(f"Invalid release path: {rel}")

    actual = set()
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if ".git" in rel.parts:
            continue
        if path.is_symlink():
            errors.append(f"Symlink excluded from publication: {rel}")
            continue
        if not path.is_file():
            continue
        actual.add(rel.as_posix())
        if BLOCKED_PARTS.intersection(rel.parts) or ".private." in path.name:
            errors.append(f"Private or raw path: {rel}")
        if path.name != ".gitignore" and path.suffix not in ALLOWED_SUFFIXES:
            errors.append(f"Unreviewed file type: {rel}")

        try:
            body = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            errors.append(f"Cannot inspect as UTF-8: {rel}")
            continue

        # Split literals so this checker does not flag its own patterns.
        personal_root = "/" + "Users/"
        if personal_root in body or "file" + "://" in body:
            errors.append(f"Local machine path in content: {rel}")
        if re.search(r"(?:notion\.so|app\.notion\.com)/[^\s]*[0-9a-f]{32}", body, re.I):
            errors.append(f"Private source-page locator requires review: {rel}")

        for url in re.findall(r"https?://[^\s<>\"`]+", body):
            try:
                query = {key.lower() for key, _ in parse_qsl(urlsplit(url).query)}
            except ValueError:
                errors.append(f"Malformed URL: {rel}")
                continue
            if query & AUTH_QUERY_KEYS:
                errors.append(f"Authorization-like URL query: {rel}")

        if path.suffix == ".md":
            # Check file targets only; anchors and external links need separate review.
            for target in re.findall(r"\]\(([^)]+)\)", body):
                target = target.split("#", 1)[0].strip("<>")
                if not target or "://" in target or target.startswith("mailto:"):
                    continue
                destination = (path.parent / target).resolve()
                if not destination.is_relative_to(ROOT):
                    errors.append(f"Link leaves publication tree: {rel}")
                elif not destination.exists():
                    errors.append(f"Missing local link target in {rel}: {target}")

    for rel in sorted(actual - allowlist):
        errors.append(f"File not on release list: {rel}")
    for rel in sorted(allowlist - actual):
        errors.append(f"Listed file missing: {rel}")

    if errors:
        print("Publication structure check failed:")
        print("\n".join(f"- {item}" for item in errors))
        return 1
    print(f"Publication structure check passed for {len(actual)} explicit files.")
    print("This does not certify privacy, originality, licensing, media coverage or content quality.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
