
def is_isogram(string):
    for i in string:
        if string.count(i) > 1:
            return True
    return False

print(is_isogram('pear'))


print(is_isogram('apple'))

        