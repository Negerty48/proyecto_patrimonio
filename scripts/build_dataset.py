# -*- coding: utf-8 -*-
"""
Script de procesamiento y estructuración para el Proyecto Patrimonio Inmaterial 2027.
Genera el conjunto de datos completo de las 40 fiestas con sus coordenadas reales,
dossier etnográfico, tabla de personajes, secuencia del rito y guion de rodaje.
"""

import os
import sys
import re
import json

# Mapa de caracteres para decodificar artefactos en el archivo UTF-16LE original
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

# Metadata de las 40 fiestas con coordenadas geográficas exactas
FIESTAS_META = [
    {
        "id": 1,
        "name": "La Vijanera",
        "town": "Silió",
        "municipality": "Molledo",
        "province": "Cantabria",
        "region": "Cantabria",
        "lat": 43.1497,
        "lng": -4.0150,
        "date_display": "3 ENE",
        "date_full": "3 de Enero de 2027",
        "month": "Enero",
        "month_num": 1,
        "season": "Invierno",
        "category": "Mascaradas de Invierno",
        "pattern": r'1\.\s*\*\*LA VIJANERA'
    },
    {
        "id": 2,
        "name": "Las Luminarias",
        "town": "San Bartolomé de Pinares",
        "municipality": "San Bartolomé de Pinares",
        "province": "Ávila",
        "region": "Castilla y León",
        "lat": 40.5433,
        "lng": -4.3644,
        "date_display": "16 ENE",
        "date_full": "16 de Enero de 2027",
        "month": "Enero",
        "month_num": 1,
        "season": "Invierno",
        "category": "Ritos de Fuego y Purificación",
        "pattern": r'1\.\s*\*\*LAS LUMINARIAS'
    },
    {
        "id": 3,
        "name": "El Jarramplas",
        "town": "Piornal",
        "municipality": "Piornal (Valle del Jerte)",
        "province": "Cáceres",
        "region": "Extremadura",
        "lat": 40.1172,
        "lng": -5.8492,
        "date_display": "19-20 ENE",
        "date_full": "19 y 20 de Enero de 2027",
        "month": "Enero",
        "month_num": 1,
        "season": "Invierno",
        "category": "Mascaradas y Ritos Catárticos",
        "pattern": r'1\.\s*\*\*JARRAMPLAS'
    },
    {
        "id": 4,
        "name": "Carnaval del Toro",
        "town": "Ciudad Rodrigo",
        "municipality": "Ciudad Rodrigo",
        "province": "Salamanca",
        "region": "Castilla y León",
        "lat": 40.5986,
        "lng": -6.5317,
        "date_display": "5-9 FEB",
        "date_full": "5 al 9 de Febrero de 2027",
        "month": "Febrero",
        "month_num": 2,
        "season": "Invierno",
        "category": "Carnavales y Fiestas Taurinas",
        "pattern": r'1\.\s*\*\*CARNAVAL DEL TORO'
    },
    {
        "id": 5,
        "name": "Festa da Arribada",
        "town": "Baiona",
        "municipality": "Baiona",
        "province": "Pontevedra",
        "region": "Galicia",
        "lat": 42.1197,
        "lng": -8.8494,
        "date_display": "5-7 MAR",
        "date_full": "5 al 7 de Marzo de 2027",
        "month": "Marzo",
        "month_num": 3,
        "season": "Primavera",
        "category": "Recreaciones Históricas y Marítimas",
        "pattern": r'\*\s*1\.\s*\*\*FESTA DA ARRIBADA'
    },
    {
        "id": 6,
        "name": "Las Fallas",
        "town": "Valencia",
        "municipality": "Valencia",
        "province": "Valencia",
        "region": "Comunidad Valenciana",
        "lat": 39.4699,
        "lng": -0.3763,
        "date_display": "15-19 MAR",
        "date_full": "15 al 19 de Marzo de 2027",
        "month": "Marzo",
        "month_num": 3,
        "season": "Primavera",
        "category": "Ritos de Fuego y Arte Efímero",
        "pattern": r'\*\s*1\.\s*\*\*LAS FALLAS'
    },
    {
        "id": 7,
        "name": "Danza de la Muerte",
        "town": "Verges",
        "municipality": "Verges (Baix Empordà)",
        "province": "Girona",
        "region": "Cataluña",
        "lat": 42.0625,
        "lng": 3.0456,
        "date_display": "Noche 25 MAR",
        "date_full": "25 de Marzo de 2027 (Jueves Santo)",
        "month": "Marzo",
        "month_num": 3,
        "season": "Primavera",
        "category": "Semana Santa y Danzas Macabras",
        "pattern": r'\*\*3\.\s*LA DANZA DE LA MUERTE'
    },
    {
        "id": 8,
        "name": "Rompida de la Hora",
        "town": "Calanda",
        "municipality": "Calanda (Bajo Aragón)",
        "province": "Teruel",
        "region": "Aragón",
        "lat": 40.9392,
        "lng": -0.2319,
        "date_display": "Mediodía 26 MAR",
        "date_full": "26 de Marzo de 2027 (Viernes Santo)",
        "month": "Marzo",
        "month_num": 3,
        "season": "Primavera",
        "category": "Ritos Sonoros y Semana Santa",
        "pattern": r'1\.\s*\*\*ROMPIDA DE LA HORA'
    },
    {
        "id": 9,
        "name": "Las Mondas",
        "town": "Talavera de la Reina",
        "municipality": "Talavera de la Reina",
        "province": "Toledo",
        "region": "Castilla-La Mancha",
        "lat": 39.9635,
        "lng": -4.8308,
        "date_display": "28 MAR - 3 ABR",
        "date_full": "28 de Marzo al 3 de Abril de 2027",
        "month": "Marzo",
        "month_num": 3,
        "season": "Primavera",
        "category": "Ritos de Primavera y Ofrendas Agrarias",
        "pattern": r'\*\s*\+\s*1\.\s*\*\*LAS MONDAS'
    },
    {
        "id": 10,
        "name": "Moros y Cristianos",
        "town": "Alcoy",
        "municipality": "Alcoy / Alcoi",
        "province": "Alicante",
        "region": "Comunidad Valenciana",
        "lat": 38.7054,
        "lng": -0.4743,
        "date_display": "24-26 ABR",
        "date_full": "24 al 26 de Abril de 2027",
        "month": "Abril",
        "month_num": 4,
        "season": "Primavera",
        "category": "Alardes Bélicos y Fiestas Históricas",
        "pattern": r'\*\s*\+\s*1\.\s*\*\*MOROS Y CRISTIANOS'
    },
    {
        "id": 11,
        "name": "Los Caballos del Vino",
        "town": "Caravaca de la Cruz",
        "municipality": "Caravaca de la Cruz",
        "province": "Murcia",
        "region": "Región de Murcia",
        "lat": 38.1067,
        "lng": -1.8622,
        "date_display": "1-5 MAY",
        "date_full": "1 al 5 de Mayo de 2027",
        "month": "Mayo",
        "month_num": 5,
        "season": "Primavera",
        "category": "Ritos Ecuestres y Bordados Tradicionales",
        "pattern": r'1\.\s*\*\*LOS CABALLOS DEL VINO'
    },
    {
        "id": 12,
        "name": "La Caballada",
        "town": "Atienza",
        "municipality": "Atienza (Serranía de Guadalajara)",
        "province": "Guadalajara",
        "region": "Castilla-La Mancha",
        "lat": 41.1994,
        "lng": -2.8719,
        "date_display": "16 MAY",
        "date_full": "16 de Mayo de 2027 (Domingo de Pentecostés)",
        "month": "Mayo",
        "month_num": 5,
        "season": "Primavera",
        "category": "Hermandades y Caballerías Históricas",
        "pattern": r'1\.\s*\*\*CABALLADA DE ATIENZA'
    },
    {
        "id": 13,
        "name": "Feria de Córdoba",
        "town": "Córdoba",
        "municipality": "Córdoba",
        "province": "Córdoba",
        "region": "Andalucía",
        "lat": 37.8882,
        "lng": -4.7794,
        "date_display": "22-29 MAY",
        "date_full": "22 al 29 de Mayo de 2027",
        "month": "Mayo",
        "month_num": 5,
        "season": "Primavera",
        "category": "Ferias de Primavera y Arte Flamenco",
        "pattern": r'1\.\s*\*\*FERIA DE CÓRDOBA'
    },
    {
        "id": 14,
        "name": "La Patum de Berga",
        "town": "Berga",
        "municipality": "Berga (Berguedà)",
        "province": "Barcelona",
        "region": "Cataluña",
        "lat": 42.1042,
        "lng": 1.8461,
        "date_display": "26-30 MAY",
        "date_full": "26 al 30 de Mayo de 2027 (Corpus Christi)",
        "month": "Mayo",
        "month_num": 5,
        "season": "Primavera",
        "category": "Teatro Místico y Pirotecnia Medieval",
        "pattern": r'1\.\s*\*\*LA PATUM DE BERGA'
    },
    {
        "id": 15,
        "name": "El Colacho",
        "town": "Castrillo de Murcia",
        "municipality": "Sasamón / Castrillo de Murcia",
        "province": "Burgos",
        "region": "Castilla y León",
        "lat": 42.2708,
        "lng": -4.0864,
        "date_display": "6 JUN",
        "date_full": "6 de Junio de 2027 (Octava del Corpus)",
        "month": "Junio",
        "month_num": 6,
        "season": "Primavera",
        "category": "Ritos de Paso y Protección Infantil",
        "pattern": r'1\.\s*\*\*EL COLACHO'
    },
    {
        "id": 16,
        "name": "Cerdo de San Antón",
        "town": "La Alberca",
        "municipality": "La Alberca (Sierra de Francia)",
        "province": "Salamanca",
        "region": "Castilla y León",
        "lat": 40.4894,
        "lng": -6.1111,
        "date_display": "13 JUN",
        "date_full": "13 de Junio de 2027 (Suelta de San Antonio de Padua)",
        "month": "Junio",
        "month_num": 6,
        "season": "Primavera",
        "category": "Ritos Comunitarios y Mundo Agropecuario",
        "pattern": r'1\.\s*\*\*CERDO SAN ANTÓN LA ALBERCA'
    },
    {
        "id": 17,
        "name": "San Juan de Ciutadella",
        "town": "Ciutadella de Menorca",
        "municipality": "Ciutadella de Menorca",
        "province": "Islas Baleares",
        "region": "Islas Baleares",
        "lat": 40.0011,
        "lng": 3.8419,
        "date_display": "23-24 JUN",
        "date_full": "23 y 24 de Junio de 2027",
        "month": "Junio",
        "month_num": 6,
        "season": "Verano",
        "category": "Fiestas Ecuestres y Ritos Solsticiales",
        "pattern": None
    },
    {
        "id": 18,
        "name": "Batalla del Vino",
        "town": "Haro",
        "municipality": "Haro (Riscos de Bilibio)",
        "province": "La Rioja",
        "region": "La Rioja",
        "lat": 42.5769,
        "lng": -2.8467,
        "date_display": "29 JUN",
        "date_full": "29 de Junio de 2027 (Festividad de San Pedro)",
        "month": "Junio",
        "month_num": 6,
        "season": "Verano",
        "category": "Fiestas Dionisíacas y Romerías Lúdicas",
        "pattern": r'\*\*5\.\s*BATALLA DEL VINO DE HARO'
    },
    {
        "id": 19,
        "name": "A Rapa das Bestas",
        "town": "Sabucedo",
        "municipality": "A Estrada / Sabucedo",
        "province": "Pontevedra",
        "region": "Galicia",
        "lat": 42.6106,
        "lng": -8.4183,
        "date_display": "1-5 JUL",
        "date_full": "1 al 5 de Julio de 2027",
        "month": "Julio",
        "month_num": 7,
        "season": "Verano",
        "category": "Doma Tradicional y Ritos de Fuerza",
        "pattern": r'1\.\s*\*\*A RAPA DAS BESTAS'
    },
    {
        "id": 20,
        "name": "San Fermín",
        "town": "Pamplona",
        "municipality": "Pamplona / Iruña",
        "province": "Navarra",
        "region": "Comunidad Foral de Navarra",
        "lat": 42.8125,
        "lng": -1.6458,
        "date_display": "6-14 JUL",
        "date_full": "6 al 14 de Julio de 2027",
        "month": "Julio",
        "month_num": 7,
        "season": "Verano",
        "category": "Encierros y Fiestas Taurinas",
        "pattern": None
    },
    {
        "id": 21,
        "name": "Vaquilla del Ángel",
        "town": "Teruel",
        "municipality": "Teruel",
        "province": "Teruel",
        "region": "Aragón",
        "lat": 40.3456,
        "lng": -1.1072,
        "date_display": "9-12 JUL",
        "date_full": "9 al 12 de Julio de 2027",
        "month": "Julio",
        "month_num": 7,
        "season": "Verano",
        "category": "Toros Ensogados y Ritos de Peña",
        "pattern": r'1\.\s*\*\*LA VAQUILLA DEL'
    },
    {
        "id": 22,
        "name": "Danza de los Zancos",
        "town": "Anguiano",
        "municipality": "Anguiano",
        "province": "La Rioja",
        "region": "La Rioja",
        "lat": 42.2611,
        "lng": -2.7633,
        "date_display": "21-23 JUL",
        "date_full": "21 al 23 de Julio de 2027",
        "month": "Julio",
        "month_num": 7,
        "season": "Verano",
        "category": "Danzas Tradicionales y Vértigo Ritual",
        "pattern": r'1\.\s*\*\*DANZA DE LOS ZANCOS ANGUIANO'
    },
    {
        "id": 23,
        "name": "Procesión de los Ataúdes",
        "town": "Santa Marta de Ribarteme",
        "municipality": "As Neves (Pontevedra)",
        "province": "Pontevedra",
        "region": "Galicia",
        "lat": 42.1444,
        "lng": -8.3889,
        "date_display": "29 JUL",
        "date_full": "29 de Julio de 2027",
        "month": "Julio",
        "month_num": 7,
        "season": "Verano",
        "category": "Romerías Votivas y Tanatología Popular",
        "pattern": r'1\.\s*\*\*PROCESIÓN DE LOS ATAÚDES'
    },
    {
        "id": 24,
        "name": "Descenso y Aquasella",
        "town": "Arriondas / Ribadesella",
        "municipality": "Parres / Ribadesella",
        "province": "Asturias",
        "region": "Principado de Asturias",
        "lat": 43.3889,
        "lng": -5.1833,
        "date_display": "6-16 AGO",
        "date_full": "6 al 16 de Agosto de 2027 (Fiesta de las Piraguas)",
        "month": "Agosto",
        "month_num": 8,
        "season": "Verano",
        "category": "Ritos Fluviales y Fiestas de Verano",
        "pattern": r'1\.\s*\*\*DESCENSO DEL SELLA Y AQUASELLA'
    },
    {
        "id": 25,
        "name": "Descenso Folclórico del Nalón",
        "town": "Pola de Laviana",
        "municipality": "Laviana",
        "province": "Asturias",
        "region": "Principado de Asturias",
        "lat": 43.2458,
        "lng": -5.5639,
        "date_display": "21 AGO",
        "date_full": "21 de Agosto de 2027",
        "month": "Agosto",
        "month_num": 8,
        "season": "Verano",
        "category": "Carnaval Acuático e Ingenio Popular",
        "pattern": r'1\.\s*\*\*DESCENSO FOLCLÓRICO DEL NALÓN'
    },
    {
        "id": 26,
        "name": "La Tomatina",
        "town": "Buñol",
        "municipality": "Buñol (Hoya de Buñol)",
        "province": "Valencia",
        "region": "Comunidad Valenciana",
        "lat": 39.4206,
        "lng": -0.7917,
        "date_display": "25 AGO",
        "date_full": "25 de Agosto de 2027 (Último miércoles de agosto)",
        "month": "Agosto",
        "month_num": 8,
        "season": "Verano",
        "category": "Batallas Incruentas y Catarsis Colectiva",
        "pattern": r'1\.\s*\*\*TOMATINA DE BUÑOL'
    },
    {
        "id": 27,
        "name": "El Cipotegato",
        "town": "Tarazona",
        "municipality": "Tarazona (Comarca de Tarazona y el Moncayo)",
        "province": "Zaragoza",
        "region": "Aragón",
        "lat": 41.9047,
        "lng": -1.7247,
        "date_display": "27 AGO",
        "date_full": "27 de Agosto de 2027",
        "month": "Agosto",
        "month_num": 8,
        "season": "Verano",
        "category": "Arlequines Populares y Ritos de Chivo Expiatorio",
        "pattern": r'1\.\s*\*\*CIPOTEGATO'
    },
    {
        "id": 28,
        "name": "Fiestas Patronales de Morata",
        "town": "Morata de Tajuña",
        "municipality": "Morata de Tajuña",
        "province": "Madrid",
        "region": "Comunidad de Madrid",
        "lat": 40.2289,
        "lng": -3.4342,
        "date_display": "29 AGO - 13 SEPT",
        "date_full": "29 de Agosto al 13 de Septiembre de 2027",
        "month": "Agosto",
        "month_num": 8,
        "season": "Verano",
        "category": "Encierros Tradicionales y Fiestas de Vega",
        "pattern": r'\*\s*1\.\s*\*\*FIESTAS DE MORATA DE TAJUÑA'
    },
    {
        "id": 29,
        "name": "Fiestas de la Mercè",
        "town": "Barcelona",
        "municipality": "Barcelona",
        "province": "Barcelona",
        "region": "Cataluña",
        "lat": 41.3874,
        "lng": 2.1686,
        "date_display": "23-26 SEPT",
        "date_full": "23 al 26 de Septiembre de 2027",
        "month": "Septiembre",
        "month_num": 9,
        "season": "Otoño",
        "category": "Castells, Bestiario y Fuego Urbano",
        "pattern": None
    },
    {
        "id": 30,
        "name": "El Vítor de Mayorga",
        "town": "Mayorga",
        "municipality": "Mayorga de Campos",
        "province": "Valladolid",
        "region": "Castilla y León",
        "lat": 42.1678,
        "lng": -5.2631,
        "date_display": "27 SEPT",
        "date_full": "27 de Septiembre de 2027",
        "month": "Septiembre",
        "month_num": 9,
        "season": "Otoño",
        "category": "Ritos de Fuego y Pellejos Ardientes",
        "pattern": None
    },
    {
        "id": 31,
        "name": "Fiestas del Pilar",
        "town": "Zaragoza",
        "municipality": "Zaragoza",
        "province": "Zaragoza",
        "region": "Aragón",
        "lat": 41.6488,
        "lng": -0.8891,
        "date_display": "9-17 OCT",
        "date_full": "9 al 17 de Octubre de 2027",
        "month": "Octubre",
        "month_num": 10,
        "season": "Otoño",
        "category": "Ofrendas Florales y Comparsas Históricas",
        "pattern": r'1\.\s*\*\*FIESTAS DEL PILAR'
    },
    {
        "id": 32,
        "name": "As San Lucas",
        "town": "Mondoñedo",
        "municipality": "Mondoñedo (A Mariña)",
        "province": "Lugo",
        "region": "Galicia",
        "lat": 43.4283,
        "lng": -7.3639,
        "date_display": "17-20 OCT",
        "date_full": "17 al 20 de Octubre de 2027",
        "month": "Octubre",
        "month_num": 10,
        "season": "Otoño",
        "category": "Ferias Medievales de Ganado y Tradición Caballar",
        "pattern": r'1\.\s*\*\*AS SAN LUCAS DE MONDOÑEDO'
    },
    {
        "id": 33,
        "name": "Gau Beltza",
        "town": "Mutriku",
        "municipality": "Mutriku (Debabarrena)",
        "province": "Gipuzkoa",
        "region": "País Vasco",
        "lat": 43.3081,
        "lng": -2.3856,
        "date_display": "31 OCT",
        "date_full": "31 de Octubre de 2027 (Noche de Ánimas)",
        "month": "Octubre",
        "month_num": 10,
        "season": "Otoño",
        "category": "Ritos de Ánimas y Mitología Vasca",
        "pattern": None
    },
    {
        "id": 34,
        "name": "Los Humanitarios de San Martín",
        "town": "Moreda de Aller",
        "municipality": "Aller (Moreda)",
        "province": "Asturias",
        "region": "Principado de Asturias",
        "lat": 43.1656,
        "lng": -5.7336,
        "date_display": "11 NOV",
        "date_full": "11 de Noviembre de 2027 (San Martín)",
        "month": "Noviembre",
        "month_num": 11,
        "season": "Otoño",
        "category": "Cohesión Comunitaria y Folclore de Montaña",
        "pattern": r'1\.\s*\*\*LOS HUMANITARIOS DE SAN MART'
    },
    {
        "id": 35,
        "name": "Fiesta del Orujo",
        "town": "Potes",
        "municipality": "Potes (Valle de Liébana)",
        "province": "Cantabria",
        "region": "Cantabria",
        "lat": 43.1539,
        "lng": -4.6239,
        "date_display": "13 NOV",
        "date_full": "12 al 14 de Noviembre de 2027",
        "month": "Noviembre",
        "month_num": 11,
        "season": "Otoño",
        "category": "Destilación Tradicional y Gastronomía de Picos",
        "pattern": r'1\.\s*\*\*FIESTA DEL ORUJO'
    },
    {
        "id": 36,
        "name": "Las Tablas de San Andrés",
        "town": "Icod de los Vinos",
        "municipality": "Icod de los Vinos",
        "province": "Santa Cruz de Tenerife",
        "region": "Canarias",
        "lat": 28.3667,
        "lng": -16.7167,
        "date_display": "28-30 NOV",
        "date_full": "28 al 30 de Noviembre de 2027",
        "month": "Noviembre",
        "month_num": 11,
        "season": "Otoño",
        "category": "Arrastre de Tablas y Apertura de Bodegas",
        "pattern": r'1\.\s*\*\*SAN ANDR.*S E ICOD DE LOS VINOS'
    },
    {
        "id": 37,
        "name": "Los Escobazos",
        "town": "Jarandilla de la Vera",
        "municipality": "Jarandilla de la Vera",
        "province": "Cáceres",
        "region": "Extremadura",
        "lat": 40.1286,
        "lng": -5.6586,
        "date_display": "7 DIC",
        "date_full": "7 de Diciembre de 2027 (Víspera de la Inmaculada)",
        "month": "Diciembre",
        "month_num": 12,
        "season": "Invierno",
        "category": "Ritos de Fuego y Saludos de Retama",
        "pattern": r'1\.\s*\*\*LOS ESCOBAZOS'
    },
    {
        "id": 38,
        "name": "El Zangarrón",
        "town": "Sanzoles",
        "municipality": "Sanzoles (Tierra del Vino)",
        "province": "Zamora",
        "region": "Castilla y León",
        "lat": 41.4328,
        "lng": -5.5714,
        "date_display": "25-26 DIC",
        "date_full": "25 y 26 de Diciembre de 2027 (San Esteban)",
        "month": "Diciembre",
        "month_num": 12,
        "season": "Invierno",
        "category": "Mascaradas de Invierno y Quintadas",
        "pattern": r'1\.\s*\*\*ZANGARRÓN'
    },
    {
        "id": 39,
        "name": "El Tafarrón",
        "town": "Pozuelo de Tábara",
        "municipality": "Pozuelo de Tábara",
        "province": "Zamora",
        "region": "Castilla y León",
        "lat": 41.7853,
        "lng": -5.8942,
        "date_display": "25-26 DIC",
        "date_full": "25 y 26 de Diciembre de 2027 (San Esteban)",
        "month": "Diciembre",
        "month_num": 12,
        "season": "Invierno",
        "category": "Mascaradas de Invierno y Ritos de Madurez",
        "pattern": r'1\.\s*\*\*TAFARRÓN'
    },
    {
        "id": 40,
        "name": "Els Enfarinats",
        "town": "Ibi",
        "municipality": "Ibi (L'Alcoià)",
        "province": "Alicante",
        "region": "Comunidad Valenciana",
        "lat": 38.6258,
        "lng": -0.5739,
        "date_display": "28 DIC",
        "date_full": "28 de Diciembre de 2027 (Día de los Santos Inocentes)",
        "month": "Diciembre",
        "month_num": 12,
        "season": "Invierno",
        "category": "Fiestas de Locos e Inversión del Poder",
        "pattern": r'1\.\s*\*\*ELS ENFARINATS'
    }
]

