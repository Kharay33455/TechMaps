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

7.  Run `python manage.py runserver` 



### NOTE:

    Edit your settings.py file and create a gitignore. Use it to stop tracking your settings.py file before you make any pushes