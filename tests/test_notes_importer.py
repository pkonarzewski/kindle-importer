import os
from io import TextIOWrapper
import codecs
from unittest import TestCase, main
import tempfile

from kindler.notes_importer import NotesParser


class TestKindleNotes(TestCase):

    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-notesfile.txt")

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
        nf = NotesParser(file_path=self.tmpfilepath)

        self.assertIsInstance(nf, NotesParser)
        self.assertIsInstance(nf.file_path, str)

    def test_parse(self):
        nf = NotesParser(file_path=self.tmpfilepath)

        self.assertEqual(len(nf.notes), 2)
        self.assertIsInstance(nf.notes, list)

    def test_single_note_structure(self):
        nf = NotesParser(file_path=self.tmpfilepath)

        note = nf.notes[0]

        self.assertIsInstance(note, dict)
        self.assertEqual({}, note)


if __name__ == "__main__":
    main()
