import csv
import sys
import os

# Comprovem que s'ha passat el fitxer com a argument
if len(sys.argv) < 2:
    print("❌ Error: Has d'indicar la ruta del fitxer CSV.")
    print("💡 Ús correcte: python netejar_desuscrits.py /ruta/al/Newsletter_Combinat_Final.csv")
    sys.exit(1)

fitxer_origen = sys.argv[1].strip("'").strip('"').strip()

if not os.path.isfile(fitxer_origen):
    print(f"❌ Error: No s'ha trobat el fitxer '{fitxer_origen}'.")
    sys.exit(1)

fitxer_desti = fitxer_origen.replace(".csv", "_Actius.csv")

usuaris_eliminats = 0
usuaris_actius = 0

print(f"🔍 Analitzant el fitxer: {fitxer_origen}")

with open(fitxer_origen, 'r', encoding='utf-8') as f_in, \
     open(fitxer_desti, 'w', newline='', encoding='utf-8') as f_out:
    
    lector = csv.reader(f_in, delimiter=';')
    escrivent = csv.writer(f_out, delimiter=';')
    
    # Llegim i escrivim la capçalera
    capcalera = next(lector)
    escrivent.writerow(capcalera)
    
    # Busquem l'índex de la columna de desuscripció
    try:
        index_unsub = capcalera.index("Unsubscribe_Date")
    except ValueError:
        print("❌ Error: No s'ha trobat la columna 'Unsubscribe_Date' al fitxer.")
        sys.exit(1)
        
    # Filtrem les files
    for fila in lector:
        # Si la columna està buida, l'usuari és actiu
        if len(fila) > index_unsub and not fila[index_unsub].strip():
            escrivent.writerow(fila)
            usuaris_actius += 1
        else:
            usuaris_eliminats += 1

print("✅ Neteja completada amb èxit!")
print(f"📉 Usuaris desuscrits eliminats: {usuaris_eliminats}")
print(f"📈 Usuaris actius conservats: {usuaris_actius}")
print(f"📄 Nou fitxer creat a: {fitxer_desti}")
