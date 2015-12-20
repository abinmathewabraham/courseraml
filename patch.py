# This script patches exersice library for submission sending.
import os

# First find all specified files in folders.

# Walk through folders


def main():

    file1 = "loadjson.m"
    file2 = "makeValidFieldName.m"
    file3 = "test.txt"

    old_string = "a"
    new_string = "bbb"
    replace_string_in_all_files(file3, old_string, new_string)

    old_string = "str=[str str0(pos0(i)+1:pos(i)-1) sprintf('_0x%X_',str0(pos(i)))];"
    new_string = "str=[str str0(pos0(i)+1:pos(i)-1) sprintf('_0x%X_',toascii(str0(pos(i))))];"
    replace_string_in_all_files(file1, old_string, new_string)
    replace_string_in_all_files(file2, old_string, new_string)

    old_string = "str=sprintf('x0x%X_%s',char(str(1)),str(2:end));"
    new_string = "str=sprintf('x0x%X_%s',toascii(str(1)),str(2:end));"
    replace_string_in_all_files(file1, old_string, new_string)
    replace_string_in_all_files(file2, old_string, new_string)


def find_occurences(filename, string_to_find):
    rootdir = os.getcwd()

    list_to_store = []
    for subdir, dirs, files in os.walk(rootdir):
        for file_ in files:
            if file_ == filename:
                print(filename + " found.")
                filepath = os.path.join(subdir, file_)
                list_to_store.append(filepath)
    return list_to_store


def replace_string_in_all_files(filename, old_string, new_string):
    for f in find_occurences(filename, old_string):
        with open(f + "_new", "wt") as fout:
            with open(f, "rt") as fin:
                for line in fin:
                    fout.write(line.replace(old_string, new_string))
        os.remove(f)
        os.rename(f + "_new", f)

main()
