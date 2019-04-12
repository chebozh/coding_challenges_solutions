"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
For example:

domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"

"""
# solution
import re


def domain_name(url):
    pattern = re.compile(r'[http|https ://]*w*\.?(.*)\.')
    result = pattern.findall(url)
    return result[0]


# examples
print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name('www.xakep.ru'))
