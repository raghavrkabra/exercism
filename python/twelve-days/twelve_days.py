predicate_list = [
        ["first", "a Partridge in a Pear Tree"],
        ["second", "two Turtle Doves"],
        ["third", "three French Hens"],
        ["fourth", "four Calling Birds"],
        ["fifth", "five Gold Rings"],
        ["sixth", "six Geese-a-Laying"],
        ["seventh", "seven Swans-a-Swimming"],
        ["eighth", "eight Maids-a-Milking"],
        ["ninth", "nine Ladies Dancing"],
        ["tenth", "ten Lords-a-Leaping"],
        ["eleventh", "eleven Pipers Piping"],
        ["twelfth", "twelve Drummers Drumming"],
        ]


def recite(start_verse: int, end_verse: int) -> list:
    """Recite some or all the verses of the twelve days to christmas poem"""
    verses = []

    for i in range(start_verse-1, end_verse):
        day = predicate_list[i][0]
        verse = ("On the {0} day of Christmas my true love"
                " gave to me: {1}".format(
                    day,
                    get_predicate(i+1, predicate_list)
                    )
                )
        verses.append(verse)

    return verses


def get_predicate(number: int, predicates: list) -> str:
    """Return the predicate part of tthe verse"""
    if number == 1:
        return "a Partridge in a Pear Tree."
    else:
        verse_end_list = [s[1] for s in reversed(predicates[1:number])]
        predicate = ", ".join(verse_end_list)
        return predicate + ", and a Partridge in a Pear Tree."
