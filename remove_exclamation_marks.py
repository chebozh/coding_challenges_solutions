"""
Description:

Remove n exclamation marks in the sentence from left to right. n is positive integer.
Examples

remove("Hi!",1) === "Hi"
remove("Hi!",100) === "Hi"
remove("Hi!!!",1) === "Hi!!"
remove("Hi!!!",100) === "Hi"
remove("!Hi",1) === "Hi"
remove("!Hi!",1) === "Hi!"
remove("!Hi!",100) === "Hi"
remove("!!!Hi !!hi!!! !hi",1) === "!!Hi !!hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",3) === "Hi !!hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",5) === "Hi hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",100) === "Hi hi hi"

"""


# solution
def remove(s, n):
    count = 0
    result = ''
    for i in s:
        if i == '!' and count < n:
            count += 1
            continue
        result += i
    return result


# Examples
print(remove("Hi!", 1))
print(remove("Hi!", 100))
print(remove("!Hi!",100))
print(remove("!!!Hi !!hi!!! !hi",1))
print(remove("!!!Hi !!hi!!! !hi",3))
print(remove("!!!Hi !!hi!!! !hi",5))
print(remove("!!!Hi !!hi!!! !hi",100))
