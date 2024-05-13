# Предиктивная аналитика больших данных 

Учебный проект для демонстрации процесса разработки сервиса предиктивной аналитики. 
Мы будем шаг за шагом разрабатывать сервис, предсказывающий цены на недвижимость. 

### Балльно-рейтинговая система:  

**Экзамен** - 60 баллов  

**Текущая успеваемость** - 40 баллов, вкл:  
4 лаб работы по 8 баллов = 32  
Активность на занятиях (тесты) = 8

Лекции и литература находятся на [Google Drive](https://drive.google.com/drive/folders/1cUry7oySkAJ5OB5lMGQcMceTO2nWxUHT?usp=drive_link)  

Текущая успеваемость студентов выставляется в таблице, которую можно найти в [файле](docs/results.csv)

Ссылки на свои репозитории и решения практических задач экзамена присылайте на почту ailabintsev@fa.ru   
Тесты проходить в классе на занятиях, в присутствии преподавателя.  

## План семинаров

### 1. Настройка окружения. Основы работы с bash, git, pycharm
Основные команды bash и git. 
Создание проекта с именем **pabd24** и публикация на github.  
Внесение первых правок через pull request.  

**Результат:**  
1. Cсылка на проект у меня на почте - 2 балла. 
2. Ветка master - защищена от прямых коммитов - 1 балл. 
3. Ветка tmp - содержит в README.md строчку о том, что это другая ветка - 1 балл. 

### 2. Сбор данных. Предобработка с помощью скриптов.  
Парсинг циан.  
Работа с переменнымы окружения .env  
Работа с хранилищем S3.  
Первичный анализ данных и скрипт предобработки данных.  

Файл .env находится в [Google Drive](https://drive.google.com/drive/folders/1cUry7oySkAJ5OB5lMGQcMceTO2nWxUHT?usp=drive_link)    
Посмотреть содержимое бакета можно по ссылке https://storage.yandexcloud.net/pabd24  

**Результат:**  
1. 3 CSV файла результатами парсинга для 1, 2, 3 комнатных квартир (по 50 на каждую) - 2 балла.  
2. Эти же файлы размещены на S3 бакете в папке с Вашим ID - 2 балла.   
3. Настроен пайплайн для загрузки Ваших данных из хранилища S3 и препроцессингу - 2 балла.   
4. В README.md Вашего проекта есть описание скриптов - 2 балла. 

### 3. Обучение модели. Оценка метрик. 

### 4. Версионирование экспериментов. Документирование проекта.