# -*- coding: utf-8 -*-
import os, random
from flask import Flask
from threading import Thread
import telebot
from telebot import types

app = Flask(__name__)
@app.route('/')
def home(): return "Bot OK"
@app.route('/health')
def health(): return "OK", 200

TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_ID = 7145036494
CHANNEL = "pkwbiwjwbekeekkw"
LINK = "https://t.me/pkwbiwjwbekeekkw"

bot = telebot.TeleBot(TOKEN, threaded=False)
os.makedirs("database", exist_ok=True)

def get_pts(uid):
    try:
        with open(f"database/{uid}.txt","r",encoding="utf-8") as f: return int(f.read() or 0)
    except: return 0
def add_pts(uid,n):
    open(f"database/{uid}.txt","w",encoding="utf-8").write(str(get_pts(uid)+n))
def is_sub(uid):
    try: return bot.get_chat_member(f"@{CHANNEL}", uid).status in ['member','administrator','creator']
    except: return True
def R(): return random.randint(1000,9999)

@bot.message_handler(commands=['start'])
def start(m):
    uid=m.from_user.id
    if not is_sub(uid):
        kb=types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton("\u0627\u0634\u062a\u0631\u0643", url=LINK))
        kb.add(types.InlineKeyboardButton("\u062a\u062d\u0642\u0642\u062a", callback_data="check"))
        bot.send_message(uid, "\u0627\u0634\u062a\u0631\u0643 \u0627\u0648\u0644\u0627\n"+LINK, reply_markup=kb)
        return
    pts=get_pts(uid)
    kb=types.InlineKeyboardMarkup(row_width=2)
    kb.add(types.InlineKeyboardButton("\u0627\u0644\u0642\u0646\u0627\u0629", url=LINK))
    kb.add(types.InlineKeyboardButton("\u0636\u0645\u0627\u0646 \u0645\u062a\u062c\u0631 5", callback_data="daman_s"), types.InlineKeyboardButton("\u0636\u0645\u0627\u0646 \u062d\u0633\u0627\u0628 5", callback_data="daman_a"))
    kb.add(types.InlineKeyboardButton("\u0636\u0645\u0627\u0646 \u0627\u0631\u0642\u0627\u0645 5", callback_data="daman_n"), types.InlineKeyboardButton("\u0636\u0645\u0627\u0646 \u0627\u064a\u0645\u064a\u0644 5", callback_data="daman_e"))
    kb.add(types.InlineKeyboardButton("\u0636\u0645\u0627\u0646 \u0634\u062d\u0646 5", callback_data="daman_sh"), types.InlineKeyboardButton("\u0636\u0645\u0627\u0646 \u0645\u062a\u0627\u0628\u0639\u064a\u0646 5", callback_data="daman_f"))
    kb.add(types.InlineKeyboardButton("\u0627\u064a\u0645\u064a\u0644 \u0648\u0647\u0645\u064a 5", callback_data="fake"), types.InlineKeyboardButton("\u062a\u0641\u0639\u064a\u0644 5", callback_data="active"))
    kb.add(types.InlineKeyboardButton("\u0643\u0648\u062f 5", callback_data="code"), types.InlineKeyboardButton("10 \u062f\u0642\u0627\u064a\u0642 5", callback_data="temp10"))
    kb.add(types.InlineKeyboardButton("\u062f\u0627\u0626\u0645 15", callback_data="perm"), types.InlineKeyboardButton("\u0645\u0634\u0641\u0631 10", callback_data="secure"))
    kb.add(types.InlineKeyboardButton("\u0634\u062d\u0646 5", callback_data="charge"), types.InlineKeyboardButton("\u062a\u062a\u0628\u0639 5", callback_data="track"))
    kb.add(types.InlineKeyboardButton("\u062e\u0635\u0645 5", callback_data="coupon"), types.InlineKeyboardButton("\u0641\u0627\u062a\u0648\u0631\u0629 5", callback_data="invoice"))
    kb.add(types.InlineKeyboardButton("\u0645\u062a\u0627\u0628\u0639\u064a\u0646 15", callback_data="follow"), types.InlineKeyboardButton("\u0644\u0627\u064a\u0643\u0627\u062a 15", callback_data="like"))
    kb.add(types.InlineKeyboardButton("\u0645\u0634\u0627\u0647\u062f\u0627\u062a 15", callback_data="view"), types.InlineKeyboardButton("\u0627\u0639\u0636\u0627\u0621 15", callback_data="member"))
    kb.add(types.InlineKeyboardButton("\u0641\u0643 \u062d\u0638\u0631 \u0634\u0627\u0645\u0644 15", callback_data="unban_all"), types.InlineKeyboardButton("\u0631\u0642\u0645 \u0648\u0647\u0645\u064a 15", callback_data="num"))
    kb.add(types.InlineKeyboardButton("\u0627\u0645\u0631\u064a\u0643\u064a 25", callback_data="usnum"), types.InlineKeyboardButton("\u0648\u0627\u062a\u0633 \u0634\u0627\u0645\u0644 15", callback_data="whats"))
    kb.add(types.InlineKeyboardButton("\u062a\u0635\u0645\u064a\u0645 5", callback_data="design"), types.InlineKeyboardButton("\u0641\u0644\u062a\u0631 5", callback_data="filter"))
    kb.add(types.InlineKeyboardButton("\u0643\u062a\u0627\u0628\u0629 5", callback_data="textpic"), types.InlineKeyboardButton("\u062c\u0648\u062f\u0629 5", callback_data="hd"))
    kb.add(types.InlineKeyboardButton("\u0644\u0648\u062c\u0648 10", callback_data="logo"), types.InlineKeyboardButton("\u0628\u0637\u0627\u0642\u0629 10", callback_data="card"))
    kb.add(types.InlineKeyboardButton("\u0628\u0627\u0646\u0631 10", callback_data="banner"), types.InlineKeyboardButton("\u0628\u0648\u0633\u062a\u0631 10", callback_data="poster"))
    kb.add(types.InlineKeyboardButton("\u0633\u064a\u0641\u064a 10", callback_data="cv"), types.InlineKeyboardButton("QR 5", callback_data="qr"))
    kb.add(types.InlineKeyboardButton("\u0646\u0634\u0631 20", callback_data="ad_post"), types.InlineKeyboardButton("\u062a\u062b\u0628\u064a\u062a 30", callback_data="ad_pin"))
    kb.add(types.InlineKeyboardButton("\u0645\u0645\u0648\u0644 50", callback_data="ad_spon"), types.InlineKeyboardButton("\u0628\u062b 100", callback_data="ad_all"))
    kb.add(types.InlineKeyboardButton(f"{pts} \u0631\u0635\u064a\u062f\u0643", callback_data="bal"))
    kb.add(types.InlineKeyboardButton("\u0634\u0631\u0627\u0621 \u0646\u0642\u0627\u0637", callback_data="buy"))
    bot.send_message(uid, f"\u0645\u062a\u062c\u0631 \u0632\u064a\u062f\u0647 - \u0643\u0644 \u0634\u064a \u064a\u0646\u0641\u0630 \u062a\u0644\u0642\u0627\u0626\u064a\n\u0631\u0635\u064a\u062f\u0643 {pts}\n{LINK}", reply_markup=kb)

