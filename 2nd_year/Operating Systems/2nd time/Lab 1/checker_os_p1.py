'''
Alberto Garcia Fernandez

Sistemas Operativos - Practica 1 - Llamadas al sistema

Este programa verifica que el formato del entregable de la practica es el correcto (sigue las especificaciones de nombrado, y esta bien comprimido).

Tambien realiza una prueba basica de funcionamiento para cada uno de los tres programas solicitados en la practica. Cumplir esta prueba no es garantia de tener la maxima nota en el ejercicio. Se trata solo de una sugerencia para que los alumnos comprueben el funcionamiento general de su programa. Los alumnos deberan ademas cumplir los otros requisitos del programa, realizar el codigo adecuado, comentarlo, probar casos extremos, y en general cumplir con las demas exigencias descritas en el enunciado de la practica. El programa crea un entorno de prueba en la carpeta /tmp/ssoo/ y crea los siguientes objetos:

Directorio dirC
Directorio dirA
Fichero f_empty.txt (vacio)
Fichero	f_aes.txt (contiene "AAAAA")
Copia de los ficheros fuente del alumno.
Ejecutables compilados a partir de los ficheros fuente del alumno.

Con todos estos objetos, realiza pruebas basicas del mywc, myls y myenv
'''
import subprocess
import signal
import os
import glob
import time
import sys
import shutil

resultString=""
result=0

def normalizeOutput(result):
	'''
	Funcion que normaliza una cadena de entrada con el fin de eliminar errores de formato. Reemplaza saltos de linea por tabuladores y elimina espacios repetidos y espacios al principio y final
	'''

	result = result.decode('ascii')

	result = result.replace("\r\n","\n");
	result = result.replace("\r","\n");
	resultList = result.split("\n")
	resultNormalized = ""
	for resultLine in resultList:
		if resultLine == "":
			continue
		resultLine = resultLine.replace("\t", " ")
		resultLine = resultLine.replace("  ", " ")
		resultLine = resultLine.strip()
		resultNormalized += (resultLine + "\t")

	resultNormalized = resultNormalized.strip()

	return resultNormalized


def lookForTargetFile(folder,targetFile):
	'''
	Funcion que busca un fichero objetivo en una carpeta y devuelve su ruta
	'''
	toReturn="-"
	found=False
	subfolders=[x[0] for x in os.walk(folder)]
	for innerFolder in subfolders:
		folders=os.listdir(innerFolder)
		for item in folders:
			if item.lower()==targetFile.lower():
				return innerFolder+"/"+item
	return toReturn
	

def checkTargetFile(folder,targetFile):
	'''
	Funcion que comprueba que un fichero objetivo existe. Si no existe, lo intenta buscar en las carpetas hijas.
	'''
	toReturn="-"
	filePath=folder+targetFile
	if not os.path.exists(filePath):
		toReturn=lookForTargetFile(folder,targetFile)
	else:
		toReturn=filePath
	return toReturn



