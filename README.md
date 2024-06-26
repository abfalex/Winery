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
python3 main.py [wine_file]
```

Вместо `wine_file` используйте путь к excel-файлу с винами (смотрите пункт "Подготовка данных" ниже).

После этого приложение будет доступно по адресу http://localhost:8000/

## Подготовка данных

Если программа требует данных в описанном формате, вам нужно создать файл Excel (или Google Sheets) и заполнить его следующим образом:

- Создайте таблицу с заголовками "Категория", "Название", "Сорт", "Цена", "Картинка" и "Акция".
- Заполните строки таблицы данными согласно вашему примеру.

Вот пример, как это может выглядеть:

```
| Категория   | Название            | Сорт           | Цена | Картинка                |       Акция         |
|-------------|---------------------|----------------|------|-------------------------|---------------------|
| Белые вина  | Белая леди          | Дамский пальчик| 399  | belaya_ledi.png         | Выгодное предложение|
| Напитки     | Коньяк классический |                | 350  | konyak_klassicheskyi.png|                     |
| Белые вина  | Ркацители           | Ркацители      | 499  | rkaciteli.png           |                     |
| Красные вина| Черный лекарь       | Качич          | 399  | chernyi_lekar.png       |                     |
| Красные вина| Хванчкара           | Александраули  | 550  | hvanchkara.png          |                     |
| Белые вина  | Кокур               | Кокур          | 450  | kokur.png               |                     |
| Красные вина| Киндзмараули        | Саперави       | 550  | kindzmarauli.png        |                     |
| Напитки     | Чача                |                | 299  | chacha.png              | Выгодное предложение|
| Напитки     | Коньяк кизиловый    |                | 350  | konyak_kizilovyi.png    |                     |
```

Пример данного формата данных можно найти в файле `wine.xlsx`.

Теперь у вас есть подготовленные данные в нужном формате для использования программы.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
