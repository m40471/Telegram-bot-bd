from flask import Flask, request, render_template
import telegram

app = Flask(__name__)
bot = telegram.Bot(token='YOUR_BOT_TOKEN')  # এখানে তোমার টেলিগ্রাম বট টোকেন বসাও

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    chat_id = request.form['chat_id']
    message = request.form['message']
    bot.send_message(chat_id=chat_id, text=message)
    return render_template('success.html')

if __name__ == '__main__':
    app.run()
  
