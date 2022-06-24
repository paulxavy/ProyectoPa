
#Importar el corpus
open('textos_articulo.txt', 'r', encoding='utf-8')
with open ('textos_articulo.txt','r', encoding='utf-8') as f:
  articulos = f.read()
#print(articulos[:500])


#Tokenizacion
import nltk
#nltk.download('punkt')
from nltk.tokenize.toktok import ToktokTokenizer
texto_ejemplo = 'hola paul,¿qué tal?'
totok = ToktokTokenizer()
palabras_separadas = totok.tokenize(texto_ejemplo)
#print(palabras_separadas)
def separa_palabras(lista_tokens):
  lista_palabras = []
  for token in lista_tokens:
    if token.isalpha():
      lista_palabras.append(token)
  return lista_palabras
#separa_palabras(palabras_separadas)


#Excluyendo caracteres y puntuaciones
def separa_palabras(lista_tokens):
  lista_palabras = []
  for token in lista_tokens:
    if token.isalpha():
      lista_palabras.append(token)
  return lista_palabras
palabras_separadas = totok.tokenize(articulos)
lista_palabras = separa_palabras(palabras_separadas)
#print(f'La cantidad de palabras en el Corpus es de :{len(lista_palabras)}')


#Contando palabras del corpus
palabras_separadas = totok.tokenize(articulos)
lista_palabras = separa_palabras(palabras_separadas)
#print(f'La cantidad de palabras en el Corpus es de :{len(lista_palabras)}')


#Nomarlizando y eliminando duplicados
def normalizar(lista_palabras):
  lista_normalizada = []
  for palabra in lista_palabras:
    lista_normalizada.append(palabra.lower())
  return lista_normalizada

palabras_normalizadas = normalizar(lista_palabras)
palabras_unicas = set(palabras_normalizadas)

#print(len(palabras_unicas))

#Operacion de Adicion
def adicionar_letras(partes):
  letras = 'abcdefghijklmnñopqrstuvwxyzáéíóú'
  nuevas_palabras = []
  for I,D in partes:
    for letra in letras:
      nuevas_palabras.append(I + letra + D)
  return nuevas_palabras
def generar_palabras(palabra):
  partes = []
  for i in range(len(palabra)+1):
    partes.append((palabra[:i],palabra[i:]))
    palabras_generadas = adicionar_letras(partes)
  return palabras_generadas
#adicionar_letras

#Corrector
def corrector(palabra):
  palabras_generadas = generar_palabras(palabra)
  palabra_corregida = max(palabras_generadas, key=probabilidad) 
  return palabra_corregida

frecuencia = nltk.FreqDist(palabras_normalizadas)
frecuencia.most_common(10)
total_palabras = len(palabras_normalizadas)

def probabilidad(palabra_generada):
  return frecuencia[palabra_generada]/total_palabras


#Evaluador
def crear_datos_prueba(nombre_archivo):
  lista_pruebas = []
  f = open(nombre_archivo, 'r')
  for fila in f:
    palabra_correcta,palabra_incorrecta = fila.split()
    lista_pruebas.append((palabra_correcta,palabra_incorrecta))
  f.close()
  return lista_pruebas

lista_pruebas = crear_datos_prueba('palabras_pruebas.txt')
def evaluador(pruebas):
  numero_palabras = len(pruebas)
  aciertos = 0
  for palabra_correcta, palabra_incorrecta in pruebas:
    palabra_corregida = corrector(palabra_incorrecta)
    if palabra_corregida == palabra_correcta:
      aciertos+=1
  tasa_acierto = round(aciertos*100 / numero_palabras,2)
  #print(f'la base de acierto del modelo es:{tasa_acierto}% de {numero_palabras} palabras')
  
evaluador(lista_pruebas)


#Operacion Eliminacion
def eliminar_caracteres(partes):
  nuevas_palabras = []
  for I,D in partes:
    nuevas_palabras.append(I +  D[1:] )
  return nuevas_palabras
def generar_palabras(palabra):
  partes = []
  for i in range(len(palabra)+1):
    partes.append((palabra[:i],palabra[i:]))
  palabras_generadas = adicionar_letras(partes)
  palabras_generadas += eliminar_caracteres(partes)
  return palabras_generadas


#Operacion de alteracion
def alterar_caracteres(partes):
  letras = 'abcdefghijklmnñopqrstuvwxyzáéíóú'
  nuevas_palabras = []
  for I,D in partes:
    for letra in letras:
      nuevas_palabras.append(I + letra + D[1:])
  return nuevas_palabras
def generar_palabras(palabra):
  partes = []
  for i in range(len(palabra)+1):
    partes.append((palabra[:i],palabra[i:]))
  palabras_generadas = adicionar_letras(partes)
  palabras_generadas += eliminar_caracteres(partes)
  palabras_generadas += alterar_caracteres(partes)
  return palabras_generadas


#Operacion de Inversion
def invertir_caracteres(partes):
  nuevas_palabras = []
  for I,D in partes:
    if len(D) > 1:
      nuevas_palabras.append(I + D[1] + D[0] + D[2:])
  return nuevas_palabras
def generar_palabras(palabra):
  partes = []
  for i in range(len(palabra)+1):
    partes.append((palabra[:i],palabra[i:]))
  palabras_generadas = adicionar_letras(partes)
  palabras_generadas += eliminar_caracteres(partes)
  palabras_generadas += alterar_caracteres(partes)
  palabras_generadas += invertir_caracteres(partes)
  return palabras_generadas


#Limitaciones del corrector
def evaluador(pruebas, vocabulario):
  numero_palabras = len(pruebas)
  aciertos = 0
  desconocidas = 0
  for palabra_correcta, palabra_incorrecta in pruebas:
    palabra_corregida = corrector(palabra_incorrecta)
    desconocidas += (palabra_correcta not in vocabulario)
    if palabra_corregida == palabra_correcta:
      aciertos+=1
  tasa_acierto = round(aciertos*100 / numero_palabras,2)
  tasa_desconocidas =  round(desconocidas*100 / numero_palabras,2)
  print(f'la base de acierto del modelo es:{tasa_acierto}% de {numero_palabras} palabras')
  print(f'la tasa de desconocidas del modelo es:{tasa_desconocidas}% de {numero_palabras} palabras')
evaluador(lista_pruebas, palabras_unicas)

#print(corrector('lgica'))