# importing the module
import json
import pandas as pd

# Opening JSON file
with open("hate_speech_meteor_output.json") as json_file:
    data = json.load(json_file)

paraphrases_list = []
tagged_paraphrases_list = []
label_list = []

for intent in ["hate"]:
    print("key")
    print(intent)
    print(data["hate"][0])
    print("*" * 100)
    paraphrases_list = paraphrases_list + [
        para for item in data["hate"] for para in item["paraphrase"][:5]
    ]
    label_list = label_list + [
        intent for item in data["hate"] for para in item["paraphrase"][:5]
    ]

paraphrases_list = paraphrases_list + data["not_hate"]
label_list = label_list + ["not_hate"] * len(data["not_hate"])

print("List of paraphrases:", len(paraphrases_list))
print("List of labels:", len(label_list))


data_mix = pd.DataFrame(columns=["Paraphrase", "label"])
data_mix["Paraphrase"] = paraphrases_list
data_mix["label"] = label_list

print(data_mix.head(10))
data_mix = data_mix.sample(frac=1).reset_index(drop=True)
print(data_mix.head(10))

with open("training_data/meteor_top5_samples/seq.in", "w") as output:
    for row in paraphrases_list:
        output.write(str(row) + "\n")

with open("training_data/meteor_top5_samples/label", "w") as output:
    for row in label_list:
        output.write(str(row) + "\n")
