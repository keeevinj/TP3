def totaldereportes ():
        tam = os.path.getsize(archivo_fisico_reportes)
        archivo_logico_reportes.seek (0,0)
        variable = pickle.load (archivo_logico_reportes)
        tamreg = archivo_logico_reportes.tell()
        cantreg = tam // tamreg
        return cantrep
def totaldereportesignorados()
	cont=0
	tam=os.path.getsize(archivo_fisico_reportes)
	archivo_logico_reportes.seek (0,0)
	while archivo_logico_reportes.tell()<tam 
		variable=pickle.load(archivo_logico_reportes)
		if variable.estadoreportes == 2:
			cont=cont+1
	return cont
