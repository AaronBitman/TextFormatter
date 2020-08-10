from justifiable_str import JustifiableStr

class OutputBuffer:
    """Class to hold and write the output"""

    def __init__(self, output_file_name):
        """Create the file object and initialize the buffer."""
        self.file_object = open(output_file_name, 'w')
        self.buffer = ""

    def write(self, text = "", new_paragraph = False):
        """ Add the 'text' parameter to the output buffer
            and maybe write some of that output."""
        
        def send_to_file():
            """ Determine what part, if any, of the text should
                be written and write it to the output file."""
            OUTPUT_LINE_LENGTH = 79

            # While there's enough text to fill a line...
            while len(self.buffer) >= OUTPUT_LINE_LENGTH:
                # If there's EXACTLY enough text...
                if len(self.buffer) == OUTPUT_LINE_LENGTH:
                    # ... we can simply write it
                    # without bothering to justify it...
                    self.file_object.write(self.buffer + '\n')
                    # ... and clear the buffer.
                    self.buffer = ""
                else: # It must be greater than the output line length.
                    # So find the last point where we can break.
                    break_point = self.buffer.rfind(
                        " ", 0, OUTPUT_LINE_LENGTH + 1)
                    # Justify the portion of the output
                    # we can handle and write it.
                    self.file_object.write(JustifiableStr(self.buffer[
                        :break_point]).full_justify(OUTPUT_LINE_LENGTH) + '\n')
                    # Now keep only the portion of
                    # the output we didn't write yet.
                    self.buffer = self.buffer[break_point + 1:]

        INDENT_LENGTH = 2
        # Trim off the final '\n'.
        text = str.rstrip(text)
        # A blank line indicates the end of a paragraph...
        if text == "":
            # ... so if there's text to write...
            if self.buffer != "":
                # ...then we can just write it without justifying it.
                self.file_object.write(self.buffer + "\n")
                self.buffer = ""
        else:
            if new_paragraph:
                # ... then indent.
                self.buffer = " " * INDENT_LENGTH
            # At the end of a line, add a space to separate
            # it from the first word of the next line.
            elif self.buffer != "":
                self.buffer += " "
            # Now we can add the new text.
            self.buffer += text
            send_to_file()

    def close(self):
        """Close the file."""
        self.file_object.close()