@bot.callback_query_handler(func=lambda c: True)
def cb(c):
    bot.answer_callback_query(c.id)
    try:
        d=c.data; uid=c.from_user.id; chat=c.message.chat.id
        if d=="check":
            if is_sub(uid):
                try: bot.delete_message(chat,c.message.message_id)
                except: pass
                start(c.message)
            else: bot.send_message(chat, "\u0645\u0627 \u0627\u0634\u062a\u0631\u0643\u062a\n"+LINK)
            return
        if d=="bal":
            bot.send_message(chat, f"\u0631\u0635\u064a\u062f\u0643: {get_pts(uid)}")
            return
        if d=="buy":
            bot.send_message(chat, f"\u0634\u0631\u0627\u0621 \u0646\u0642\u0627\u0637:\n5=1000 \u064a\u0645\u0646\u064a\n15=2500\n30=5000\n100=15000\nID {uid}")
            return
        prices={"daman_s":5,"daman_a":5,"daman_n":5,"daman_e":5,"daman_sh":5,"daman_f":5,"fake":5,"active":5,"code":5,"temp10":5,"perm":15,"secure":10,"charge":5,"track":5,"coupon":5,"invoice":5,"follow":15,"like":15,"view":15,"member":15,"unban_all":15,"num":15,"usnum":25,"whats":15,"design":5,"filter":5,"textpic":5,"hd":5,"logo":10,"card":10,"banner":10,"poster":10,"cv":10,"qr":5,"ad_post":20,"ad_pin":30,"ad_spon":50,"ad_all":100}
        price=prices.get(d,5)
        if get_pts(uid)<price:
            bot.send_message(chat, f"\u062a\u062d\u062a\u0627\u062c {price} \u0631\u0635\u064a\u062f\u0643 {get_pts(uid)}")
            return
        if d in ["unban_all","whats"]:
            bot.send_message(chat, f"\u0627\u0631\u0633\u0644 \u0627\u0644\u0631\u0642\u0645 +967\n\u0627\u0644\u0633\u0639\u0631 {price}")
            bot.register_next_step_handler_by_chat_id(chat, lambda m, p=price: do_unban(m,p))
            return
        if d in ["design","logo","card","banner","poster","cv","filter","hd","textpic"]:
            bot.send_message(chat, f"\u0627\u0631\u0633\u0644 \u0627\u0644\u0635\u0648\u0631\u0629 {d}\n\u0627\u0644\u0633\u0639\u0631 {price}")
            bot.register_next_step_handler_by_chat_id(chat, lambda m, t=d, p=price: do_photo(m,t,p))
            return
        if d.startswith("daman_"):
            bot.send_message(chat, "\u0627\u0631\u0633\u0644 \u0627\u0633\u0645 \u0645\u062a\u062c\u0631\u0643")
            bot.register_next_step_handler_by_chat_id(chat, lambda m, t=d, p=price: do_daman(m,t,p))
            return
        add_pts(uid,-price)
        bot.send_message(chat, f"\u2705 \u062a\u0645 \u062a\u0646\u0641\u064a\u0630 {d} - \u062e\u0635\u0645 {price} \u0631\u0635\u064a\u062f\u0643 {get_pts(uid)}\n/start")
    except Exception as e:
        print(e)

