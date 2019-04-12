"""
Complete the function/method so that it returns the url with anything after the anchor (#) removed.

Examples:

# returns 'www.codewars.com'
remove_url_anchor('www.codewars.com#about')

# returns 'www.codewars.com?page=1'
remove_url_anchor('www.codewars.com?page=1')

"""
# solution
import re


def remove_url_anchor(url):
    return re.sub(r'#\w*', '', url)


# examples
print(remove_url_anchor('www.codewars.com?page=1'))
print(remove_url_anchor('www.codewars.com#about'))
print(remove_url_anchor('www.google.com#hello'))
