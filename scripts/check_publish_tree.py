#!/usr/bin/env python3
"""Check this draft's explicit publication boundary; never publish or modify files."""

from pathlib import Path
import re
import sys
import hashlib
from urllib.parse import parse_qsl, urlsplit


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "release-files.txt"
ALLOWED_SUFFIXES = {".md", ".json", ".txt", ".py", ".svg", ".mmd", ".yml", ".yaml"}
BLOCKED_PARTS = {"private", "raw", "downloads", "notion-exports", "media-audit"}

# Exact selected course assets and source pages, not a blanket exemption.
AUTHORIZED_COURSE_IMAGES = {'assets/course-examples/07-photo-text-before.png': 'beba32fca9808fed7da3c27cedbf8aab57b60ff7cc5bddabc6845d09b4b24197',
 'assets/course-examples/07-photo-text-overlay.png': 'b8b98017641e1b4b66f25ffdf567c34086ef7fede65453b31bebe6eff154e514',
 'assets/course-examples/07-upload-after.png': '7b4efe883b6da7f75837746435e23d687798d169867827e91121034f38dc1f2f',
 'assets/course-examples/07-upload-before.png': '4c70d65fffd697041491a726ff984119d6c205988b9fcfd4855df79fd7ec4f4b',
 'assets/course-examples/08-borders-after.png': '9aa61c2cfd7cb229c1ffb39115770ea500a37ea438e45d989aef24c8d7bc9a7f',
 'assets/course-examples/08-borders-before.png': '2e080910f4ace7e1eaaca585c24f9bc8c715acb3dd6b4e20e03dc4e7adfcee95',
 'assets/course-examples/08-empty-after.png': '2f068e8d52ecfbf131acc2226de26ac2a1d706144765e53ac90bc00f79b3717d',
 'assets/course-examples/08-empty-before.png': 'f0339a0f4f22c98b58a1bfe0c2b95914609b962f5425725310733ae1077d6ec4',
 'assets/course-examples/ch01-feature.png': '12bdd3190b3fe8820cf172ede2c04c214e582ec06f1782c65a89b2a743a668a9',
 'assets/course-examples/ch01-iteration.png': '2070090c24724448869c6fe5d4f9a034ae7ec23355c74220bd63e95439a2d057',
 'assets/course-examples/ch01-layout-choices.png': '8dad04b3631009e96c24360f07060c33fd886a68cdf0fc7c529f22f506e26e18',
 'assets/course-examples/ch02-hierarchy-after.png': '2fe8e3e902395821363ffb0f3103ab294651a3b60426a68603cb9984edaa3a8e',
 'assets/course-examples/ch02-hierarchy-before.png': '3ef677fc2929bc44850abcd17a37c5d4d16aedae5b0860e854f563f3c78f0e57',
 'assets/course-examples/ch03-spacing-after.png': '6c29c681b7644f87b14f9d8b9ae5b020a1511b48a4e6a7f1484c3b12a6787a3b',
 'assets/course-examples/ch03-spacing.png': 'b59c49037b23a15027aa80f79c223f61d61f0deadb33361dcf08e35e75ab0355',
 'assets/course-examples/ch03-width-after.png': 'c2f2007784a48c99d255b4e35cae463a1324978a5e9aed8ad0d884b93644a879',
 'assets/course-examples/ch03-width-before.png': '03feca102444ca50a5ebe486695a3291424f73f2d5a4635d5182b3f0fc0076a3',
 'assets/course-ref-ui/color-and-direction.png': '0e6ecffe36934efd50ff5c1887c2e288d84706b941e159c4710131c383e18210',
 'assets/course-ref-ui/color-only-chart.png': 'aeeee1ace1e482d45dde826a91e9577d14da465b01002ef2b67de5c29e1238e3',
 'assets/course-ref-ui/reading-width-45-55.png': 'cfe3541e086927138f9aabe9db78193abde9214c0f2bb6edfe4211e762bd0486',
 'assets/course-ref-ui/reading-width-55-75.png': '2fc0a61d0764575b5607d074e4c04792daec8bc14357e79bc745c6d778e33bfb',
 'assets/course-ref-ui/shadow-button-comparison.png': '23ea20b90ef5e4b202ae81667ed3149efd5f3fb30755c9b965942ddb2ea0a22d',
 'assets/course-ref-ui/shadow-height-diagram.png': '61f319269d5c2f81b129d2213520c6d373a246b1741585fbd58497edaa432fee'}
AUTHORIZED_NOTION_PAGES = ('226886bc60ff81038183c9e2df0070a4',
 '226886bc60ff8118a0dafdf98c4a9180',
 '226886bc60ff8132bb93f7b13fd24284',
 '226886bc60ff8158b4a5e17a99089c8d',
 '226886bc60ff8161b76bcbb97a54288c',
 '226886bc60ff816ab5f3fdf71d91d18f',
 '226886bc60ff8192b8b7f384a7340a10',
 '226886bc60ff819380c8dbb868cda8ed',
 '226886bc60ff819db46cf4740e7a5632',
 '226886bc60ff81c88a58eb4bd0948b1a',
 '226886bc60ff81cc837fd7c33926663a',
 '226886bc60ff81cf96e3df611fbbcb7d')
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
        if path.suffix.lower() == ".png":
            raw = path.read_bytes()
            expected = AUTHORIZED_COURSE_IMAGES.get(rel.as_posix())
            if expected is None or not raw.startswith(b"\x89PNG\r\n\x1a\n") or hashlib.sha256(raw).hexdigest() != expected:
                errors.append(f"Unapproved or changed course image: {rel}")
            continue
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
        for match in re.finditer(r"(?:notion\.so|app\.notion\.com)/[^\s]*?([0-9a-f]{32})", body, re.I):
            if match.group(1).lower() not in AUTHORIZED_NOTION_PAGES:
                errors.append(f"Unapproved Notion page locator: {rel}")
        # A small set of recognizable credential shapes; this is not a complete secret scanner.
        secret_patterns = (r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
                           r"\bgh[pousr]_[A-Za-z0-9_]{30,}\b", r"\bAKIA[0-9A-Z]{16}\b")
        if any(re.search(pattern, body) for pattern in secret_patterns):
            errors.append(f"Credential-like value: {rel}")

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
