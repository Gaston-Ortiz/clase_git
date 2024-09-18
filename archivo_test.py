import pandas as pd

# Creamos un dataFrame de prueba
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Edad': [25, 30, 35],
    'Ciudad': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

print(df)