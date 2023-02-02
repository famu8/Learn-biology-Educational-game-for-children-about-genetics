# -*- coding: utf-8 -*-
"""
Created on Fri May  1 18:17:48 2020

@author: famu8
"""

#%%

#PROYECTO PROMGRAMACIÓN 

#%%   
# =========================================================================
# =========================MENÚ PRINCIPAL==================================
# =========================================================================
print("Bienvenido al menú princiapl de ---" "nombre programa" "--- en este programa podrás encontrar diferentes juegos con los que podrás aprender a cerca de genética (cadenas de ADN) a la vez que te diviertes")
print("")
print("Antes de comenzar deberás leer y comprender las siguientes normas:")
print("")
print("Introduzca de manera correcta los datos que le pida el programa")
print("2.Es necesario poseer uno o varios fihceros FASTA para poder ejecutar los programas si estos lo requieren.")
print("1.A la hora de escribir el nombre del fichero X que se quiere analizar es necesario añadir la extension "'.x'" para evitar errores." )
print("")

def menu_de_eleccion():
    
    verdadero=False
    numero=0
    
    while not verdadero:
        
        try:
            numero = int(input("Introduce un numero entero que corresponda con el tipo de programa a ejecutar: "))
            verdadero=True
            
        except ValueError:
            
            print("Error, introduce un numero entero que corresponda con el tipo de programa a ejecutar: ")
    
    return numero

salir = False
opcion = 0 

while not salir:
 
    print ("1. Porcentaje de bases")
    print ("2. Cadenas aleatorias")
    print ("3. Comparar secuencias")
    print ("4. Similitud entre especies")
    print ("5. Salir del programa")
     
    print ("Elija una de las posibles opciones ")
 
    opcion = menu_de_eleccion()
 
    if opcion == 1:
        print ("Has elegido: porcentaje de bases") 
        print("")
        principal1()
    elif opcion == 2:
        print ("Has elegido: cadenas aleatorias ")
        print("")
        principal2()
    elif opcion == 3:
        print("Has elegido: comparar secuencias ")
        print("")
        principal3()
    elif opcion == 4:
        print("Has elegido: similitud entre especies")
        print("")
        principal4()
    elif opcion == 5:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 4, por favor")
print("")
print ("Fin del programa")


#%%
# SUBPROGRAMA NUMERO 1
'''
EN ESTE PRIMER PROGRAMA SE PIDE AL USUARIO :
    1.EL NOMBRE DE UN FICHERO FASTA A ANALIZAR:
    2. COMIENZO Y FINAL PARA ANALIZAR EL FASTA
    3. EL NUMERO DE CARACTERES QUE EL USUARIO DESEA QUE APAREZCAN POR PANTALLA
    ------------------------------------------------------------------------
    ESTE FICHERO FASTA SE COMPARARA CON EL DICCIONARIO QUE HEMOS CREADO A TRAVÉS DEL USO 
    DE LA FUNCION fromtxt2dicc; SE IMPRIMIRÁ LA PROTEINA CORRESPONDIENTE AL FICHERO 
    FASTA INTRODUCIDO POR EL USUARIO Y SE MOTRARÁ POR PANTALLA EL PORCENTAJE DE LOS 
    AMINOACIDOS QUE MÁS SE REPITEN, LOS QUE NO CUMPLAN EL PORCENTAJE NECESARIO SE 
    AÑADIRÁN A 'OTROS'

'''


def fromtxt2dicc(nombre_fich_codones): 
    fich = open(nombre_fich_codones)
    gencode = {}
    for linea in fich:
        t = linea.strip().split(" ") 
        codon = t[0]
        proteina = t[1]
        gencode[codon] = proteina
    fich.close()    
    return gencode


