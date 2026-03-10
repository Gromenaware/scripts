import csv
import glob
import os
import sys

# 1. Comprovem si s'ha passat la ruta com a argument
if len(sys.argv) < 2:
    print("❌ Error: Has d'indicar la ruta de la carpeta.")
    print("💡 Ús correcte: python juntar_csv.py /ruta/de/la/carpeta")
    sys.exit(1)

# 2. Agafem la ruta (el primer argument després del nom de l'script)
carpeta_origen = sys.argv[1]

# Netegem possibles cometes que la terminal hagi afegit
carpeta_origen = carpeta_origen.strip("'").strip('"').strip()

# 3. Comprovem que la carpeta existeix
if not os.path.isdir(carpeta_origen):
    print(f"❌ Error: La ruta '{carpeta_origen}' no és vàlida o no és una carpeta.")
    sys.exit(1)

print(f"📁 Cercant fitxers CSV a: {carpeta_origen}")

ruta_cerca = os.path.join(carpeta_origen, "*.csv")
fitxers_csv = glob.glob(ruta_cerca)

# Definim el nom del fitxer final
fitxer_resultat = os.path.join(carpeta_origen, "Newsletter_Combinat_Final.csv")

if not fitxers_csv:
    print("⚠️ No s'han trobat fitxers CSV a la carpeta indicada.")
else:
    # Filtrem per no incloure el fitxer resultat si ja existeix d'una execució anterior
    fitxers_a_processar = [f for f in fitxers_csv if f != fitxer_resultat]
    
    if not fitxers_a_processar:
        print("⚠️ Només s'ha trobat el fitxer combinat anterior. No hi ha res de nou per unir.")
        sys.exit(0)
        
    print(f"🔄 S'han trobat {len(fitxers_a_processar)} fitxers. Processant...")
    
    # 4. Unifiquem els fitxers
    with open(fitxer_resultat, 'w', newline='', encoding='utf-8') as sortida:
        escrivent = csv.writer(sortida, delimiter=';')
        
        fitxers_processats = 0
        for nom_fitxer in fitxers_a_processar:
            with open(nom_fitxer, 'r', encoding='utf-8') as f:
                lector = csv.reader(f, delimiter=';')
                try:
                    capcalera = next(lector)
                except StopIteration:
                    continue # Saltem el fitxer si està completament buit
                
                # Escrivim la capçalera només pel primer fitxer vàlid
                if fitxers_processats == 0:
                    escrivent.writerow(capcalera)
                    
                # Escrivim la resta de dades
                for fila in lector:
                    escrivent.writerow(fila)
                    
            fitxers_processats += 1
            
    print(f"✅ Èxit! S'han combinat {fitxers_processats} fitxers.")
    print(f"📄 Fitxer creat a: {fitxer_resultat}")