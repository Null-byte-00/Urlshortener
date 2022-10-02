# Urlshortener
A tool for turning long urls into short links
## requirements:
<ul>
<li>python3 (download from https://www.python.org/downloads/)</li>
<li>virtualenv(run: pip install virtualenv )</li>
</ul>

# To use:
### Clone repository:
```
git clone https://github.com/Null-byte-00/Urlshortener/new/main
```
###  Enter repository's directory
```
cd UrlShortener
```
### Create a virtual enviroment 
```
virtualenv venv
```
### Activte your virtual enviroment
Bash:
```
sorce venv/Scripts/activate
```
Powershell:
```
.\venv\Scripts\activate.ps1
```
### install requirements
```
pip install -r requirements.txt
```
### Create database
```
python urlshortener/manage.py makemigrations
python urlshortener/manage.py migrate
```
### Run the server
```
python urlshortener/manage.py runserver
```
Now go to http://127.0.0.1:8000