# lee la primera secuencia del fichero
def fasta2sec(FASTA) :
    try:
        F = open (FASTA)        
        secuencia = ""
        for linea in F : #creamos una funcion para convertir fasta a secuencia 
            linea = linea.strip("\n")
            if len(linea) != 0 and linea[0] != ">":
                secuencia = secuencia + linea
    except: 
        print("Error el fichero con nombre" + FASTA + "no existe")  
        
    return secuencia

def sec2prot(secuenciawell, gencode, comienzo, final): 
    prot = ""
    for i in range(comienzo, final, 3) :
      codon = secuenciawell[i:i+3] #funcion que pasas de secuencia a aminoacido leyendo el diccionario del gencode
      if codon in gencode:
        prot = prot +  gencode[codon]
        
    return prot

def pedirLimites():
    comienzo = int(input("Posición de comienzo [> 0]: "))
    final = int(input("Posición de finalización [> 0]: "))
    
    # con este bulce controlo los errores
    while True:
        
        if final <= comienzo:
            print("Error, vuelva a introducir los valores [comienzo < final] de manera correcta")
            comienzo = int(input("Posición de comienzo: ")) #Aquí protegemos el código ya que no tendría sentido que el usuario introdujera una posición de finalización de menor valor que la de comienzo.
            final = int(input("Posición de finalización: "))
            
         
        elif final < 0 or comienzo < 0:
             print("Error, vuelva a introducir los valores [comienzo > 0,final > 0] de manera correcta")
             comienzo = int(input("Posición de comienzo: ")) 
             final = int(input("Posición de finalización: "))
           
        else:
            break 
        
    return comienzo, final



def imprimirAncho(secuenciawell, caracXlinea):
    imprimidos = 0
    for i in range(0, len(secuenciawell)):
        print(prot[i],end="")
        imprimidos = imprimidos + 1
        if imprimidos == caracXlinea:
            print("")
            imprimidos = 0
            
            
def distribucionAmino(prot):
    lista = []
    for amino in prot:
        if amino not in lista:
            lista.append(amino)
    lista.sort()
    veces = []
    porcentajes = []
    seleccionados = []
    total = 0
    for amino in lista:
        cuantos = prot.count(amino)
        veces.append(cuantos)
        if cuantos/len(prot)*100 > 7:
            total = total + cuantos/len(prot)
            seleccionados.append(amino)
            porcentajes.append(cuantos/len(prot))    
    resto = 1 - total    
    seleccionados.append("otros")
    porcentajes.append(resto)
    
    print(porcentajes)
    print(seleccionados)
    
    import matplotlib.pyplot as plt
    
    labels = seleccionados
    sizes = porcentajes
    explode = [0] * len(labels)
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels = labels, autopct='%1.2f%%',
            shadow=True, startangle = 90)
    ax1.axis('equal')  
    plt.show()

##################################################################################
#Programa principal

def principal1():
    # 1. Cargamos el diccionario
    gencode = fromtxt2dicc("codones.txt")
    
    # 2. Pedir los datos
    FASTA = input("Introduce el nombre del fichero FASTA que desea analizar: ")#aqui hay que escribir coronavirus.fasta
    caracXlinea = int(input("Número de caracteres por línea que desea que aparezcan en resultados (consola): "))
    comienzo, final = pedirLimites()
    
    # 3. Mostrar los datos introducidos
    print("Analizando datos introducidos".center(50,"="))
    print("")
    print("RESULTADOS".center(50,"="))
    print("")
    print("Nombre del fichero fasta:", FASTA)
    print("")
    print("Caracteres por linea:", caracXlinea)
    print("")
    print("Se analizará desde:", comienzo, "hasta:", final)
    print("")
    
    # llamo a la funcion para que me lea la secuencia,
    # y recojo la secuencia en la variable secuenciawell
    secuenciawell = fasta2sec(FASTA) 
    
    
    # llamo a la funcion le paso la secuencia, el diccionario, el incio y el final, y me devuelve la proteina
    prot = sec2prot(secuenciawell, gencode, comienzo, final)
    print("Proteina equivalente:", prot, end="")
    print("")
    # Finalmente se presentan los resultados
    print("")
    print("A continuación se muestra la secuencia de aminoácidos correspondiente a la traducción de la secuencia de ADN comprendida entre la posición de comienzo y finalización:\n")
    
    imprimirAncho(prot, caracXlinea)
    print("")    
    distribucionAmino(prot) #funcion para mostrar los resultados graficamente
    print("")




   
