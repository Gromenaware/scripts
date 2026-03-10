import pandas as pd
import os
import sys

print("📊 --- Unificador de fitxers Excel ---")

# Definim els noms dels fitxers d'entrada i el de sortida
fitxer1 = "Contactos_rrhh_040226.xlsx"
fitxer2 = "Contactos_2602026_7881pax.xlsx"
fitxer_resultat = "Contactos_Unificats.xlsx"

# Comprovem que els fitxers existeixen a la carpeta actual
if not os.path.exists(fitxer1):
    print(f"❌ Error: No s'ha trobat el fitxer '{fitxer1}'.")
    sys.exit(1)

if not os.path.exists(fitxer2):
    print(f"❌ Error: No s'ha trobat el fitxer '{fitxer2}'.")
    sys.exit(1)

print("⏳ Llegint els fitxers... (això pot trigar uns segons depenent de la mida)")

try:
    # Llegim els dos fitxers Excel
    df1 = pd.read_excel(fitxer1)
    df2 = pd.read_excel(fitxer2)
    
    # Creem el nou fitxer Excel amb múltiples pestanyes
    with pd.ExcelWriter(fitxer_resultat, engine='openpyxl') as writer:
        # Escrivim cada DataFrame en una pestanya diferent
        df1.to_excel(writer, sheet_name='RRHH', index=False)
        df2.to_excel(writer, sheet_name='Contactos_7881', index=False)
        
    print(f"✅ Procés completat amb èxit!")
    print(f"📄 S'ha creat el fitxer: {fitxer_resultat}")
    print("   - Pestanya 1: 'RRHH'")
    print("   - Pestanya 2: 'Contactos_7881'")

except Exception as e:
    print(f"❌ S'ha produït un error durant el procés: {e}")
