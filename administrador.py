def totaldereportes ():
        tam = os.path.getsize(archivo_fisico_reportes)
        archivo_logico_reportes.seek (0,0)
        variable = pickle.load (archivo_logico_reportes)
        tamreg = archivo_logico_reportes.tell()
        cantreg = tam // tamreg
        return cantrep
def totaldereportesignorados()
	tam=os.path.getsize(archivo_fisico_reportes)
	pos=0
	archivo_logico_reportes.seek (0,0)
    variable=pickle.load(archivo_logico_reportes)
    while archivo_logico_reportes.tell()<tam 
    	pos=archivo_logico_reportes.tell()
    	variable=pickle.load(archivo_logico_reportes)
