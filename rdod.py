from utlis.rank import setrank,isrank,remrank,remsudos,setsudo, GPranks,IDrank
from utlis.send import send_msg, BYusers, GetLink,Name,Glang
from utlis.locks import st,getOR
from utlis.tg import Bot
from config import *

from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import threading, requests, time, random, re, json
import importlib

from pyrogram.types import (
     InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
)
from os import listdir
from os.path import isfile, join
def updateMsgs(client, message,redis):
  userID = message.from_user.id
  chatID = message.chat.id
  userFN = message.from_user.first_name
  title = message.chat.title
  rank = isrank(redis,userID,chatID)
  text = message.text
 
  if text and not redis.sismember("{}Nbot:ReplySend".format(BOT_ID),chatID):
   if text == "تف":
    Bot("sendMessage",{"chat_id":chatID,"text":"اتـفــل اقـوة😔😂.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "شلونكم" or text == "شلونك" or text == "شونك" or text == "شونكم":
    Bot("sendMessage",{"chat_id":chatID,"text":"تـمـام قـلـبي 💙+ انـت شـلـونـك شـخـبـارك؟","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "صاكه":
    Bot("sendMessage",{"chat_id":chatID,"text":"اوفف دز صـورتـهـا 🥲😂","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "وينك":
    Bot("sendMessage",{"chat_id":chatID,"text":"يـمـك حـبــيـي 💙.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "منورين":
    Bot("sendMessage",{"chat_id":chatID,"text":"نـورك حـبــيـي 💙.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "هاي":
    Bot("sendMessage",{"chat_id":chatID,"text":"هـايـات حـبـي 💕.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "🙊":
    Bot("sendMessage",{"chat_id":chatID,"text":"ابــوس الخـجـلان 🥲💙","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "😢":
    Bot("sendMessage",{"chat_id":chatID,"text":"لـتـبـجـي حـيـاتـي 💕.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "😭":
    Bot("sendMessage",{"chat_id":chatID,"text":"لـتـبـجـي حـيـاتـي 💕.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "منور":
    Bot("sendMessage",{"chat_id":chatID,"text":"نــورك ♥️.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "😒":
    Bot("sendMessage",{"chat_id":chatID,"text":"شـبـيـك حـبـي 🖤.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "مح":
    Bot("sendMessage",{"chat_id":chatID,"text":"اوفف عـسـل 🍯♥️.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "شكرا" or text == "ثكرا":
    Bot("sendMessage",{"chat_id":chatID,"text":"الــعـفـو عـمـري 💕.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "انته وين":
    Bot("sendMessage",{"chat_id":chatID,"text":"بالــبــ🏠ــيــت","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "اكرهك":
    Bot("sendMessage",{"chat_id":chatID,"text":" عـليـك الله حـبـنـي😔😂.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "اريد اكبل":
    Bot("sendMessage",{"chat_id":chatID,"text":"بـطـران 🥲😂.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "ضوجه":
    Bot("sendMessage",{"chat_id":chatID,"text":"وفف كـلـش 🙂🖤.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "اروح اصلي":
    Bot("sendMessage",{"chat_id":chatID,"text":"اجـي اصـلـي وراك 😔😂.️","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "صاك":
    Bot("sendMessage",{"chat_id":chatID,"text":"اخ دزي صـورتـته😔😂.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "اجيت" or text == "اني اجيت":
    Bot("sendMessage",{"chat_id":chatID,"text":"كل الـهـلا ♥️.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "حفلش":
    Bot("sendMessage",{"chat_id":chatID,"text":"اي خـوش زلـمه ومـن حـقك😔😂.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "نايمين":
    Bot("sendMessage",{"chat_id":chatID,"text":"لا بـعـدنه 🖤","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "اكو احد":
    Bot("sendMessage",{"chat_id":chatID,"text":"اي حـبـي تـفضـل 💙.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "شكو":
    Bot("sendMessage",{"chat_id":chatID,"text":"كـلـشي مـاكـو لا صـيـر حـشري😔😂.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "انت منو":
    Bot("sendMessage",{"chat_id":chatID,"text":"تـاج راسـك الـفـوك حـبي😔😂.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "كلخرا":
    Bot("sendMessage",{"chat_id":chatID,"text":"خرا بحـلكك حـيـوان 🙂😂","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "حبيبتي":
    Bot("sendMessage",{"chat_id":chatID,"text":"هـا قـلـبي ♥️.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "حروح اسبح":
    Bot("sendMessage",{"chat_id":chatID,"text":"اجـي اسـبحـكك😔😂.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "😔":
    Bot("sendMessage",{"chat_id":chatID,"text":"لــضـوج يـحـبي💙.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "☹️":
    Bot("sendMessage",{"chat_id":chatID,"text":"لــضـوج يـحـبي💙","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "جوعان":
    Bot("sendMessage",{"chat_id":chatID,"text":"نـاكل سـوه؟","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "لتحجي":
    Bot("sendMessage",{"chat_id":chatID,"text":"ونـت شـعلـيك حـاجـي بـحـلــكك 😉🤣","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "معليك" or text == "شعليك":
    Bot("sendMessage",{"chat_id":chatID,"text":"بـكـيفـي 🙂😂.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "شدسون" or text == "شداتسوون" or text == "شدتسون":
    Bot("sendMessage",{"chat_id":chatID,"text":"نـسـولـف 💙.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "يومه فدوه":
    Bot("sendMessage",{"chat_id":chatID,"text":"فدؤه الج حياتي 😍😙","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "افلش":
    Bot("sendMessage",{"chat_id":chatID,"text":"خـوش زلـمه 😔😂.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "احبج":
    Bot("sendMessage",{"chat_id":chatID,"text":"انـي هـم حـبـيــيي💕.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "شكو ماكو":
    Bot("sendMessage",{"chat_id":chatID,"text":"كـلـشي مـاكــو 🙃♥️️","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "اغير جو":
    Bot("sendMessage",{"chat_id":chatID,"text":"تـغـير جـو لـو تـزحـف ؏ بـنـات 😔😂","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "😋":
    Bot("sendMessage",{"chat_id":chatID,"text":"وفف لـسانـك 🥲♥️","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "😡":
    Bot("sendMessage",{"chat_id":chatID,"text":"اخ عـصـبـي😔😂.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "مرحبا":
    Bot("sendMessage",{"chat_id":chatID,"text":"مـراحــب ♥️.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "سلام" or text == "السلام عليكم" or text == "سلام عليكم" or text == "سلامن عليكم" or text == "السلامن عليك":
    Bot("sendMessage",{"chat_id":chatID,"text":"وعـلــيكم الـسـلام 💙.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "واكف":
    Bot("sendMessage",{"chat_id":chatID,"text":"لا بـعـدنـي شـغـال 🙃🖤.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "🚶🏻":
    Bot("sendMessage",{"chat_id":chatID,"text":"نـمـشي ســوة💕؟","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "البوت واكف":
    Bot("sendMessage",{"chat_id":chatID,"text":"لا بـعـدنـي شـغـال 🙃🖤.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "ضايج":
    Bot("sendMessage",{"chat_id":chatID,"text":"وفف ابـوس الـضايـج انــي🥲♥️.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "ضايجه":
    Bot("sendMessage",{"chat_id":chatID,"text":"وفف ابـوس الـضايـج انــي🥲♥️.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "😳" or text == "😳😳" or text == "😳😳😳":
    Bot("sendMessage",{"chat_id":chatID,"text":"شـبـيـك مـصـدوم 😔😂؟","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "صدك":
    Bot("sendMessage",{"chat_id":chatID,"text":"قـابـل اجـذب عـلـيـك ؟","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "شغال":
    Bot("sendMessage",{"chat_id":chatID,"text":"اي حـبــيبي شـغـال 🙃🖤.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "تخليني":
    Bot("sendMessage",{"chat_id":chatID,"text":"اي اخـليك بـنـص عـيني 🥲💕.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "فديتك" or text == "فديتنك":
    Bot("sendMessage",{"chat_id":chatID,"text":"مـح حـياتـي♥️.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "بوت":
    Bot("sendMessage",{"chat_id":chatID,"text":"نعم يا بعد قلبي 🥰.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "فير":
    Bot("sendMessage",{"chat_id":chatID,"text":"أقلكن من أولها الي بدا تزحف عليي مرتبط ترا 😌💔","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "زاحف":
    Bot("sendMessage",{"chat_id":chatID,"text":"لـيـش اكـو احـله من زحـف😔😂.🌝","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "حلو":
    Bot("sendMessage",{"chat_id":chatID,"text":"مـثـلـك 💕.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "عاش":
    Bot("sendMessage",{"chat_id":chatID,"text":"مـح 💙.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "مات":
    Bot("sendMessage",{"chat_id":chatID,"text":"طـبه مـرض 😔😂.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "ورده" or text == "وردة":
    Bot("sendMessage",{"chat_id":chatID,"text":"عـطـرها 💕.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "شسمك":
    Bot("sendMessage",{"chat_id":chatID,"text":"مـكـتـوب فـوك🙂😂.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "فديت" or text == "فطيت":
    Bot("sendMessage",{"chat_id":chatID,"text":"فـدوه لـوجـهك 💙.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "واو":
    Bot("sendMessage",{"chat_id":chatID,"text":"جـمـيــل 🖤.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "زاحفه" or text == "زاحفة":
    Bot("sendMessage",{"chat_id":chatID,"text":"لـيـش اكـو احـله من زحـف😔😂.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "حبيبي" or text == "حبي":
    Bot("sendMessage",{"chat_id":chatID,"text":"هـا حـيـاتـي🥲♥️.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "حبيبتي":
    Bot("sendMessage",{"chat_id":chatID,"text":"امـوت بـيك💕.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "حياتي":
    Bot("sendMessage",{"chat_id":chatID,"text":"هـا قـلـبي ♥️.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "عمري":
    Bot("sendMessage",{"chat_id":chatID,"text":"هـا قـلـبي ♥️. ","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "اسكت":
    Bot("sendMessage",{"chat_id":chatID,"text":"ما اسـكـت 😔😂.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "بتحبني":
    Bot("sendMessage",{"chat_id":chatID,"text":"بـمـوت فـيـك 💕.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "موجود":
    Bot("sendMessage",{"chat_id":chatID,"text":"اي حـب تــفـضل 💗.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "اكلك":
    Bot("sendMessage",{"chat_id":chatID,"text":"كـول قـلـبي ♥️.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "فدوه" or text == "فدوة" or text == "فطوه" or text == "فطوة":
    Bot("sendMessage",{"chat_id":chatID,"text":"لـوجـهـك ♥️.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "دي":
    Bot("sendMessage",{"chat_id":chatID,"text":"دعـبـل 🙂😂.","reply_to_message_id":message.message_id,"parse_mode":"html"})

   if text == "اشكرك":
    Bot("sendMessage",{"chat_id":chatID,"text":"تـدلـل يـحـبي 💕.","reply_to_message_id":message.message_id,"parse_mode":"html"})


