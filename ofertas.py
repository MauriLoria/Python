from simpledbf import Dbf5
import pandas as pd
import os
import dbf

dbfPath = "c:/AFA/OFERTAS.DBF"
if os.path.exists(dbfPath)==False:
    exit()


df = Dbf5(dbfPath, codec= "latin1").to_dataframe()
print(df.loc[:,("CODIGO","DETALLE")])

def agregar(codigo, detalle, fijo, promo, descan, efectivo, feci, fecv, bonif, bulto, scan):
    global df
    nuevo = pd.DataFrame({'CODIGO': codigo, 'DETALLE': detalle,'FIJO': fijo,
                        'PROMO': promo, 'DESCAN': descan, 'EFECTIVO': efectivo,
                        'FECI': feci, 'FECV': fecv, 'BONIF': bonif, 'BULTO': bulto,
                        'SCAN': scan}, index=['row1'])
    df1 = pd.concat([df, nuevo], ignore_index=True)
    df1 = df1.sort_values(by= "DETALLE")
    return df1

codigo, detalle, descan, feci, fecv, scan, otro = '', '', '', '', '', '', "N"
fijo, promo, efectivo, bonif, bulto = 0, 0, 0, 0, 0

while otro == "N" or otro == "n":
    codigo = input("Ingrese un nuevo Código: ")
    if codigo in df.values:
        print("Código ya está ingresado")
        #otro = "S"
    else:
        detalle = input("Ingrese el Detalle: ")
        fijo = float(input("Ingrese el Precio Fijo: "))
        promo = float(input("Ingrese Dto. Promo: "))
        efectivo = float(input("Ingrese Dto. por Efectivo: "))
        feci = input("Ingrese Fecha Inicio Promo: ")
        fecv = input("Ingrese Fecha Vcto. Promo: ")
        descan = input("Ingrese Dto. por Cantidad S/N: ")
        bonif = float(input("Ingrese Bonificación: "))
        bulto = float(input("Ingrese Bulto: "))
        scan = input("Ingrese Codigo de Barras ")
        conf = input("Confirma el ingreso? s/n: ")
        if conf == "s" or conf == "S":
            df3 = agregar(codigo, detalle, fijo, promo, descan, efectivo, feci, fecv, bonif, bulto, scan)
            df3 = df3.sort_values(by= "DETALLE")
            print(df3)
            df3 = df3.fillna({
                'CODIGO': '',
                'DETALLE': '',
                'FIJO': 0,
                'PROMO': 0,
                'DESCAN': '',
                'EFECTIVO': 0,
                'FECI': '',
                'FECV': '',
                'BONIF': 0,
                'BULTO': 0,
                'SCAN': ''
            })

            nuevo_dbf = dbfPath
            estructura = 'CODIGO C(8); DETALLE C(20); FIJO N(11,3); PROMO N(6,4); DESCAN C(1); EFECTIVO N(6,4); FECI C(8); FECV C(8); BONIF N(6,4); BULTO N(6,2); SCAN C(24) '

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
                    str(fila['CODIGO']),
                    str(fila['DETALLE']),
                    float(fila['FIJO']),
                    float(fila['PROMO']),
                    str(fila['DESCAN']),
                    float(fila['EFECTIVO']),
                    str(fila['FECI']),
                    str(fila['FECV']),
                    float(fila['BONIF']),
                    float(fila['BULTO']),
                    str(fila['SCAN']),
                ))

            tabla.close()

