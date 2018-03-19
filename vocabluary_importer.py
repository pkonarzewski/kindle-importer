"""
Import words from Kindle.
"""
import os
import codecs
import sqlite3

db_path = './data/vocabulary/vocab.db'
out_path = './data/Slowka z Kindla.md'

query = """
SELECT stem, "usage"
FROM WORDS AS w
    LEFT JOIN LOOKUPS AS l
        ON l.word_key = w.id
"""

try:
    # Init connection
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    with codecs.open(out_path, mode='w') as f:
        f.write('## Słówka\n')

        for row in c.execute(query):
            f.write('* **{}** - {}\n'.format(row[0], row[1]))
        f.write('\n')

finally:
    c.close()
