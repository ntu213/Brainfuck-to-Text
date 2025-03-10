import os
import sys

def testcode(s):
	opened, closed = 0, 0
	for c in s:
		if c == '[':
			opened += 1
		if c == ']':
			closed += 1
	if (opened != closed):
		print("SYNTAX ERROR")
		exit()

def errorMan(idx, val):
	if (val < 0 or val > 255):
		print("INCORRECT VALUE")
		exit()

code = ""
whitelist = "><+-.,[]"

entry = "."
stop = False
while entry != "" and not stop:
	if len(sys.argv) > 1 and code == "":
		if len(sys.argv) > 1:
			entry = sys.argv[1]
	else:
		entry = input("code $> ")

	if os.path.exists(entry.strip()) and code == "":
		entry = open(entry).read()
		stop = True

	code += "+-"
	for c in entry:
		if c in whitelist:
			code += c

testcode(code)

tab = [0]
pos = []
size = 1
idx = 0
i = 0
while i < len(code):
	i+=1
	match (code[i-1]):
		case ('+'):
			tab[idx] += 1
			errorMan(idx, tab[idx])
			continue
		case ('-'):
			tab[idx] -= 1
			errorMan(idx, tab[idx])
			continue
		case ('>'):
			idx += 1
			if idx == size:
				size += 1
				tab.append(0)
			errorMan(idx, tab[idx])
			continue
		case ('<'):
			idx -= 1
			if idx < 0:
				size += 1
				tab = [0] + tab
				idx = 0
			errorMan(idx, tab[idx])
			continue
		case ('.'):
			print(end=chr(tab[idx]))
			continue
		case (','):
			c = input() + "\n"
			tab[idx] = ord(c[0])
			continue
		case ('['):
			pos.append(i)
			continue
		case (']'):
			if (tab[idx]):
				i = pos[len(pos) - 1]
				continue
			pos.pop()
			continue
		case default:
			pass

