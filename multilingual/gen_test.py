import json
import pandas as pd

# Opening JSON file
# with open("test/dataset_en_test.json") as json_file:
#     data = json_file.read()

# Opening JSON file
with open("test/dataset_de_test.json") as json_file:
    data2 = json_file.read()

print(data2)

seq = []
label = []

json_objects2 = data2.strip().split("\n")

# for json_str in json_objects1:
#     json_str = json_str.strip()
#     review_data = json.loads(json_str)
#     print("*" * 100)
#     print(review_data)
#     seq.append(review_data["review_body"])
#     label.append(review_data["stars"])

for json_str in json_objects2:
    json_str = json_str.strip()
    review_data = json.loads(json_str)
    print("*" * 100)
    print(review_data)
    seq.append(review_data["review_body"])
    label.append(review_data["stars"])

data_mix = pd.DataFrame(columns=["Paraphrase", "label"])
data_mix["Paraphrase"] = seq
data_mix["label"] = label

print(data_mix.head(10))
data_mix = data_mix.sample(frac=1).reset_index(drop=True)
data_mix_train = data_mix[500:]
data_mix_test = data_mix[:500]
print(data_mix.head(10))

with open("seq_train_de.in", "w") as output:
    for row in data_mix_train["Paraphrase"]:
        output.write(str(row) + "\n")

with open("label_train_de", "w") as output:
    for row in data_mix_train["label"]:
        output.write(str(row) + "\n")

with open("seq_test_de_.in", "w") as output:
    for row in data_mix_test["Paraphrase"]:
        output.write(str(row) + "\n")

with open("label_test_de", "w") as output:
    for row in data_mix_test["label"]:
        output.write(str(row) + "\n")
