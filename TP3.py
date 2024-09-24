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

class estudiantes:
	def __init__(self):
		self.email=""
		self.nombre=""
		self.sexo=""
		self.contraseña=""
		self.estado=""
		self.hobbies=""
		self.materia_fav=""
		self.deporte_fav=""
		self.materia_fuerte=""
		self.materia_debil=""
		self.biografia=""
		self.pais=""
		self.ciudad=""
		self.fecha_nacimiento=""

#Crear metodo para formatear los strings?
#Es para que todos los registros sean del mismo tamaño

	def formato(self):
		self.email=self.email.ljust(32)
		self.nombre=self.nombre.ljust(32)
		self.contraseña=self.contraseña.ljust(32)
		self.hobbies=self.hobbies.ljust(255)
		self.materia_fav=self.materia_fav.ljust(16)
		self.deporte_fav=self.deporte_fav.ljust(16)
		self.materia_fuerte=self.materia_fuerte.ljust(16)
		self.materia_debil=self.materia_debil.ljust(16)
		self.biografia=self.biografia.ljust(16)
		self.pais=self.pais.ljust(32)
		self.ciudad=self.ciudad.ljust(32)
		self.fecha_nacimiento=self.fecha_nacimiento.ljust(10)
		
class moderadores:
	def __init__(self):
		self.email=""
		self.contraseña=""
		self.estado=""

class administradores:
	def __init__(self):
		self.email=""
		self.contraseña=""

def verificar_archivo(path):
	if os.path.exists(path):
		archivo_log=open(path,"r+b")
	else:
		archivo_log=open(path,"w+b")
	return archivo_log

def inicializar_arr(arreglo,tamaño):
	arreglo=[None]*tamaño
	for i in range(tamaño):
		arreglo[i]=administradores()

	

def cargar_archivo_administradores(path):
	global archivo_logico_administradores
	archivo_logico_administradores.seek(0,0)
	administrador=administradores()
	administrador.email="Prueba@utn.edu.ar"
	#Hay que ajustar todos los string con el mismo "Largo" para que todos los registros sean del mismo tamaño.
	administrador.email=administrador.email.ljust(32)
	administrador.contraseña="123456"
	administrador.contraseña=administrador.contraseña.ljust(32)
	pickle.dump(administrador,archivo_logico_administradores)
	archivo_logico_administradores.flush()
	archivo_logico_administradores.close()


def main():
	global archivo_logico_administradores
	global arr_estudiantes
	global arr_administradores
	global arr_moderadores
	archivo_fisico_estudiantes= os.getcwd()+"\\estudiantes.dat"
	archivo_fisico_administradores= os.getcwd()+"\\administradores.dat"
	archivo_fisico_moderadores= os.getcwd()+"\\moderadores.dat"
	archivo_logico_estudiantes=verificar_archivo(archivo_fisico_estudiantes)
	archivo_logico_administradores=verificar_archivo(archivo_fisico_administradores)
	archivo_logico_moderadores=verificar_archivo(archivo_fisico_moderadores)
	#arr_estudiantes=inicializar_arr(arr_estudiantes,8,estudiantes)
	arr_administradores=inicializar_arr(arr_administradores,4)
	#arr_moderadores=inicializar_arr(arr_moderadores,4,moderadores)
	cargar_archivo_administradores(archivo_fisico_administradores)

arr_estudiantes=[]
arr_administradores=[]
arr_moderadores=[]

main()

def print_menu_inicio():
    print("0. Salir")
    print("1. Login")
    print("2. Registrarse")


