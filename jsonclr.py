import json

# # 불러오기
# with open('C:\\test.json', 'r') as f:
#     json_data = json.load(f)
# print(json.dumps(json_data, indent="\t"))

with open('ingredient.json', 'rt', encoding='UTF8') as f:
    names = [x.get("name") for x in json.load(f) if x.get("name")]
    print(names)

# 저장하기
with open('ingredient1.json', 'w', encoding='utf-8') as make_file:
    json.dump(names, make_file, indent="\t")

# with open('C:\\test.json', 'r') as f:
#     json_data = json.load(f)
#
# print(json.dumps(json_data, indent="\t"))