#%%##############################################################################
# SUBPROGRAMA 2 
'''
SE PIDEN AL USUARIO:
    1.LA LONGITUD DE LA CADENA DE ADN RANDOM A CREAR
    2.CUANTOS CARCATERES QUIERE QUE APAREZCAN POR CONSOLA
    3.EL TIPO DE FICHERO QUE QUE QUIERE GENERAR [.csv/.fasta/.txt]
    4.EL NOMBRE DEL FICHERO QUE GENERARÁ 
    ----------------------------------------------
    POR PANTALLA SE OBTIENE, LA SECUENCIA ALEATORIA DE ADN CON EL NUMERO DE
    CARACTERS INTRODUCIDOS REGULADOS POR EL  NUMERO DE CARACTERES POR LINEA DE
    COMANDO; SE OBTIENE UN GRAFICO DE TARTA UE MUESTRA EL PORCENTAJE DE CADA 
    BASE. 
    SE GENERA UN FICHERO EN LA RUTA DONDE TENGA GUARDADA EL PROGRAMA EL 
    USUARIO
    '''
    
import random
import matplotlib.pyplot as plt



def randomstr(long):
  bases=["A","T","C","G"]
  secuencia=""
  for n in range(long):
    secuencia  =  secuencia + random.choice(bases)
    
  return secuencia 



def porcentaje(secuencia):
  perA=(secuencia.count("A")/len(secuencia))*100
  perT=(secuencia.count("T")/len(secuencia))*100
  perC=(secuencia.count("C")/len(secuencia))*100
  perG=(secuencia.count("G")/len(secuencia))*100
  
  return [perA,perT,perC,perG]



def recaudar(secuencia,caracXlinea):
  newsecuencia=""
  for n in range(0,len(secuencia),caracXlinea):
    newsecuencia = newsecuencia+secuencia[n:n+caracXlinea]+"\n"
    
  return newsecuencia

  
#CON EL SIGUIENTE BUCLE CONTROLAMOS QUE EL USUARIO INTRODUZCA DE MANERA CORRECTA LOS DATOS 
def pedirLongitud():
    long=int(input("Longitud para la cadena aleatoria de ADN:"))
    caracXlinea=int(input("¿Cuántos caracteres quiere que aparezcan por linea de comando?:"))
    while True: 
        if long <= 0: 
            print("Error introduzca una longitud válida.")
            long=int(input("Longitud para la cadena aleatoria de ADN:"))
        
        elif caracXlinea <= 0:
            print("Error introduzca una longitud válida.")
            caracXlinea=int(input("¿Cuántos caracteres quiere que aparezcan por linea de comando?:"))
        
        else: 
            break 
        
    return long, caracXlinea


def tipofichero():
    
    nombre=input("Nombre para el fichero que se generará:")
    tipo_fichero=input("¿Qué tipo de fichero quiere generar [.csv/.fasta/.txt]?")
    tipo_fichero.lower()
    
    while True: 
        if tipo_fichero == ".csv"  or  tipo_fichero == ".fasta" or  tipo_fichero == ".txt":
            break
        else: 
            print("Error, introduzca un formato válido")
            tipo_fichero=input("¿Qué tipo de fichero quiere generar [csv,fasta,txt]?")
    
      
    return tipo_fichero, nombre

def juntar_nombre_and_fichero(tipo_fichero,nombre):
    
    nombre_and_tipo = nombre + tipo_fichero

    return nombre_and_tipo
    

