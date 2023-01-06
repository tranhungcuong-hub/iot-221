# IOT-Irrigation-App

## Installation

### Clone source code using git:

```bash
git clone https://github.com/tranhungcuong-hub/iot-221.git
```

### Create virtual environment

```python
python -m venv env
```

### Activate env

For MacOS and Ubuntu
```python
source env/bin/activate
```

For window
```python
env/Scripts/activate
```

### Install all packages in requirements.txt

```python
pip install -r requirements.txt
```

## Usage

First, Start the local server
To do it, we have to entry the folder contain manage.py
Then using command:
```python
python manage.py makemigrations
python manage.py migrate
```

Second step, run the server:
```python
python manage.py runserver
```

Now we will run the flutter application.
You have to install flutter.
Go to folder my app.
then use command:
```flutter
flutter run
```

Remember to open your virtual device before running flutter application.