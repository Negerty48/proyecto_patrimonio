# -*- coding: utf-8 -*-
import os, sys, re

char_map = {
    0xb1: 'ñ', 0xb3: 'ü', 0xb4: 'ï', 0xb7: 'ú', 0xbd: '¡', 0xbe: 'ó',
    0xcb: 'Ó', 0xd0: 'Ñ', 0xd3: 'à', 0xda: 'é', 0xdd: 'í', 0xdf: 'á',
    0xed: '¿', 0xf9: '—', 0xfb: '–', 0xfe: 'ç', 0x250c: 'Ú', 0x2510: '¿',
    0x2514: 'À', 0x2534: 'Á', 0x2550: 'Í', 0x2554: 'É', 0x2557: '!', 0x2584: 'Ü', 0x2591: 'º'
}

def clean_str(s):
    return ''.join(char_map.get(ord(c), c) for c in s)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
proj_path = os.path.join(base_dir, '.references', 'PROYECTO PATRIMONIO INMATERIAL 2027.md')

with open(proj_path, 'r', encoding='utf-16') as f:
    text = clean_str(f.read())

# List of regex markers for all main sections in PROYECTO
# (including non-map ones, to accurately define boundaries)
markers = [
    (1, r'1\.\s*\*\*LA VIJANERA'),
    (2, r'1\.\s*\*\*LAS LUMINARIAS'),
    (3, r'1\.\s*\*\*JARRAMPLAS'),
    (None, r'1\.\s*\*\*CARNAVAL ITUREN Y ZUBIETA'),
    (None, r'1\.\s*\*\*LA ENDIABLADA'),
    (4, r'1\.\s*\*\*CARNAVAL DEL TORO'),
    (5, r'\*\s*1\.\s*\*\*FESTA DA ARRIBADA'),
    (6, r'\*\s*1\.\s*\*\*LAS FALLAS'),
    (7, r'\*\*3\.\s*LA DANZA DE LA MUERTE'),
    (8, r'1\.\s*\*\*ROMPIDA DE LA HORA'),
    (9, r'\*\s*\+\s*1\.\s*\*\*LAS MONDAS'),
    (10, r'\*\s*\+\s*1\.\s*\*\*MOROS Y CRISTIANOS'),
    (None, r'TOROS ENSOGADOS DE SAN MARCOS'),
    (None, r'DÍA DE LA ALMADÍA'),
    (11, r'1\.\s*\*\*LOS CABALLOS DEL VINO'),
    (12, r'1\.\s*\*\*CABALLADA DE ATIENZA'),
    (13, r'1\.\s*\*\*FERIA DE CÓRDOBA'),
    (14, r'1\.\s*\*\*LA PATUM DE BERGA'),
    (15, r'1\.\s*\*\*EL COLACHO'),
    (16, r'1\.\s*\*\*CERDO SAN ANTÓN LA ALBERCA'),
    (None, r'1\.\s*\*\*PASO DEL FUEGO'),
    (18, r'\*\*5\.\s*BATALLA DEL VINO DE HARO'),
    (19, r'1\.\s*\*\*A RAPA DAS BESTAS'),
    (21, r'1\.\s*\*\*LA VAQUILLA DEL ÁNGEL'),
    (22, r'1\.\s*\*\*DANZA DE LOS ZANCOS ANGUIANO'),
    (23, r'1\.\s*\*\*PROCESIÓN DE LOS ATAÚDES'),
    (24, r'1\.\s*\*\*DESCENSO DEL SELLA Y AQUASELLA'),
    (25, r'1\.\s*\*\*DESCENSO FOLCLÓRICO DEL NALÓN'),
    (26, r'1\.\s*\*\*TOMATINA DE BUÑOL'),
    (27, r'1\.\s*\*\*CIPOTEGATO'),
    (28, r'\*\s*1\.\s*\*\*FIESTAS DE MORATA DE TAJUÑA'),
    (31, r'1\.\s*\*\*FIESTAS DEL PILAR'),
    (32, r'1\.\s*\*\*AS SAN LUCAS DE MONDOÑEDO'),
    (None, r'1\.\s*\*\*FIESTA DE LA TRANSHUMANCIA'),
    (34, r'1\.\s*\*\*LOS HUMANITARIOS DE SAN MARTÍN'),
    (35, r'1\.\s*\*\*FIESTA DEL ORUJO'),
    (36, r'1\.\s*\*\*SAN ANDRÉS E ICOD DE LOS VINOS'),
    (None, r'1\.\s*\*\*PROCESIÓN DEL HUMO'),
    (37, r'1\.\s*\*\*LOS ESCOBAZOS'),
    (38, r'1\.\s*\*\*ZANGARRÓN'),
    (39, r'1\.\s*\*\*TAFARRÓN'),
    (40, r'1\.\s*\*\*ELS ENFARINATS'),
    (None, r'1\.\s*\*\*FIESTA DE LOS LOCOS'),
    (None, r'\*\*BONUS TRACK\.\*\*')
]

spans = []
for num, pat in markers:
    m = re.search(pat, text, re.IGNORECASE)
    if m:
        spans.append((m.start(), num, pat))
    else:
        print(f"FAILED TO FIND PATTERN: {num} - {pat}")

spans.sort()
print(f"Found {len(spans)} boundary markers")
for i in range(len(spans)):
    start, num, pat = spans[i]
    end = spans[i+1][0] if i+1 < len(spans) else len(text)
    length = end - start
    if num is not None:
        print(f"Fiesta #{num:2d}: length {length:6d} chars (from {start:6d} to {end:6d})")
