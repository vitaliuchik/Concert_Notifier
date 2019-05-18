# Concert Notifier

Додаток `Concert Notifier` дозволяє на основі аналізу облікового запису Google Play Music користувача визначати його улюблених виконавців. Додаток моніторить сервіс [Concert UA](http://concert.ua) та повідомляє користувача, якщо хтось із його улюблених виконавців буде мати концерт на території Ураїни в найближчому майбутньому.


Інструкція
----------
Установити пакети з requirements.txt

    $ pip install -r requirements.txt
    
Запустити файл login.py з консолі

    $ python scripts/login.py
 
Після запуску програмою браузера, авторизуватися в обліковому записі Google Play Music

Скопіювати ключ доступу з браузера, який появиться після авторизації

Вставити ключ доступу в поле вводу в консолі запущеної програми

Після завершення роботи програми login.py запустити app.py

    $ export FLASK_APP=app.py
    $ flask run

В полі вводу веб-додатку ввести Device ID пристрою, на якому ви користуєтесь сервісом Google Play Music та кількість улюблених виконавців для аналізу

В разі успішного знаходження концерту хоча б одного улюбленого виконавця на території України, додаток повертає сторінку з силками на події.

Credits
-------
Vitalii Papka


License
-------
Copyright (c) [2019] [Vitalii Papka]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
  
