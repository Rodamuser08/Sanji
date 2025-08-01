import time
from telebot import TeleBot, types
from gatet import Tele
from hit_sender import send  


admin_name = "@strawhatchannel96"


with open('token.txt', 'r') as token_file:
    token = token_file.read().strip()

bot = TeleBot(token, parse_mode="HTML") 

@bot.message_handler(commands=['sj'])
def check_card(message):
   try:
        cc = message.text.split('/sj', 1)[1].strip()
        user_id = message.from_user.id
        username = message.from_user.username or "NoUsername"

        msg = bot.reply_to(message, "Checking your card...")
        msg_id = msg.message_id  
        start_time = time.time()

        
        if not cc:
            bot.edit_message_text(
                chat_id=message.chat.id, message_id=msg_id,
                text="Invalid card format. Please use the correct format: `cc|mm|yy|cvv`",
                parse_mode="Markdown"
            )
            return

        try:
            last = str(Tele(cc))
        except:
            last = 'Error while making payment'
        print(last)
        
        if "receipt" in last:
        	last = 'Payment successful 🔥'

        time_taken = round(time.time() - start_time, 2)

        send_response = send(cc, last, username, time_taken)

        print(send_response)

        
        try:
            bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=msg_id,
                text=send_response,
                parse_mode="HTML" 
            )
        except Exception as e:
            print(f"Error editing message: {e}")
            print(f"Problematic Response: {send_response}")
            bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=msg_id,
                text="An error occurred while processing your request. Please try again later."
            )

   except Exception as e:
        bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=msg_id,
            text="An error occurred while processing your request."
        )
        print(f"Error: {e}")

# Start the bot
bot.infinity_polling(timeout=25, long_polling_timeout=5)
