#   This is TECHMAPS

## How to run first time

1.  Install python

2.  Create a folder, name it techmaps

2.  CD into the folder and pull from git by running in console `git clone https://github.com/Kharay33455/TechMaps.git` *You would only clone here, pull afterwards*

3.  Go back to tech maps and create your virtual environment 
    *  venv =>    `python -m venv <name_of_env>`
    *  virtualenv => `virtualenv <name_of_env>`

4. Activate your environment
    *   windows: `<name_of_env>/scripts/activate`
    *   linux:  `source <name_of_env>/bin/activate`

5.  cd back into the folder you pulled from git.. where you can see the *requirements.txt* file.

6.  run `pip install -r requirements.txt`

7.  IN the same path ad .gitignore, create a .env file `code .env` for windows or `nano .env` for linux
    *   Add the following <br/>

        DB_URL = db.sqlite3 <br/>
        SECRET_KEY =   pickAnyLongStringValueMakeItVeryLongAndAddThese:)(U(T*R&YTY@*&*(#U&(*(*#&&*)))))avoidquotesymbols <br/>
        DEBUG = True

7.  Run `python manage.py migrate`

8.  run `python manage.py runserver`

