import os
from io import TextIOWrapper
import codecs
from unittest import TestCase, main
import tempfile

from kindler.notes_importer import NotesFile


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
        nf = NotesFile(self.tmpfilepath)
        self.assertIsInstance(nf, NotesFile)
        self.assertEqual(nf.file_name, self.tmpfilepath)
        self.assertIsInstance(nf.note_file, TextIOWrapper)

    def test_get_note(self):
        nf = NotesFile(self.tmpfilepath)

        note1 = next(nf)
        self.assertEqual(len(note1), 4)

        note2 = next(nf)
        self.assertEqual(len(note2), 4)

        n3 = next(nf)
        self.assertIsNone(n3)


class TestNotesParsing(TestCase):
    def test_parsing_entry(self):
        pass

    def test_converting_to_json(self):
        pass

    def test_converting_to_md(self):
        pass


if __name__ == "__main__":
    main()
