import re

s = 'A licence or license'

pattern = 'licen[cs]e'
matches = re.finditer(pattern, s)

for match in matches:
    print(match.group())

s = 'news/100'
pattern = '\w+/\d+'

matches = re.finditer(pattern, s)
for match in matches:
    print(match)

s = 'news/100'
pattern = '\w+/(\d+)'

matches = re.finditer(pattern,s)
for match in matches:
    print(match)

s = 'news/100'
pattern = '\w+/(\d+)'

matches = re.finditer(pattern,s)
for match in matches:
    for index in range(0, match.lastindex + 1):
        print(match.group(index))

s = 'news/100'
pattern = '(?P<resource>\w+)/(?P<id>\d+)'

matches = re.finditer(pattern,s)
for match in matches:
    print(match.groupdict())

s = 'news/2021/12/31'
pattern = '(?P<resource>\w+)/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})'

matches = re.finditer(pattern,s)
for match in matches:
    print(match.groupdict())