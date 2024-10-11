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



def contador_reportes (condicion):
    tam = os.path.getsize(archivo_fisico_reportes)
    archivo_logico_reportes.seek (0,0)
    contador = 0
    while archivo_logico_reportes.tell() < tam:
        variable = pickle.load(archivo_logico_reportes)
        if variable.estadoreporte == condicion:
                contador = contador + 1
    return contador
