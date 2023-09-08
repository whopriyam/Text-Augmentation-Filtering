# opening the file in read mode
my_file = open("multilingual/label_test_de", "r")

# reading the file
data = my_file.read()

# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
data_into_list = data.replace("\n", ".").split(".")

my_file.close()

# printing the data
print(set(data_into_list))


classes = ["1", "2", "3", "4", "5"]

print({key: data_into_list.count(key) for key in classes})
