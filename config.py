import os
from dotenv import load_dotenv

load_dotenv()

# توکن ربات - از @BotFather بگیرید
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# آیدی عددی ادمین‌ها (با کاما جدا کنید اگر چند نفر هستند) مثال: 123456789,987654321
ADMIN_IDS = [int(x.strip()) for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip()]

# اطلاعات کارت برای پرداخت
CARD_NUMBER = os.getenv("CARD_NUMBER", "0000-0000-0000-0000")
CARD_HOLDER = os.getenv("CARD_HOLDER", "نام صاحب حساب")

# مسیر دیتابیس - روی Railway پیشنهاد میشه از Volume استفاده کنید تا دیتا پاک نشه
DB_PATH = os.getenv("DB_PATH", "bot.db")

# نام برند/ربات که در پیام خوش‌آمدگویی نمایش داده میشه
BRAND_NAME = os.getenv("BRAND_NAME", "X4G")

# بنر قبل از خوش‌آمدگویی (/start)
# اگر START_BANNER_ENABLED=0 باشد بنر نشان داده نمی‌شود
START_BANNER_ENABLED = os.getenv("START_BANNER_ENABLED", "1").strip() not in ("0", "false", "False", "no")
START_BANNER_TEXT = os.getenv(
    "START_BANNER_TEXT",
    (
        "🎯 <b>پیشنهاد ویژه</b>\n\n"
        "سرویس پایدار · تحویل سریع · پشتیبانی پاسخ‌گو\n"
        "از منوی پایین «🛍 خرید سرویس» یا «🎁 تست رایگان» را امتحان کن."
    ),
).replace("\\n", "\n")
# عکس بنر: یا لینک مستقیم https یا file_id تلگرام (یکی کافی است)
START_BANNER_PHOTO_URL = os.getenv("START_BANNER_PHOTO_URL", "").strip()
START_BANNER_PHOTO_FILE_ID = os.getenv("START_BANNER_PHOTO_FILE_ID", "").strip()

# آیدی پشتیبانی (بدون @) - در دکمه «ارتباط با پشتیبانی» استفاده میشه
SUPPORT_USERNAME = os.getenv("SUPPORT_USERNAME", "SuppX4G")

# کانال‌/گروه‌های عضویت اجباری — با کاما جدا کنید
# می‌تونه آیدی عددی (مثل -1001234567890) یا یوزرنیم با/بدون @ باشه (مثل @mychannel یا mychannel)
# مثال Railway: REQUIRED_CHANNELS=-1001234567890,@X4GChannel
# اگه خالی باشه، عضویت اجباری غیرفعاله
REQUIRED_CHANNELS = [x.strip() for x in os.getenv("REQUIRED_CHANNELS", "").split(",") if x.strip()]

# تنظیمات سیستم رفرال (دعوت دوستان)
REFERRAL_REQUIRED_COUNT = int(os.getenv("REFERRAL_REQUIRED_COUNT", "3"))   # تعداد خرید موفق لازم
REFERRAL_REWARD_VOLUME = int(os.getenv("REFERRAL_REWARD_VOLUME", "50"))   # حجم هدیه گیمینگ (گیگ)
# پاداش ورود با لینک دعوت — به هر دو طرف (دعوت‌کننده + دعوت‌شونده)
REFERRAL_JOIN_BONUS = int(os.getenv("REFERRAL_JOIN_BONUS", "30000"))

# تعرفه‌های پیش‌فرض سرویس گیمینگ - فقط در اولین اجرا (وقتی دیتابیس خالیه) استفاده میشه
# بعد از اون، قیمت‌ها از دیتابیس خونده میشن و از طریق دستور ادمین توی خود ربات قابل تغییرن
DEFAULT_GAMING_PLANS = [
    (10, 70000),
    (20, 140000),
    (30, 210000),
    (40, 280000),
    (50, 350000),
]

# تعرفه‌های پیش‌فرض سرویس مولتی لوکیشن (وبگردی) - فقط در اولین اجرا استفاده میشه
DEFAULT_MULTI_PLANS = [
    ("تک کاربره نامحدود یک‌ماهه", 150000),
    ("دو کاربره نامحدود یک‌ماهه", 250000),
    ("تک کاربره نامحدود دو‌ماهه", 250000),
    ("دو کاربره نامحدود دو‌ماهه", 450000),
]


