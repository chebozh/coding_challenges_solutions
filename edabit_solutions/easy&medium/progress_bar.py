"""ASCII Charts (Part 1: Progress Bar)

Given a character and a value between 0 and 100, return a string that represents a simple progress bar.

The value represents a percentage.
The bar should begin and end with "|"
Repeat the character to fill the bar, with each character equivalent to 10%
Use spaces to pad the bar to a length of 10 characters.
A single space comes after the bar, then a message with the % completion (e.g. "Progress: 60%")
If the value is 100, the message should be "Completed!".

Examples

progress_bar("#", 0) ➞ "|          | Progress: 0%"

progress_bar("=", 40) ➞ "|====      | Progress: 40%"

progress_bar("#", 60) ➞ "|######    | Progress: 60%"

progress_bar(">", 100) ➞ "|>>>>>>>>>>| Completed!"

"""


# solution
def progress_bar(bar, progress):
    str_1 = f'|{bar * (progress // 10)}'
    str_2 = f'{" " * (10 - (progress // 10))}|'
    str_3 = f'Progress: {progress}%' if progress < 100 else 'Completed!'
    progress = f'{str_1}{str_2} {str_3}'
    return progress


if __name__ == '__main__':
    assert progress_bar("#", 0) == "|          | Progress: 0%"

    assert progress_bar("=", 40) == "|====      | Progress: 40%"

    assert progress_bar("#", 60) == "|######    | Progress: 60%"

    assert progress_bar(">", 100) == "|>>>>>>>>>>| Completed!"
