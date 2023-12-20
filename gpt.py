from pyrogram import Client, filters
from pyrogram.types import Message
import requests


api_id = "10613468"
api_hash = "7dd4310ae796d1155c1da48a0d8b0794"
bot_token = "6986318068:AAHBC04rac3vgMW3CYKLWgH-hnpeH8VtZ28"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_message(filters.command("start"))
def start_command(client, message):
    user = message.from_user
    name = user.first_name if user.first_name else ""
    client.send_message(
        chat_id=message.chat.id,
        text=f"Merhaba {name}! Jesus GPT Bot'a Hoş Geldin\n\n"
             f"Bana Çekinmeden Her Şeyi Sorabilirsin.\n\n"
             f"Lütfen Sorularınızı /gpt komutu ile girin."
    )


@app.on_message(filters.command("gpt"))
def gpt_command(client, message):
    if len(message.text.split()) > 1:
        text = " ".join(message.text.split()[1:])
        client.send_message(message.chat.id, "Cevap Yükleniyor...")
        response = get_gpt_response(text)
        client.delete_messages(message.chat.id, message.message_id)
        client.send_message(message.chat.id, response)
    else:
        client.send_message(message.chat.id, "Üzgünüm, Sizi Anlayamadım. Lütfen Sorularınızı /gpt Komutu ile Girin! \n\nÖrnek: /gpt Merhaba! Nasılsın?")


def get_gpt_response(text):
    api_url = "https://dev-gpts.pantheonsite.io/wp-admin/js/apis/WormGPT.php?text="
    response = requests.get(api_url + text.replace(" ", "-"))
    return response.text

app.run()