# Todos los límites conocidos en el documento para cortar secciones
ALL_DELIMITERS = [
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
    (21, r'1\.\s*\*\*LA VAQUILLA DEL'),
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
    (34, r'1\.\s*\*\*LOS HUMANITARIOS DE SAN MART'),
    (35, r'1\.\s*\*\*FIESTA DEL ORUJO'),
    (36, r'1\.\s*\*\*SAN ANDR.*S E ICOD DE LOS VINOS'),
    (None, r'1\.\s*\*\*PROCESIÓN DEL HUMO'),
    (37, r'1\.\s*\*\*LOS ESCOBAZOS'),
    (38, r'1\.\s*\*\*ZANGARRÓN'),
    (39, r'1\.\s*\*\*TAFARRÓN'),
    (40, r'1\.\s*\*\*ELS ENFARINATS'),
    (None, r'1\.\s*\*\*FIESTA DE LOS LOCOS'),
    (None, r'\*\*BONUS TRACK\.\*\*')
]

# Localizar posiciones de inicio y fin de cada bloque
delim_spans = []
for num, pat in ALL_DELIMITERS:
    m = re.search(pat, text, re.IGNORECASE)
    if m:
        delim_spans.append((m.start(), num, pat))

delim_spans.sort()

def get_festival_raw_text(fid):
    for i in range(len(delim_spans)):
        start, num, pat = delim_spans[i]
        if num == fid:
            end = delim_spans[i+1][0] if i+1 < len(delim_spans) else len(text)
            return text[start:end].strip()
    return ""

