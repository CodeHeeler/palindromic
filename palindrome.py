import re


def is_palindrome(sentence):
    # Could keep same name, but this helped me track what I had accomplished
    no_special = re.sub(r'[^A-Za-z]', "", sentence.lower())
    # no_caps_no_special = no_special.lower()
    # no_spaces = sentence.replace(" ", "")

    # Note to self: saw an elegant solution using strings only (no list)
    # It indexed the first, negative indexed the last, then used a slice
    # to pass the newly sized sentence for recursion.  Might use in future!
    my_list = list(no_special)

    if len(my_list) <= 1:
        return True

    first = my_list[0]
    rest = my_list[1:]
    last = rest.pop()
    space = " "
    new_sentence = space.join(rest)

    if ((first == last) and is_palindrome(new_sentence)):
            return True
    else:
        return False


def main():
    test_case = input("Enter a word or sentence to check: ")
    if is_palindrome(test_case):
        print("{} is a palindrome!".format(test_case))
    else:
        print("{} is not a palindrome.".format(test_case))


if __name__ == '__main__':
    main()
