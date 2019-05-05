
from zipfile import ZipFile
import os

#Get files (No empty directory)
def get_all_file_paths(directory):
	file_paths = []
	for root, directories, files in os.walk(directory):
		for filename in files:
			filepath = os.path.join(root,filename)
			file_paths.append(filepath)
	return file_paths

def zipper(directory):
    zipname = os.path.basename(directory) + '.zip'
    file_paths = get_all_file_paths(directory)
    
    with ZipFile(zipname,'w') as zip:
            for file in file_paths:
                    zip.write(file)
                    print("\t"+file)
                    global count
                    count += 1

directory = os.getcwd()
directs = os.listdir(directory)
global count
count = 0

for direct in directs:
    if (os.path.isdir(direct)):
        files = get_all_file_paths(direct)
        if (len(files) > 0):
            print("\033[0;31;40m Archive : "+direct)
            zipper(direct)

print('\n{} files zipped successfully'.format(count))

input()

