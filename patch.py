# This script patches exersice library for submission sending.
import os

# First find all specified files in folders.

# Walk through folders
def main():
	rootdir = os.getcwd()

	loadjsonPath = ""
	makeValidFieldNamePath = ""

	for subdir, dirs, files in os.walk(rootdir):
		for file_ in files:
			if file_ == "loadjson.m":
				print("ololo")
				loadjsonPath = os.path.join(subdir, file_)
			if file_ == "makeValidFieldName.m":
				print("atata")
				makeValidFieldNamePath = os.path.join(subdir, file_)

	old_string = "str=sprintf('x0x%X_%s',char(str(1)),str(2:end));"
	new_string = "str=sprintf('x0x%X_%s',toascii(str(1)),str(2:end));"		
	replace_string_in_file(makeValidFieldNamePath, old_string, new_string)

	old_string = "str=[str str0(pos0(i)+1:pos(i)-1) sprintf('_0x%X_',str0(pos(i)))];"
	new_string = "str=[str str0(pos0(i)+1:pos(i)-1) sprintf('_0x%X_',toascii(str0(pos(i))))];"
	replace_string_in_file(loadjsonPath, old_string, new_string)

#def find_all_occurences(filename, string_to_find):


def replace_string_in_file(filename, old_string, new_string):
	with open(filename + "_new", "wt") as fout:
		with open(filename, "rt") as fin:
			for line in fin:
				fout.write(line.replace(
					old_string,
					new_string))
	os.remove(filename)
	os.rename(filename + "_new", filename)

main()