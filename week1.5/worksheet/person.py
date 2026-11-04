# Worksheet 1.5: Person class

from datetime import date


class Person:
    """A class representing a person with a name and a birth date."""

    def __init__(self, name, birth):
        """Initializes the person with name and birth date."""
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not name:
            raise ValueError("Name cannot be an empty string.")
        if not isinstance(birth, date):
            raise TypeError("Birth must be a date object.")

        self.name = name
        self.birth = birth

    def initials(self):
        """Returns the uppercase initial letters of each part of the person's name."""
        parts = self.name.split()
        return "".join(part[0].upper() for part in parts)

    def is_birthday(self):
        """Returns True if today is the person's birthday, False otherwise."""
        today = date.today()
        return (today.month, today.day) == (self.birth.month, self.birth.day)
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
