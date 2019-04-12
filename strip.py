"""Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
 Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples

The output expected would be:

apples, pears
grapes
bananas

The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"

"""


# solution


def solution(string, markers):
    result = []
    marker = None
    s_split_on_newline = string.split('\n')
    for line in s_split_on_newline:
        if any(char in line for char in markers):
            for char in line:
                if char in markers:
                    marker = char
                    break
        clean_line = line.split(marker)[0].strip(' ') if marker else line.strip(' ')
        result.append(clean_line)
    return '\n'.join(result)


# examples
s = """apples, pears # and bananas
grapes
avocado @apples"""
print(solution(s, ['@', '!']))  # -> apples, pears # and bananas\ngrapes\navocado
print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))  # "apples, pears\ngrapes\nbananas"