def testExerciseWC(folder):
	'''
	Funcion que realiza la prueba sugerida del programa mywc
	'''

	global resultString 
	global result
	global minipunto
	#Definimos los nombres del fichero de codigo fuente, programa y fichero de prueba
	targetFile="mywc.c"
	programFile="mywc"
	
	#Buscamos el fichero fuente
	filePath=checkTargetFile(folder,targetFile)
	if filePath=="-":
		print ("CHECKER:", targetFile, "not found")
		return "-"
	
	#Compilamos el fichero fuente
	programPath=folder+programFile
	compiled=subprocess.call(["gcc", filePath,"-o", programPath])
	if compiled != 0:
		print ("CHECKER:", "Compile error", targetFile)
		return "-"

	#Realizamos la prueba sugerida (wc <fichero>)
	result1 = subprocess.check_output(["wc", folder+testFile])

	#Ejecutamos el programa del alumno
	cmd = programPath + " " + folder+testFile
	pro = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True, preexec_fn=os.setsid)  
	time.sleep(0.5)
	os.killpg(pro.pid, signal.SIGTERM) 

	result2, stderr = pro.communicate()

	#Obtenemos las salidas de la prueba con la que vamos a comparar y de la ejecucion del programa del alumno
	expectedResult = normalizeOutput(result1)
	obtainedResult = normalizeOutput(result2)

	#Comparamos las salidas e imprimimos resultados
	print ("MYWC CHECKER. Expected output:")
	print (result1.decode('ascii'))
	print ("MYWC CHECKER. Program output:") 
	print (result2.decode('ascii'))

	if result1 == result2:
		print ("MYWC CHECKER. CORRECT TEST")
		resultString += "1 " 
		result += 1
	else:
		print ("MYWC CHECKER. INCORRECT TEST. Outputs differ")
		resultString += "0 "


	#Realizamos la prueba sugerida (wc <fichero empty>)
	result1 = subprocess.check_output(["wc", folder+"f_empty.txt"])

	#Ejecutamos el programa del alumno
	cmd = programPath + " " + folder+"f_empty.txt"
	pro = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True, preexec_fn=os.setsid)
	time.sleep(0.5)
	os.killpg(pro.pid, signal.SIGTERM)

	result2, stderr = pro.communicate()

	#Obtenemos las salidas de la prueba con la que vamos a comparar y de la ejecucion del programa del alumno
	expectedResult = normalizeOutput(result1)
	obtainedResult = normalizeOutput(result2)

	#Comparamos las salidas e imprimimos resultados
	print ("MYWC CHECKER. Expected output:")
	print (result1.decode('ascii'))
	print ("MYWC CHECKER. Program output:")
	print (result2.decode('ascii'))

	if result1 == result2:
		print ("MYWC CHECKER. CORRECT TEST")
		resultString += "1 "
		result += 1
	else:
		print ("MYWC CHECKER. INCORRECT TEST. Outputs differ")
		resultString += "0 "


	#Realizamos la prueba sugerida (wc <fichero que no existe>)
	result1 = 255

	#Ejecutamos el programa del alumno
	cmd = programPath + " " + folder+"notfound.txt"
	pro = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True, preexec_fn=os.setsid)
	time.sleep(0.5)
	os.killpg(pro.pid, signal.SIGTERM)

	result2, stderr = pro.communicate()
	result2 = pro.returncode

	#Comparamos las salidas e imprimimos resultados
	print ("MYWC CHECKER. Expected output:")
	print (result1)
	print ("MYWC CHECKER. Program output:" )
	print (result2)

	if result1 == result2:
		print ("MYWC CHECKER. CORRECT TEST")
		resultString += "1 "
		result += 1
	else:
		print ("MYWC CHECKER. INCORRECT TEST. Outputs differ")
		resultString += "0 "
	#Realizamos la prueba sugerida (wc nofile)
	result1 = 255

	#Ejecutamos el programa del alumno
	cmd = programPath 
	pro = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True, preexec_fn=os.setsid)
	time.sleep(0.5)
	os.killpg(pro.pid, signal.SIGTERM)

	result2, stderr = pro.communicate()
	result2 = pro.returncode

	#Comparamos las salidas e imprimimos resultados
	print ("MYWC CHECKER. Expected output:")
	print (result1)
	print ("MYWC CHECKER. Program output:" )
	print (result2)

	if result1 == result2:
		print ("MYWC CHECKER. CORRECT TEST")
		resultString += "1 "
		result += 1
	else:
		print ("MYWC CHECKER. INCORRECT TEST. Outputs differ")
		resultString += "0 "


