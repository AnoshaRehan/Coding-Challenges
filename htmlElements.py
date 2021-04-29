''' Have the function HTMLElements(str) read the str parameter being passed which will be a string of HTML DOM elements and plain text.
The elements that will be used are: b, i, em, div, p. For example: if str is "<div><b><p>hello world</p></b></div>" then this string of
DOM elements is nested correctly so your program should return the string true.

If a string is not nested correctly, return the first element encountered where, if changed into a different element, would result in a
properly formatted string. If the string is not formatted properly, then it will only be one element that needs to be changed. For example:
if str is "<div><i>hello</i>world</b>" then your program should return the string div because if the first <div> element were changed into
a <b>, the string would be properly formatted.

Examples

Input: "<div><div><b></b></div></p>"
Output: div

Input: "<div>abc</div><p><em><i>test test test</b></em></p>" '''

import re


def HTMLElements(strParam):
    open_tags = ['<b>', '<i>', '<em>', '<div>', '<p>']
    close_tags = ['</b>', '</i>', '</em>', '</div>', '</p>']

    stack = []

    tags = re.split('(<[^>]*>)', strParam)
    for tag in tags:
        if tag in open_tags:
            stack.append(tag)
        elif tag in close_tags:
            check = close_tags.index(tag)
            if (len(stack) > 0) and (open_tags[check] == stack[len(stack)-1]):
                stack.pop()
    if stack:
        return stack[-1].replace('<', '').replace('>', '')

    return True


print(HTMLElements(input()))
