#api_yamdb
Проект «YaMDb»

Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:\
`git clone https://github.com/SVSergej/api_yamdb.git` \
`cd api_yamdb`

Cоздать и активировать виртуальное окружение:\
`python3 -m venv env` \
`source venv/bin/activate`

Установить зависимости из файла requirements.txt:
`python3 -m pip install --upgrade pip` \
`pip install -r requirements.txt`

Выполнить миграции:\
`python3 manage.py migrate` \
`python3 manage.py makemigrations`

Запустить проект:\
`python3 manage.py runserver` 

Более подробная документация о проекте:\
`http://127.0.0.1:8000/redoc/`
