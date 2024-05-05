- Python 3.9
- SQLLite3
- Django
- Bootstrap 5.3

To keep the project realtively simple there is no JavaScript at the moment.
If we want to improve the UX in the future we can use HTMX and JQuery 
to get a more App like feel.


Project Setup locally
Python 3.9 should be installed and active

1. Create a virtualenv in a directory of your choice and activate it
```
python -m venv /path/to/new/virtual/environment
```
```
source /YourVirtualEnvPath/bin/activate
```
2. Clone the repository

3. Move to directory which contains the file
```
requirements.txt
```
4. install the requirements.txt file
```
pip install -r requirements.txt
```
5. Move to directory events
```
cd events
```
6. Start the local server
```
python3 manage.py runserver
```