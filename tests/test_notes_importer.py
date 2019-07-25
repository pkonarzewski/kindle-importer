import os
from io import TextIOWrapper
import codecs
from unittest import TestCase, main
import tempfile
import json
import codecs

from kindler.notes_importer import NotesParser


class TestKindleNotes(TestCase):
    tmpdir = tempfile.gettempdir()
    tmpfilepath = os.path.join(tmpdir, "tmp-notesfile.txt")

    note_file_content = """gigants-peter watts (PK)
- Your Highlight on Location 145-145 | Added on Saturday, October 13, 2018 6:51:00 AM

gestate in the vacuum past the viewport. Even best-case
==========
gigants-peter watts
- Your Highlight on Location 168-169 | Added on Saturday, October 13, 2018 6:55:24 AM

displacement vector and it’s getting hotter. Or maybe closer. It’s hard to tell; our senses are hazy that far out, and
==========

"""

    def setUp(self):
        with codecs.open(self.tmpfilepath, "wb", encoding="utf8") as f:
            f.write(self.note_file_content)

    def test_init(self):
        nf = NotesParser(file=self.tmpfilepath)

        self.assertIsInstance(nf, NotesParser)
        self.assertIsInstance(nf.file, str)

        self.assertIsInstance(nf.notes, dict)
        self.assertIsInstance(nf.notes["notes"], list)
        self.assertEqual(len(nf.notes["notes"]), 2)

    def test_single_notes_structure(self):
        nf = NotesParser(file=self.tmpfilepath)

        one_note = nf.notes["notes"][0]

        self.assertIsInstance(one_note, dict)

        self.assertListEqual(
            list(one_note.keys()), ["book", "location_date", "content", "note_hash"]
        )

    def test_to_json(self):
        nf = NotesParser(file=self.tmpfilepath)

        file_path = os.path.join(self.tmpdir, "test.json")
        nf.to_json(file_path)

        with codecs.open(file_path, "r", encoding="utf8") as f:
            json_from_file = json.load(f)

        self.assertDictEqual(nf.notes, json_from_file)

    def test_to_md(self):
        nf = NotesParser(file=self.tmpfilepath)

        file_path = os.path.join(self.tmpdir, "test.md")

        # raise ValueError(nf.to_md(file_path))


if __name__ == "__main__":
    main()
