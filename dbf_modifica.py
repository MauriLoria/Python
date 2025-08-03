from simpledbf import Dbf5
import pandas as pd
import os
import dbf

dbfPath = "c:/AVILES/LOCALIDA.DBF"
if os.path.exists(dbfPath)==False:
    exit()

df = Dbf5(dbfPath, codec= "latin1").to_dataframe()

#def agregar(codpostal, localidad, codtele, provincia, df):
#    nuevo = pd.DataFrame({'CODPOSTAL': codpostal, 'LOCALIDAD': localidad,
#                        'CODTELE': codtele, 'PROVINCIA': provincia}, index=['row3'])
#    df2 = pd.concat([df, nuevo], ignore_index=True)
#    df3 = df2.sort_values(by= "CODPOSTAL")
#    print(df3)
#    df = df3
#    return df


df2 = df.sort_values(by= "CODPOSTAL")

agregar= pd.DataFrame({'CODPOSTAL': ["9600"], 'LOCALIDAD': ["SAN ANDRES"],
                        'CODTELE': ["2027"], 'PROVINCIA': ["MAS FELICIDAD"]},
                          index=['row3'])
df3 = pd.concat([df2, agregar], ignore_index=True)

# Hacer el agregado con la funcion "agregar"
#agregar(9600, "BOMBINHAS", 2026, "FAMILIA", df)
print(df3)

df3 = df3.fillna({
    'CODPOSTAL': '',
    'LOCALIDAD': '',
    'CODTELE': '',
    'PROVINCIA': ''
})

print(df3.isna().sum())

nuevo_dbf = "c:/AVILES/LOCALIDAD.DBF"

estructura = 'CODPOSTAL C(4); LOCALIDAD C(20); CODTELE C(5); PROVINCIA C(20)'
if os.path.exists(nuevo_dbf):
    os.remove(nuevo_dbf)

tabla = dbf.Table(
    nuevo_dbf,
    estructura,
    codepage='cp1252'
)
tabla.open(mode=dbf.READ_WRITE)

for _, fila in df3.iterrows():
    tabla.append((
        str(fila['CODPOSTAL']),
        str(fila['LOCALIDAD']),
        str(fila['CODTELE']),
        str(fila['PROVINCIA'])
    ))

tabla.append({
    'CODPOSTAL': '9700',
    'LOCALIDAD': 'BOMBINHAS',
    'CODTELE': '2026',
    'PROVINCIA': 'FAMILIA'
    })
tabla.append({
    'CODPOSTAL': '9800',
    'LOCALIDAD': 'PUNTA DEL ESTE',
    'CODTELE': '2025',
    'PROVINCIA': 'URUGUAY'
    })

tabla.close()

