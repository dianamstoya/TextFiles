def remove_prefix(string: str, prefix: str) -> str:
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:]


def remove_suffix(string: str, suffix: str) -> str:
    if string.endswith(suffix):
        return string[:-len(suffix)]
    else:
        return string[:]


filename = 'Jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)

chars = "' Twasebv"
# no_apostrophe = first.strip(chars)
# print(no_apostrophe)
for character in first:
    if character in chars:
        print(f'removing "{character}"')
    else:
        break

print('*' * 80)

for character in first[::-1]:
    if character in chars:
        print(f'removing "{character}"')
    else:
        break

print('*'*80)

twas_removed = first.removeprefix("'Twas")
print(twas_removed)
toves_removed = first.removesuffix("toves")
print(toves_removed)
print('*'*80)

print(remove_suffix('bolero', 'ro'))
