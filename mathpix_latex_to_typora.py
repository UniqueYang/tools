import os
import base64
import requests
import json
import pyperclip

env = os.environ

default_headers = {
    'app_id': env.get('APP_ID', 'xxxxxxxxx'),
    'app_key': env.get('APP_KEY', 'xxxxxxxxxx'),
    'Content-type': 'application/json'
}

service = 'https://api.mathpix.com/v3/latex'

#
# Return the base64 encoding of an image with the given filename.
#


def image_uri(filename):
    image_data = open(filename, "rb").read()
    return "data:image/jpg;base64," + base64.b64encode(image_data).decode()

#
# Call the Mathpix service with the given arguments, headers, and timeout.
#


def latex(args, headers=default_headers, timeout=30):
    r = requests.post(service,
                      data=json.dumps(args), headers=headers, timeout=timeout)
    return json.loads(r.text)


def mathpix_clipboard():  # 识别剪贴板公式
    os.system(
        'xclip -selection clipboard -t image/png -o > /home/yang/Documents/latex/equa.png')
    r = latex({
        'src': image_uri("/home/yang/Documents/latex/equa.png"),
        'formats': ['latex_simplified']
    })
    pyperclip.copy("$" + r['latex_simplified'] + "$")

if __name__ == '__main__':
    mathpix_clipboard()
