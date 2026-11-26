"""Self-checkout one-liner: the till judges the basket.

Rubric (most important first):
1. Funny single-line remark from a judgmental self-checkout machine.
2. Real laugh on a single read; twist/sting a stranger gets with no context.
3. Machine voice: smug and petty about the basket and the bagging.
4. Tight: no setup padding, every word earns its place.
5. Fresh, not the self-checkout joke everyone has heard.
Gate: /output/entry.txt must be UTF-8, 1-200 chars, not only whitespace.
"""

import os

LINE = (
    "Fourteen energy drinks, one banana, and a scented candle "
    "you are bagging like evidence: I have scanned your 2 a.m. "
    "chest-pain search, and it is not in stock."
)


def validate(text):
    if not text or not text.strip():
        raise ValueError("entry is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError("entry is %d chars, over the 200-char cap" % len(text))
    words = text.split()
    if len(words) > 35:
        raise ValueError("entry is %d words, over the 35-word cap" % len(words))
    if len(words) < 5:
        raise ValueError("entry is too short to land a joke")
    return text


def main():
    line = validate(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(line)
    print("chars: %d" % len(line))


if __name__ == "__main__":
    main()