def testExerciseLS(folder):
	'''
	Funcion que realiza la prueba sugerida del programa myls
	'''
	global resultString
	global result
	global minipunto
	#Definimos los nombres del fichero de codigo fuente y programa
	targetFile="myls.c"
	programFile="myls"

	#Buscamos el fichero fuente
	filePath=checkTargetFile(folder,targetFile)
	if filePath=="-":
		print ("CHECKER:", targetFile, "not found")
		return "-"

	#Compilamos el fichero fuente
	programPath=folder+programFile
	compiled=subprocess.call(["gcc", filePath,"-o", programPath])
	if compiled != 0:
		print ("CHECKER:", "Compiler error", targetFile)
		return "-"

	#Realizamos la prueba sugerida (ls -f1 <carpeta>)
	result1 = subprocess.check_output(["ls","-f1",folder])

	#Ejecutamos el programa del alumno
	cmd = programPath + " " + folder
	pro = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True, preexec_fn=os.setsid)  
	time.sleep(0.5)
	os.killpg(pro.pid, signal.SIGTERM) 
	result2, stderr = pro.communicate()

	#Obtenemos las salidas de la prueba con la que vamos a comparar y de la ejecucion del programa del alumno
	expectedResult = normalizeOutput(result1)
	obtainedResult = normalizeOutput(result2)

	#Comparamos las salidas e imprimimos resultados
	print ("MYLS CHECKER. Expected output:" )
	print (result1.decode('ascii'))
	print ("MYLS CHECKER. Program output:" )
	print (result2.decode('ascii'))

	if result1 == result2:
		print ("MYLS CHECKER. CORRECT TEST")
		resultString += "1 "
		result += 1
	else:
		print ("MYLS CHECKER. INCORRECT TEST. Outputs differ")
		resultString += "0 "


	#Realizamos la prueba sugerida (ls -f -1 nothing)
	result1 = subprocess.check_output(["ls","-f1"])

	#Ejecutamos el programa del alumno
	cmd = programPath
	pro = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True, preexec_fn=os.setsid)
	time.sleep(0.5)
	os.killpg(pro.pid, signal.SIGTERM)
	result2, stderr = pro.communicate()

	#Obtenemos las salidas de la prueba con la que vamos a comparar y de la ejecucion del programa del alumno
	expectedResult = normalizeOutput(result1)
	obtainedResult = normalizeOutput(result2)

	#Comparamos las salidas e imprimimos resultados
	print ("MYLS CHECKER. Expected output:" )
	print (result1.decode('ascii'))
	print ("MYLS CHECKER. Program output:" )
	print (result2.decode('ascii'))

	if result1 == result2:
		print ("MYLS CHECKER. CORRECT TEST")
		resultString += "1 "
		result += 1
	else:
		print ("MYLS CHECKER. INCORRECT TEST. Outputs differ")
		resultString += "0 "


	#Realizamos la prueba sugerida (ls -f -1 nothing)
	result1 = 255

	#Ejecutamos el programa del alumno
	cmd = programPath+" directory not found"
	pro = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True, preexec_fn=os.setsid)
	time.sleep(0.5)
	os.killpg(pro.pid, signal.SIGTERM)
	result2, stderr = pro.communicate()
	result2 = pro.returncode
	#Obtenemos las salidas de la prueba con la que vamos a comparar y de la ejecucion del programa del alumno

	#Comparamos las salidas e imprimimos resultados
	print ("MYLS CHECKER. Expected output:")
	print (result1)
	print ("MYLS CHECKER. Program output:" )
	print (result2)

	if result1 == result2:
		print ("MYLS CHECKER. CORRECT TEST")
		resultString += "1 "
		result += 1
	else:
		print ("MYLS CHECKER. INCORRECT TEST. Outputs differ")
		resultString += "0 "


def testExerciseISHERE(folder):
	'''
	Funcion que realiza la prueba sugerida del programa myishere
	'''

	global resultString 
	global result
	global minipunto
	#Definimos los nombres del fichero de codigo fuente, programa y fichero de prueba
	targetFile="myishere.c"
	programFile="myishere"
	
	#Buscamos el fichero fuente
	filePath=checkTargetFile(folder,targetFile)
	if filePath=="-":
		print ("CHECKER:", targetFile, "not found")
		return "-"
	
	#Compilamos el fichero fuente
	programPath=folder+programFile
	compiled=subprocess.call(["gcc", filePath,"-o", programPath])
	if compiled != 0:
		print ("CHECKER:", "Compile error", targetFile)
		return "-"

	#Realizamos la prueba sugerida (f1.txt en p1_test)
	result1 = subprocess.check_output(["echo","File f1.txt is in directory p1_test"])

	#Ejecutamos el programa del alumno
	os.chdir(folder)
	cmd = programPath + " p1_test f1.txt"
	pro = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True, preexec_fn=os.setsid)  
	time.sleep(0.5)
	os.killpg(pro.pid, signal.SIGTERM)
	result2, stderr = pro.communicate()

	#Obtenemos las salidas de la prueba con la que vamos a comparar y de la ejecucion del programa del alumno
	obtainedResult = normalizeOutput(result2)

	#Comparamos las salidas e imprimimos resultados
	print ("MYISHERE CHECKER. Expected output:" )
	print (result1.decode('ascii'))
	print ("MYISHERE CHECKER. Program output:" )
	print (result2.decode('ascii'))

	if result1 == result2:
		print ("MYISHERE CHECKER. CORRECT TEST")
		resultString += "1 "
		result += 1
	else:
		print ("MYISHERE CHECKER. INCORRECT TEST. Outputs differ")
		resultString += "0 "


	#Realizamos la prueba sugerida (f1.txt en p1_test)
	result1 = subprocess.check_output(["echo","File f2.txt is not in directory p1_test"])

	#Ejecutamos el programa del alumno
	cmd = programPath  + " p1_test f2.txt"
	pro = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True, preexec_fn=os.setsid)
	time.sleep(0.5)
	os.killpg(pro.pid, signal.SIGTERM)
	result2, stderr = pro.communicate()

	#Obtenemos las salidas de la prueba con la que vamos a comparar y de la ejecucion del programa del alumno
	obtainedResult = normalizeOutput(result2)

	#Comparamos las salidas e imprimimos resultados
	print ("MYISHERE CHECKER. Expected output:" )
	print (result1.decode('ascii'))
	print ("MYISHERE CHECKER. Program output:" )
	print (result2.decode('ascii'))

	if result1 == result2:
		print ("MYISHERE CHECKER. CORRECT TEST")
		resultString += "1 "
		result += 1
	else:
		print ("MYISHERE CHECKER. INCORRECT TEST. Outputs differ")
		resultString += "0 "


	#Realizamos la prueba sugerida (dir not exist)
	result1 = 255

	#Ejecutamos el programa del alumno
	cmd = programPath  + " p1 f2.txt"
	pro = subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True, preexec_fn=os.setsid)
	time.sleep(0.5)
	os.killpg(pro.pid, signal.SIGTERM)
	result2, stderr = pro.communicate()
	result2 = pro.returncode
	#Obtenemos las salidas de la prueba con la que vamos a comparar y de la ejecucion del programa del alumno

	#Comparamos las salidas e imprimimos resultados
	print ("MYISHERE CHECKER. Expected output:")
	print (result1)
	print ("MYISHERE CHECKER. Program output:" )
	print (result2)

	if result1 == result2:
		print ("MYISHERE CHECKER. CORRECT TEST")
		resultString += "1 "
		result += 1
	else:
		print ("MYISHERE CHECKER. INCORRECT TEST. Outputs differ")
		resultString += "0 "



