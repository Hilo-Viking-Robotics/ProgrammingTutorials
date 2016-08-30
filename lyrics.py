f = open("work.txt","r")

lib = []
for line in f:
	i = line.strip().lower()
	out = "".join(c for c in i if c not in ('!','.',':',',',"'",'?'))
	for a in out.split(" "):
		lib.append(a)

dict = {}

for word in lib:
	if word in dict:
		dict[word] += 1
	else:
		dict[word] = 1

goldenWord = ""
reset = 0

for words in dict:
	if dict[goldenWord] < dict[words]:
		goldenWord = words

print goldenWord
print dict[goldenWord]


