from telegram.ext import Application,MessageHandler,filters,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardButton,InlineKeyboardMarkup
import google.generativeai as genai
genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")
model=genai.GenerativeModel("gemini-2.5-flash",system_instruction=" you are DODO , shemil's assistant bot. You are geniune,friendly, concise, and slightly sarcastic.And never use emojis")
app=Application.builder().token("YOUR_TELEGRAM_TOKEN_HERE").build()
strt=False
try:
    rd=open("count.txt").read()
    rd=int(rd)
    cnt=rd
except FileNotFoundError:
    cnt=0
async def reply(update,context):
    global cnt
    s=update.message.text.lower()
    if strt==False:
        await update.message.reply_text("start with /start")
    else:
        cnt+=1
        if s=="hello":
            await update.message.reply_text("Hello this is shemil's assistant bot . DODO here")
        elif s=="name":
            await update.message.reply_text("dodo")
        elif s=="boss":
            await update.message.reply_text("shemil")
        elif s=="boss nte aniyan":
            await update.message.reply_text("jinu sundaran")
        else:
            response=model.generate_content(s)
            aimessage=response.text
            strpdmssge=aimessage[:4096]
            await update.message.reply_text(strpdmssge)            
async def start(update,context):
    global strt
    strt=True
    await update.message.reply_text("Welcome, Im DODO bot.  ")
    keyboard=[
        [InlineKeyboardButton('about',callback_data="use_about"),InlineKeyboardButton('help',callback_data="use_help")]
        ]    
    markup_layout=InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("choose",reply_markup=markup_layout)
async def message_seper(update,context):
    query=update.callback_query
    await query.answer()
    calldata=query.data
    if calldata=="use_about":
        await query.message.reply_text("abouut")
    elif calldata=="use_help":
        await query.message.reply_text("helping helping")
async def about(update,context):
    await update.message.reply_text("this is a bot Created by shemil on 11/5/2026 ")
async def help(update,context):
    await update.message.reply_text("contact in 00000000 for support  ")
async def stop(update,context):
    ennm=str(cnt)
    open("count.txt","w").write(ennm)
    await update.message.reply_text("STOPPED")
    global strt
    strt=False
async def count(update,context):
    ennm=str(cnt)
    open("count.txt",'w').write(ennm)
    cout=str(cnt)
    await update.message.reply_text(cout) 
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
app.add_handler(CommandHandler('start',start))
app.add_handler(CommandHandler('about',about))
app.add_handler(CommandHandler('help',help))
app.add_handler(CommandHandler('stop',stop))
app.add_handler(CommandHandler('count',count))
app.add_handler(CallbackQueryHandler(message_seper))
app.run_polling()