def do_photo(m,typ,price):
    try:
        if m.content_type!='photo':
            bot.send_message(m.chat.id, "\u0627\u0631\u0633\u0644 \u0635\u0648\u0631\u0629 \u0641\u0642\u0637")
            return
        add_pts(m.from_user.id,-price)
        bot.send_photo(m.chat.id, m.photo[-1].file_id, caption=f"\u2705 \u0645\u0646\u0641\u0630 {typ} - \u062e\u0635\u0645 {price} \u0631\u0635\u064a\u062f\u0643 {get_pts(m.from_user.id)}\n{LINK}")
    except: pass

def do_daman(m,typ,price):
    try:
        add_pts(m.from_user.id,-price)
        bot.send_message(m.chat.id, f"\u2705 \u0636\u0645\u0627\u0646 {typ} \u0645\u0646\u0641\u0630:\n{m.text}\n\u0630\u0647\u0628\u064a 7 \u0627\u064a\u0627\u0645\n{R()}-WARRANTY\n{LINK}\n\u0631\u0635\u064a\u062f\u0643 {get_pts(m.from_user.id)}")
    except: pass

def do_unban(m,price):
    try:
        add_pts(m.from_user.id,-price)
        bot.send_message(m.chat.id, f"\U0001f513 \u0641\u0643 \u062d\u0638\u0631 \u0634\u0627\u0645\u0644 \u0645\u0646\u0641\u0630 \u0644\u0644\u0631\u0642\u0645 {m.text}\n\u2705 \u0648\u0627\u062a\u0633 + \u062a\u0644\u064a\u062c\u0631\u0627\u0645 + \u0627\u064a\u0645\u0648\n{LINK}\n\u0631\u0635\u064a\u062f\u0643 {get_pts(m.from_user.id)}")
    except: pass

@bot.message_handler(content_types=['photo'])
def photo_any(m):
    bot.send_message(m.chat.id, "\u0627\u0644\u0635\u0648\u0631\u0629 \u0648\u0635\u0644\u062a \u2705 /start")

@bot.message_handler(commands=['add'])
def add_cmd(m):
    if m.from_user.id!=ADMIN_ID: return
    try:
        _, uid, pts = m.text.split()
        add_pts(int(uid), int(pts))
        bot.send_message(int(uid), f"\u062a\u0645 \u0634\u062d\u0646 {pts} \u0631\u0635\u064a\u062f\u0643 {get_pts(int(uid))}")
    except: pass

def run_bot():
    while True:
        try: bot.infinity_polling(timeout=60, long_polling_timeout=60)
        except: continue

if __name__=="__main__":
    Thread(target=run_bot, daemon=True).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",10000)))