# ---------- پنل VPN (Variables) ----------
# نوع: pasarguard | marzban | marzneshin | sanaei
PANEL_TYPE = (os.getenv("PANEL_TYPE") or os.getenv("PASARGUARD_PANEL_TYPE") or "pasarguard").strip().lower()
if PANEL_TYPE in ("3x-ui", "3xui", "x-ui", "xui", "sanaei"):
    PANEL_TYPE = "sanaei"
if PANEL_TYPE in ("marzneshin", "marznesh"):
    PANEL_TYPE = "marzneshin"

PANEL_BASE_URL = (os.getenv("PANEL_BASE_URL") or os.getenv("PASARGUARD_BASE_URL") or "").rstrip("/")
PANEL_USERNAME = os.getenv("PANEL_USERNAME") or os.getenv("PASARGUARD_USERNAME") or ""
PANEL_PASSWORD = os.getenv("PANEL_PASSWORD") or os.getenv("PASARGUARD_PASSWORD") or ""
PANEL_API_KEY = os.getenv("PANEL_API_KEY") or os.getenv("PASARGUARD_API_KEY") or ""

# سازگاری با کد قدیمی
PASARGUARD_BASE_URL = PANEL_BASE_URL
PASARGUARD_USERNAME = PANEL_USERNAME
PASARGUARD_PASSWORD = PANEL_PASSWORD
PASARGUARD_API_KEY = PANEL_API_KEY

# فقط سنایی: Inbound ID
PANEL_INBOUND_ID = (os.getenv("PANEL_INBOUND_ID") or os.getenv("SANAEI_INBOUND_ID") or "").strip()

PASARGUARD_TEST_TEMPLATE_ID = os.getenv("PASARGUARD_TEST_TEMPLATE_ID", "").strip() or None
if PASARGUARD_TEST_TEMPLATE_ID is not None:
    try:
        PASARGUARD_TEST_TEMPLATE_ID = int(PASARGUARD_TEST_TEMPLATE_ID)
    except ValueError:
        PASARGUARD_TEST_TEMPLATE_ID = None

PASARGUARD_TEST_DATA_LIMIT_GB = float(
    os.getenv("PANEL_TEST_DATA_LIMIT_GB") or os.getenv("PASARGUARD_TEST_DATA_LIMIT_GB") or "0.3"
)
PASARGUARD_TEST_EXPIRE_HOURS = int(
    os.getenv("PANEL_TEST_EXPIRE_HOURS") or os.getenv("PASARGUARD_TEST_EXPIRE_HOURS") or "48"
)

_raw_groups = os.getenv("PASARGUARD_TEST_GROUPS") or os.getenv("PASARGUARD_TEST_GROUP_IDS") or ""
PASARGUARD_TEST_GROUPS = [x.strip() for x in _raw_groups.split(",") if x.strip()]
_raw_tg = os.getenv("PASARGUARD_TEST_GROUPS_GAMING", "").strip()
PASARGUARD_TEST_GROUPS_GAMING = [x.strip() for x in _raw_tg.split(",") if x.strip()] or list(PASARGUARD_TEST_GROUPS)
_raw_tm = os.getenv("PASARGUARD_TEST_GROUPS_MULTI", "").strip()
PASARGUARD_TEST_GROUPS_MULTI = [x.strip() for x in _raw_tm.split(",") if x.strip()] or list(PASARGUARD_TEST_GROUPS)
FREE_TEST_CLEANUP_INTERVAL_SEC = int(os.getenv("FREE_TEST_CLEANUP_INTERVAL_SEC", "300"))

PASARGUARD_TEST_LOCATION_GAMING = os.getenv("PASARGUARD_TEST_LOCATION_GAMING", "گیمینگ")
PASARGUARD_TEST_LOCATION_MULTI = os.getenv(
    "PASARGUARD_TEST_LOCATION_MULTI",
    os.getenv("PASARGUARD_TEST_LOCATION_NAME", "مولتی لوکیشن"),
)
PASARGUARD_TEST_USERNAME_PREFIX = os.getenv("PASARGUARD_TEST_USERNAME_PREFIX", "test_")
PASARGUARD_TEST_LOCATION_NAME = os.getenv("PASARGUARD_TEST_LOCATION_NAME", "مولتی لوکیشن")
PASARGUARD_TEST_SERVICE_NAME = os.getenv("PASARGUARD_TEST_SERVICE_NAME", "تست")

