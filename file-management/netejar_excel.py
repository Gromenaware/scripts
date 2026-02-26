import pandas as pd

# 1. Definir los nombres de los archivos
archivo_entrada = 'Contactos_2602026_totales.xlsx'
archivo_salida = 'Contactos_2602026_Limpios.xlsx'

print(f"Cargando el archivo: {archivo_entrada}...")

# 2. Leer el archivo Excel
# Asumimos que los datos están en la primera hoja (Sheet1)
df = pd.read_excel(archivo_entrada)

# Contar cuántos registros hay inicialmente
total_inicial = len(df)
print(f"Registros iniciales encontrados: {total_inicial}")

# 3. Eliminar duplicados basados en la columna 'email'
# keep='first' conserva la primera aparición del correo y elimina las siguientes
df_limpio = df.drop_duplicates(subset=['email'], keep='first')

# Contar cuántos registros quedaron y cuántos se eliminaron
total_final = len(df_limpio)
duplicados_eliminados = total_inicial - total_final

print(f"Se han eliminado {duplicados_eliminados} contactos duplicados.")
print(f"Registros finales únicos: {total_final}")

# 4. Exportar el resultado a un nuevo archivo Excel
print("Guardando el nuevo archivo limpio...")
df_limpio.to_excel(archivo_salida, index=False)

print(f"¡Proceso completado! Archivo guardado como: {archivo_salida}")
