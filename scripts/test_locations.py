# -*- coding: utf-8 -*-
import json, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('data/fiestas_data.json', encoding='utf-8') as f:
    fiestas = json.load(f)

with open('data/spain_provinces.js', encoding='utf-8') as f:
    text = f.read()
    json_str = text.split('=', 1)[1].strip().rstrip(';')
    provinces = json.loads(json_str)

def point_in_poly(x, y, poly):
    n = len(poly)
    inside = False
    p1x, p1y = poly[0]
    for i in range(n + 1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def find_province(lng, lat):
    for feat in provinces['features']:
        pname = feat['properties']['name']
        geom = feat['geometry']
        coords = geom['coordinates']
        if geom['type'] == 'Polygon':
            for ring in coords:
                if point_in_poly(lng, lat, ring):
                    return pname
        elif geom['type'] == 'MultiPolygon':
            for poly in coords:
                for ring in poly:
                    if point_in_poly(lng, lat, ring):
                        return pname
    return 'UNKNOWN'

mismatches = 0
for f in fiestas:
    found_prov = find_province(f['lng'], f['lat'])
    ok = (found_prov.lower() in f['province'].lower() or f['province'].lower() in found_prov.lower())
    if not ok:
        mismatches += 1
    status = 'OK' if ok else 'CHECK'
    print(f"[{f['id']:2d}] {f['name']:25s} | ({f['lat']:.4f}, {f['lng']:.4f}) | Exp: {f['province']:18s} | GeoJSON: {found_prov:18s} | {status}")

print(f"\nTotal mismatches: {mismatches} / {len(fiestas)}")