_default_test_msg = (
    "✅ تست با موفقیت آماده شد\n\n"
    "👤 نام کاربری تست : {username}\n"
    "🌐 لوکیشن : {location}\n"
    "⌛ مدت زمان : {duration}\n"
    "📊 حجم تست : {volume}\n\n"
    "لینک اتصال 📎 :\n"
    "{subscription_url}\n\n"
    "🧑‍🦯 شما میتوانید شیوه اتصال را با فشردن دکمه زیر و انتخاب سیستم عامل خود را دریافت کنید"
)
PASARGUARD_TEST_MESSAGE = os.getenv("PANEL_TEST_MESSAGE") or os.getenv("PASARGUARD_TEST_MESSAGE") or _default_test_msg


def is_panel_auto_enabled() -> bool:
    """آیا ساخت خودکار روی پنل فعال است؟"""
    if not PANEL_BASE_URL:
        return False
    if PANEL_TYPE == "sanaei":
        return bool(PANEL_USERNAME and PANEL_PASSWORD and PANEL_INBOUND_ID)
    if PANEL_API_KEY:
        return True
    return bool(PANEL_USERNAME and PANEL_PASSWORD)

# ---------- سرویس خریداری‌شده (بعد از تأیید رسید) ----------
# گروه‌های سرویس پولی — اگر خالی باشد از PASARGUARD_TEST_GROUPS استفاده می‌شود
_raw_svc_groups = os.getenv("PASARGUARD_SERVICE_GROUPS", "").strip()
PASARGUARD_SERVICE_GROUPS = (
    [x.strip() for x in _raw_svc_groups.split(",") if x.strip()]
    if _raw_svc_groups
    else list(PASARGUARD_TEST_GROUPS)
)

PASARGUARD_SERVICE_USERNAME_PREFIX = os.getenv("PASARGUARD_SERVICE_USERNAME_PREFIX", "svc_")
PASARGUARD_SERVICE_LOCATION_NAME = os.getenv(
    "PASARGUARD_SERVICE_LOCATION_NAME",
    os.getenv("PASARGUARD_TEST_LOCATION_NAME", "مولتی لوکیشن نیم بها"),
)

# مدت پیش‌فرض گیمینگ (روز) — پلن گیمینگ فقط حجم دارد
PASARGUARD_GAMING_EXPIRE_DAYS = int(os.getenv("PASARGUARD_GAMING_EXPIRE_DAYS", "30"))
# اگر از لیبل مولتی مدت استخراج نشد
PASARGUARD_MULTI_EXPIRE_DAYS = int(os.getenv("PASARGUARD_MULTI_EXPIRE_DAYS", "30"))

# قالب پیام تحویل سرویس خریداری‌شده
# {username} {service_name} {location} {duration} {volume} {subscription_url}
PASARGUARD_SERVICE_MESSAGE = os.getenv(
    "PASARGUARD_SERVICE_MESSAGE",
    (
        "✅ سرویس با موفقیت ایجاد شد\n\n"
        "👤 نام کاربری سرویس : {username}\n"
        "🚀 نام سرویس: {service_name}\n"
        "🌐 لوکیشن: {location}\n"
        "⏳ مدت زمان: {duration}\n"
        "📊 حجم سرویس: {volume}\n\n"
        "لینک اتصال:\n"
        "{subscription_url}\n\n"
        "🧑‍🦯 شما میتوانید شیوه اتصال را با فشردن دکمه زیر و انتخاب سیستم عامل خود را دریافت کنید"
    ),
)

# ---------- آموزش استفاده (ویدیو تلگرام) ----------
# فرمت: نام|لینک,نام|لینک
# مثال: TUTORIAL_LINKS=v2rayNG|https://t.me/xxx/10,Streisand|https://t.me/xxx/11
_raw_tutorials = os.getenv("TUTORIAL_LINKS", "").strip()
TUTORIAL_LINKS = []
for _part in _raw_tutorials.split(","):
    _part = _part.strip()
    if not _part or "|" not in _part:
        continue
    _name, _url = _part.split("|", 1)
    _name, _url = _name.strip(), _url.strip()
    if _name and _url.startswith("http"):
        TUTORIAL_LINKS.append((_name, _url))

TUTORIAL_PROMPT = os.getenv(
    "TUTORIAL_PROMPT",
    (
        "📚 <b>آموزش استفاده</b>\n\n"
        "برای کدام برنامه می‌خواهید آموزش ببینید؟\n"
        "روی دکمه بزنید تا ویدیو باز شود."
    ),
)

# هشدار سرویس وقتی حجم باقی‌مانده از این مقدار کمتر شد (گیگ)
SERVICE_WARN_REMAINING_GB = float(os.getenv("SERVICE_WARN_REMAINING_GB", "1"))
SERVICE_WATCH_INTERVAL_SEC = int(os.getenv("SERVICE_WATCH_INTERVAL_SEC", "600"))
