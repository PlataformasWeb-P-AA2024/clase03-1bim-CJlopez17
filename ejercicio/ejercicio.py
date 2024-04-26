import csv

archivo = open ('data/Listado-Instituciones-Educativas-distribuidas-por-zona-distrito-y-circuito.csv')

lineas = archivo.readLines()

encabezado = lineas[0]
linea = lineas[1]

encabezado = encabezado.split["|"]
linea = linea.split["|"]

archivo.close()

pagina = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
    <meta charset = "utf-8">
    <title>Información de Institución</title>
</head>
<body>
    
</body>
"""