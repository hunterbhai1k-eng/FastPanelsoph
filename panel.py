import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram Bot Token
BOT_TOKEN = "8612461575:AAF3_iuT1zUorjV5_jptr1AmCga-7D30MMg"

# QR Code Image URL
QR_CODE_URL = "https://i.postimg.cc/k5QZ4WWC/IMG-20260823-WA0003.jpg"

# Products & Prices Data
PRODUCTS = {
    "BRMOD_ANDROID_ROOT": {"name": "BRMOD ANDROID ROOT", "plans": {"1 Day": "80", "7 Days": "250", "15 Days": "600", "1 Month": "900"}},
    "BRMOD_SILENTAIM_PC": {"name": "BRMOD SILENTAIM PC", "plans": {"1 Day": "80", "7 Days": "250", "15 Days": "600", "1 Month": "900"}},
    "SNAKE_CARROM_POOL": {"name": "SNAKE CARROM POOL", "plans": {"1 Day": "80", "7 Days": "250", "15 Days": "600", "1 Month": "900"}},
    "FLUORITE_8BALL_IOS": {"name": "Fluorite 8 BallPool iOS", "plans": {"1 Day": "80", "7 Days": "250", "15 Days": "600", "1 Month": "900"}},
    "DRIP_PROXY_ANDROID": {"name": "DRIP PROXY ANDROID", "plans": {"1 Day": "80", "7 Days": "250", "15 Days": "600", "1 Month": "900"}},
    "DRIP_CLIENT_APKMOD": {"name": "DRIP CLIENT APKMOD", "plans": {"1 Day": "80", "7 Days": "250", "15 Days": "600", "1 Month": "900"}},
    "HG_CHEAT_APKMOD": {"name": "HG CHEAT APKMOD", "plans": {"1 Day": "80", "7 Days": "250", "15 Days": "600", "1 Month": "900"}},
    "LKTEAM_ROOT_PC": {"name": "LKTEAM ROOT + PC", "plans": {"1 Day": "80", "7 Days": "250", "15 Days": "600", "1 Month": "900"}},
    "DRIP_CLIENT_ROOT": {"name": "DRIP CLIENT ROOT", "plans": {"1 Day": "80", "7 Days": "250", "15 Days": "600", "1 Month": "900"}},
    "8BP_EZTEAM_ANDROID": {"name": "8BP EZTEAM ANDROID", "plans": {"1 Day": "80", "7 Days": "250", "15 Days": "600", "1 Month": "900"}},
    "PSH4X_8BALL_POOL": {"name": "PSH4X 8BALL POOL", "plans": {"1 Day": "80", "7 Days": "250", "15 Days": "600", "1 Month": "900"}},
    "PATOTEAM_APKMOD": {"name": "PATOTEAM APKMOD", "plans": {"1 Day": "80", "7 Days": "250", "15 Days": "600", "1 Month": "900"}},
    "FLUORITE_IOS_FF": {"name": "FLUORITE IOS FF", "plans": {"1 Day": "80", "7 Days": "250", "15 Days": "600", "1 Month": "900"}},
    "ESIGN_CERTIFICATE": {"name": "ESIGN CERTIFICATE", "plans": {"1 Day": "80", "7 Days": "250", "15 Days": "600", "1 Month": "900"}},
    "AKLOADER_ANDROID": {"name": "AKLOADER ANDROID", "plans": {"1 Day": "80", "7 Days": "250", "15 Days": "600", "1 Month": "900"}},
    "PRIME_APKMOD": {"name": "PRIME APKMOD", "plans": {"1 Day": "80", "7 Days": "250", "15 Days": "600", "1 Month": "900"}},
    "GBOX_OFFICIAL": {"name": "GBOX OFFICIAL", "plans": {"1 Day": "80", "7 Days": "250", "15 Days": "600", "1 Month": "900"}},
    "HAXXCKER_ROOT": {"name": "HAXXCKER ROOT", "plans": {"1 Day": "80", "7 Days": "250", "15 Days": "600", "1 Month": "900"}},
    "DRIP_CLIENT_PC_EXE": {"name": "DRIP CLIENT PC EXE", "plans": {"1 Day": "80", "7 Days": "250", "15 Days": "600", "1 Month": "900"}},
    "BALA_MODE": {"name": "BALA MODE", "plans": {"1 Hour": "30", "3 Hours": "70", "6 Hours": "100", "15 Days": "500"}}
}

