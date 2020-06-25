"""In this kata, you will make a function that converts between camelCase, snake_case, and kebab-case.

You must write a function that changes to a given case. It must be able to handle all three case types:

py> change_case("snakeCase", "snake")
"snake_case"
py> change_case("some-lisp-name", "camel")
"someLispName"
py> change_case("map_to_all", "kebab")
"map-to-all"
py> change_case("doHTMLRequest", "kebab")
"do-h-t-m-l-request"
py> change_case("invalid-inPut_bad", "kebab")
None
py> change_case("valid-input", "huh???")
None
py> change_case("", "camel")
""

Your function must deal with invalid input as shown, though it will only be passed strings. Furthermore, all valid
identifiers will be lowercase except when necessary, in other words on word boundaries in camelCase."""
import re


# solution
def change_case(identifier, targetCase):
    if identifier == '':
        return identifier

    validation = [is_word_camel_case(identifier), is_word_kebab_case(identifier), is_word_snake_case(identifier)]

    if not any(validation):
        return None

    if targetCase == 'snake':
        return to_snake_case(identifier)
    elif targetCase == 'kebab':
        return to_kebab_case(identifier)
    elif targetCase == 'camel':
        return to_camel_case(identifier)
    else:
        return None


def to_camel_case(word):
    word_split = []
    if is_word_camel_case(word):
        return word
    elif is_word_kebab_case(word):
        word_split = split_kebab_case_word(word)
    elif is_word_snake_case(word):
        word_split = split_snake_case_word(word)

    word_split = word_split[:1] + [w.capitalize() for w in word_split[1:]]
    return ''.join(word_split)


def to_kebab_case(word):
    word_split = []
    if is_word_kebab_case(word):
        return word
    elif is_word_camel_case(word):
        word_split = split_camel_case_word(word)
    elif is_word_snake_case(word):
        word_split = split_snake_case_word(word)
    return '-'.join(word_split)


def to_snake_case(word):
    word_split = []
    if is_word_snake_case(word):
        return word
    elif is_word_kebab_case(word):
        word_split = split_kebab_case_word(word)
    elif is_word_camel_case(word):
        word_split = split_camel_case_word(word)

    return '_'.join(word_split)


def split_camel_case_word(word):
    word_split = re.sub(r"([A-Z])", r" \1", word).split()
    return [w.lower() for w in word_split]


def split_kebab_case_word(word):
    return word.split('-')


def split_snake_case_word(word):
    return word.split('_')


def is_word_camel_case(word):
    return word != word.lower() and word != word.upper() and '_' not in word and '-' not in word


def is_word_kebab_case(word):
    return word.islower() and '-' in word and '_' not in word


def is_word_snake_case(word):
    return word.islower() and '_' in word and '-' not in word


# examples
print(change_case("snakeCase", "snake"))
print(change_case("some-lisp-name", "camel"))
print(change_case('doHTMLRequest', 'kebab'))
print(change_case('kebabCamel-case', 'snake'))
print(change_case("valid-input", "huh???"))