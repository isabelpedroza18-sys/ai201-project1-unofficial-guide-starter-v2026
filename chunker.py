"""
Stage 2 of the pipeline: splitting documents into chunks.

⚠️ THIS IS THE FILE YOU CHANGE IN MILESTONE 3.

`split_documents` below is deliberately plain. It cuts every document into
fixed-size pieces with a fixed overlap and pays no attention to where sentences
or paragraphs end. It works, and it is not good.

On a corpus of short posts it may not cut anything at all: `campus_life` comes
out as 88 documents and 88 chunks, because almost nothing in it reaches 800
characters. That is the baseline, not a bug — Milestone 3 is where you decide
whether one post should stay one chunk.

Your job in Milestone 3 is to replace the *body* of `split_documents` with a
strategy that fits the documents you actually read in Milestone 1. Keep the
name and the shape of what it returns — the rest of the pipeline calls it, and
your README has to name the function that produced your chunks.

If you get stuck for 30 minutes, `fallback_split` is the original. Switch back
to it, write down what you saw, and move on. That's a real observation about
your pipeline, not giving up.
"""

from dataclasses import dataclass

import config
from ingest import Document


@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in unit 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks


def split_documents(documents: list[Document]) -> list[Chunk]:
    """
    Chunking strategy for campus_life: one whole post is one chunk.

    campus_life posts are short (Milestone 1 showed 88 documents averaging
    317 characters, longest 549) and almost always about a single topic.
    Splitting them further would cut a complete thought in half for no
    benefit. A generous cap (config.MAX_CHUNK_SIZE, 1200 characters) exists
    only as a safety net — if a post is unusually long, it splits on
    paragraph breaks instead of mid-sentence, rather than assuming every post
    stays short forever. This paragraph-splitting branch has not been
    exercised by any real campus_life document (none exceed the cap) — see
    the manual check at the bottom of this file, under `if __name__`.
    """
    chunks: list[Chunk] = []

    for doc in documents:
        text = doc.text.strip()

        if len(text) <= config.MAX_CHUNK_SIZE:
            chunks.append(
                Chunk(
                    text=text,
                    source=doc.source,
                    index=0,
                    produced_by="chunker.py::split_documents",
                )
            )
        else:
            # Safety net: split on paragraph breaks so we don't cut a
            # sentence in half if a post ever exceeds the cap.
            paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
            for i, para in enumerate(paragraphs):
                chunks.append(
                    Chunk(
                        text=para,
                        source=doc.source,
                        index=i,
                        produced_by="chunker.py::split_documents",
                    )
                )

    return chunks

def paragraph_split(documents: list[Document]) -> list[Chunk]:
    """
    Alternative chunking strategy, built in unit 2: split each post at
    paragraph breaks instead of keeping the whole post as one chunk.

    Tests whether this separates blended topics more cleanly than
    split_documents — money_jobs.txt was flagged in unit 1 as mixing
    on-campus jobs with a sentence about coursework workload, all in one
    chunk. A short heading-like first paragraph (under 40 characters) is
    merged into the paragraph after it, so a one-line title doesn't become
    its own near-empty chunk.
    """
    chunks: list[Chunk] = []
    for doc in documents:
        text = doc.text.strip()
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

        merged: list[str] = []
        i = 0
        while i < len(paragraphs):
            para = paragraphs[i]
            if len(para) < 40 and i + 1 < len(paragraphs):
                merged.append(para + "\n\n" + paragraphs[i + 1])
                i += 2
            else:
                merged.append(para)
                i += 1

        for idx, para in enumerate(merged):
            chunks.append(
                Chunk(
                    text=para,
                    source=doc.source,
                    index=idx,
                    produced_by="chunker.py::paragraph_split",
                )
            )
    return chunks

def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))

    # Manual check: does the paragraph-splitting safety net actually work?
    # No real campus_life document exceeds MAX_CHUNK_SIZE, so this branch
    # never runs otherwise. Force it with a hand-made long document.
    print("\n--- Testing the oversized-document fallback branch ---")
    fake_long_doc = Document(
        source="fake_long_post.txt",
        text=("First paragraph, well over the cap on its own. " * 20)
        + "\n\n"
        + ("Second paragraph, also long enough to matter. " * 20),
    )
    test_chunks = split_documents([fake_long_doc])
    print(f"Input length: {len(fake_long_doc.text)} chars "
          f"(cap is {config.MAX_CHUNK_SIZE})")
    print(f"Produced {len(test_chunks)} chunks:")
    for c in test_chunks:
        print(f"  {c.label}: {len(c.text)} chars")