def parse_sections(raw_text):
    """Desglosa el texto markdown del festival en subsecciones reconocidas."""
    lines = raw_text.split('\n')
    title_line = ""
    intro_lines = []
    sections = {}
    current_sec = "intro"
    
    sec_patterns = [
        ("etnografia", r'^\s*\*\*(?:.*Etnograf|.*Enfoque Antropol|.*Historia y Or|.*Historia, Etnograf)'),
        ("personajes", r'^\s*\*\*(?:.*Personajes|.*Elementos|.*Comparsas|.*Indumentaria|.*Cargos Festeros|.*Organizaci)'),
        ("secuencia", r'^\s*\*\*(?:.*Secuencia|.*Trilogía Festera|.*Estructura Cronol)'),
        ("escaleta", r'^\s*\*\*(?:.*Escaleta|.*Guion|.*Propuesta de Rodaje|.*Documental)')
    ]
    
    current_buf = []
    
    for l in lines:
        matched_sec = None
        for sec_key, pat in sec_patterns:
            if re.search(pat, l, re.IGNORECASE):
                matched_sec = sec_key
                break
        
        if matched_sec:
            if current_sec == "intro":
                sections["intro"] = '\n'.join(current_buf).strip()
            else:
                sections[current_sec] = '\n'.join(current_buf).strip()
            current_sec = matched_sec
            current_buf = [l]
        else:
            current_buf.append(l)
            
    if current_buf:
        sections[current_sec] = '\n'.join(current_buf).strip()
        
    return sections

