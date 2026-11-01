import os, smtplib, ssl, base64
u = os.environ["GMAIL_USER"].strip(); p = os.environ["GMAIL_APP_PASSWORD"].replace(" ", "").strip()
print("user domain:", u.split("@")[-1], "| user local part length:", len(u.split("@")[0]))
def b(x): return base64.b64encode(x.encode()).decode()
for port in (465, 587):
    for mech in ("PLAIN", "LOGIN"):
        try:
            if port == 465:
                s = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context(), timeout=60); s.ehlo()
            else:
                s = smtplib.SMTP("smtp.gmail.com", 587, timeout=60); s.ehlo(); s.starttls(context=ssl.create_default_context()); s.ehlo()
            print(port, "AUTH advertised:", s.esmtp_features.get("auth"))
            if mech == "PLAIN":
                r = s.docmd("AUTH", "PLAIN " + b("\0" + u + "\0" + p))
            else:
                r1 = s.docmd("AUTH", "LOGIN " + b(u)); print("  LOGIN step1:", r1[0])
                r = s.docmd(b(p))
            print(port, mech, "->", r[0], r[1].decode(errors="replace")[:300])
            s.close()
        except Exception as e:
            print(port, mech, "EXC", type(e).__name__, e)
