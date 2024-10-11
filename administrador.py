def ReportesEstadisticos
	tam=os.path.getsize(archivo_fisico_reportes)	
	archivo_logico_reportes.seek(0,0)
	tamRegistro= pickle.load(archivo_logico_reportes)
	pickle.tell(archivo_logico_reportes)
	CantReportes=tam//archivo_logico_reportes