if(__name__=="__main__"):
	'''
	Funcion main de la aplicacion. Obtiene el fichero pasado como argumento. Lo descomprime, chequea su formato y finalmente lanza las pruebas.
	'''

	if (sys.version_info[0] < 3):
		print ('ERROR: Python3 must be used\n\tpython3 checker_p1.py <submission.zip>')
		sys.exit(0)

	#Comprobamos que se ha pasado un fichero como argumento
	if not len(sys.argv) == 2:
		print ('Uso: python3 checker_p1.py <submission.zip>')
	else:
		print ('CHECKER: correcting', sys.argv[1])
		inputFile = sys.argv[1]
		
		#Comprobamos que el fichero existe
		if not os.path.isfile(inputFile):
			print ("The file", inputFile, "does not exist")
			sys.exit(0)
	
		#Comprobamos el formato del nombre del fichero
		tokens=inputFile.replace(".zip","")
		tokens=tokens.split("_")
		if len(tokens) != 3 and len(tokens) != 4 and len(tokens) != 5:
			print ("Incorrect file name format: os_p1_AAAAA_BBBBB_CCCCC.zip")
			sys.exit(0)
			
		ssoo=tokens[0]
		p1=tokens[1]
		u1=tokens[2]
		u2=""
		u3=""
		if len(tokens)>3:
			u2=tokens[3]
			if len(tokens)>4:
				u3=tokens[4]
		if not (ssoo == "os" and p1 == "p1"):
			print ("Incorrect file name format: os_p1_AAAAA_BBBBB_CCCCC.zip")
			sys.exit(0)

		print ("CHECKER: NIA 1",u1, "NIA 2", u2, "NIA 3", u3)
		
		#Preparamos la carpeta temporal donde se realizaran las pruebas
		tempFolder= os.getcwd() + "/checker/"
		testFile="f_aes.txt"
		if os.path.exists(tempFolder):
			subprocess.call(["rm", "-r",tempFolder])

		os.mkdir(tempFolder)
		os.mkdir(tempFolder+"dirC")
		os.mkdir(tempFolder+"dirA")

		subprocess.call(["touch",tempFolder+"f_empty.txt"])		
		subprocess.call("echo -n \"AAAAA\" > " + tempFolder + testFile, shell=True)
		
		subprocess.call(["cp",inputFile,tempFolder])
		subprocess.call(["touch",tempFolder+"dirA/"+"f_sizetrue.txt"])
		subprocess.call("echo -n \"AAAAA\" > " + tempFolder + testFile, shell=True)

		os.mkdir(tempFolder+"p1_test")
		subprocess.call(["touch",tempFolder+"p1_test/f1.txt"])	

		print ('CHECKER: decompressing')

		#Descomprimimos el fichero en la carpeta temporal
		zipresult=subprocess.call(["unzip",tempFolder+"*.zip","-d",tempFolder])
		if not zipresult == 0:
			print ("Error decompressing zip file")
			sys.exit(0)
		
		#Comprobamos que el fichero de authors existe
		if not os.path.isfile(tempFolder+"authors.txt"):
			print ("The file authors.txt does not exist")
			sys.exit(0)

		
		#Realizamos una prueba basica de cada uno de los programas

		testExerciseWC(tempFolder)

		testExerciseLS(tempFolder)

		testExerciseISHERE(tempFolder)
		
		resultString
		print(resultString) 
		result
		print ("Grade: ", result)
		subprocess.call("echo " + str(result) + "> grade.txt", shell=True)
		
		shutil.rmtree(tempFolder)