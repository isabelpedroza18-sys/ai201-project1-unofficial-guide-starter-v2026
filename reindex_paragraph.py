"""
Unit 2 improvement: index the corpus a second way, using paragraph_split
instead of split_documents, into a separate variant ("paragraph") so both
can be queried side by side without deleting either one.

Run this once after adding paragraph_split to chunker.py:

    python reindex_paragraph.py

Then compare the two variants with the normal commands:

    python app.py --variant paragraph retrieve "Can I study during my on-campus job?"
    python app.py --variant default   retrieve "Can I study during my on-campus job?"
"""

import time

import config
from ingest import load_documents, describe as describe_docs
from chunker import paragraph_split, describe as describe_chunks
from store import build_index

corpus = config.CORPUS
print(f"Corpus: {corpus}")

started = time.time()

documents = load_documents(corpus)
print(f"  loaded   {describe_docs(documents)}")

chunks = paragraph_split(documents)
print(f"  chunked  {describe_chunks(chunks)}")

print(f"  embedding {len(chunks)} chunks...")
count = build_index(chunks, corpus=corpus, variant="paragraph")

elapsed = time.time() - started
print(f"  stored   {count} chunks in {elapsed:.1f}s, variant='paragraph'")
