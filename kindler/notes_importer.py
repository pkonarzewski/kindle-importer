"""
Import notes from Kindle and convert to more readable form.
"""

import re
import os
import codecs
from collections import OrderedDict


class NotesFile:
    """Wrapper on notes text file."""

    def __init__(self, file_name: str, separator: str = "=========="):
        self.file_name = file_name
        self.separator = separator
        self.note_file = codecs.open(self.file_name, encoding='utf8', mode='r')

    def __iter__(self):
        return self

    def __next__(self):
        note = []

        with

        with codecs.open(self.file_name, encoding="utf-8") as f:
            for line in f:
                note.append(line.strip())

                if line.startswith(self.separator):
                    yield note
                    note = []

            raise StopIteration


class NotesParser:
    """Kindle notes parser.

    """

    note_pattern = re.compile(
        r"^(?P<title>.+) \((?P<author>.+)\)"
        # '^- Your Highlight on Location (?P<from_location>/d+)-(?P<to_location>/d+) | Added on (?P<date>.+)$' +
        # '' +
        # '^(?P<note_content>.+)$'
    )

    def __init__(self, file: str):
        self.file = file

    def parse(self, start=0):
        """x.

        1st - book title
        2nd - highlight location | date
        3rd - note content
        """

        current_rows = []

        with codecs.open(self.file, encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                if line == "==========":
                    print(self.line_count)

                    if current_rows[3] == "":
                        pass
                    else:
                        self.add_note(current_rows)
                    current_rows = []
                else:
                    current_rows.append(line)
                self.line_count += 1

        self.parsed = True

    def add_note(self, rows):
        """x.

        {Title} ({Author})
        - Your Highlight on Location {from}-{to} | Added on {Friday, October 12, 2018 8:00:03 AM}

        {note content}
        ==========

        """

        # print(self.note_pattern)
        print(" ".join(rows))
        matched = self.note_pattern.search(" ".join(rows))
        print(matched.groups)
        # from_pos, to_pos, note_date = self.extract(rows[1], '- Your Highlight on Location {from}-{to} | Added on {Friday, October 12, 2018 8:00:03 AM}')
        # note_content = re.search(rows[3], '.+')

        # self.notes.append({'title': first_row.group(1), 'author': first_row.group(2)})

    def extract(self, text, pattern):
        """x."

        """
        return text

        #     kindle_notes.append(note_row)
        #     note_row = []
        # else:
        #     note_row.append(line)


# def load_kindle_notes(fpath):
#     """Import kindle file and transform to 2d array."""
#     kindle_notes = []
#     note_row = []

#     with codecs.open(fpath, encoding='utf-16be') as f:
#         for line in f:

#             if line == '==========':
#                 kindle_notes.append(note_row)
#                 note_row = []
#             else:
#                 note_row.append(line)

#     return kindle_notes


# def parse_notes(kindle_notes):
#     """Parse 2d array to ordered dict."""

#     notes_dict = OrderedDict()

#     for line in kindle_notes:
#         title = line[0]
#         notes = ' '.join(line[2:]).strip()

#         if notes == '':
#             continue

#         if title not in notes_dict.keys():
#             notes_dict[title] = [notes]
#         else:
#             notes_dict[title].append(notes)

#     return notes_dict


# def save_markdown(notes_dict, out_path):
#     """Save notes as markdown file."""

#     if os.path.exists(out_path):
#         raise IOError('File already exists:', out_path)

#     with codecs.open(out_path, mode='w') as f:

#         for book, notes in notes_dict.items():
#             f.write('## {}\n'.format(book))
#             for n in notes:
#                 f.write('* {}\n'.format(n))

#             f.write('\n')


# in_path = "tests/excample_clippings.txt"
# out_path = "data/Notatki z Kindla.md"

# kparser = KindleNoteParser(file=in_path)
# kparser.parse()

# print('Read file:', in_path)
# knotes = load_kindle_notes(in_path)
# print('Parsing notes')
# notes_dict = parse_notes(knotes)
# print('Save to file:', out_path)
# save_markdown(notes_dict, out_path)


if __name__ == "__main__":
    print("test")
