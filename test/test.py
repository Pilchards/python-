#coding=utf-8

input_data = open("all_path.txt", "r+")
for index,each in enumerate(input_data):
    if index > 20:
        input_data.truncate()
        input_data.tell()
input_data.close()


