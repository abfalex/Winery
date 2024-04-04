# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Установка

1. Склонируйте репозиторий на свой компьютер:

```bash
git clone https://github.com/abfalex/Winery.git
```

2. Перейдите в каталог проекта:

```bash
cd Winery
```

3. Создайте и активируйте виртуальное окружение (опционально):

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Установите зависимости из файла `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Запуск

Запустите приложение с помощью команды:

```bash
python main.py [wine_file]
```

Вместо `wine_file` используйте путь к excel-файлу с винами.

После этого приложение будет доступно по адресу http://localhost:8000/

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
