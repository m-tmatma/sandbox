import os

for root, dirs, files in os.walk('C:\Program Files (x86)'):
	for file in files:
		base, ext = os.path.splitext(file)
		if ext == '.exe':
			fullPath = os.path.join(root, file)
			print (fullPath)
