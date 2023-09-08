# importing the module
import json
import pandas as pd

# Opening JSON file
with open("atis_meteor_output.json") as json_file:
    data = json.load(json_file)

paraphrases_list = []
tagged_paraphrases_list = []
label_list = []

for intent in list(data.keys())[1:]:
    print("key")
    print(intent)
    print(data[intent][0]["paraphrase"])
    print("*" * 100)
    paraphrases_list = paraphrases_list + [
        para for item in data[intent] for para in item["paraphrase"][:5]
    ]
    label_list = label_list + [
        intent for item in data[intent] for para in item["paraphrase"][:5]
    ]


print("List of paraphrases:", len(paraphrases_list))
print("List of labels:", len(label_list))


for item in data["atis_flight"]:
    if item["tagged_sent"] != "not":
        paraphrases_list.append(item["original_sent"])
        label_list.append("atis_flight")

print("List of paraphrases:", len(paraphrases_list))
print("List of labels:", len(label_list))

data_mix = pd.DataFrame(columns=["Paraphrase", "Tag", "label"])
data_mix["Paraphrase"] = paraphrases_list
data_mix["label"] = label_list

print(data_mix.head(10))
data_mix = data_mix.sample(frac=1).reset_index(drop=True)
print(data_mix.head(10))

with open("atis_data/meteor_top5_samples/seq.in", "w") as output:
    for row in paraphrases_list:
        output.write(str(row) + "\n")

with open("atis_data/meteor_top5_samples/label", "w") as output:
    for row in label_list:
        output.write(str(row) + "\n")
