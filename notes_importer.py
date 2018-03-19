"""
Import notes from Kindle and convert to markdown.
"""
import os
import codecs
from collections import OrderedDict


def load_kindle_notes(fpath):
    """Import kindle file and transform to 2d array."""
    kindle_notes = []
    note_row = []

    with codecs.open(fpath, encoding='utf8') as f:
        for line in f:
            line = line.strip().replace('\ufeff', '')

            if line == '==========':
                kindle_notes.append(note_row)
                note_row = []
            else:
                note_row.append(line)

    return kindle_notes


def parse_notes(kindle_notes):
    """Parse 2d array to ordered dict."""

    notes_dict = OrderedDict()

    for line in kindle_notes:
        title = line[0]
        notes = ' '.join(line[2:]).strip()

        if notes == '':
            continue

        if title not in notes_dict.keys():
            notes_dict[title] = [notes]
        else:
            notes_dict[title].append(notes)

    return notes_dict


def save_markdown(notes_dict, out_path):
    """Save notes as markdown file."""

    if os.path.exists(out_path):
        raise IOError('File already exists:', out_path)

    with codecs.open(out_path, mode='w') as f:

        for book, notes in notes_dict.items():
            f.write('## {}\n'.format(book))
            for n in notes:
                f.write('* {}\n'.format(n))

            f.write('\n')


if __name__ == "__main__":

    in_path = 'data/My Clippings.txt'
    out_path = 'data/Notatki z Kindla.md'

    print('Read file:', in_path)
    knotes = load_kindle_notes(in_path)
    print('Parsing notes')
    notes_dict = parse_notes(knotes)
    print('Save to file:', out_path)
    save_markdown(notes_dict, out_path)
