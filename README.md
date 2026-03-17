### How to Run the Project

Clone the repository and navigate to it from the command line:

```
git clone https://github.com/yandex-praktikum/anfisa2sprint.git
```

```
cd anfisa2sprint
```

Create and activate a virtual environment:

Windows
```
python -m venv venv
source venv/Scripts/activate
```
Linux/macOS
```
python3 -m venv venv
source venv/bin/activate
```

Upgrade `pip`:

Windows
```
python -m pip install --upgrade pip
```
Linux/macOS
```
python3 -m pip install --upgrade pip
```

Install dependencies from `requirements.txt`:

```
pip install -r requirements.txt
```

Apply migrations:

Windows
```
python manage.py makemigrations
python manage.py migrate
```

Linux/macOS
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Run the project:

Windows
```
python manage.py runserver
```

Linux/macOS
```
python3 manage.py runserver
```
