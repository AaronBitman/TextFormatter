class JustifiableStr(str):
    """String class with a full-justify method"""
    def __new__(cls, *args, **kw):
        """Initialize the string."""
        return str.__new__(cls, *args, **kw)

    def full_justify(self, length):
        """Justify a line of text so that it's a number of characters equal
            to a number of characters equal to the 'length' parameter.
            Do this by adding whitespaces to existing whitespaces."""

        # Count the spaces in the string, excluding leading
        # spaces (which we'll assume are for indentation).
        spaces_in_string = self.lstrip().count(' ')

        # Determine how many spaces must be added.
        spaces_to_add = length - len(self)

        # We need the string as a list of characters to manipulate it.
        string_as_char_list = [char for char in self.ljust(length)]

        # Determine how many spaces must be added to EACH space.
        pad_for_all_spaces = spaces_to_add // spaces_in_string

        # Determine how many extra spaces we need in addition.
        pad_remainder = spaces_to_add % spaces_in_string

        # Loop backwards through the character list, writing the
        # end of the given string to the end of the final string.
        read_index = len(self) - 1
        write_index = length - 1
        while write_index > read_index:

            # If it's a space, pad it.
            if string_as_char_list[read_index] == ' ':

                # Add the padding we need for all spaces.
                for i in list(range(0, pad_for_all_spaces)):
                    string_as_char_list[write_index] = ' '
                    write_index -= 1

                # If there's still a remainder left, add some of that too.
                if pad_remainder > 0:
                    string_as_char_list[write_index] = ' '
                    write_index -= 1
                    pad_remainder -= 1

            # Whether the character is a space or not, copy it and keep going.
            string_as_char_list[write_index] = string_as_char_list[read_index]
            write_index -= 1
            read_index -= 1

        # Convert the character list back to a string.
        self = "".join(string_as_char_list)
        return self
