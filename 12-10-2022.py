s = input()

h1 = s.find('h')
h2 = s.rfind('h')

print(s[:h1] + s[h2 + 1:])