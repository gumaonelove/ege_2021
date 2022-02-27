s = '1' * 70


while s.find("11111") != -1:
    s = s.replace('2222', '1', 1)
    s = s.replace('1111', '2', 1)

print(s)