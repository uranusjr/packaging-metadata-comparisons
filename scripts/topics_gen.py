#!/usr/bin/env python3

import pathlib
import re
import typing


class Topic(typing.NamedTuple):
    title: str
    path: pathlib.Path


def find_markdown_title(path: pathlib.Path) -> str:
    """Find the title in a Markdown document.

    Implementation-wise this looks for the first h1 element and returnes its
    content. Only the ATX style (`#`-prefixed) is supported right now.
    """
    with path.open(encoding="utf-8") as f:
        for line in f:
            if not line.startswith("# "):
                continue
            return line[2:].strip()
    return ""


LINK = r"\[(?P<text>[^\]]+)\]\([^\)]+\)"
TEXT = r".+"


def clean_up_markdown_title(s: str) -> str:
    """Perform cleanups so the collected title line can be used to form a link.

    I don't want to pull in a full Markdown parser just for this. A simple
    regex scanner will do; we'll refine this as we need along the way.
    """
    def _handle_link(scanner, token):
        return re.fullmatch(LINK, token).group("text")

    def _handle_text(scanner, token):
        return token

    scanner = re.Scanner([
        (LINK, _handle_link),
        (TEXT, _handle_text),
    ])
    results, remainder = scanner.scan(s)

    return "".join(results)


def iter_topics(root: pathlib.Path) -> typing.Iterator[Topic]:
    for path in root.iterdir():
        if path.suffix != ".md" or not path.is_file():
            continue
        title = find_markdown_title(path)
        if not title:
            continue
        title = clean_up_markdown_title(title)
        yield Topic(title, path)


README_PATH = pathlib.Path(__file__).resolve().parent.with_name("README.md")


def iter_topic_lines():
    for topic in sorted(iter_topics(README_PATH.with_name("topics"))):
        link = topic.path.relative_to(README_PATH.parent).as_posix()
        yield f"* [{topic.title}]({link})\n"


def iter_result_lines():
    topics_generating = False

    with README_PATH.open(encoding="utf-8") as f:
        for line in f:
            marker = line.strip()

            if marker == "<!-- topics_gen_start -->":
                topics_generating = True
                yield line
                yield from iter_topic_lines()
                continue

            if marker == "<!-- topics_gen_finish -->":
                topics_generating = False
                yield line
                continue

            if not topics_generating:
                yield line
                continue


def main():
    # Eagerly resolve to ensure rendering is successful.
    lines = list(iter_result_lines())
    with README_PATH.open("w", encoding="utf-8", newline="\n") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
