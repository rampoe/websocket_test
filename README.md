# websocket_test

## 📖 Installation
websocket_test can be installed via Pip. To start, clone the repo to your local computer and change into the proper directory.

```
$ git clone https://github.com/wsvincent/websocket_test.git
$ cd websocket_test
```

### Pip

```
$ python -m venv .venv

# Windows
$ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
$ .venv\Scripts\Activate.ps1

# macOS
$ source .venv/bin/activate

(.venv) $ pip install -r requirements.txt
(.venv) $ python manage.py migrate
(.venv) $ python manage.py createsuperuser
(.venv) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```