def grafico(secuencia,porcent): 
    labels = ['A','T','C','G']
    sizes = porcent
    explode = [0] * len(labels)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels = labels, autopct='%1.2f%%',
            shadow=True, startangle = 90)
    ax1.axis('equal')  
    plt.show()



##########################PROGRAMA PRINCIPAL####################################
    


def principal2(): 
    
    long, caracXlinea = pedirLongitud()
    tipo_fichero, nombre = tipofichero()
    nombre_and_tipo = juntar_nombre_and_fichero(tipo_fichero,nombre)
    
    print("")
    print("Aánlisis de los datos introducidos".center(50,"="))
    print("")
    print("La cadena aleatoria posee", long, "caracteres")
    print("")
    print("Se mostrarán", caracXlinea, "caracteres por linea en la consola")
    print("")
    print("El nombre del fichero a generar es:", nombre, "y será un fichero de tipo:", tipo_fichero)
    print("")
    
    secuencia=randomstr(long)
    porcent = porcentaje(secuencia)
    newsecuencia = recaudar(secuencia,caracXlinea)
    

    with open(juntar_nombre_and_fichero(tipo_fichero,nombre),"w") as file: #CON ESTE METODO PARA ABRIR FICHEROS NO TENEMOS QUE UTILIZAR EL CLOSE()
    
        file.write(">"+"\n") 
        file.write(newsecuencia)
    
    print("RESULTADOS GRÁFICOS".center(55,"="))
    
    grafico(secuencia,porcent)
    print("")
    print("La nueva secuencia es:",newsecuencia)
    print("Los porcentajes son: A: %.2f%% / T: %.2f%% / C: %.2f%% / G: %.2f%%"%(porcent[0],porcent[1],porcent[2],porcent[3]))
    print("")
    
    
    
    
    
    
    
#%%##############################################################################
#SUBPROGRAMA 3 
'''
EN ESTE PROGRAMA SE PIDE AL USUARIO :
    1.LA LONGITUD PARA CREAR DOS CADENAS DE ADNS ALEATORIAS
    -------------------------------------------------
    SE COMPARAN Y SE MOSTRARÁ LA SIMILUTD EN POCENTAJE 
    QUE PRESENTAN DICHAS CADENAS
'''



def pedirlongitud1():
    long=int(input("Longitud para la cadena aleatoria de ADN:"))
    while True: 
        if long <= 0: 
            print("Error introduzca una longitud válida.")
            long=int(input("Longitud para la cadena aleatoria de ADN:"))
        else: 
            break 
        
    return long
       
    

def randomstr1(long):
  bases=["A","T","C","G"]
  secuencia1=""
  for n in range(long):
    secuencia1  =  secuencia1 + random.choice(bases)
    
  return secuencia1

def comparasecuencias(sec1,sec2):
  contador = 0
  for n in range(len(list(sec1))):
    if sec1[n] == sec2[n]:
      contador = contador + 1
      
  porcentaje1=(contador/len(sec1))*100 
  
  return porcentaje1

##########################PROGRAMA PRINCIPAL####################################
def principal3():
    long = pedirlongitud1()
    secuencia1 = randomstr1(long)
    sec1=randomstr1(long) 
    sec2=randomstr1(long)
    porcentaje1=comparasecuencias(sec1,sec2)
    print("Analizando los datos introducidos".center(50,"="))
    print("")
    print("La cadena de ADN 1 es:\n",sec1)
    print("")
    print("La cadena de ADN 2 es:\n",sec2)
    print("")
    print("Las secuencias presentan un parecido del %.2f%%" %porcentaje1)
    print("")









