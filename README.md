# palindromic
Palindromic Assignment, W01D3

Check to see if a sentence is a palindrome or not.

We have a main function that asks for a sentence input from the user,
calls our Boolean function is_palindrome, and then prints whether the input
is a palindrome or is not a palindrome.

In is_palindrome, we remove special characters, spaces, and lower any
capital letters, convert to a list, compare the first and last element,
convert the new smaller list back to a string and recursively call our
function with this new string until we only have one item/character left.
Finally, we return True or False.
