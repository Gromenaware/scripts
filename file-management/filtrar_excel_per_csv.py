import pandas as pd
import os
import sys

print("🔍 --- Filtrant Excel segons usuaris actius del CSV ---")

# Noms dels fitxers
fitxer_csv = "Newsletter_Combinat_Final_Actius.csv"
fitxer_excel = "Contactos_Unificats.xlsx"
fitxer_resultat = "Contactos_Unificats_Filtrats.xlsx"

# Comprovem que existeixen
if not os.path.exists(fitxer_csv) or not os.path.exists(fitxer_excel):
    print("❌ Error: Assegura't que els fitxers CSV i Excel són a la mateixa carpeta.")
    sys.exit(1)

try:
    print("⏳ Llegint els usuaris actius del CSV...")
    # Llegim el CSV (sabem que està separat per punt i coma)
    df_csv = pd.read_csv(fitxer_csv, sep=';', encoding='utf-8')
    
    # Extraiem els correus de la columna 'Email_ID', els passem a minúscules i traiem espais en blanc
    # per assegurar-nos que coincideixen perfectament
    correus_actius = set(df_csv['Email_ID'].dropna().astype(str).str.lower().str.strip())
    print(f"✅ S'han carregat {len(correus_actius)} correus únics del CSV.")

    print("⏳ Processant l'Excel pestanya per pestanya...")
    # Obrim l'Excel original i preparem el nou per escriure
    excel_original = pd.ExcelFile(fitxer_excel)
    
    with pd.ExcelWriter(fitxer_resultat, engine='openpyxl') as writer:
        for nom_pestanya in excel_original.sheet_names:
            # Llegim la pestanya actual
            df_pestanya = pd.read_excel(excel_original, sheet_name=nom_pestanya)
            total_inicial = len(df_pestanya)
            
            # Normalitzem la columna 'email' de l'Excel per poder comparar-la
            if 'email' in df_pestanya.columns:
                correus_excel = df_pestanya['email'].astype(str).str.lower().str.strip()
                
                # Filtrem: ens quedem només amb les files on el correu estigui a la nostra llista d'actius
                df_filtrat = df_pestanya[correus_excel.isin(correus_actius)]
                total_final = len(df_filtrat)
                
                print(f"   👉 Pestanya '{nom_pestanya}': s'han mantingut {total_final} de {total_inicial} contactes.")
            else:
                print(f"   ⚠️ Avís: La pestanya '{nom_pestanya}' no té cap columna anomenada 'email'. Es deixa intacta.")
                df_filtrat = df_pestanya
                
            # Guardem el resultat a la mateixa pestanya del nou fitxer
            df_filtrat.to_excel(writer, sheet_name=nom_pestanya, index=False)

    print(f"\n🎉 Procés completat amb èxit!")
    print(f"📄 S'ha creat el fitxer amb els contactes filtrats: {fitxer_resultat}")

except Exception as e:
    print(f"❌ S'ha produït un error: {e}")
