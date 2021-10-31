import re
from typing import Collection

def prepare(col):
    """
    Esta función convierte datos para facilitar su análisis.
    Args:
    col(pandas series): serie de datos que queremos convertir.
    return:
    Convierte la serie en lista y devuelve los elementos en minúscula, sin espacios a los lados y reemplaza espacio (" ") por _ ("_")
    """  
    col = list(col)
    return [i.lower().strip().replace(" ","_") for i in col]

def uniform(data,findthis,replaceforthis):
    new = []
    for i  in list(data):
        if findthis in i:
            new.append(re.sub((f'^\w.+({findthis})*.'),str(replaceforthis),i))
        else:
            new.append(i)
    return new

def strdata(col):
    return [str(i) for i in col]
    
def uniforme(data,findthis,replaceforthis):
    new = []
    for i  in list(data):
        if findthis in i:
            new.append(re.sub(f'(\S+|{findthis}.*)',str(replaceforthis),i))
        else:
            new.append(i)
    return new