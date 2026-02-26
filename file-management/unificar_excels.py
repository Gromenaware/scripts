import pandas as pd

# 1. Cargar el primer archivo (tiene encabezados)
df1 = pd.read_excel('Contactos_linkedin_120126_agile_6589pax_filtrado.xlsx')

# 2. Cargar el segundo archivo (sin encabezados, asignamos los principales)
# Asumimos que las primeras 3 columnas son email, apellidos y nombre
df2 = pd.read_excel('lista_contactos_brevo_20251023_1394pax_AGILE611.xlsx', header=None)
df2.rename(columns={0: 'email', 1: 'apellidos_x', 2: 'nombre_x'}, inplace=True)

# 3. Unir ambos archivos (apilarlos uno debajo del otro)
df_final = pd.concat([df1, df2], ignore_index=True)

# 4. Eliminar contactos duplicados basados en la columna 'email'
df_final.drop_duplicates(subset=['email'], keep='first', inplace=True)

# 5. Exportar el resultado a un nuevo archivo Excel
df_final.to_excel('Contactos_Unificados_Agile611.xlsx', index=False)
print("¡Archivo unificado creado con éxito!")
