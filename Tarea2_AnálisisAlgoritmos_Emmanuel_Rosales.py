##*******************************************************************************
##
## Instituto Tecnológico de Costa Rica - Ingeniería en Computación.
##
## Tarea número 2 de Análisis de Algoritmos.
##
## Profesor     : Mauricio Rojas.
##
## Autor        : Emmanuel Rosales Salas.
##
## Grupo        : 40 -CASJ-
##
## Fecha        : 9 de Marzo del 2015.
##
## Programa     : determinaPosición.
##
## Descripción  : Este programa determina las posiciones de los 2 valores
##                más grandes en una lista (arreglo) utilizando la técnica
##                de divide y conquista del curso Análisis de Algoritmos.
##
## Entradas     : Una lista de números enteros de tamaño N.
##
## Salidas      : Dos números los cuales indican las posiciones de los valores
##                más grandes de la lista.
##
## Restricciones: La lista debe ser de números enteros.
##
##********************************************************************************

## Variables Globales.
lista2 = []

def determinaPosicion(lista):
    
    """Hacer los comentarios
       Entradas     : Una lista (arreglo) de números enteros
       Salidas      : Dos números que indican la posición de
                      los 2 valores de mayor tamaño en la lista.
       Restricciones: La lista debe ser de valores enteros.
    """
    resultado = ""
    mitad = len(lista) // 2
    listaOriginal = lista[:]
    ## Revisa si la lista es menor de 2 elementos, ya que 2
    ## es el caso base para poder retornar las posiciones
    ## de los 2 elementos más grandes.
    if len(lista) < 2:
        resultado = "La lista debe tener minimo 2 números"

    ## Si el largo de la lista es de 2, determina cual de
    ## los 2 números es el mayor y retorna la posición de
    ## ambos.
    elif len(lista) == 2:
        if lista[0] > lista[1]:
            resultado = "La posición del elemento más grande es: "+str(listaOriginal.index(lista[-2]))+"\n"+"La posición del segundo elemento más grande es: " + str(listaOriginal.index(lista[-1]))
        else:
            resultado = "La posición del elemento más grande es: "+str(listaOriginal.index(lista[-1]))+"\n"+"La posición del segundo elemento más grande es: " + str(listaOriginal.index(lista[-2]))

    ## Si el largo de la lista es mayor al caso base, aquí
    ## es donde empieza el algoritmo de divide y conquista
    ## a trabajar.
    elif len(lista) > 2:
        ## Llama la función del mergeSort.
        mergeSort(lista)
        if lista2[-2] > lista2[-1]:
            resultado = "La posición del elemento más grande es: "+ str(listaOriginal.index(lista2[-2]))+"\n"+"La posición del segundo elemento más grande es: " + str(listaOriginal.index(lista2[-1]))
        else:
            resultado = "La posición del elemento más grande es: "+str(listaOriginal.index(lista2[-1]))+"\n"+"La posición del segundo elemento más grande es: " + str(listaOriginal.index(lista2[-2]))
    return resultado



def mergeSort(lista):
    """
       Esta función es el popular algoritmo de mergesort que utiliza la técnica de
       Divide y conquista, el mismo se encuentra modificado y adaptado para que
       funcione para este programa en específico.(Piggyback)

       Entradas     : Lista
       Salidas      : Lista ordenada
       Restricciones: Ninguna.
       
    """
    global lista2
    if len(lista) > 1:
        mitad = len(lista)//2
        mitadizq = lista[:mitad]
        mitader = lista[mitad:]

        mergeSort(mitadizq)
        mergeSort(mitader)

        i=0
        j=0
        k=0
        while i < len(mitadizq) and j < len(mitader):
            if mitadizq[i] < mitader[j]:
                lista[k] = mitadizq[i]
                i += 1
            else:
                lista[k] = mitader[j]
                j += 1
            k += 1

        while i < len(mitadizq):
            lista[k] = mitadizq[i]
            i += 1
            k += 1

        while j < len(mitader):
            lista[k] = mitader[j]
            j += 1
            k += 1
    lista2 = lista

def main():
    """
       Esta función despliega un menu para que el usuario
       ingrese el tamaño del arreglo y cada uno de sus
       elementos, una vez el arreglo creado, llama a la
       función determinaPosicion(lista) y le pasa la
       lista como parámetro.

       Entradas     : El tamaño de la lista y sus valores.
       Salidas      : Las posiciones de los 2 elementos más grandes.
       Restricciones: La lista debe tener mínimo 2 elementos.
       
    """
    
    print("""             *-----------------------------------------------------*
             *                                                     *
             *                   Bienvenido                        *
             *                                                     *
             *  Instrucciones: 1- Primero debe de asignar el largo *
             *  de la lista. 2- Debe ingresar uno por uno el valor *
             *  de cada entrada. 3- Ver los resultados             *
             *                                                     *
             *                                                     *
             *-----------------------------------------------------*""")
    ## Pregunta el tamaño del arreglo al usuario.
    tamano = int(input("Ingrese el tamaño del arreglo que desea: "))
    lista=[]
    ## Le solicita al usuario los elementos de la lista y los agrega a ella.
    for x in range(tamano):
        a = int(input("Ingrese el valor para la posición " +str(x)+ " del arreglo --> "))
        lista.append(a)
    print("\n"+"Su lista es: ",lista)
    print("")
    print(determinaPosicion(lista))

## Llamado de la función principal
main()

    
