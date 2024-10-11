def totaldereportes ():
        tam = os.path.getsize(archivo_fisico_reportes)
        archivo_logico_reportes.seek (0,0)
        variable = pickle.load (archivo_logico_reportes)
        tamreg = archivo_logico_reportes.tell()
        cantreg = tam // tamreg
        return cantrep
def totaldereportesignorados()
	repignorados=0
    for i in range(len(tamreg)):
        if estadoreporte[i] == 2:
            repignorados=repignorados+1
    return repignorados
    porcentajerepignorados=cantreg/repignorados
    return porcentajerepignorados
