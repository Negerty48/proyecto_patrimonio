# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/fiestas_data.json', encoding='utf-8') as f:
    d = json.load(f)

print(f"JSON syntax valid! Total items: {len(d)}")
gau = [x for x in d if x['id'] == 33][0]
print(f"Fiesta #33: {gau['name']} - {gau['town']} ({gau['province']}) - {gau['date_full']}")
print(f"Summary preview: {gau['summary'][:160]}...")
print(f"Etnografia: {len(gau['etnografia'])} chars")
print(f"Personajes: {len(gau['personajes'])} chars")
print(f"Secuencia: {len(gau['secuencia'])} chars")
print(f"Escaleta: {len(gau['escaleta'])} chars")
