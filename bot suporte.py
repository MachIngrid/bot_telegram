#Author: Ingrid Machado e Gabrielly Bassetto
#08/11/2023

import telebot

token = "6407693635:AAESbXsdK0eZZDXwAV3JAl3VGmmnDVy93fY"
suporte_ids = []# nao esta reconhecendo
bot = telebot.TeleBot(token)



@bot.message_handler(commands=['adicionar_id'])
def add_id(message):
    print(message.chat.id)
    id_novo = message.chat.id

    if id_novo >0:
       if id_novo not in suporte_ids:
          suporte_ids = suporte_ids.append(id_novo)#nor appendisg
          bot.reply_to(message , 'Cadastro realizado com sucesso, você agora faz parte do grupo suporte') 
       else:
           bot.reply_to(message , 'Seu id já está cadastrado no grupo suporte') 
    else:
         bot.reply_to(message , 'Não é possivel se cadastrar através de um grupo, entre no chat privado com o bot e tente novamente ') 

             

def verifica(message):
    return True

@bot.message_handler(func=verifica)
def suport(message):
    palavras = ('suporte','dispon','cadastro','cfg')
    texto = str(message.text).upper()
    
    for palavra in palavras:
      if palavra.upper() in texto:
           bot.reply_to(message,"Aguarde, a equipe de suporte está sendo acionada")

           for id in suporte_ids:
              bot.send_message(id , f'Atencão, {message.from_user.first_name} está solicitando suporte no Grupo: {message.chat.title}') 


      break          

               
print(suporte_ids)

bot.polling(non_stop=True)    