import pandas as pd
import glob
import re
import os
import csv

def extreure_minuts(temps_str):
    """Converteix cadenes de text com '2h 15m', '45m' o '1h' a minuts totals."""
    if pd.isna(temps_str):
        return 0
    temps_str = str(temps_str).lower()
    hores = 0
    minuts = 0
    
    match_h = re.search(r'(\d+)\s*h', temps_str)
    if match_h:
        hores = int(match_h.group(1))
        
    match_m = re.search(r'(\d+)\s*m', temps_str)
    if match_m:
        minuts = int(match_m.group(1))
        
    return (hores * 60) + minuts

fitxers = glob.glob("*.csv")
dades_alumnes = {}

if not fitxers:
    print("⚠️ No s'han trobat fitxers CSV a la carpeta actual.")
else:
    print(f"S'han trobat {len(fitxers)} fitxers. Processant dades...\n")

for fitxer in fitxers:
    try:
        # 1. Obrim el fitxer manualment per buscar a quina fila comencen les dades
        with open(fitxer, 'r', encoding='utf-16') as f:
            linies = f.readlines()
            
        fila_capcalera = -1
        separador = '\t'
        
        # Busquem la línia que conté "Nom" o "Nombre" o "Name"
        for i, linia in enumerate(linies):
            if 'Nom' in linia or 'Nombre' in linia or 'Name' in linia:
                fila_capcalera = i
                # Detectem si fa servir tabulacions o comes
                if ',' in linia and '\t' not in linia:
                    separador = ','
                break
                
        if fila_capcalera == -1:
            print(f"⚠️ Saltant '{fitxer}': No s'ha trobat cap fila amb la paraula 'Nom'.")
            continue

        # 2. Llegim el CSV dient-li exactament on comença
        df = pd.read_csv(fitxer, sep=separador, encoding='utf-16', skiprows=fila_capcalera)
        
        # 3. Busquem les columnes dinàmicament
        col_durada = next((col for col in df.columns if 'durada' in col.lower() or 'duración' in col.lower() or 'duration' in col.lower()), None)
        col_nom = next((col for col in df.columns if 'nom' in col.lower() or 'nombre' in col.lower() or 'name' in col.lower()), None)

        if not col_nom or not col_durada:
            print(f"⚠️ Saltant '{fitxer}': Columnes invàlides. Trobades: {list(df.columns)}")
            continue

        for index, row in df.iterrows():
            nom = row[col_nom]
            if pd.isna(nom):
                continue
                
            minuts = extreure_minuts(row[col_durada]) 
            
            # Apliquem la regla del 5 de febrer (límit de 205 minuts)
            if "2-05-26" in fitxer and minuts > 205:
                minuts = 205
                
            if nom in dades_alumnes:
                dades_alumnes[nom] += minuts
            else:
                dades_alumnes[nom] = minuts
                
    except UnicodeError:
        print(f"❌ Error de codificació al fitxer '{fitxer}'. Intenta obrir-lo i guardar-lo de nou.")
    except Exception as e:
        print(f"❌ Error processant el fitxer '{fitxer}': {e}")

# 4. Resultats
if dades_alumnes:
    print("="*50)
    print("📊 RESULTATS D'ASSISTÈNCIA (Mínim requerit: 1581 min)")
    print("="*50)

    for nom in sorted(dades_alumnes.keys()):
        minuts_totals = dades_alumnes[nom]
        
        if minuts_totals >= 1581:
            estat = "✅ Supera el 80%"
        else:
            estat = "❌ No arriba"
            
        h = minuts_totals // 60
        m = minuts_totals % 60
        
        print(f"{nom}: {minuts_totals} minuts ({h}h {m}m) -> {estat}")