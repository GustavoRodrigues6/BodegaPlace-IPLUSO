from manage_wine import insert_wine

WINES = [
    {"Brand": "Vinho do Porto", "Year": 2015, "Price": 25.0, "Region": "Douro", "Description": "Um vinho fortificado, doce e encorporado", "Nutrition": 20, "Supplier": 74354, "Stock": 23 },
    {"Brand": "Château Margaux", "Year": 2018, "Price": 450.0, "Region": "Bordeaux", "Description": "Elegante e encorpado, com notas de frutas vermelhas", "Nutrition": 14, "Supplier": 33324, "Stock": 124 },
    {"Brand": "Penfolds Grange", "Year": 2020, "Price": 700.0, "Region": "Barossa Valley", "Description": "Frutas escuras e taninos sedosos", "Nutrition": 15, "Supplier": 56257, "Stock": 85 },
    {"Brand": "Antinori Tignanello", "Year": 2019, "Price": 120.0, "Region": "Toscana", "Description": "Blend sofisticado com toques de baunilha", "Nutrition": 13.5, "Supplier": 56458, "Stock": 320 },
    {"Brand": "Almaviva", "Year": 2021, "Price": 150.0, "Region": "Valle Central", "Description": "Notas de especiarias e frutas maduras", "Nutrition": 14.5, "Supplier": 78589, "Stock": 215 },
    {"Brand": "Vega Sicilia Único", "Year": 2016, "Price": 500.0, "Region": "Ribera del Duero", "Description": "Vinho espanhol icônico com maturação longa", "Nutrition":1, "Supplier": 99876, "Stock": 78 },
    {"Brand": "Opus One", "Year": 2017, "Price": 350.0, "Region": "Napa Valley", "Description": "Aromas complexos de frutos vermelhos e carvalho", "Nutrition": 14.5, "Supplier": 23342, "Stock": 90 },
    {"Brand": "Sassicaia", "Year": 2018, "Price": 250.0, "Region": "Bolgheri", "Description": "Notas minerais e taninos refinados", "Nutrition": 13.5, "Supplier": 11129, "Stock": 180 },
    {"Brand": "Don Melchor", "Year": 2021, "Price": 120.0, "Region": "Maipo Valley", "Description": "Frutas negras e toque de chocolate amargo", "Nutrition": 14.5, "Supplier": 44560, "Stock": 400 },
    {"Brand": "Montes Alpha M", "Year": 2021, "Price": 80.0, "Region": "Colchagua Valley", "Description": "Blend potente e equilibrado", "Nutrition": 15, "Supplier": 34437, "Stock": 530 },
    {"Brand": "Barolo Riserva", "Year": 2017, "Price": 200.0, "Region": "Piemonte", "Description": "Aromas intensos e taninos marcantes", "Nutrition": 14, "Supplier": 20215, "Stock": 150 },
    {"Brand": "Châteauneuf-du-Pape", "Year": 2019, "Price": 90.0, "Region": "Ródano", "Description": "Frutas vermelhas maduras com notas de especiarias", "Nutrition": 14, "Supplier": 64278, "Stock": 275 },
    {"Brand": "Carmelo Patti", "Year": 2018, "Price": 60.0, "Region": "Mendoza", "Description": "Vinho argentino com notas de ameixas e cerejas", "Nutrition": 13.5, "Supplier": 34438, "Stock": 350 },
    {"Brand": "Quinta do Crasto", "Year": 2020, "Price": 35.0, "Region": "Douro", "Description": "Vinho português robusto e aromático", "Nutrition": 14, "Supplier": 76643, "Stock": 1900 },
    {"Brand": "Meerlust Rubicon", "Year": 2019, "Price": 50.0, "Region": "Stellenbosch", "Description": "Blend sul-africano com notas de cassis e tabaco", "Nutrition": 14.5, "Supplier": 49802, "Stock": 500 },
    {"Brand": "Catena Zapata Adrianna", "Year": 2018, "Price": 180.0, "Region": "Mendoza", "Description": "Elegância e equilíbrio com toque mineral", "Nutrition": 14, "Supplier": 94386, "Stock": 130 },
    {"Brand": "Clos Apalta", "Year": 2019, "Price": 200.0, "Region": "Colchagua Valley", "Description": "Frutas maduras e especiarias exóticas", "Nutrition": 15, "Supplier": 12653, "Stock": 230 },
    {"Brand": "Torres Mas La Plana", "Year": 2020, "Price": 70.0, "Region": "Penedès", "Description": "Aromas florais e de frutas negras", "Nutrition": 14.5, "Supplier": 42983, "Stock": 400 },
    {"Brand": "Beringer Private Reserve", "Year": 2018, "Price": 150.0, "Region": "Napa Valley", "Description": "Notas de cerejas pretas e mocha", "Nutrition": 15, "Supplier": 54309, "Stock": 120 },
    {"Brand": "Croft Vintage Port", "Year": 2016, "Price": 120.0, "Region": "Douro", "Description": "Vinho do Porto de caráter intenso e encorpado", "Nutrition": 20, "Supplier": 22200, "Stock": 300 },
    {"Brand": "Amarone della Valpolicella", "Year": 2017, "Price": 75.0, "Region": "Vêneto", "Description": "Notas de frutas secas e chocolate", "Nutrition": 15, "Supplier": 31331, "Stock": 600 },
    {"Brand": "Lafite Rothschild", "Year": 2015, "Price": 1000.0, "Region": "Bordeaux", "Description": "Excepcional, com grande potencial de guarda", "Nutrition": 13.5, "Supplier": 23987, "Stock": 50 },
    {"Brand": "Quinta do Vallado", "Year": 2020, "Price": 45.0, "Region": "Douro", "Description": "Frutas maduras e taninos macios", "Nutrition": 14, "Supplier": 75543, "Stock": 320 },
    {"Brand": "Luís Pato Vinha Pan", "Year": 2019, "Price": 35.0, "Region": "Bairrada", "Description": "Vinho português com notas terrosas e florais", "Nutrition": 13.5, "Supplier": 12410, "Stock": 410 },
]
for wine in WINES:
    insert_wine(wine["Brand"], wine["Year"], wine["Price"], wine["Region"], wine["Description"], wine["Nutrition"], wine["Supplier"], wine["Stock"])