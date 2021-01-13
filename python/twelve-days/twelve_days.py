TWELVE_DAYS = {
        "days": [
            "first", "second", "third", "fourth", "fifth", "sixth",
            "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
            ],

        "gift_list": [
                "a Partridge in a Pear Tree",
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
    """Recite some or all of the verses of the poem."""
    return [get_verse(i) for i in range(start_verse, end_verse + 1)]


def get_verse(verse_number: int) -> str:
    """Return the verse at verse_number."""
    # verse_number is one more then the indic of day in the list
    day = TWELVE_DAYS["days"][verse_number-1]

    # gift list at the end of the verse
    gift_list = TWELVE_DAYS["gift_list"]
    if verse_number == 1:
        gifts = gift_list[0] + "."
    else:
        gifts = (", ".join(reversed(gift_list[1:verse_number])) +
                 ", and " + gift_list[0] + ".")

    return f"On the {day} day of Christmas my true love gave to me: {gifts}"
