from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment
from datetime import datetime
from dateutil.relativedelta import relativedelta
from openpyxl.worksheet.table import Table
import shutil
import os


TEMPLATE_PATH = "templates/Modulo-00.xlsx"
EXPORT_PATH = "scripts/exports"

def formatear_cuit(cuit):

    cuit = cuit.strip()

    cuit = "".join(filter(str.isdigit, cuit))

    if len(cuit) != 11:
        raise ValueError("CUIT Invalido")
    
    return f"{cuit[:2]}-{cuit[2:10]}-{cuit[10]}"

def generar_periodos(desde, hasta):

    fecha_desde = datetime.strptime(
        desde,
        "%Y-%m"
    )

    fecha_hasta = datetime.strptime(
        hasta,
        "%Y-%m"
    )

    periodos = []

    while fecha_desde <= fecha_hasta:

        periodos.append(
            fecha_desde.strftime("%Y-%m")
        )

        fecha_desde += relativedelta(
            months=1
        )

    return periodos


def generar_modulo(empresa,cuit,desde,hasta,acta):

    cuit_formateado = formatear_cuit(cuit)

    caracteres_invalidos = ["/", ":", "|"]

    for caracter in caracteres_invalidos:
       empresa = empresa.replace(caracter, "-")

    empresa_nombre = empresa.upper()

    nombre_archivo = f"Acta N° {acta} - {empresa_nombre}.xlsx"
    ruta_salida = os.path.join(EXPORT_PATH,nombre_archivo)

    # copia de template
    shutil.copy(TEMPLATE_PATH, ruta_salida)

    # abrir excel
    wb = load_workbook(ruta_salida)

    periodos = generar_periodos(
        desde,
        hasta
    )
    
    # HOJA BASE
    ws_base = wb.active
    
    # CREAR HOJAS
    for index, periodo in enumerate(periodos):

        if index == 0:

            ws = ws_base

        else:

            ws = wb.copy_worksheet(ws_base)

        ws.title = periodo

        if index != 0 and ws_base.tables:

            tabla_original = list(ws_base.tables.values())[0]

            nueva_tabla = Table(
                displayName = F"Modulo_00_{index:03}",
                ref=tabla_original.ref
            )

            nueva_tabla.tableStyleInfo = (
                tabla_original.tableStyleInfo
            )

            ws.add_table(nueva_tabla)
   
        # llevar datos al excel
        ws["B4"] = empresa.upper()
        ws["B4"].font = Font(
            name="Arial",   #tipo de letra
            size=20,        #tamaño        
            bold=True,      #negrita
            italic=True,    #cursiva
        )
        ws["B4"].alignment = Alignment(
            vertical="bottom",
            horizontal="left",
        )

        ws["C5"] = cuit_formateado
        ws["C5"].font = Font(
            name="Arial",
            size=11,
            italic=True,
        )
        ws["C5"].alignment = Alignment(
            vertical="bottom",
            horizontal="right",
        )

        ws["I6"] = periodo
        ws["I6"].font = Font(
            name="Arial",
            size=11,
            italic=True
        )
        ws["I6"].alignment = Alignment(
            vertical="bottom",
            horizontal="right",
        )

        ws["C6"] = acta
        ws["C6"].font = Font(
            name="Arial",
            size=11,
            italic=True,
            )
        ws["C6"].alignment = Alignment(
            vertical="bottom",
            horizontal="right",
        )
    
    wb.save(ruta_salida)

    return ruta_salida

    