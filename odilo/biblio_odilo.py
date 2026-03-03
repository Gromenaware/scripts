import requests

# 1. Definim les capçaleres
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'ie',
    'Host': 'odiloid.odilo.us'
}

url_api = 'https://odiloid.odilo.us/ClientId'

try:
    # 2. Fem la petició
    print("⏳ Obtenint dades del servidor...")
    response = requests.get(url_api, headers=headers)
    response.raise_for_status()
    
    # 3. Convertim a JSON (llista de diccionaris)
    bibliolist_response = response.json()
    
    # 4. Filtrem només les URLs
    llista_urls = [biblio['url'] for biblio in bibliolist_response if 'url' in biblio]
    
    # 5. Mostrem el resultat per pantalla
    print(f"✅ S'han trobat {len(llista_urls)} biblioteques. Aquí tens les URLs:\n")
    
    for url in llista_urls:
        print(url)

except requests.exceptions.RequestException as e:
    print(f"❌ Hi ha hagut un error amb la petició: {e}")