#%%##############################################################################
# SUBPROGRAMA 4 
'''

EN ESTE PROGRAMA SE PEDIRÁ AL USUARIO: 
    1.DOS POSICIONES UNA DE INCIO Y OTRA DE FINALIZACION 
    2.INTRODUCIR EL NOMBRE DE DOS FICHEROS FASTA PARA:
        2.1 COMPARAR LAS SECUENCIAS CODIFICANTES QUE POSEEN UN PARECIDO DE NUCLEOTIDOS ENTRE LAS POSICIONES INTRODUCIDAS POR EL USUARIO
        2.2 COMPARAR LAS PROTEINAS CODIFICADAS QUE POSEEN PARECIDO DE AMINOACIDOS ENTRE LAS POSICIONES INTRODUCIDAS POR EL USUARIO
    ---------------------------------------
    SE MUESTRA POR PANTALLA: 
        1. Las secuencias codificantes poseen un parecido en nucleotidos
        2. Las proteínas codificadas poseen un parecido en aminoacidos
        
'''

def fromtxt2dicc1(nombre_fich_codones): 
    fich = open(nombre_fich_codones)
    gencode1 = {}
    for linea in fich:
        t = linea.strip().split(" ") 
        codon = t[0]
        proteina = t[1]
        gencode1[codon] = proteina
    fich.close() 
    
    return gencode1


def pedirLimites1():
    comienzo = int(input("Posición de comienzo [> 0]: "))
    final = int(input("Posición de finalización [> 0]: "))
    # con este bulce controlo los errores
    while True:
        
        if final <= comienzo:
            print("Error, vuelva a introducir los valores [comienzo < final] de manera correcta")
            comienzo = int(input("Posición de comienzo: ")) #Aquí protegemos el código ya que no tendría sentido que el usuario introdujera una posición de finalización de menor valor que la de comienzo.
            final = int(input("Posición de finalización: "))
            
         
        elif final < 0 or comienzo < 0:
             print("Error, vuelva a introducir los valores [comienzo > 0,final > 0] de manera correcta")
             comienzo = int(input("Posición de comienzo: ")) 
             final = int(input("Posición de finalización: "))
           
        else:
            break 
        
    return comienzo, final
  

      
def fasta2sec1(FASTA) :
    try:
        F = open (FASTA)        
        secuencia = ""
        for linea in F : #creamos una funcion para convertir fasta a secuencia 
            linea = linea.strip("\n")
            if len(linea) != 0 and linea[0] != ">":
                secuencia = secuencia + linea
    except: 
        print("Error el fichero con nombre" + FASTA + "no existe")  
        
    return secuencia



def trozo(secuencia,comienzo,final):
    
  secuencia = secuencia[comienzo:final]
  
  return secuencia




def comparasecuencias1(sec1,sec2):
  contador = 0
  for n in range(len(list(sec1))):
    if sec1[n] == sec2[n]:
      contador = contador + 1
      
  porcentaje=(contador/len(sec1))*100 
  
  return porcentaje




def dna2prot(orf,gencode1):
  proteina=""
  
  numbases=int(len(orf)/3)*3
  for n in range(0,numbases,3):
    proteina = proteina + gencode1[orf[n:n+3]]
    
  return proteina


def principal4():
    gencode1 = fromtxt2dicc1("codones.txt") #cargamos el diccionario 
    
    print("Analizando los resultados".center(55,"="))
    print("")
    print("Se va a realizar el análisis de similutd entre las especies: chimpancé y humano")
    comienzo, final = pedirLimites1()
    print("")
    print("Se analizarán los archivos desde", comienzo, "hasta", final)
    
    geno1=fasta2sec1("humano.fasta")
    geno2=fasta2sec1("chimpance.fasta")

  
    trozo1=trozo(geno1,comienzo,final)
    trozo2=trozo(geno2,comienzo,final)
    
    prot1=dna2prot(trozo1)
    prot2=dna2prot(trozo2)
    
    porcentaje_nucelotidos = comparasecuencias1(trozo1,trozo2)
    porcentaje_aminos = comparasecuencias1(prot1,prot2)
    
    print("Las secuencias codificantes poseen un parecido en nucleotidos del %.2f%%"%porcentaje_nucelotidos)
    print("")
    print("Las proteínas codificadas poseen un parecido en aminoacidos del %.2f%%"%porcentaje_aminos)
       




























