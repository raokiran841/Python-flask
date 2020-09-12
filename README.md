create a folder "newFlask" say.
on cmd to this folder location and type
  python -m venv venv
venv folder will be created.
Now activate venv
  venv\Scripts\activate.bat
for MacOS
  source venv/Scripts/activate
to deactivate
  deactivate

check the list of packages insatlled already
  pip list
install flask
  pip install flask [--proxy=optional]
  pip list
create a app.py file in the folder
write the code and run using
  python app.py
