"""
Remove HTML tags and return string without:

1) <tag> and </tag>
2) <tag/>
3) <tag />
4) html tags with attributes.
Don't trim space, tab etc.

You have to use regexp.

Tests are using function:
String.prototype.replace(your regexp, "")
Have fun :)

"""
import re

reg = re.compile(r'<\w\s?\w*.*?>|</\w*>')

# examples
print(re.sub(reg, "", "<div>test</div>"))  # , "test");
print(re.sub(reg, "", "<a href='#'>go to <b>start</b> page</a>"))  # , "go to start page")
print(re.sub(reg, "", "aaabbb<i>sss</i>zzz<hr/>vvv<hr /><br/>"))  # , "aaabbbssszzzvvv")
print(re.sub(reg, "", "<img src='home.jpg'/>foto description"))  # , "foto description")
print(re.sub(reg, "", "<p>first section<b>bold text</b>second part    </p>"))  # , "first sectionbold textsecond part    ")
print(re.sub(reg, "", "<div>text\ntext <span>2</span></div>"))  # ,"text\ntext 2")
print(re.sub(reg, "", "<html lang = 'pl' ><body>content of body ... </body> ... </html>"))  # , "content of body ...  ... ")
print(re.sub(reg, "", "<div><span></span></div>"))  # ,"")
print(re.sub(reg, "", ""))  # ,"")
print(re.sub(reg, "", "a"))  # ,"a")
