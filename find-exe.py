import os

exeList = []

for root, dirs, files in os.walk('C:\Program Files (x86)'):
	for file in files:
		base, ext = os.path.splitext(file)
		if ext == '.exe':
			fullPath = os.path.join(root, file)
			print (fullPath)
			exeList.append(fullPath)

with open('files.txt', 'w') as fout:
	for fullPath in exeList:
		fout.write(fullPath + '\n')
