# Para ocultar los caracteres
import getpass
# Para limpiar la consola y para manipular archivos
import os
# Para usar delay
from time import sleep
# Para ruleta y generación de likes en matriz
import random
# Para calcular la edad
from datetime import datetime
# Para manipular archivos
import os.path
import pickle
import io

import os
import os.path
import pickle
import io

class estudiantes:
	def __init__(self):
		self.email=email
		self.nombre=nombre
		self.sexo=sexo
		self.contraseña=contraseña
		self.estado=estado
		self.hobbies=hobbies
		self.materia_fav=materia_fav
		self.deporte_fav=deporte_fav
		self.materia_fuerte=materia_fuerte
		self.materia_debil=materia_debil
		self.biografia=biografia
		self.pais=pais
		self.ciudad=ciudad
		self.fecha_nacimiento=fecha_nacimiento

class moderadores:
	def __init__(self):
		self.email=email
		self.contraseña=contraseña
		self.estado=estado

class administradores:
	def __init__(self):
		self.email=email
		self.contraseña=contraseña

def verificar_archivo(path,tipo):
	if os.path.exists(path):
		archivo_log=open(path,"r+b")
	else:
		archivo_log=open(path,"w+b")

def main():
	print("Esto")
	print(os.getcwd()+)
	s=input()

def inicializar():

	archivo_fisico_estudiantes= os.getcwd()+"estudiantes.dat"
	archivo_fisico_administradores= os.getcwd()+"administradores.dat"
	archivo_fisico_moderadores= os.getcwd()+"moderadores.dat"	

	if os.path.exists(archivo_log):
        archivo_log = open(archivo_fisico, "r+b")
    else:
		archivo_log = open(archivo_fisico, "w+b")

main()

