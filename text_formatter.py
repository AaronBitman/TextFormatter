from output_buffer import OutputBuffer

class TextFormatter:
    """ Class for formatting text"""
    def format_text(self):
        """ Reformat a text file so that it indents
            paragraphs and fully justifies the text."""
        beginning_of_paragraph = True
        end_of_paragraph = False
        input_file = open("unformatted.txt", 'r')
        out_buf = OutputBuffer("formatted.txt")
        input_line = input_file.readline()
        while input_line != "":
            out_buf.write(input_line, beginning_of_paragraph)
            if end_of_paragraph:
                beginning_of_paragraph = True
                end_of_paragraph = False
            else:
                beginning_of_paragraph = False
            input_line = input_file.readline()
            if input_line == "\n":
                end_of_paragraph = True
        out_buf.write()
        input_file.close()
        out_buf.close()

if __name__ == '__main__':
    tf = TextFormatter()
    tf.format_text()

