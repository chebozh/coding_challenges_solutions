"""How Many Unique Styles?

There are many different styles of music and many albums exhibit multiple styles.
Create a function that takes a list of musical styles from albums and returns how many styles are unique.
Examples

unique_styles([
  "Dub,Dancehall",
  "Industrial,Heavy Metal",
  "Techno,Dubstep",
  "Synth-pop,Euro-Disco",
  "Industrial,Techno,Minimal"
]) ➞ 9

unique_styles([
  "Soul",
  "House,Folk",
  "Trance,Downtempo,Big Beat,House",
  "Deep House",
  "Soul"
]) ➞ 7
"""


def unique_styles(albums):
    albums_unique = set(','.join(albums).split(','))
    return len(albums_unique)


if __name__ == '__main__':
    assert unique_styles([
        "Dub,Dancehall",
        "Industrial,Heavy Metal",
        "Techno,Dubstep",
        "Synth-pop,Euro-Disco",
        "Industrial,Techno,Minimal"
    ]) == 9

    assert unique_styles([
        "Soul",
        "House,Folk",
        "Trance,Downtempo,Big Beat,House",
        "Deep House",
        "Soul"
    ]) == 7
