# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self,name,birth):
    "initializes the person with name and birth date"
        if isinstance(name,str):
            raise TypeError("name must be a string.")
        if not name:
            raise ValueError("name cannot be an empty string.")
        if not isinstance(birth,date):
            raise TypeError("birth must be a date")
        self.name=name
        self.birth=birth
    def initials(self):
        """Returns the uppercase initial letters of each part of the person's name."""
        parts=self.name.split()
        return "".join(part[0].upper()for part in parts)
    def is_birthday(self):
        """Returns True if today is the persons birthday, False otherwise"""
        today=date.today()
        return (today.month, today.day) == (self.birth.month, self.birth.day)
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
