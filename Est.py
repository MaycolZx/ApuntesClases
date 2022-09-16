# muestraList = [1,1,1,1,2,2,7,7,7,7,7,7]

# muestraList = ["Mar","Mar","Mar","Mar","Mar","Mar",
#                 "Montaña","Montaña","Montaña",
#                 "Campo","Campo","Campo","Campo"]

# muestraList = [2,1,1,0,1,2,1,5,3,6,
#                 1,2,0,3,0,1,1,2,3,4,
#                 4,2,1,1,1,2,0,3,1,1]

muestraList = [7,6,4,4,6,6,2,7,4,7,6,5,5,5,6,5,2,7,3,6,4,3,6,5,6,4,7,5,7,5,7,6,6,6,7,3,6,4,6,5]

muestraList = [1.67, 1.72,1.81,1.72,1.74,1.83,1.84,1.88,1.92,1.75, 1.84,1.86,1.73,1.84,1.87,1.83,1.81,1.77,1.73,1.75,1.78
                ,1.77,1.67,1.83,1.83,1.72,1.71,1.85,1.84,1.93,1.82,1.69,1.70,1.81,1.66,1.76,1.75,1.80,1.79,1.84,1.86
                ,1.80,1.77,1.80,1.76,1.88,1.75,1.79,1.87,1.79,1.77,1.67,1.74,1.75,1.78,1.77,1.74,1.73,1.83,1.76,1.83
                ,1.77,1.75,1.77,1.77,1.84,1.83,1.79,1.82,1.76,1.76,1.76,1.79,1.88,1.66,1.80,1.72,1.75,1.79,1.77]

# finalizar = int(input("Num de datos: "))
# while(finalizar != 0):
#     muestra = int(input("Ingrese una muestra: "))
#     muestraList.append(muestra)
#     print(muestraList)
#     finalizar = finalizar - 1

#Funcion de Frecuencia acumulada a nivel general
def frecAcumulada_General (listaMuestras = [],numDecimal = int):
    listFrecAcumul_Gen = []
    numeroFreAcum = 0
    for l in listaMuestras:
        numeroFreAcum = numeroFreAcum + l
        listFrecAcumul_Gen.append(round(numeroFreAcum,numDecimal))
    return listFrecAcumul_Gen


def cuantitativo_Cualitativo(lista = [], numDecimales = int ):
    listaDescart = []

    listFrecAbsolt = []
    listFrecRelatv = []
    listFrecRelPorc = []
     
    #Frecuencia absoluta: número de datos observados en cada categoría o modalidad
    totalFrecAbsot = 0
    for i in (lista):
        if (i not in listaDescart):
            # print(f"FrecuenciaAbsoluta de {i} = {lista.count(i)}")
            totalFrecAbsot = totalFrecAbsot + lista.count(i)
            listFrecAbsolt.append(lista.count(i))
            listaDescart.append(i)
    


    #Frecuencia relativa: en cada categoría es igual a su frecuencia entre el total de observaciones.
    totalFrecRelat = 0
    for j in listFrecAbsolt:
        numero = j / totalFrecAbsot
        numero = round(numero, numDecimales)
        totalFrecRelat = totalFrecRelat + numero
        listFrecRelatv.append(numero)
    totalFrecRelat = round(totalFrecRelat,2)
    
    #Frecuencia relativa porcentual: es la frecuencia relativa expresada en tanto por ciento
    totalFrecRelPorc = 0
    for k in listFrecAbsolt:
        numero = (k / totalFrecAbsot)*100
        numero = round(numero, numDecimales)
        totalFrecRelPorc = totalFrecRelPorc + numero
        listFrecRelPorc.append(numero)

    #Frecuencia Acumulada
    listFrecAcumul = frecAcumulada_General(listFrecAbsolt,0)
    #Frecuencia Acumulada Relativa
    listFrecAcuRela = frecAcumulada_General(listFrecRelatv,2)

    #'Modalidaes','FrecuenciaAbsoluta','FrecuenciaRelativa','FrecuenciaAcumulada','FrecuenciaAcumuladaRelativa','FrecuenciaRealativaPorc'
    print ("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format('Modalidaes','Frecuencia','Frecuencia',
                                        'Frecuencia','Frecuencia','Frecuencia'))
    print ("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(' ','Absoluta','Relativa',
                                        'Acumulada','AcumuRelat','RealativaPorc'))
    print ("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format('-----','-----','-----','-----','-----','-----'))
    print ("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format('X_i','f_i','fr_i/T','F_i','Fr_i','Fr_%'))
    print ("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format('-----','-----','-----','-----','-----','-----'))
    for i in range(len(listaDescart)):
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(listaDescart[i],listFrecAbsolt[i],listFrecRelatv[i],listFrecAcumul[i]
        ,listFrecAcuRela[i],listFrecRelPorc[i]))
    print ("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format('TOTAL = ',totalFrecAbsot,totalFrecRelat,' ',' ',totalFrecRelPorc))


def caso_Cuali_Or_Cuanti_Or_CuantiCont():
    print("-----------------------------------------------------------------------------")
    print("1. Caso Cualitativo: ej.[Mar,Mar,Mar,Mar,Montaña,...,Campo,Campo,Campo]")
    print("2. Caso Cuantitativo: ej.[1,2,2,2,1,1,7,8,...,8]")
    print("3. Caso Cuantitativo Continuo: ej.[1.67,1.72,1.81,1.72,1.74,...,1.77]")
    print("-----------------------------------------------------------------------------")
    muestraList = [7,6,4,4,6,6,2,7,4,7,6,5,5,5,6,5,2,7,3,6,4,3,6,5,6,4,7,5,7,5,7,6,6,6,7,3,6,4,6,5]

    casoCualoCuan = int(input("Escriba que caso quiere tratar: "))
    if casoCualoCuan == 1:
        cuantitativo_Cualitativo(muestraList,2)
    elif casoCualoCuan == 2:
        muestraList.sort()
        cuantitativo_Cualitativo(muestraList,2)
    elif casoCualoCuan == 3:
        print("falta anyadir el caso Cuantitativo continuo")

caso_Cuali_Or_Cuanti_Or_CuantiCont()

    




