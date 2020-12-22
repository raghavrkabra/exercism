twelve_days = {
        "days":[
            "first", "second", "third", "fourth", "fifth", "sixth",
            "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
            ],

        "gift_list":[
                "a Partridge in a Pear Tree.",
                "two Turtle Doves",
                "three French Hens",
                "four Calling Birds",
                "five Gold Rings",
                "six Geese-a-Laying",
                "seven Swans-a-Swimming",
                "eight Maids-a-Milking",
                "nine Ladies Dancing",
                "ten Lords-a-Leaping",
                "eleven Pipers Piping",
                "twelve Drummers Drumming",
                ]
    }


def recite(start_verse: int, end_verse: int) -> list:
    """Recite some or all of the verses of the poem"""
    verses = []

    for i in range(start_verse-1, end_verse):
        verse = get_verse(i+1) # 'i' is one less then the verse we want
        verses.append(verse)

    return verses


def get_verse(verse_number: int) -> str:
    """Return the verse at verse_number"""

    # verse_number is one more then the indic of day in the list
    day = twelve_days["days"][verse_number-1]

    verse = ("On the {0} day of Christmas my true love"
            " gave to me: {1}".format(
                day,
                get_gifts(verse_number, twelve_days["gift_list"])
                )
            )
    return verse


def get_gifts(verse_number: int, gift_list: list) -> str:
    """Return the gift of the verse"""
    if verse_number == 1:
        return gift_list[0]
    else:
        # gifts here contains all the gifts except the first one
        # as we need to add an "and" before it in the poem
        gifts = ", ".join(reversed(gift_list[1:verse_number]))
        return gifts + ", and " + gift_list[0]
