from typing import List


class Solution:
    def evenly_divide_number(self, number, num_parts):
        if num_parts <= 0:
            return [0]
        quotient, remainder = divmod(number, num_parts)
        result = [quotient + 1] * remainder + [quotient] * (num_parts - remainder)
        result.sort(reverse=True)
        return result

    def get_spaces(self, length):
        return " " * length

    def place_spaces_line(self, line, maxWidth):
        temp_line = ""
        for j, word in enumerate(line):
            space = ""
            if j < len(line) - 1:
                space = self.get_spaces(1)

            temp_line += word + space

        rem_space = maxWidth - len(temp_line)
        temp_line += self.get_spaces(rem_space)

        return temp_line

    def place_evenly_spaces(self, line, maxWidth, line_ln):
        remaining_space = maxWidth - line_ln
        spaces = self.evenly_divide_number(remaining_space, len(line) - 1)

        temp_line = ""

        for j, word in enumerate(line):
            space = ""
            if j < len(spaces):
                space = self.get_spaces(spaces[j])

            temp_line += word + space

        rem_space = maxWidth - len(temp_line)
        temp_line += self.get_spaces(rem_space)

        return temp_line

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []
        line_ln = 0
        for i, w in enumerate(words):

            if line_ln + len(w) + (len(line)) <= maxWidth:
                line_ln += len(w)
                line.append(w)

                if i == len(words) - 1:
                    temp_line = self.place_spaces_line(line, maxWidth)
                    result.append(temp_line)
            else:

                if i == len(words) - 1:
                    temp_line = self.place_evenly_spaces(line, maxWidth, line_ln)
                    result.append(temp_line)

                    line = [w]
                    line_ln = len(w)

                    temp_line = self.place_spaces_line(line, maxWidth)
                    result.append(temp_line)  

                else:
                    temp_line = self.place_evenly_spaces(line, maxWidth, line_ln)
                    result.append(temp_line)
                    line = [w]
                    line_ln = len(w)

        return result