import pandas as pd
import numpy as np
import math

# Load the Excel file
file_name = '/Users/guillemhernandezsola/Downloads/Contactos_linkedin_120126_agile_6589pax_filtrado.xlsx'

print("Llegint el fitxer Excel...")

# --- CORRECCIÓ AQUÍ ---
# Fem servir read_excel en lloc de read_csv
df = pd.read_excel(file_name) 
# ----------------------

# Display head and info to understand the structure
print(df.head())
print(df.info())

# Total number of rows
total_rows = len(df)
print(f"Total rows: {total_rows}")

# Number of splits
n = 5
# Fem servir math.ceil o np.ceil per assegurar que no deixem files fora
chunk_size = int(np.ceil(total_rows / n))

# Split and save
output_files = []
print(f"Dividint en {n} parts...")

for i in range(n):
    start_row = i * chunk_size
    end_row = min((i + 1) * chunk_size, total_rows)
    
    # Si per algun motiu start_row supera el total, parem
    if start_row >= total_rows:
        break
        
    chunk = df.iloc[start_row:end_row]
    
    output_filename = f'Contactos_linkedin_part_{i+1}.xlsx'
    chunk.to_excel(output_filename, index=False)
    output_files.append(output_filename)

print(f"Files created: {output_files}")