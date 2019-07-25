"""
Import notes from Kindle and convert to more readable form.
"""

import re
import os
import codecs
import hashlib
import json
from datetime import datetime


class NotesParser:
    """Kindle notes parser.

    """

    separator = "=========="

    def __init__(self, file: str):
        self.file = file
        self.start_date = datetime.today()
        self.notes = self._load_notes()

    def _load_notes(self):
        """x."""

        notes = {}
        notes["file_name"] = self.file
        notes["date"] = self.start_date.strftime("%Y-%m-%d %H:%M:%S")
        notes["notes"] = []

        note_row = self._parse()

        for n in note_row:
            notes["notes"].append(self.parse_note(n))

        return notes

    def _parse(self):
        """x."""

        notes_list = []

        note = []
        with codecs.open(self.file, encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                if line == self.separator:
                    notes_list.append(note)
                    note = []
                else:
                    note.append(line)

        return notes_list

    def parse_note(self, row_note):
        """x."""

        return dict(
            book=row_note[0],
            location_date=row_note[1],
            content=row_note[3],
            note_hash=hashlib.md5(
                (row_note[0] + row_note[3]).encode("utf-8")
            ).hexdigest(),
        )

    def to_json(self, file):
        """x."""
        with codecs.open(file, "w", encoding="utf8") as f:
            json.dump(self.notes, f)

    def to_md(self, file, grouped=True, append=True):
        """x."""

        notes_sorted = sorted(self.notes["notes"], key=lambda k: k["book"])

        with codecs.open(file, mode="a", encoding="utf8") as f:
            for note in self.notes["notes"]:
                f.write(note["content"])


if __name__ == "__main__":

    notep = NotesParser(file=args[0])
    notep.to_json(args[1])
