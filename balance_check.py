"""
You are given a (small) check book as a - sometimes - cluttered (by non-alphanumeric characters) string:

"1000.00
125 Market 125.45
126 Hardware 34.95
127 Video 7.45
128 Book 14.32
129 Gasoline 16.10"

The first line shows the original balance. Each other line (when not blank) gives information: check number, category,
 check amount.

First you have to clean the lines keeping only letters, digits, dots and spaces.

Then return a report as a string (underscores show spaces -- don't put them in your solution. They are there so you can
 see them and how many of them you need):

"Original_Balance:_1000.00
125_Market_125.45_Balance_874.55
126_Hardware_34.95_Balance_839.60
127_Video_7.45_Balance_832.15
128_Book_14.32_Balance_817.83
129_Gasoline_16.10_Balance_801.73
Total_expense__198.27
Average_expense__39.65"

On each line of the report you have to add the new balance and then in the last two lines the total expense and the
average expense. So as not to have a too long result string we don't ask for a properly formatted result.
"""
import re


def balance(book):
    all_nums_pattern = re.compile(r'[\d.]+')
    running_balance = float(all_nums_pattern.search(book).group(0))
    total_expense = 0.0
    expense_count = 0
    new_book = []
    book_split = book.splitlines()
    new_book.append('Original Balance: {}'.format(all_nums_pattern.search(book).group(0)))
    for line in book_split:
        if line != '':
            numbers = all_nums_pattern.findall(line)
            if len(numbers) == 2:
                running_balance = round(float(running_balance) - float(numbers[1]), 2)
                expense_count += 1
                total_expense += float(numbers[1])
                new_line = line + ' {}'.format(running_balance)
                new_line = re.sub(r'^([\d.]+) [^a-zA-Z]*', '\\1 ', new_line)
                new_line = re.sub(r'[^a-zA-Z]* ([\d.]+) ', ' \\1 ', new_line)
                new_line = re.sub(r' ([\d.]+)$', ' Balance \\1', new_line)
                new_book.append(new_line)
        else:
            new_book.append(line)
    total_expense = round(total_expense, 2)
    average_expense = round(total_expense / expense_count, 2)
    new_book.append('Total expense  {}'.format(total_expense))
    new_book.append('Average expense  {}'.format(average_expense))
    return '\n'.join(new_book)


# example

s = """1000.00
125 Market 125.45
126 Hardware 34.95
127 Video 7.45
128 Book 14.32
129 Gasoline 16.10"""
print(balance(s))
