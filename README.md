# Patrimonio Inmaterial 2027 🇪🇸
### Atlas Cartográfico Interactivo de Fiestas, Mascaradas y Rituales Tradicionales de España

Aplicación web interactiva desarrollada para documentar, geolocalizar y divulgar **40 de las manifestaciones rituales y festivas más singulares del patrimonio cultural inmaterial de España**. 

Al hacer clic sobre cualquiera de las fiestas situadas en el mapa, se despliega en el lateral derecho un dossier etnográfico exhaustivo que incluye:
- 📜 **Etnografía y Raíz Antropológica**: Origen histórico, etimología, funciones propiciatorias y significado simbólico.
- 🎭 **Personajes y Atrezo**: Tabla con los personajes rituales, indumentaria tradicional y roles comunitarios.
- ⏳ **Secuencia del Rito**: Cronología paso a paso del desarrollo festivo.
- 🎬 **Guion Documental (12–15 min)**: Escaleta audiovisual profesional con códigos de tiempo, propuestas visuales y notas de diseño sonoro.

---

## 🚀 Despliegue Inmediato en GitHub Pages

Este proyecto es una aplicación web 100% estática (HTML5 + CSS + JavaScript Vanilla + GeoJSON). **No requiere Node.js, compilación ni configuración de servidor**. Para publicarlo gratuitamente en GitHub Pages:

### Paso 1: Subir el proyecto a GitHub
Abre una terminal (PowerShell o Git Bash) en la carpeta del proyecto y ejecuta:

```powershell
# 1. Inicializar git si no lo habías hecho
git init

# 2. Añadir todos los archivos y crear el primer commit
git add .
git commit -m "feat: publicación inicial del mapa interactivo de patrimonio 2027"

# 3. Vincular con tu repositorio en GitHub
git branch -M main
git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git

# 4. Subir la rama principal
git push -u origin main
```

### Paso 2: Activar GitHub Pages en el repositorio
1. Entra a tu repositorio en GitHub desde el navegador: `https://github.com/TU_USUARIO/TU_REPOSITORIO`.
2. Ve a la pestaña **Settings** (Configuración) en la parte superior.
3. En el menú lateral izquierdo, haz clic en **Pages**.
4. En el apartado **Build and deployment**:
   - **Source**: `Deploy from a branch`
   - **Branch**: selecciona `main` y en la carpeta elige `/ (root)`.
5. Haz clic en **Save** (Guardar).

En aproximadamente **1 minuto**, GitHub Pages publicará tu web en:
`https://TU_USUARIO.github.io/TU_REPOSITORIO/`

---

## 💻 Ejecución en Local

Puedes visualizar y probar la aplicación en tu propio ordenador de dos formas:

1. **Apertura directa**:
   Haz doble clic sobre el archivo [`index.html`](index.html) para abrirlo directamente en tu navegador (Chrome, Edge, Firefox, Safari).
2. **Servidor HTTP local**:
   ```powershell
   python -m http.server 8000
   ```
   Y abre en tu navegador: `http://localhost:8000`.

---

## 🗺️ Características Técnicas y Cartográficas

- **Cartografía Oficial de Fondo**:
  - 🗺️ **Mapa Oficial IGN (España)**: Conexión con los servicios WMTS del Instituto Geográfico Nacional de España con orografía, carreteras, municipios y relieve sin marcas de agua ni necesidad de API Keys.
  - ⛰️ **Relieve Físico (Esri Topo)**: Capa alternativa con sombreado de relieve orográfico.
- **División Provincial y Comunal Vectorial**:
  - Incorpora polígonos GeoJSON con las 52 provincias y 19 comunidades autónomas de España con efectos de sombreado y *hover* interactivo que indica las fiestas catalogadas en cada provincia.
