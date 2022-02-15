def rev(string):
    return string[::-1]


data = "illusion never changed into something raalwide awake amd i can see the perfect sky ees torn youre a little late is already torn"
words = data.split()

for var in words:
    for var1 in words:
        if rev(var) == var1:
            if words.index(var) > words.index(var1):
                print(var1)
