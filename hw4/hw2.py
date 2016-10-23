import os

path = raw_input("Enter your path: ")
file = raw_input("Enter name of your file/directory: ")
s = os.listdir(path)
for i in s:
	if i == file:
		os.chdir(path)
		abspath = os.path.abspath(file)
		print abspath
		if os.path.isdir(abspath):
			print 'Directory'
		else:
			print "File"
		print 'Size: %s' % os.stat(abspath).st_size
		print "Creation time: %s" %(os.stat(abspath).st_ctime)
		print "Modification time: %s" %(os.stat(abspath).st_mtime)