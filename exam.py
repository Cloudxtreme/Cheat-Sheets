import urllib2

# response = urllib2.urlopen('http://www.gutenberg.org/cache/epub/100/pg100.txt')
# html = response.read()

f = open('pg100.txt.1', 'r+')
html = f.read()

word = 'the'
word_len = len(word)

leng = len(html)
word_count = 0
start = 0 
run = True
print "Length:"+str(leng)


while run:
	pos = html.find('the', start, leng)
	if pos >= 0:
		print("====== Found <{0}> at <{1}>".format(word, str(pos)))
		word_count = word_count+1
		start = pos+word_len

		# search 5 words after "the"
		run_find_5_words = True
		new_start = start
		new_word_count = 0

		words = html[new_start:new_start+50].split()
		words = words[0:5]
		print words
		
	else:
		run = False

print 'Total words: '+ str(word_count)

selected_lines = []
lines = html.split('\n')
for i in range(len(lines)):
	pos = lines[i].find('world')
	if pos >= 0:
		selected_lines.append(i)

lines_5_percent = int( 0.05 * float(len(selected_lines)))
print("== total lines <{0}>".format(len(lines)))
print("== total lines with world <{0}>".format(len(selected_lines)))
print("== 5% of lines with world <{0}>".format(lines_5_percent))

for i in range(lines_5_percent):
	print lines[selected_lines[i]]
