<<<<<<< HEAD
# Предиктивная аналитика больших данных

Учебный проект для демонстрации процесса разработки сервиса предиктивной аналитики. 


## Installation 

Клонируйте репозиторий, создайте виртуальное окружение, активируйте и установите зависимости:  

```sh
git clone https://github.com/yourgit/pabd24
cd pabd24
python -m venv venv

source venv/bin/activate  # mac or linux
.\venv\Scripts\activate   # windows

pip install -r requirements.txt
```

## Usage

### 1. Сбор данных о ценах на недвижимость 
Скрипт parse_cian.py используется для извлечения информации о продаже квартир с веб-сайта cian.ru. По умолчанию он собирает данные о продаже однокомнатных квартир с первых двух страниц сайта и сохраняет результаты в формате CSV в папке data/raw.
```sh
python src/parse_cian.py
```


### 2. Выгрузка данных в хранилище S3 

Скрипт upload_to_s3.py предназначен для загрузки указанных локальных файлов данных в хранилище Amazon S3. Для работы скрипта необходим файл .env с ключами доступа AWS, расположенный в корне проекта. Основные параметры скрипта включают:

-i, --input: список файлов данных для загрузки в S3. По умолчанию эти файлы указаны непосредственно в скрипте.
```sh
python src/upload_to_s3.py -i data/raw/file1.csv data/raw/file2.csv
``` 

### 3. Загрузка данных из S3 на локальную машину  
Скрипт download_from_s3.py предназначен для загрузки файлов с хранилища Amazon S3 обратно на локальный диск. Он поддерживает следующие параметры:

-i, --input: список файлов, которые требуется загрузить с S3 на локальную машину. По умолчанию эти файлы уже указаны непосредственно в коде скрипта.

```sh
python src/download_from_s3.py -i data/raw/file1.csv data/raw/file2.csv
``` 
### 4. Предварительная обработка данных  
Файл preprocess_data.py преобразует сырые данные в датасеты для обучения и валидации. Записывает результаты в папку data/proc.
параметры:
-s, --split - доля данных, идущая на обучающий набор (по умолчанию 0.9).
-i, --input - список CSV файлов для обработки (по умолчанию указаны в скрипте).

```sh
python src/preprocess_data.py -s 0.9 -i data/raw/file1.csv data/raw/file2.csv
``` 

### 5. Обучение модели 
Файл train_model.py производит обучение модели и сохранение контрольной точки. Для предсказания цены недвижимости используется линейная регрессия. Модель обучается на данных о площади квартиры и её цене.
Параметры:

-m, --model - путь для сохранения обученной модели (по умолчанию 'models/linear_regression_v01.joblib').

```sh
python src/train_model.py -m models/linear_regression_v01.joblib
``` 


### 6. Запуск приложения flask 

todo

### 7. Использование сервиса через веб интерфейс 

Для использования сервиса используйте файл `web/index.html`.  

>>>>>>> 194c62d94fc5690fff1a5395b67bd68f18a20f98