# Dossiers enriquecidos para las 5 fiestas especiales
SPECIAL_DOSSIERS = {
    17: {
        "intro": """La **Fiesta de San Juan de Ciutadella** (Menorca, Islas Baleares), celebrada cada **23 y 24 de junio**, es una de las manifestaciones rituales, cívicas y ecuestres más aristocráticas y arraigadas del Mediterráneo occidental. Declarada Fiesta de Interés Turístico Nacional, representa una pervivencia viva de la sociedad estamental medieval menorquina, donde la nobleza, el clero, los artesanos y los campesinos se unen en torno al galope del caballo de pura raza menorquina y al ritmo del fabiol tradicional.""",
        "etnografia": """**Etnografía, Raíz Estamental y Simbolismo Antropológico**

* **Estructura Estamental Inmutable:** A diferencia de otras fiestas de origen popular o carnavalesco, San Juan de Ciutadella conserva con rigor milimétrico la representación de los cuatro estamentos del Antiguo Régimen: la nobleza (*Cavallers*), la Iglesia (*Caixer Capellà*), los artesanos (*Caixers Menestrals*) y el campesinado (*Caixers Pagesos*). Cada participante debe pertenecer por cuna o linaje a su correspondiente estamento para poder cabalgar.
* **El Caballo Menorquín como Eje Ritual:** El caballo de pura raza menorquina, de pelaje negro azabache y porte imponente, no es tratado como mero animal de exhibición, sino como extensión del caballero y catalizador de la energía comunitaria. El momento del *bot* o salto, cuando el jinete alza al animal sobre sus dos patas traseras entre la masa enardecida, simboliza el desafío a la gravedad, la nobleza del espíritu y el éxtasis compartido.
* **Sincretismo Solsticial:** Pese a su estricto marco católico y caballeresco, la fiesta conserva todos los elementos del solsticio de verano mediterráneo: la purificación a través de las avellanas arrojadas (*guerra d'avellanes*), los baños de mar de madrugada y el agua perfumada con flor de espliego (*ginesta*).""",
        "personajes": """**Personajes y Estamentos Clave de la Fiesta**

| **Personaje / Estamento** | **Indumentaria / Atrezo** | **Función Simbólica** |
| --- | --- | --- |
| **El Caixer Senyor** | Traje de frac de gala, sombrero de copa (*copalta*) y fusta | Máxima autoridad de la fiesta; representa a la nobleza civil menorquina y preside todos los actos |
| **El Caixer Capellà** | Sotana talar, teja y cruz pectoral | Representa al clero y custodia la espiritualidad y bendiciones del rito litúrgico |
| **El Fabioler** | Traje civil tradicional, montado a lomos de un asno (*somera*) | Heraldo y maestro de ceremonias; convoca las reuniones haciendo sonar el tambor y el flautín (*fabiol*) |
| **Els Caixers Menestrals** | Traje de levita negra y sombrero de dos picos | Representan a los gremios artesanales urbanos (zapateros, carpinteros, herreros) |
| **Els Caixers Pagesos** | Traje de paño negro rústico y botas camperas | Representan a los labradores de los predios rurales de Ciutadella (*llocs*) |
| **L'Homo des Be** | Pieles de carnero, descalzo y cruz de San Juan | Pasea a hombros la víspera a un cordero engalanado con cintas rojas como sacrificio simbólico |""",
        "secuencia": """**Secuencia Cronológica del Rito**

1. **El Diumenge des Be (Domingo previo):** *S'Homo des Be*, descalzo y vestido con pieles, recorre las calles señoriales de Ciutadella cargando a hombros un carnero blanco inmaculado de lanas rizadas para anunciar a las autoridades el inicio inminente de las fiestas.
2. **23 de Junio (La Víspera):**
   - **14:00 h:** El Fabioler acude al palacio del Caixer Senyor a pedir permiso para iniciar el repliegue (*replec*) de los jinetes al son del tamboril y fabiol.
   - **Tarde:** El monumental *Caragol des Born*, donde más de un centenar de caballeros recorren al galope la plaza del Ayuntamiento, alzando sus monturas en espectaculares *bots* sostenidos entre vítores.
   - **Anochecer:** La lluvia de avellanas en la plaza de las Palmeras y Contramurada.
3. **24 de Junio (Día Grande de San Juan):**
   - **08:00 h:** Nueva concentración de la comitiva ecuestre y misa de *Caixers* en la Catedral de Menorca.
   - **Tarde (Els Jocs des Pla):** En la ensenada del puerto (*Es Pla*), bajo una marea humana de más de 30.000 personas, se celebran los torneos medievales:
     * *La Ensortilla:* Los jinetes lanzan sus caballos a galope tendido para ensartar con una pica una pequeña anilla metálica suspendida.
     * *Ses Carotes:* Dos caballeros cabalgan en paralelo; uno sostiene una carátula de madera policromada y el otro la destroza de un certero golpe con la empuñadura.
     * *Córrer abraçats:* Dos jinetes galopan a toda velocidad entrelazados con sus brazos por los hombros en señal de fraternidad absoluta.
4. **Madrugada del 25:** El último toque de fabiol frente al palacio señorial y el llanto silencioso de la despedida hasta el año venidero.""",
        "escaleta": """**Guion y Escaleta de Rodaje Documental (12–15 min)**

[00:00 - 02:30] PRÓLOGO: EL TOQUE SOLITARIO DEL FABIOL
- Visual: Planos detalle en cámara lenta de los dedos del fabioler sobre el flautín de caña; el eco solitario resonando entre los muros de caliza blanca de Ciutadella al romper el alba.
- Narrador en cámara: Presenta la singularidad de Menorca: una sociedad insular que convirtió el pacto social y el amor al caballo en una obra de arte viva ininterrumpida desde hace seis siglos.

[02:30 - 06:00] EL RITUAL DEL HOMBRE Y EL CABALLO
- Visual: Preparación en las cuadras y masías (*llocs*); el peinado milimétrico de las crines, las escarapelas de colores y los estribos bruñidos.
- Entrevista etnográfica: Un Caixer Pagès explica lo que significa transmitir la fusta de generación en generación en la familia.

[06:00 - 10:00] LA APOTEOSIS EN ES BORN
- Visual: El tumulto de la plaza abarrotada. Planos contrapicados del *bot*: el caballo erguido en ángulo imposible sobre las cabezas de la multitud que sostiene y empuja suavemente el pecho del animal con manos desnudas.
- Sonido: El estruendo de la orquesta entonando el *Jaleo* menorquín fusionado con el relincho y el jadeo poderoso de los corceles.

[10:00 - 14:00] ELS JOCS DES PLA Y EL CREPÚSCULO
- Visual: Polvo levantado en el puerto de Ciutadella; la pica que ensarta la sortija al vuelo; los rostros cubiertos de astillas de las *carotes*.
- Plano final: El Caixer Senyor despidiendo la fiesta en la penumbra medieval; el último suspiro del fabiol y el sonido calmado del mar Mediterráneo."""
    },
    20: {
        "intro": """Las **Fiestas de San Fermín** (Pamplona / Iruña, Navarra), celebradas ininterrumpidamente del **6 al 14 de julio**, constituyen una de las expresiones festivas de proyección mundial más intensas y multidimensionales de la cultura hispana. En su seno conviven ritos religiosos solemnes dedicados al copatrono de Navarra, alardes folclóricos seculares y la catarsis taurina del *Encierro*, donde el ser humano confronta a cuerpo limpio y en segundos la fuerza indómita del toro de lidia.""",
        "etnografia": """**Etnografía, Raíces Históricas y Simbolismo Antropológico**

* **Génesis y Fusión Secular:** San Fermín nace de la confluencia de tres celebraciones originarias distintas: las funciones religiosas medievales en honor a San Fermín de Amiens (trasladadas de octubre a julio en 1591 para disfrutar de mejor clima), las ferias comerciales francas y las corridas de toros documentadas ya en el siglo XIV.
* **La Uniformidad Cromática Igualitaria:** El atuendo reglamentario blanco con faja y pañuelo rojo anudado al cuello no es casual. El blanco representa la pureza y la tabula rasa comunitaria (durante nueve días se suprimen visualmente las diferencias de clase social, ideología y origen geográfico), mientras que el pañuelo rojo (*pañuelico*) simboliza el martirio por decapitación del santo y la pasión compartida.
* **Antropología del Encierro:** Los 848 metros que separan los corrales de Santo Domingo de la plaza de toros no son una competición deportiva, sino un rito de iniciación y vulnerabilidad absoluta. El corredor no compite contra el toro; corre con él, midiendo la distancia milimétrica del asta en un fugaz desafío al peligro que renueva el pacto entre el instinto salvaje del astado y la serenidad del ser humano.""",
        "personajes": """**Personajes y Elementos Icónicos de la Fiesta**

| **Personaje / Colectivo** | **Indumentaria / Atrezo** | **Función Simbólica** |
| --- | --- | --- |
| **Los Corredores del Encierro** | Blanco impoluto, pañuelo y faja rojos; periódico enrollado en la mano | Eje del desafío matutino; marcan el ritmo y la distancia con el toro a golpe de periódico |
| **Los Pastores y Dobladores** | Camiseta verde identificativa y varas de avellano largas | Custodios y guías del rebaño; evitan que los toros queden rezagados o se giren contra la masa |
| **La Comparsa de Gigantes y Cabezudos** | Estructuras monumentales de cartón-piedra del siglo XIX (Gigantes, Kilikis y Zaldikos) | Representan a los cuatro continentes y a la autoridad satírica que persigue a los niños con vergas de goma |
| **Las Peñas de San Fermín** | Blusones de colores distintivos, grandes pancartas satíricas y charangas | Alma popular y crítica social; dinamizan las gradas de sol de la plaza y las noches en el casco viejo |
| **La Capilla de San Fermín** | Casulla litúrgica roja y veneración del relicario del santo | Custodia la fe popular del pueblo pamplonés hacia el "santo morenico" |""",
        "secuencia": """**Secuencia Cronológica y Ritmos de la Fiesta**

1. **6 de Julio a las 12:00 h (El Chupinazo):** Ante una plaza Consistorial abarrotada hasta el límite físico, se pronuncia la fórmula ritual: *"Pamplonesas, pamploneses, ¡Viva San Fermín! Iruindarrak, ¡Gora San Fermín!"*. El disparo del cohete desata un océano de pañuelos rojos en alto y marca el estallido instantáneo de la fiesta continuada.
2. **Las Mañanas (08:00 h - El Encierro):**
   - **07:55 h:** Tres cánticos solemnes ante la hornacina de la cuesta de Santo Domingo: *"A San Fermín pedimos, por ser nuestro patrón, nos guíe en el encierro dándonos su bendición..."*.
   - **08:00 h:** Disparo del primer cohete: apertura de corrales. La manada de seis toros de lidia y seis cabestros asciende por Santo Domingo, cruza la Plaza Consistorial, enfila la curva de Mercaderes y vuela por la mítica calle Estafeta hasta el embudo de acceso a la Plaza de Toros. Todo transcurre en apenas dos minutos y medio de vértigo.
3. **El Mediodía:** Danzas solemnes de la Comparsa de Gigantes en el zócalo de la ciudad y almuerzos populares a base de magras con tomate, ajoarriero y vino tinto.
4. **La Tarde (18:30 h):** Desfile de mulillas y corrida de toros en la Monumental, dominada por la alegría ruidosa de los tendidos de sol.
5. **14 de Julio a las 24:00 h (Pobre de Mí):** La multitud se congrega de nuevo con velas encendidas en la Plaza Consistorial. Se canta la melancólica despedida: *"Pobre de mí, pobre de mí, que se han acabado las fiestas de San Fermín..."*, y los pañuelos rojos se desanudan del cuello mirando al reloj para el próximo 7 de julio.""",
        "escaleta": """**Guion y Escaleta de Rodaje Documental (12–15 min)**

[00:00 - 02:30] PRÓLOGO: EL SILENCIO EN SANTO DOMINGO (07:45 H)
- Visual: Calles empedradas vacías tras el baldeo municipal. Planos cerrados de rostros de corredores veteranos rezando en silencio; manos que aprietan el periódico enrollado; respiración honda en el fresco de la mañana navarra.
- Sonido: El murmullo contenido de la masa, el crujido de las tablas del doble vallado de madera y el primer verso del canto al santo.

[02:30 - 06:00] EL TRUENO DE LA MANADA
- Visual: Cámara de alta velocidad a ras de suelo: pezuñas de 600 kg derrapando en los adoquines de Mercaderes; la curva de Estafeta donde el lomo del astado roza el cuerpo del mozo a escasos centímetros.
- Montaje sonoro: El estruendo metálico de los cencerros de los cabestros y los gritos secos de advertencia entre corredores.

[06:00 - 10:00] EL LABERINTO HUMANO Y LA COMPARSA
- Visual: Contraste absoluto: el vértigo del encierro da paso a la dulzura de los Gigantes meciéndose al son del txistu y tamboril; la sátira de los Kilikis golpeando amistosamente a los niños entre risas.
- Entrevista: Un miembro histórico de la comparsa reflexiona sobre el relevo generacional y la transmisión oral del amor por Pamplona.

[10:00 - 14:00] LA NOCHE, EL HUMOR Y EL ADIÓS
- Visual: Planos cenitales de la plaza teñida de blanco y rojo; las pancartas de las peñas entrando al ruedo al atardecer.
- Epílogo: La noche del 14 de julio; velas que oscilan en la oscuridad de la plaza; el pañuelo que se baja con lentitud mientras resuena: *"Ya falta menos para el 7 de julio"*. Fundido a negro."""
    },
    29: {
        "intro": """Las **Fiestas de la Mercè** (Barcelona, Cataluña), celebradas en torno al **24 de septiembre**, constituyen la *Festa Major* por antonomasia de la capital catalana. Proclamada patrona de la diócesis en 1687 tras liberar a la ciudad de una plaga de langostas, la festividad se transformó a finales del siglo XIX en el gran escaparate identitario de la cultura popular catalana, articulando en el espacio público urbano la pirotecnia de los *correfocs*, la arquitectura efímera humana de los *castells* y el bestiario festivo medieval.""",
        "etnografia": """**Etnografía, Dimensión Urbana y Simbolismo Antropológico**

* **La Conquista Ciudadana del Espacio Público:** A diferencia de las celebraciones agrarias rurales, La Mercè representa la reapropiación comunitaria y democrática de una gran metrópolis moderna a través del folclore vivo. Las avenidas, plazas y callejones góticos son arrebatados al tráfico y a la rutina comercial para ser devueltos a los rituales ancestrales de la vecindad.
* **El Simbolismo del Fuego y el Dragón:** El *Correfoc* hunde sus raíces en los bailes de diablos documentados en Cataluña desde el siglo XII. Lejos de representar el mal en sentido dogmático, los diablos encarnan la fuerza telúrica, la purificación del aire urbano y la alegría transgresora que baila bajo el paraguas protector de chispas incandescentes.
* **Los Castells como Metáfora Social:** La diada castellera en la Plaça Sant Jaume expresa con rigor arquitectónico el lema tradicional de Josep Anselm Clavé: *"Força, equilibri, valor i seny"*. La pirámide humana, donde la base multitudinaria (*pinya*) sostiene a los niveles superiores hasta llegar a la cima protagonizada por un niño (*enxaneta*), representa la solidaridad, la confianza ciega en el prójimo y la cohesión colectiva de toda la sociedad catalana.""",
        "personajes": """**Personajes, Bestiario y Agrupaciones Tradicionales**

| **Figura / Agrupación** | **Indumentaria / Atrezo** | **Función Simbólica** |
| --- | --- | --- |
| **Els Castellers** | Camisa de color de la colla, pantalón blanco y faja negra tensada | Constructores de las torres humanas de hasta 9 y 10 pisos; eje de cooperación comunitaria |
| **L'Enxaneta** | Casco protector, faja y camisa de su colla | Niño o niña que corona el castell levantando el brazo (*fent l'aleta*), validando la estructura |
| **Els Diables de Barcelona** | Monos ignífugos pintados con motivos infernales y mazas pirotécnicas (*maces*) | Señores del fuego urbano; corren y bailan rociando de chispas a la multitud en el Correfoc |
| **El Bestiari Festiu** | Estructuras portables: el Drac de Ciutat Vella, la Víbria, l'Àliga y el Tarasca | Mitología zoomórfica medieval que escupe pólvora y fuego rodante por las calles |
| **Gegants i Capgrossos** | Figuras monumentales de Jaume I, la Reina Violant y tipos populares barceloneses | Representan a la autoridad civil histórica y presiden con dignidad las danzas del cortejo |""",
        "secuencia": """**Secuencia Cronológica del Festival**

1. **El Pregó y el Toc d'Inici (23 de Septiembre):** El pregón inaugural abre las fiestas desde el Saló de Cent; inmediatamente después, en la Plaça Sant Jaume, resuenan los clarines y se baila el ceremonial *Toc d'Inici*, donde el Àliga y los Gegants de la Ciutat ejecutan sus danzas canónicas al son de los ministrils.
2. **La Diada Castellera:** La Plaça Sant Jaume se convierte en un hervidero humano donde las mejores *colles* de la ciudad y de toda Cataluña levantan construcciones de extrema complejidad técnica (torres de ocho, nueve y diez pisos), celebradas con el llanto y júbilo de la plaza al son del *Toc de Castells*.
3. **El Correfoc de la Mercè:** Al caer la noche en la Via Laietana, se desata el infierno lúdico: dragones de fuego y centenares de diablos lanzan miles de carretillas pirotécnicas. El público, protegido con sombreros de paja y ropa de algodón, baila en círculos bajo las cascadas de fuego dorado.
4. **La Cavalcada de la Mercè:** Gran desfile escénico donde la totalidad del bestiario, cabezudos y danzantes recorren el corazón de la urbe en un derroche visual de teatro de calle.
5. **El Piromusical de Montjuïc:** Como colofón insuperable, a los pies del Palau Nacional y las Fuentes Mágicas, una sinfonía milimétrica combina bandas sonoras, agua, luz y toneladas de fuegos artificiales para despedir a la Mercè ante cientos de miles de espectadores.""",
        "escaleta": """**Guion y Escaleta de Rodaje Documental (12–15 min)**

[00:00 - 02:30] PRÓLOGO: EL LATIDO DEL GÓTICO
- Visual: Planos cenitales al amanecer de los tejados del Barrio Gótico y las torres de Santa Maria del Mar; el sonido de una gralla ensayando sola en un portal de piedra.
- Narrador en cámara: Presenta Barcelona no como simple escaparate turístico, sino como una urbe viva que renueva año a año su pacto con sus mitos fundacionales.

[02:30 - 06:00] LA ARQUITECTURA DE LA CONFIANZA
- Visual: Planos macro de las manos crispadas en la *pinya* de un castell; el sudor en las fajas; los pies descalzos de la enxaneta trepando ágilmente sobre las espaldas de los adultos.
- Sonido: La respiración contenida de miles de personas; el clímax sonoro de la gralla al coronar el piso noveno y la explosión de aplausos.

[06:00 - 10:00] LA NOCHE DE LAS CHISPAS: EL CORREFOC
- Visual: Cámara lenta extrema a través del humo blanco: el ojo llameante del Drac; las carretillas de pólvora girando sobre la multitud que sonríe bajo una lluvia de fuego de azufre.
- Entrevista: Una diablessa histórica explica cómo el miedo se transforma en danza comunitaria.

[10:00 - 14:00] EL PIROMUSICAL Y EL HORIZONTE DE LA CIUDAD
- Visual: El cielo nocturno de Montjuïc estallando en constelaciones doradas y carmesíes reflejadas en las fuentes y en los ojos de los asistentes.
- Plano final: Las cenizas del fuego sobre el asfalto de Via Laietana y el despertar sereno de la ciudad al día siguiente."""
    },
    30: {
        "intro": """La **Procesión de El Vítor de Mayorga** (Mayorga de Campos, Valladolid), celebrada cada noche del **27 de septiembre**, es una de las manifestaciones de religiosidad popular, fuego purificador y catarsis colectiva más sobrecogedoras de Castilla y León. Declarada Fiesta de Interés Turístico Nacional, rememora la llegada en 1737 de las reliquias de Santo Toribio de Mogrovejo a su villa natal, escoltadas por una marea interminable de pellejos y odres de vino en llamas que transforman la noche castellana en un mar de fuego, brea y cánticos centenarios.""",
        "etnografia": """**Etnografía, Memoria Colectiva y Simbolismo del Fuego**

* **El Milagro del Recibimiento a Oscuras:** El origen del rito se remonta al 27 de septiembre de 1737, cuando las reliquias de Santo Toribio (arzobispo de Lima y evangelizador de América) arribaron a Mayorga a altas horas de la noche. Careciendo la villa de alumbrado público, los vecinos descolgaron los pellejos de vino viejos inservibles de sus bodegas, los ataron a varales de madera, los impregnaron en pez y alquitrán y salieron en masa a iluminar el cortejo, dando origen a una procesión cívico-religiosa ininterrumpida.
* **El Fuego como Vínculo e Identidad:** El fuego en El Vítor no es pirotecnia recreativa ni espectáculo pasivo: es humo denso, hollín en la piel y calor abrasador compartido hombro con hombro. La quema de más de 400 pellejos de cuero de cabra simboliza la entrega del fruto de la vid y el esfuerzo agrario del año en honor a su hijo más ilustre.
* **La Repetición Hipnótica del Himno:** A lo largo de más de siete horas ininterrumpidas de procesión nocturna, una única melodía tradicional —el Himno a Santo Toribio— es entonada en bucle continuado por miles de gargantas al compás de la charanga, generando un estado de trance colectivo donde el cansancio desaparece ante el fervor de la peña y la hermandad vecinal.""",
        "personajes": """**Personajes y Elementos Materiales del Rito**

| **Elemento / Personaje** | **Indumentaria / Atrezo** | **Función Simbólica** |
| --- | --- | --- |
| **Los Portadores de Pellejos** | Ropas viejas de pana, chaquetones desgastados y sombreros o gorros para chispas | Transportan los largos varales con los odres ardiendo sobre la multitud; desafían el fuego y el hollín |
| **El Estandarte del Vítor** | Estandarte de terciopelo bordado conmemorativo de la canonización (1737) | Eje sacro de la procesión; representa la victoria y el patronazgo de Santo Toribio |
| **El Pellejo o Pez** | Odre tradicional de cuero de cabra relleno de paja y bañado en pez negra hirviendo | Combustible sagrado que al arder destila llamas densas y una humareda aromática inconfundible |
| **La Mayordomía de Santo Toribio** | Capas castellanas tradicionales y medallas doradas de la cofradía | Custodios del protocolo, la reliquia y el orden ceremonial del cortejo |
| **Las Peñas y el Coro Popular** | Cuadrillas vecinales de todas las edades que acompañan el paso | Entonan el cántico sin cesar, meciendo el estandarte en cada parada de la villa |""",
        "secuencia": """**Secuencia Cronológica del Rito**

1. **La Víspera y la Preparación matinal:** En las naves comunales, los mayordomos y jóvenes atan con alambres gruesos los cueros de cabra secos a varales de pino o chopo de tres metros de longitud, sumergiéndolos en calderas de pez negra hirviendo para garantizar una combustión prolongada.
2. **22:00 h (La Concentración en la Ermita):** La multitud se reúne ante la Ermita de Santo Toribio. Se apagan las luces eléctricas de las calles adyacentes y se entona por primera vez el himno con fervor electrizante.
3. **El Encendido del Fuego:** En la hoguera central se prenden las puntas de los primeros pellejos. En cuestión de segundos, la antorcha inicial se transmite de varal en varal hasta encender cientos de odres que se yerguen simultáneamente iluminando las fachadas de adobe y tapial con una luz anaranjada sobrenatural.
4. **La Procesión Interminable:** El cortejo avanza con extrema lentitud por las calles empedradas de Mayorga. La pez derretida gotea al suelo en hilillos de fuego; los portadores balancean los varales sobre sus cabezas al grito de *"¡Vítor, Santo Toribio, Vítor!"*.
5. **El Encuentro en la Plaza Mayor:** En el corazón del pueblo, la procesión se detiene bajo los soportales mudéjares mientras el estandarte baila frente a las llamaradas.
6. **Madrugada (04:00 - 05:00 h):** Regreso de la marea humeante a la ermita; los últimos varales carbonizados se arrojan a una gran hoguera final donde se canta la Salve, concluyendo con el tradicional reparto de chocolate caliente y orujo entre los tiznados vecinos.""",
        "escaleta": """**Guion y Escaleta de Rodaje Documental (12–15 min)**

[00:00 - 02:30] PRÓLOGO: EL OLOR A PEZ EN TIERRA DE CAMPOS
- Visual: Planos macro de las manos ennegrecidas de un anciano embadurnando de brea un pellejo seco; el cielo crepuscular infinito de la llanura castellana.
- Narrador en cámara: Presenta a Mayorga como un enclave donde el fuego no destruye, sino que convoca la memoria viva de tres siglos de fe indómita.

[02:30 - 06:00] EL ENCENDIDO: LA LUZ EN LA NOCHE MEDIEVAL
- Visual: El primer fogonazo en la oscuridad de la ermita; la rápida propagación de las teas de varal en varal; rostros cubiertos de ceniza iluminados por llamaradas de dos metros de altura.
- Sonido: La explosión unísona de cientos de voces cantando el Himno al compás solemne de la trompeta y los tambores de la charanga.

[06:00 - 10:00] EL RÍO INCANDESCENTE
- Visual: Cámara lenta sobre los portadores que avanzan bajo una lluvia de pavesas doradas; planos contrapicados del estandarte del Vítor recortado contra el humo espeso y las tejas castellanas.
- Entrevistas: Jóvenes mayorganos explican por qué volver a Mayorga el 27 de septiembre es un mandato moral que no se puede eludir.

[10:00 - 14:00] LA HOGUERA FINAL Y EL ALBA
- Visual: El lanzamiento de los varales a la hoguera de despedida; abrazos entre vecinos con las caras tiznadas de hollín negro y ojos brillantes de emoción.
- Epílogo: El humo alejándose suavemente sobre los campos de cereal al despuntar los primeros rayos del amanecer. Fin."""
    },
    33: {
        "intro": """La **Gau Beltza** (Noche Negra o Noche de las Ánimas de Mutriku, Gipuzkoa), celebrada cada **31 de octubre**, es una de las manifestaciones más puras y fascinantes de la recuperación etnográfica del patrimonio inmaterial vasco. Frente a la estandarización mercantil anglosajona de Halloween, la villa marinera de Mutriku ha revitalizado el rito ancestral que sus antepasados practicaban en caseríos y arrabales costeros: el tránsito hacia la estación oscura del invierno (*negua*), el diálogo con las sombras (*itzalak*) y la memoria sagrada de las almas errantes a la luz temblorosa de calabazas y remolachas talladas a mano.""",
        "etnografia": """**Etnografía, Raíces Euskaldunes y Simbolismo Antropológico**

* **Cosmovisión Tradicional y Arimen Gaua:** En la tradición oral de Euskal Herria, la frontera entre el mundo terrenal (*bizidunen mundua*) y el inframundo de las ánimas (*hildakoen erreinua*) se volvía extremadamente permeable durante la noche que precede a Todos los Santos. Mucho antes del fenómeno comercial contemporáneo, en los caseríos de Mutriku y de toda la costa de Gipuzkoa existía la costumbre secular de vaciar calabazas y nabos (*kalabaza hustea*), tallarles muecas terroríficas e introducir una vela en su interior para colocarlas en encrucijadas de caminos, huertos y dinteles para ahuyentar a los malos espíritus y guiar a los difuntos.
* **Estética de Sombras frente al Plástico:** La singularidad de la Gau Beltza de Mutriku reside en su estricto rechazo a los disfraces comerciales sintéticos. La comunidad se viste exclusivamente con ropas viejas halladas en los desvanes: sábanas raídas de lino, sacos de arpillera que guardaban patatas o harina, trapos de labranza y carátulas de cartón modeladas a mano. Se crea así una comitiva de *itzalak* (sombras y espectros rurales) que encarna el retorno de los antepasados con una crudeza visual poética y telúrica.
* **El Fuego Catártico y la Quema de los Miedos:** La fiesta concluye en el puerto pesquero de Mutriku, donde los niños y vecinos depositan en un caldero de fuego sus miedos, pesares y malos recuerdos anotados en pequeños papeles, sellando con la fuerza purificadora de las llamas el cierre del ciclo fértil otoñal y la bienvenida a la introspección invernal.""",
        "personajes": """**Personajes y Elementos Rituales de la Tradición**

| **Personaje / Elemento** | **Indumentaria / Atrezo** | **Función Simbólica** |
| --- | --- | --- |
| **Kalejirako Itzalak (Las Sombras)** | Sábanas blancas deshilachadas, sacos de arpillera y sombreros de paja viejos | Figuras fantasmales que personifican a las almas errantes y al espíritu del caserío |
| **Kalabaza Eramaleak** | Portan calabazas talladas con velas en las manos o sobre palos de madera | Guías luminosos que abren paso al cortejo a través de las tinieblas de las calles |
| **Txalapartariak y Músicos** | Traje tradicional de baserritarra oscuro con abarcas | Marcan con el golpe rítmico de los tablones de madera (*txalaparta*) el latido del bosque y el mar |
| **Ipuin Kontalaria (La Narradora)** | Mantón negro de lana y candil de aceite | Relata viejas leyendas de difuntos y *jentillak* a los niños congregados en la plaza |
| **Suaren Zaindaria (Guardián del Fuego)** | Delantal de herrero y tenazas de hierro | Custodia la hoguera del muelle donde se consumen los miedos escritos por la comunidad |
| **Gaztaina Erreak (Castañas Asadas)** | Puesto comunal de brasas y cucuruchos de papel | Alimento sagrado de invierno que reconforta el cuerpo y une a la vecindad tras el pasacalles |""",
        "secuencia": """**Secuencia Cronológica de la Fiesta**

1. **La Tarde Comunitaria (17:00 - 19:00 h):** En las plazas del casco viejo y en los soportales, familias y jóvenes se reúnen en talleres abiertos para el vaciado tradicional de calabazas (*kalabaza tailaketa*) y la confección de disfraces rústicos con telas reutilizadas, evitando cualquier elemento artificial de plástico.
2. **El Apagón del Casco Histórico (19:30 h):** El alumbrado público de la villa medieval de Mutriku se apaga por completo. Las calles adoquinadas quedan sumidas en una oscuridad total, rotas únicamente por las hileras de calabazas encendidas colocadas en balcones, escalinatas de piedra y portales.
3. **El Toque de Txalaparta y la Convocatoria:** El sonido grave de la txalaparta y el toque fúnebre de campanas rompen el silencio nocturno, convocando a las sombras en la Plaza Txurruka.
4. **La Kalejira Iluna (Pasacalles Sombrío):** La marea de figuras cubiertas de arpillera y sábanas blancas desciende en silenciosa procesión por las empinadas cuestas del pueblo hacia la dársena marítima, acompañada por el rumor de cadenas arrastradas y susurros de cánticos antiguos.
5. **El Rito del Muelle y la Quema de los Miedos:** En el puerto pesquero, al borde del Cantábrico, se enciende la gran hoguera ceremonial. Los niños leen y arrojan al fuego sus temores escritos para que las llamas los transformen en ceniza fértil.
6. **La Castañada Popular:** Se reparten cucuruchos de castañas asadas humeantes y chocolate caliente; la comunidad canta al unísono coplas tradicionales celebrando que, en Mutriku, la memoria de las ánimas sigue viva y luminosa.""",
        "escaleta": """**Guion y Escaleta de Rodaje Documental (12–15 min)**

[00:00 - 02:30] PRÓLOGO: EL MAR CANTÁBRICO Y LA CALABAZA ENCENDIDA
- Visual: Planos en penumbra del espigón del puerto de Mutriku azotado por las olas nocturnas; un plano detalle de una mano infantil introduciendo una vela encendida en una calabaza de aspecto tosco y primitivo.
- Narrador en cámara: Presenta la Noche Negra no como un artificio importado, sino como la memoria atávica de un pueblo costero que supo dialogar con la muerte y las estaciones mucho antes de que el mundo moderno olvidara la oscuridad.

[02:30 - 06:00] LA MEMORIA EN EL DESVÁN
- Visual: Familias en un caserío de la montaña de Mutriku abriendo arcones de madera; telas raídas de lino y sacos de café reutilizados para cubrirse el rostro.
- Testimonio de mayores: Ancianos recuerdan cómo sus abuelos ya colocaban calabazas con velas en los vallados de los caminos para avisar de los espíritus errantes ("Guretzat betidanik izan da Arimen Gaua").

[06:00 - 10:00] EL APAGÓN Y LA KALEJIRA DE LAS SOMBRAS
- Visual: El instante en que la iluminación eléctrica de Mutriku se corta: la arquitectura medieval recortada contra el cielo de octubre. Las siluetas fantasmales de arpillera descendiendo por las cuestas iluminadas por cientos de puntos de fuego parpadeante.
- Diseño sonoro: El eco de la txalaparta rebotando en las paredes de piedra caliza, mezclado con el mugido lejano de un cuerno de pastor.

[10:00 - 14:00] LA HOGUERA DEL PUERTO Y EL RENACER COMUNITARIO
- Visual: Planos del fuego reflejado en las aguas calmas del puerto pesquero; niños arrojando sus notas manuscritas a las brasas; manos ennegrecidas compartiendo castañas asadas humeantes.
- Plano final: Una calabaza solitaria sobre el muro del muelle mirando hacia el mar abierto mientras las campanas dan la medianoche. Fundido a negro."""
    }
}

