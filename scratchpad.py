# class NotesFile:
#     """Wrapper on notes text file."""

#     def __init__(self, file_name: str, separator: str = "=========="):
#         self.file_name = file_name
#         self.separator = separator
#         self.notes = self.load_notes()

#     def __iter__(self):
#         return self

#     def __next__(self):
#         note = []

#         for line in self.note_file:
#             note.append(line.strip())

#             if line.startswith(self.separator):
#                 yield note
                # note = []

        # raise StopIteration







        # return dict(zip(range(1,len(row_note)), row_note))

    # def add_note(self, rows):
    #     """x.

    #     {Title} ({Author})
    #     - Your Highlight on Location {from}-{to} | Added on {Friday, October 12, 2018 8:00:03 AM}

    #     {note content}
    #     ==========

    #     """

    #     # print(self.note_pattern)
    #     print(" ".join(rows))
    #     matched = self.note_pattern.search(" ".join(rows))
    #     print(matched.groups)
        # from_pos, to_pos, note_date = self.extract(rows[1], '- Your Highlight on Location {from}-{to} | Added on {Friday, October 12, 2018 8:00:03 AM}')
        # note_content = re.search(rows[3], '.+')

        # self.notes.append({'title': first_row.group(1), 'author': first_row.group(2)})

    # def extract(self, text, pattern):
    #     """x."

    #     """
    #     return text

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
