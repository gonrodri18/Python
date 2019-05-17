# Escribir un programa que abra el fichero con información sobre el PIB per cápita de los países de la Unión Europea (url:https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true), pregunte por las iniciales de un país y muestre el PIB per cápita de ese país de todos los años disponibles.

f = open('datos.webarchive', 'r')
contenido = f.readlines()
for i in range (len(contenido)):
    line=contenido[i]. split('\t')
    #print(linea[0])
#Pais = input('Iniciales de un país de la UE:')





