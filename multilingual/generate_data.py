# importing the module
import json
import pandas as pd

# Opening JSON file
# with open("en/multi_en_meteor_output.json") as json_file:
#     data = json.load(json_file)

# Opening JSON file
with open("de/multi_de_levenshtein_output.json") as json_file:
    data2 = json.load(json_file)

paraphrases_list = []
label_list = []

for intent in list(data2.keys()):
    print("*" * 100)

    # paraphrases_list = paraphrases_list + [
    #     para for item in data[intent] for para in item["paraphrase"][:5]
    # ]
    # label_list = label_list + [
    #     intent for item in data[intent] for para in item["paraphrase"][:5]
    # ]

    paraphrases_list = paraphrases_list + [
        para for item in data2[intent] for para in item["paraphrase"][:5]
    ]
    label_list = label_list + [
        intent for item in data2[intent] for para in item["paraphrase"][:5]
    ]


print("List of paraphrases:", len(paraphrases_list))
print("List of labels:", len(label_list))

print("List of paraphrases:", len(paraphrases_list))
print("List of labels:", len(label_list))

data_mix = pd.DataFrame(columns=["Paraphrase", "label"])
data_mix["Paraphrase"] = paraphrases_list
data_mix["label"] = label_list

print(data_mix.head(10))
data_mix = data_mix.sample(frac=1).reset_index(drop=True)
print(data_mix)

with open("training_data/leven_top_5_samples/seq_de.in", "w") as output:
    for row in paraphrases_list:
        output.write(str(row) + "\n")

with open("training_data/leven_top_5_samples/label_de", "w") as output:
    for row in label_list:
        output.write(str(row) + "\n")
