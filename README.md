# 🚗 Concessionari Django - CRUD de Marques i Models

Aquest projecte és una aplicació web desenvolupada amb el framework **Django** per a la gestió d'un concessionari. Permet administrar marques de cotxes i els seus models associats mitjançant una interfície d'usuari intuïtiva amb operacions CRUD completes. 

Aquest repositori correspon a l'entrega de l'activitat de desplegament d'un Framework de servidor.

## 🌟 Característiques principals
* **CRUD complet**: Operacions per Crear, Llegir, Actualitzar i Esborrar (CRUD) marques de cotxes des del *frontend*.
* **Bases de Dades Relacionals**: Implementació d'una relació *Un a Molts* (1:N) on una Marca pot tenir múltiples Models de cotxe.
* **Panell d'Administració**: Configuració de l'Admin de Django per gestionar tant les Marques com els Models de forma interna.
* **Disseny UI**: Interfície estilitzada utilitzant l'herència de plantilles de Django (`base.html`).

## 🛠️ Tecnologies utilitzades
* Python 3
* Django (Framework Backend)
* SQLite (Base de dades per defecte)
* HTML/CSS (Frontend)

## 🚀 Instal·lació i ús

Si vols clonar i executar aquest projecte al teu entorn local, segueix aquests passos:

**1. Clona el repositori:**
\`\`\`bash
git clone https://github.com/aybkh/django-crud-concessionari.git
cd django-crud-concessionari
\`\`\`

**2. Crea i activa l'entorn virtual:**
\`\`\`bash
python3 -m venv env
source env/bin/activate
\`\`\`

**3. Instal·la les dependències:**
\`\`\`bash
pip install -r requirements.txt
\`\`\`

**4. Aplica les migracions de la base de dades:**
\`\`\`bash
python3 manage.py migrate
\`\`\`

**5. Crea un superusuari per accedir a l'admin:**
\`\`\`bash
python3 manage.py createsuperuser
\`\`\`

**6. Executa el servidor local:**
\`\`\`bash
python3 manage.py runserver
\`\`\`

Un cop arrencat, pots accedir a la web principal anant a `http://127.0.0.1:8000/` i al panell d'administració a `http://127.0.0.1:8000/admin`.

---
**Autor:** Ayoub El Khalifi Idrissi El Jerari

