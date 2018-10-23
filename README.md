# Project 2

Для project 2 я створила інтернет-сервіс обміну повідомленнями Slack, 
використовуючи мови Python та JavaScript, а також технології Flask та Socket.IO.

При першому відвідуванні сайту користувач повинен ввести ім'я, яке буде пов'язане з кожним повідомленням, надісланим користувачем.
Якщо користувач покине сайт та відвідає його знову, його ім'я збережеться. Пізніше його можна буде змінити.

Коритувач може вибрати один з існуючих каналів чи створити новий, якщо каналу з такою назвою ще не існує.
Якщо користувач покине сайт під час перегляду певного каналу, при наступному відвідуванні сайту його автоматично скерує на цей канал.

При виборі каналу відображаються останні 100 повідомлень, які біли надіслані у цьому каналі. 
Користувач може додати нове непорожнє повідомлення і воно з'явиться на екранах усіх користувачів, які зараз переглядають цей канал.
Окрім власне тексту повідомлення відображаються також його автор та час надсилання.

---

For project 2 I created an online massaging service Slack,
using such languages as Python and JavaScript and aslo such tecnologies as Flask and Socket.IO.

At the first visit of the site user must type in the name, that will be associated with every message the user sends.
If the user leaves the site and visits it again his username will be saved.
Later it can be changed.

The user can choose one of the existing channels or create a new one, if a channel with this name doesn`t already exist.
If the user leaves the site during the review of some particular channel, during the naxt visit he will be automatically redirected to that channel.

When choosing a channel, the last 100 massages that were sent in this channel will be displayed.
The user can add a new unemptymassage and it will appear on the screens of all users, who are currently viewing this channel.
Besides accually the text of the massage, his author and the time whet it was sent are also displayed.