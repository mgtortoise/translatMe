import telebot
import random
from googletrans import Translator
from telebot import types
translator = Translator()
api_key = '5049908225:AAGMRgnSPG06i2lvQcI3bSEEQiMZf1HyDb0'
bot = telebot.TeleBot(api_key)

@bot.message_handler(content_types=['text'])
def any_msg(message):
    user_exist = False
    with open('account.txt','r') as acfile:
        ac_id = acfile.readlines()
        for ac_id in ac_id:
            ac_id = ac_id.strip('\n')
            if ac_id == str(message.chat.id):
                user_exist = True
                break
                
        print('first for breaked')
        if user_exist:
            print('us exist')
            us_return = ''
            if message.text == '/game':
                print('game')
                with open('mydata.txt','r') as file:
                    alltext = file.readlines()
                    for k in range(0,5):
                        randText = random.choice(alltext)
                        randMy = randText.strip('\n')
                        translate_text = translator.translate(randText,dest='my')
                        result = '{0} = {1}\n'.format(randMy,translate_text.text)
                        us_return += result
                    bot.reply_to(message,us_return)
                    
            elif message.text == '/history':
                print('history view')
                search_hist =''
                with open('search_words.txt','r') as histFile:
                    resul = histFile.readlines()
                    for i in resul:
                        i = i.strip('\n')
                        i = '{}\n'.format(i)
                        search_hist += i
                print(search_hist)
                bot.reply_to(message,search_hist)
                        
                
                
            else:
                print('other')
                result = translator.translate(message.text,dest='my')
                print(result.text)
                with open('search_words.txt','a') as searchWords:
                    searchWords.write(message.text)
                    searchWords.write('\n')
                bot.reply_to(message,result.text)
            
            
                    
    print(message.chat.id)
    if message.text == 'IC4U':
        print('Ok')
        accid = str(message.chat.id)
        us_exist = False
        with open('account.txt','r') as rdFile:
            ac_id = rdFile.readlines()
            for acc in ac_id:
                acc = acc.strip('\n')
                if acc == accid:
                    print('user exist')
                    us_exist = True
                    break
            print("breaked for Loop")
            if us_exist:
                print('us exist')
                
            else:
                print('insert data')
                with open('account.txt','a+') as wFile:
                    wFile.write(accid)
                    wFile.write('\n')
                    
                    
                    
        
                
       
                        
            
            
                
                    
                    
                
        
    
            
if __name__ == '__main__':
    print('Main')
    bot.polling()