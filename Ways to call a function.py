def send_email(message, recipient, sender='university.help@gmail.com'):
    ending = ('.com', '.ru', '.net')
    if "@" not in recipient or not recipient.endswith(ending) or "@" not in sender or not sender.endswith(ending):
        print(f"невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"нестандартный отправитель! письмо отправлено с адреса {sender} на адрес {recipient}.")




send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
