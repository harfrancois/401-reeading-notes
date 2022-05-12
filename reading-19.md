# Python Regular Expression
source - https://www.datacamp.com/tutorial/python-regular-expression-tutorial

Regular Expressions, often shortened as regex, are a sequence of characters used to check whether a pattern 
exists in a given text (string) or not.

. - A period. Matches any single character except the newline character.
^ - A caret. Matches the start of the string.
$ - Matches the end of string.
[abc] - Matches a or b or c.
[a-zA-Z0-9] - Matches any letter from (a to z) or (A to Z) or (0 to 9).

\ - Backslash.
If the character following the backslash is a recognized escape character, then the special meaning of the 
term is taken. Else if the character following the \ is not a recognized escape character, then the \ is treated 
like any other character and passed through. \ can be used in front of all the metacharacters to remove their 
special meaning.

\w - Lowercase 'w'. Matches any single letter, digit, or underscore.
\W - Uppercase 'W'. Matches any character not part of \w (lowercase w).

\s - Lowercase 's'. Matches a single whitespace character like: space, newline, tab, return.
\S - Uppercase 'S'. Matches any character not part of \s (lowercase s).

\d - Lowercase d. Matches decimal digit 0-9.
\D - Uppercase d. Matches any character that is not a decimal digit.

\t - Lowercase t. Matches tab.
\n - Lowercase n. Matches newline.
\r - Lowercase r. Matches return.
\A - Uppercase a. Matches only at the start of the string. Works across multiple lines as well.
\Z - Uppercase z. Matches only at the end of the string.

TIP: ^ and \A are effectively the same, and so are $ and \Z. Except when dealing with MULTILINE mode. Learn more about 
it in the flags section.

\b - Lowercase b. Matches only the beginning or end of the word.

+ - Checks if the preceding character appears one or more times starting from that position.
* - Checks if the preceding character appears zero or more times starting from that position.
? - Checks if the preceding character appears exactly zero or one time starting from that position.

{x} - Repeat exactly x number of times.
{x,} - Repeat at least x times or more.
{x, y} - Repeat at least x times but no more than y times.

# shutil — High-level File Operations
source - https://pymotw.com/3/shutil/
The shutil module includes high-level file operations such as copying and archiving.
Visit site for doc.