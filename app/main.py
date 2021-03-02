from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/blogs.db")


def main():
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    user = User()
    user.surname = "Dead"
    user.name = "Line"
    user.age = 24
    user.position = "your dead"
    user.speciality = "your kill"
    user.address = "module_1"
    user.email = "dead_line@yandex.lyceum.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    user = User()
    user.surname = "Qwerty"
    user.name = "asd"
    user.age = 123
    user.position = "cap"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "random@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()
