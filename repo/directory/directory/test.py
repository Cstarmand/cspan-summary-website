import json, os, ast

with open(os.path.join(os.path.dirname(__file__), "senate_data_summaries.json"), 'r') as info:
        house_all_data = json.load(info)

for x in range(len(house_all_data)):
    house_all_data[x] = ast.literal_eval(house_all_data[x])

print(house_all_data[0]['link'])

#print(ast.literal_eval(house_all_data[0])['link'])

#print(dict(house_all_data[0]))

#print(dict(house_all_data[0])['link'])