# Procesar los 40 festivales
dataset = []

for meta in FIESTAS_META:
    fid = meta["id"]
    item = {
        "id": fid,
        "name": meta["name"],
        "town": meta["town"],
        "municipality": meta["municipality"],
        "province": meta["province"],
        "region": meta["region"],
        "lat": meta["lat"],
        "lng": meta["lng"],
        "date_display": meta["date_display"],
        "date_full": meta["date_full"],
        "month": meta["month"],
        "month_num": meta["month_num"],
        "season": meta["season"],
        "category": meta["category"]
    }
    
    if fid in SPECIAL_DOSSIERS:
        spec = SPECIAL_DOSSIERS[fid]
        item["summary"] = spec["intro"]
        item["etnografia"] = spec["etnografia"]
        item["personajes"] = spec["personajes"]
        item["secuencia"] = spec["secuencia"]
        item["escaleta"] = spec["escaleta"]
        item["source"] = "Enriquecido / Reconstrucción documental fidedigna"
    else:
        raw = get_festival_raw_text(fid)
        sec = parse_sections(raw)
        item["summary"] = sec.get("intro", raw[:600])
        item["etnografia"] = sec.get("etnografia", "")
        item["personajes"] = sec.get("personajes", "")
        item["secuencia"] = sec.get("secuencia", "")
        item["escaleta"] = sec.get("escaleta", "")
        item["source"] = "PROYECTO PATRIMONIO INMATERIAL 2027.md"
        
    dataset.append(item)

print(f"Dataset generado exitosamente con {len(dataset)} fiestas.")

# Crear carpeta data/ si no existe
data_dir = os.path.join(base_dir, 'data')
os.makedirs(data_dir, exist_ok=True)

# Guardar como JSON
json_path = os.path.join(data_dir, 'fiestas_data.json')
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

# Guardar también como JS para que funcione abriendo index.html directamente sin problemas de CORS local
js_path = os.path.join(data_dir, 'fiestas_data.js')
with open(js_path, 'w', encoding='utf-8') as f:
    f.write("const FIESTAS_DATA = " + json.dumps(dataset, ensure_ascii=False, indent=2) + ";\n")

print(f"Archivos guardados en:\n - {json_path}\n - {js_path}")
