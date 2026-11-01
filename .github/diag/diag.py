import os, smtplib, ssl
u = os.environ.get("GMAIL_USER", ""); p = os.environ.get("GMAIL_APP_PASSWORD", ""); t = os.environ.get("MAIL_TO", "")
def info(name, v):
    print(f"{name}: len={len(v)} has_leading/trailing_space={v != v.strip()} has_newline={chr(10) in v or chr(13) in v} ascii={v.isascii()}")
info("GMAIL_USER", u); info("GMAIL_APP_PASSWORD", p); info("MAIL_TO", t)
print("user looks like gmail:", u.strip().lower().endswith("@gmail.com"), "| user==to:", u.strip().lower()==t.strip().lower())
pc = p.replace(" ", "").strip()
print("password without spaces: len", len(pc), "all lowercase letters:", pc.isalpha() and pc.islower())
try:
    s = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context(), timeout=60)
    print("connect ok:", s.ehlo()[0])
    try:
        print("login:", s.login(u.strip(), pc))
    except Exception as e:
        print("LOGIN FAILED:", type(e).__name__, e)
    s.quit()
except Exception as e:
    print("CONNECT FAILED:", type(e).__name__, e)
