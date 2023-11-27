# Serie Fibonacci

# Importamos la librería de test
import unittest

numero = 10 #Mandamos el número para generar la serie
listaNum = [] # Creamos la lista de numeros

def serieFibonacci():
        numero1 = 1 # Le asignamos el primer valor
        numero2 = 0 # Le asignamos el segundo valor
        for i in range(numero): # Entramos en el bucle y damos las vueltas que le hemos asignado
            suma = numero1 + numero2 # Sumamos los dos numeros
            numero1 = numero2 # Igualamos el primer valor al segundo valor
            numero2 = suma # Igualamos el segundo valor a la suma
            listaNum.append(suma)


def extraerNum(indice): # Extraemos el numero de la lista para comprobarlo en el test
    if (indice < 0):
        return("No existe ese valor")
    else:
        return listaNum[indice]


# numero = input("Introduce hasta donde quieres ver la serie: ")
# serieFibonacci(int(numero))

# Definimos la clase Test
class Test(unittest.TestCase):
    serieFibonacci()
# Definimos los test que queremos hacer
    def testFibo1(self):
        self.assertEqual(extraerNum(5), 8)
    def testFibo2(self):
        self.assertEqual(extraerNum(-1), 'No existe ese valor')
    def testFibo3(self):
        self.assertEqual(extraerNum(0), 1)

# Ejecutamos la prueba de código
if __name__ == "__main__":
    unittest.main()