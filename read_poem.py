# jabber = open('Jabberwocky.txt', 'r')
#
# for line in jabber:
#     print(line.rstrip())
#     # print(len(line))
#
# jabber.close()

# the file closes automatically when the with block terminates
# with open('Jabberwocky.txt', 'r') as jabber:
#     # for line in jabber:
#     #     print(line.rstrip())
#     lines = jabber.readlines()  # RETURNS A LIST OF LINES
#
# print(lines)
# print(lines[-1:])
# # REVERSED!
# for line in reversed(lines):
#     print(line, end='')

# with open('Jabberwocky.txt') as jabber:
#     text = jabber.read()  # RETURNS A SINGLE STRING
#
# print(text)

with open('Jabberwocky.txt') as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break

print('*' * 80)

with open('Jabberwocky.txt') as jabber:
    for line in jabber:
        print(line.rstrip())
        if 'jubjub' in line.casefold():
            break
