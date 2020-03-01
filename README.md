# Online courses

## Возможности

##### Все пользователи системы имеют следующие возможности:
- Регистрация (при регистрации выбирается роль пользователя -
Преподаватель/Студент)
- Авторизация(через jwt token)

##### Преподаватели имеют следующие возможности:

- CRUD своих курсов
- Добавление/Удаление студента к своему курсу
- Добавление нового преподавателя к своему курсу
- CRUD Лекций своих курсов (Лекция - это тема и файл с презентацией)
- К каждой лекции добавлять домашние задания (Текстовая информация)
- Просмотр выполненных домашних заданий
- К каждому выполненному домашнему заданию выставлять/менять оценки
для каждого студента, который отправил домашнее задание
- К каждой оценки добавлять комментарии.

##### Студенты имеют следующие возможности:
- Просмотр курсов, в которые студента добавил преподаватель
- Просмотр доступных лекций в рамках выбранного доступного курса
- Просмотр ДЗ доступной лекции
- Отправка ДЗ на проверку
- Просмотр своих ДЗ
- Просмотр оценок своих ДЗ
- Просмотр/Добавление комментариев к оценке.

На все действия установленны permissions, чтобы пользователи у которых нет доступа к этому курсу не смогли просмотрть/что-либо сделать в нём.

## Документация по api:
##### localhost:port/swagger/

## Docker
В docker-compose.yml вам нужно указать путь, где будут храниться данные с базы данных.
Для первого запуска используйте команду:

sudo docker-compose up -d --build

Порт по умолчанию установлен 2504

## Техническая информация:
- При создании курса создатель помещается также в поле Teachers. Удалить его от туда не получится. 
- Добавление учителей/ студентов происходит через методы create/update/put. Если вы ввели id пользователя, который уже находится в поле teachers, то он удалится и наоборот.
- Загружаемые файлы хранятся в папке uploads
- Файл удалится из хранилища при удалении модели, к которой он привзяан
