import numpy as np
import pandas as pd



def media_evolve(lista_datos: list):
    """Calculate the mean (average) of a list of numbers"""
    if not lista_datos:
        return 0
    return sum(lista_datos) / len(lista_datos)

def mediana_evolve(lista_datos: list):
    """Calculate the median of a list of numbers"""
    if not lista_datos:
        return 0
    
    sorted_datos = sorted(lista_datos)
    n = len(sorted_datos)
    
    if n % 2 == 0:
        # Even number of elements - average of middle two
        return (sorted_datos[n//2 - 1] + sorted_datos[n//2]) / 2
    else:
        # Odd number of elements - middle element
        return sorted_datos[n//2]

def percentil_evolve(lista_datos: list, percentil: int):
    """Calculate the percentile of a list of numbers"""
    if not lista_datos:
        return 0
    
    if percentil < 0 or percentil > 100:
        raise ValueError("Percentile must be between 0 and 100")
    
    sorted_datos = sorted(lista_datos)
    n = len(sorted_datos)
    
    index = (percentil / 100) * (n - 1)
    
    if index.is_integer():
        return sorted_datos[int(index)]
    else:
        lower_index = int(index)
        upper_index = lower_index + 1
        fraction = index - lower_index
        return sorted_datos[lower_index] + fraction * (sorted_datos[upper_index] - sorted_datos[lower_index])

def varianza_evolve(lista_datos: list):
    """Calculate the variance of a list of numbers"""
    if not lista_datos:
        return 0
    
    mean = media_evolve(lista_datos)
    squared_diffs = [(x - mean) ** 2 for x in lista_datos]
    return sum(squared_diffs) / len(lista_datos)

def desviacion_evolve(lista_datos: list):
    """Calculate the standard deviation of a list of numbers"""
    if not lista_datos:
        return 0
    
    variance = varianza_evolve(lista_datos)
    return variance ** 0.5

def IQR_evolve(lista_datos: list):
    """Calculate the Interquartile Range (IQR) of a list of numbers"""
    if not lista_datos:
        return 0
    
    q1 = percentil_evolve(lista_datos, 25)
    q3 = percentil_evolve(lista_datos, 75)
    return q3 - q1




if __name__ == "__main__":
    
    np.random.seed(42)
    edad = list(np.random.randint(20, 60, 100))
    salario =  list(np.random.normal(45000, 15000, 100))
    experiencia = list(np.random.randint(0, 30, 100))


    np.random.seed(42)
    df = pd.DataFrame({
        'edad': np.random.randint(20, 60, 100),
        'salario': np.random.normal(45000, 15000, 100),
        'experiencia': np.random.randint(0, 30, 100)
    })

    print("resultado pandas")
    print("--------------------------------")
    print(df.describe())

    print("resultado funciones")
    print("--------------------------------")

    print(media_evolve(edad))
    print(mediana_evolve(edad))
    print(percentil_evolve(edad, 50))
    print(varianza_evolve(edad))
    print(desviacion_evolve(edad))
    print(IQR_evolve(edad))

    print(media_evolve(salario))
    print(mediana_evolve(salario))
    print(percentil_evolve(salario, 50))
    print(varianza_evolve(salario))
    print(desviacion_evolve(salario))
    print(IQR_evolve(salario))

    print(media_evolve(experiencia))
    print(mediana_evolve(experiencia))
    print(percentil_evolve(experiencia, 50))
    print(varianza_evolve(experiencia))
    print(desviacion_evolve(experiencia))
    print(IQR_evolve(experiencia))