# Main Menu Generator
def get_main_menu():
    keyboard = [
        [InlineKeyboardButton("🛒 Shop Now", callback_data='shop_now')],
        [InlineKeyboardButton("📦 My Orders", callback_data='my_orders'), InlineKeyboardButton("👤 Profile", callback_data='profile')],
        [InlineKeyboardButton("💳 Add Balance", callback_data='add_balance'), InlineKeyboardButton("👥 Referral", callback_data='referral')],
        [InlineKeyboardButton("🎰 Lucky Spin", callback_data='lucky_spin')],
        [InlineKeyboardButton("📚 Tutorials", callback_data='tutorials'), InlineKeyboardButton("💬 Support", callback_data='support')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Start Command Handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = (
        f"🤖 **JIBON MODS SHOP** 🛍️\n\n"
        f"Welcome, **{user.first_name}**!\n\n"
        f"⭐ **SHOP FEATURES** ⭐\n"
        f"🔑 Premium Game Keys\n"
        f"⚡ Instant Delivery 24/7\n"
        f"🔒 100% Secure Payment\n"
        f"🏷️ Best Prices Guaranteed\n"
        f"🎁 Referral Rewards\n"
        f"🤝 Professional Support"
    )
    await update.message.reply_text(text, reply_markup=get_main_menu(), parse_mode='Markdown')

# Button Callback Handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    user = query.from_user

    if data == 'back_to_menu':
        await query.message.edit_text(
            f"🤖 **JIBON MODS SHOP** 🛍️\n\nWelcome back, **{user.first_name}**!",
            reply_markup=get_main_menu(),
            parse_mode='Markdown'
        )

    elif data == 'shop_now':
        keyboard = []
        for key, p in PRODUCTS.items():
            keyboard.append([InlineKeyboardButton(f"🛒 {p['name']}", callback_data=f"prod_{key}")])
        keyboard.append([InlineKeyboardButton("⬅️ Back to Menu", callback_data='back_to_menu')])
        
        await query.message.edit_text(
            "🎮 **CHOOSE YOUR PRODUCT** 🎮\n\nSelect a product below:",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='Markdown'
        )

    elif data.startswith('prod_'):
        prod_key = data.replace('prod_', '')
        product = PRODUCTS[prod_key]
        
        keyboard = []
        for plan_name, price in product['plans'].items():
            keyboard.append([InlineKeyboardButton(f"Buy {plan_name} - ₹{price}", callback_data=f"pay_{price}")])
        keyboard.append([InlineKeyboardButton("⬅️ Back to Shop", callback_data='shop_now')])

        text = f"📊 **{product['name']}**\n\n🏷️ **STOCK & PRICING:**\n"
        for plan_name, price in product['plans'].items():
            text += f"✅ **{plan_name}**: ₹{price}\n"

        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    elif data == 'profile':
        text = (
            f"👤 **YOUR PROFILE** 👤\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"🆔 **Account Information**\n"
            f"🪪 **User ID**: `{user.id}`\n"
            f"👤 **Name**: {user.first_name}\n\n"
            f"💰 **Balance Details**\n"
            f"💵 **Current**: ₹0.00\n\n"
            f"📊 **Statistics**\n"
            f"📦 **Total Orders**: 0\n"
            f"💸 **Total Spent**: ₹0.00\n"
            f"💳 **Total Deposited**: ₹0.00\n"
            f"🎁 **Referral Earned**: ₹0.00\n"
            f"👥 **Total Referrals**: 0\n\n"
            f"🔗 **Your Referral Link**\n"
            f"https://t.me/{context.bot.username}?start=ref_{user.id}\n\n"
            f"📢 Share and earn 20% commission on purchases!"
        )
        keyboard = [
            [InlineKeyboardButton("💳 Add Balance", callback_data='add_balance')],
            [InlineKeyboardButton("⬅️ Back to Shop", callback_data='back_to_menu')]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

    elif data == 'add_balance' or data.startswith('pay_'):
        amount = data.replace('pay_', '') if data.startswith('pay_') else "your desired amount"
        caption_text = f"📲 **UPI PAYMENT SCANNER**\n\nPay ₹{amount} by scanning the QR code below.\n\nAfter payment, send the screenshot to support for balance update."
        
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back to Menu", callback_data='back_to_menu')]])
        
        await query.message.delete()
        await context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=QR_CODE_URL,
            caption=caption_text,
            reply_markup=keyboard,
            parse_mode='Markdown'
        )

    elif data in ['my_orders', 'referral', 'lucky_spin', 'tutorials', 'support']:
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back to Menu", callback_data='back_to_menu')]])
        await query.message.edit_text(f"🛠️ **{data.replace('_', ' ').title()}** feature will be available soon!", reply_markup=keyboard)

# Main Execution
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