- **Recuadro Inset de Canarias (Fiesta #36)**:
  - En la esquina inferior izquierda se sitúa el recuadro cartográfico dedicado a las Islas Canarias con la fiesta de **Las Tablas de San Andrés** en Icod de los Vinos (Tenerife). Se oculta y muestra de forma reactiva según los filtros activos.
- **Buscador y Filtros Dinámicos**:
  - Búsqueda en tiempo real por texto (nombre, municipio, provincia o palabras clave como *fuego*, *mascarada*, *toro*, *vino*).
  - Filtro por **Estación** (Invierno, Primavera, Verano, Otoño).
  - Filtro por **Mes** (Enero a Diciembre).
  - Filtro por **Categoría ritual** (*Mascaradas*, *Ritos de Fuego*, *Taurinas*, *Ecuestres*, *Batallas Dionisíacas*, *Romerías*, *Danzas*, *Ánimas*).
- **Navegación Secuencial**:
  - Botones de salto `← Anterior` y `Siguiente →` para recorrer las 40 fiestas en orden cronológico anual.

---

## 📋 Catálogo de las 40 Fiestas

| N.º | Fiesta | Municipio / Comarca | Provincia | Fecha | Tipología Ritual |
|:---:|---|---|---|---|---|
| **1** | La Vijanera | Silió (Molledo) | Cantabria | 3 ENE | Mascarada de Invierno |
| **2** | Las Luminarias | San Bartolomé de Pinares | Ávila | 16 ENE | Ritos de Fuego y Purificación |
| **3** | El Jarramplas | Piornal (Valle del Jerte) | Cáceres | 19–20 ENE | Mascarada y Rito Catártico |
| **4** | Carnaval del Toro | Ciudad Rodrigo | Salamanca | 5–9 FEB | Carnavales y Fiestas Taurinas |
| **5** | Festa da Arribada | Baiona | Pontevedra | 5–7 MAR | Recreación Histórica Marítima |
| **6** | Las Fallas | Valencia | Valencia | 15–19 MAR | Ritos de Fuego y Arte Efímero |
| **7** | Danza de la Muerte | Verges (Baix Empordà) | Girona | 25 MAR | Semana Santa y Danza Macabra |
| **8** | Rompida de la Hora | Calanda (Bajo Aragón) | Teruel | 26 MAR | Ritos Sonoros y Tamboradas |
| **9** | Las Mondas | Talavera de la Reina | Toledo | 28 MAR – 3 ABR | Ritos de Primavera y Ofrenda Agraria |
| **10** | Moros y Cristianos | Alcoy / Alcoi | Alicante | 24–26 ABR | Alardes Bélicos y Fiestas Históricas |
| **11** | Los Caballos del Vino | Caravaca de la Cruz | Murcia | 1–5 MAY | Ritos Ecuestres y Bordados |
| **12** | La Caballada | Atienza | Guadalajara | 16 MAY | Hermandades y Caballería Histórica |
| **13** | Feria de Córdoba | Córdoba | Córdoba | 22–29 MAY | Ferias de Primavera y Flamenco |
| **14** | La Patum de Berga | Berga (Berguedà) | Barcelona | 26–30 MAY | Teatro Místico y Pirotecnia Medieval |
| **15** | El Colacho | Castrillo de Murcia | Burgos | 6 JUN | Ritos de Paso y Protección Infantil |
| **16** | Cerdo de San Antón | La Alberca (Sierra de Francia) | Salamanca | 13 JUN | Ritos Comunitarios Ganaderos |
| **17** | San Juan de Ciutadella | Ciutadella de Menorca | Baleares | 23–24 JUN | Fiestas Ecuestres y Ritos Solsticiales |
| **18** | Batalla del Vino | Haro (Riscos de Bilibio) | La Rioja | 29 JUN | Romerías Lúdicas y Dionisíacas |
| **19** | A Rapa das Bestas | Sabucedo (A Estrada) | Pontevedra | 1–5 JUL | Doma Tradicional y Fuerza Física |
| **20** | San Fermín | Pamplona / Iruña | Navarra | 6–14 JUL | Encierros y Ritos Taurinos |
| **21** | Vaquilla del Ángel | Teruel | Teruel | 9–12 JUL | Toros Ensogados y Ritos de Peña |
| **22** | Danza de los Zancos | Anguiano | La Rioja | 21–23 JUL | Danzas Tradicionales y Vértigo Ritual |
| **23** | Procesión de los Ataúdes | Santa Marta de Ribarteme (As Neves) | Pontevedra | 29 JUL | Romerías Votivas y Tanatología |
| **24** | Descenso y Aquasella | Arriondas / Ribadesella | Asturias | 6–16 AGO | Ritos Fluviales y Piragüismo |
| **25** | Descenso del Nalón | Pola de Laviana | Asturias | 21 AGO | Carnaval Acuático Popular |
| **26** | La Tomatina | Buñol | Valencia | 25 AGO | Batallas Incruentas de Verano |
| **27** | El Cipotegato | Tarazona | Zaragoza | 27 AGO | Arlequines y Chivos Expiatorios |
| **28** | Fiestas Patronales | Morata de Tajuña | Madrid | 29 AGO – 13 SEPT | Encierros y Fiestas de Vega |
| **29** | Fiestas de la Mercè | Barcelona | Barcelona | 23–26 SEPT | Castells, Bestiario y Fuego Urbano |
| **30** | El Vítor de Mayorga | Mayorga de Campos | Valladolid | 27 SEPT | Ritos de Fuego y Pellejos Ardientes |
| **31** | Fiestas del Pilar | Zaragoza | Zaragoza | 9–17 OCT | Ofrendas Florales y Comparsas |
| **32** | As San Lucas | Mondoñedo | Lugo | 17–20 OCT | Ferias de Ganado Caballar |
| **33** | **Gau Beltza** | **Mutriku (Debabarrena)** | **Gipuzkoa** | **31 OCT** | **Noche de Ánimas y Mitología Vasca** |
| **34** | Humanitarios de S. Martín | Moreda de Aller | Asturias | 11 NOV | Cohesión Vecinal y Fabada Tradicional |
| **35** | Fiesta del Orujo | Potes (Valle de Liébana) | Cantabria | 13 NOV | Alquitaras y Destilación Tradicional |
| **36** | Tablas de San Andrés | Icod de los Vinos | S.C. Tenerife | 28–30 NOV | Arrastre de Tablas y Vino Nuevo |
| **37** | Los Escobazos | Jarandilla de la Vera | Cáceres | 7 DIC | Ritos de Fuego y Saludos de Retama |
| **38** | El Zangarrón | Sanzoles (Tierra del Vino) | Zamora | 25–26 DIC | Mascaradas de Invierno y Quintos |
| **39** | El Tafarrón | Pozuelo de Tábara | Zamora | 25–26 DIC | Mascaradas de Invierno y Ritos de Paso |
| **40** | Els Enfarinats | Ibi (L'Alcoià) | Alicante | 28 DIC | Fiesta de Inocentes e Inversión Social |

> 📌 **Reconstrucción documental**: La fiesta **n.º 33: Gau Beltza (Mutriku)**, presente en el mapa original pero ausente en el texto base, fue reconstruida con todo el rigor antropológico, tabla de personajes y escaleta audiovisual. Asimismo, las fiestas **#17, #20, #29 y #30** fueron desarrolladas a partir de sus menciones en el *Bonus Track*.

---

## 📂 Estructura del Repositorio

```text
proyecto_patrimonio/
├── index.html                   # Aplicación web completa interactiva
├── README.md                    # Documentación del proyecto y guía de despliegue
├── .gitignore                   # Exclusiones de archivos temporales y entornos
│
├── data/
│   ├── fiestas_data.js          # Dataset de las 40 fiestas con coordenadas y dossiers (JS)
│   ├── fiestas_data.json        # Dataset estructurado en JSON
│   ├── spain_provinces.js       # Polígonos GeoJSON de las 52 provincias de España
│   └── spain_communities.js     # Polígonos GeoJSON de las 19 Comunidades Autónomas
│
├── scripts/
│   ├── build_dataset.py         # Script ETL que procesa los archivos markdown originales
│   ├── test_locations.py        # Validador geográfico (point-in-polygon de las 40 fiestas)
│   ├── test_slice.py            # Validador de corte y parseo documental
│   └── verify.py                # Comprobación de integridad del dataset
│
└── .references/                 # Archivos originales de referencia
    ├── MAPA PROYECTO PATRIMONIO.md
    └── PROYECTO PATRIMONIO INMATERIAL 2027.md
```

---

## 📜 Licencias y Reconocimientos

- **Cartografía base**: [Instituto Geográfico Nacional de España (IGN)](https://www.ign.es) bajo licencia CC-BY 4.0 / Esri World Topographic Map.
- **División administrativa GeoJSON**: Datos cartográficos abiertos de provincias y comunidades autónomas de España.
- **Librerías de código abierto**: [Leaflet.js](https://leafletjs.com/), [Tailwind CSS](https://tailwindcss.com/), [Lucide Icons](https://lucide.dev/), [Marked.js](https://marked.js.org/).
