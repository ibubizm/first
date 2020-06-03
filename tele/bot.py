import requests

import wather

TOKEN = '1261204527:AAGdMEYgn3VllPVDNSC4PctAwCYxEOH-tzw'
URL = f'https://api.telegram.org/bot{TOKEN}/'


# print(URL)
# 'https://api.telegram.org/bot1261204527:AAGdMEYgn3VllPVDNSC4PctAwCYxEOH-tzw/sendmessage?chat_id=902879948&text=zuzu'

def get_updates():
    url = URL + 'getUpdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']

    text = data['result'][-1]['message']['text']

    message = {
        'chat_id': chat_id,
        'text': text
    }
    return message


def send_message(chat_id, text='Wait please'):
    url = URL + 'sendMessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():
    answer = get_message()
    chat_id = answer['chat_id']
    text = answer['text']
    while True:
        try:
            if 'Minsk' or 'London' or 'Moscow' in text:
                send_message(chat_id, str(wather.get_wather()))
        except:
            None


if __name__ == '__main__':
    main()
