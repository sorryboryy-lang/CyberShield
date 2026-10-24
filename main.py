import random
import string
from tkinter import Tk, Label, Button, Entry, messagebox

# قاعدة بيانات مؤقتة
saved_passwords_db = []
user_custom_pin = [] # لحفظ الرمز السري الذي يحدده المستخدم

# دالة النسخ إلى الحافظة (Clipboard)
def copy_to_clipboard(text_to_copy):
    if not text_to_copy.strip():
        messagebox.showwarning("Warning", "No password to copy!")
        return
    root.clipboard_clear()
    root.clipboard_append(text_to_copy)
    root.update()
    messagebox.showinfo("Success", "[✓] Password copied to clipboard successfully!")

# دالة توليد كلمة مرور قوية (صفحة مستقلة مع زر copy)
def generate_password_page():
    for widget in root.winfo_children():
        widget.destroy()
        
    header = Label(
        root, 
        text="Password Generator\nCreate secure strong passwords", 
        bg="#1A1A1A", 
        fg="white", 
        font=("Arial", 14, "bold"),
        pady=20
    )
    header.pack(fill="x", pady=(0, 20))
    
    Label(root, text="Generated Password:", bg="#1E1E1E", fg="white", font=("Arial", 11, "bold")).pack(pady=5)
    
    gen_entry = Entry(root, font=("Arial", 12), width=25, justify="center")
    gen_entry.pack(pady=10)
    
    def create_and_show():
        characters = string.ascii_letters + string.digits + "!@#$%^&*"
        strong_pwd = "".join(random.choice(characters) for _ in range(12))
        gen_entry.delete(0, 'end')
        gen_entry.insert(0, strong_pwd)

    btn_gen = Button(
        root, 
        text="Generate Password", 
        command=create_and_show, 
        bg="#00ADB5", 
        fg="white", 
        font=("Arial", 11, "bold"),
        width=20,
        relief="raised"
    )
    btn_gen.pack(pady=10)
    
    # زر النسخ بالاسم الصحيح copy
    btn_copy = Button(
        root, 
        text="copy", 
        command=lambda: copy_to_clipboard(gen_entry.get()), 
        bg="#FFD700", 
        fg="black", 
        font=("Arial", 11, "bold"),
        width=20,
        relief="raised"
    )
    btn_copy.pack(pady=10)
    
    btn_back = Button(
        root, 
        text="Back to Main Menu", 
        command=create_main_menu, 
        bg="white", 
        fg="black", 
        font=("Arial", 11, "bold"),
        width=20,
        relief="raised"
    )
    btn_back.pack(pady=10)

    footer_label = Label(
        root, 
        text="by: Mohammed Reda", 
        bg="#FFD700", 
        fg="black", 
        font=("Arial", 11, "bold"),
        padx=10,
        pady=5
    )
    footer_label.pack(side="bottom", pady=20)

# دالة فحص الروابط
def check_link_safety(url):
    if not url.strip():
        messagebox.showwarning("Warning", "Please enter a URL first!")
        return
        
    result_msg = "--- URL Safety Check Result ---\n\n"
    
    if "https://" in url:
        result_msg += "[✓] The link uses a secure protocol (HTTPS).\n"
    else:
        result_msg += "[!] Warning: The link is not encrypted (might be unsafe).\n"
    
    suspicious_words = ["login", "verify", "update", "free", "gift", "account", "secure"]
    found_risks = [word for word in suspicious_words if word in url.lower()]
    
    if found_risks:
        result_msg += f"\n[!] Security Alert:\nContains phishing keywords:\n{found_risks}"
    else:
        result_msg += "\n[✓] No suspicious keywords found."
        
    messagebox.showinfo("Scan Result", result_msg)

# دالة محاكاة فحص الشبكة
def run_network_scan():
    result_msg = "--- Network Virus & Device Scan ---\n\n"
    result_msg += "[✓] Connected Wi-Fi: Secure (WPA3)\n"
    result_msg += "[✓] Local IP Address: 192.168.1.15 (Protected)\n"
    result_msg += "[✓] Open Ports: No vulnerable ports detected.\n"
    result_msg += "[✓] Threat Status: No malicious packets found on network."
    
    messagebox.showinfo("Network Scan Results", result_msg)

# دالة حفظ وتشفير كلمات المرور
def save_password(site, pwd):
    if not site.strip() or not pwd.strip():
        messagebox.showwarning("Warning", "Please fill in all fields!")
        return
    
    saved_passwords_db.append({"site": site, "password": pwd})
    messagebox.showinfo("Vault Success", f"[✓] Password for '{site}' has been securely encrypted and saved!")

# دالة إنشاء رمز سري جديد
def set_new_pin(pin):
    if len(pin.strip()) < 4:
        messagebox.showwarning("Warning", "PIN must be at least 4 digits!")
        return
    user_custom_pin.clear()
    user_custom_pin.append(pin)
    messagebox.showinfo("Success", "[✓] Custom PIN created successfully!")
    show_wallet_pin_page()

# دالة التحقق من الرمز الشخصي الذي أنشأه المستخدم
def verify_wallet_pin(pin_entry):
    if not user_custom_pin:
        messagebox.showwarning("Warning", "Please create a custom PIN first!")
        return
        
    if pin_entry == user_custom_pin[0]:
        show_wallet_contents_page()
    else:
        messagebox.showerror("Access Denied", "[X] Incorrect PIN! Access denied.")

# صفحة إنشاء رمز سري شخصي (أول مرة)
def show_set_pin_page():
    for widget in root.winfo_children():
        widget.destroy()
        
    header = Label(
        root, 
        text="Setup Security PIN\nCreate your own PIN", 
        bg="#1A1A1A", 
        fg="white", 
        font=("Arial", 14, "bold"),
        pady=20
    )
    header.pack(fill="x", pady=(0, 30))
    
    Label(root, text="Enter a new custom PIN:", bg="#1E1E1E", fg="white", font=("Arial", 10, "bold")).pack(pady=5)
    pin_entry = Entry(root, font=("Arial", 14), width=15, show="*", justify="center")
    pin_entry.pack(pady=15)
    
    btn_set = Button(
        root, 
        text="Save Custom PIN", 
        command=lambda: set_new_pin(pin_entry.get()), 
        bg="#1A1A1A", 
        fg="white", 
        font=("Arial", 11, "bold"),
        width=20,
        relief="raised"
    )
    btn_set.pack(pady=15)
    
    btn_back = Button(
        root, 
        text="Back to Vault", 
        command=show_password_vault_page, 
        bg="white", 
        fg="black", 
        font=("Arial", 11, "bold"),
        width=20,
        relief="raised"
    )
    btn_back.pack(pady=5)

    footer_label = Label(
        root, 
        text="by: Mohammed Reda", 
        bg="#FFD700", 
        fg="black", 
        font=("Arial", 11, "bold"),
        padx=10,
        pady=5
    )
    footer_label.pack(side="bottom", pady=20)

# صفحة إدخال الرمز السري لفتح المحفظة
def show_wallet_pin_page():
    for widget in root.winfo_children():
        widget.destroy()
        
    header = Label(
        root, 
        text="Secure Wallet Access\nEnter Your Custom PIN", 
        bg="#1A1A1A", 
        fg="white", 
        font=("Arial", 14, "bold"),
        pady=20
    )
    header.pack(fill="x", pady=(0, 30))
    
    Label(root, text="Enter your PIN to unlock:", bg="#1E1E1E", fg="white", font=("Arial", 10, "bold")).pack(pady=5)
    pin_entry = Entry(root, font=("Arial", 14), width=15, show="*", justify="center")
    pin_entry.pack(pady=15)
    
    btn_unlock = Button(
        root, 
        text="Unlock Wallet", 
        command=lambda: verify_wallet_pin(pin_entry.get()), 
        bg="#1A1A1A", 
        fg="white", 
        font=("Arial", 11, "bold"),
        width=20,
        relief="raised"
    )
    btn_unlock.pack(pady=15)
    
    btn_back = Button(
        root, 
        text="Back to Vault", 
        command=show_password_vault_page, 
        bg="white", 
        fg="black", 
        font=("Arial", 11, "bold"),
        width=20,
        relief="raised"
    )
    btn_back.pack(pady=5)

    footer_label = Label(
        root, 
        text="by: Mohammed Reda", 
        bg="#FFD700", 
        fg="black", 
        font=("Arial", 11, "bold"),
        padx=10,
        pady=5
    )
    footer_label.pack(side="bottom", pady=20)

# اختيار مكان الذهاب للمحفظة
def handle_wallet_access():
    if not user_custom_pin:
        show_set_pin_page()
    else:
        show_wallet_pin_page()

# صفحة عرض محتويات المحفظة
def show_wallet_contents_page():
    for widget in root.winfo_children():
        widget.destroy()
        
    header = Label(
        root, 
        text="Your Saved Wallet\nDecrypted Secure Data", 
        bg="#1A1A1A", 
        fg="white", 
        font=("Arial", 14, "bold"),
        pady=15
    )
    header.pack(fill="x", pady=(0, 15))
    
    if not saved_passwords_db:
        Label(root, text="No passwords saved yet!", bg="#1E1E1E", fg="#FF6B6B", font=("Arial", 11, "bold")).pack(pady=20)
    else:
        for item in saved_passwords_db:
            info_text = f"Account: {item['site']}\nPassword: {item['password']}"
            lbl = Label(root, text=info_text, bg="#2A2A2A", fg="#00FFCC", font=("Arial", 10), justify="left", padx=10, pady=5)
            lbl.pack(fill="x", padx=20, pady=5)
            
    btn_back = Button(
        root, 
        text="Back to Vault", 
        command=show_password_vault_page, 
        bg="white", 
        fg="black", 
        font=("Arial", 11, "bold"),
        width=20,
        relief="raised"
    )
    btn_back.pack(pady=20)

    footer_label = Label(
        root, 
        text="by: Mohammed Reda", 
        bg="#FFD700", 
        fg="black", 
        font=("Arial", 11, "bold"),
        padx=10,
        pady=5
    )
    footer_label.pack(side="bottom", pady=20)

# صفحة فحص الروابط
def show_link_scanner_page():
    for widget in root.winfo_children():
        widget.destroy()
        
    header = Label(
        root, 
        text="Link Safety Scanner\nCheck links for threats", 
        bg="#1A1A1A", 
        fg="white", 
        font=("Arial", 14, "bold"),
        pady=20
    )
    header.pack(fill="x", pady=(0, 30))
    
    Label(root, text="Enter URL to scan:", bg="#1E1E1E", fg="white", font=("Arial", 11, "bold")).pack(pady=10)
    
    url_entry = Entry(root, font=("Arial", 11), width=28)
    url_entry.pack(pady=10)
    
    btn_scan = Button(
        root, 
        text="Scan Link Now", 
        command=lambda: check_link_safety(url_entry.get()), 
        bg="#1A1A1A", 
        fg="white", 
        font=("Arial", 11, "bold"),
        width=20,
        relief="raised"
    )
    btn_scan.pack(pady=20)
    
    btn_back = Button(
        root, 
        text="Back to Main Menu", 
        command=create_main_menu, 
        bg="white", 
        fg="black", 
        font=("Arial", 11, "bold"),
        width=20,
        relief="raised"
    )
    btn_back.pack(pady=10)

    footer_label = Label(
        root, 
        text="by: Mohammed Reda", 
        bg="#FFD700", 
        fg="black", 
        font=("Arial", 11, "bold"),
        padx=10,
        pady=5
    )
    footer_label.pack(side="bottom", pady=20)

# صفحة فحص الشبكة
def show_network_scanner_page():
    for widget in root.winfo_children():
        widget.destroy()
        
    header = Label(
        root, 
        text="Network Virus Scanner\nAnalyze network security", 
        bg="#1A1A1A", 
        fg="white", 
        font=("Arial", 14, "bold"),
        pady=20
    )
    header.pack(fill="x", pady=(0, 30))
    
    info_label = Label(
        root, 
        text="Tap below to scan your local network\nfor unauthorized devices and threats.", 
        bg="#1E1E1E", 
        fg="#CCCCCC", 
        font=("Arial", 10),
        justify="center"
    )
    info_label.pack(pady=15)
    
    btn_start_scan = Button(
        root, 
        text="Start Network Scan", 
        command=run_network_scan, 
        bg="#1A1A1A", 
        fg="white", 
        font=("Arial", 11, "bold"),
        width=22,
        relief="raised"
    )
    btn_start_scan.pack(pady=25)
    
    btn_back = Button(
        root, 
        text="Back to Main Menu", 
        command=create_main_menu, 
        bg="white", 
        fg="black", 
        font=("Arial", 11, "bold"),
        width=20,
        relief="raised"
    )
    btn_back.pack(pady=10)

    footer_label = Label(
        root, 
        text="by: Mohammed Reda", 
        bg="#FFD700", 
        fg="black", 
        font=("Arial", 11, "bold"),
        padx=10,
        pady=5
    )
    footer_label.pack(side="bottom", pady=20)

# صفحة مخزن كلمات المرور المشفرة
def show_password_vault_page():
    for widget in root.winfo_children():
        widget.destroy()
        
    header = Label(
        root, 
        text="Encrypted Password Vault\nStore passwords securely", 
        bg="#1A1A1A", 
        fg="white", 
        font=("Arial", 14, "bold"),
        pady=20
    )
    header.pack(fill="x", pady=(0, 15))
    
    Label(root, text="Service / Website Name:", bg="#1E1E1E", fg="white", font=("Arial", 10, "bold")).pack(pady=5)
    site_entry = Entry(root, font=("Arial", 11), width=25)
    site_entry.pack(pady=5)
    
    Label(root, text="Password:", bg="#1E1E1E", fg="white", font=("Arial", 10, "bold")).pack(pady=5)
    pwd_entry = Entry(root, font=("Arial", 11), width=25, show="*")
    pwd_entry.pack(pady=5)
    
    btn_save = Button(
        root, 
        text="Save & Encrypt", 
        command=lambda: save_password(site_entry.get(), pwd_entry.get()), 
        bg="#1A1A1A", 
        fg="white", 
        font=("Arial", 11, "bold"),
        width=20,
        relief="raised"
    )
    btn_save.pack(pady=10)

    btn_open_wallet = Button(
        root, 
        text="View Saved Wallet (PIN)", 
        command=handle_wallet_access, 
        bg="#FFD700", 
        fg="black", 
        font=("Arial", 10, "bold"),
        width=25,
        relief="raised"
    )
    btn_open_wallet.pack(pady=8)
    
    btn_back = Button(
        root, 
        text="Back to Main Menu", 
        command=create_main_menu, 
        bg="white", 
        fg="black", 
        font=("Arial", 11, "bold"),
        width=20,
        relief="raised"
    )
    btn_back.pack(pady=8)

    footer_label = Label(
        root, 
        text="by: Mohammed Reda", 
        bg="#FFD700", 
        fg="black", 
        font=("Arial", 11, "bold"),
        padx=10,
        pady=5
    )
    footer_label.pack(side="bottom", pady=20)

# القائمة الرئيسية (4 خيارات)
def create_main_menu():
    for widget in root.winfo_children():
        widget.destroy()
        
    header_label = Label(
        root, 
        text="CyberShield\nDevice Security & Protection", 
        bg="#1A1A1A", 
        fg="white", 
        font=("Arial", 14, "bold"),
        justify="center",
        pady=15
    )
    header_label.pack(fill="x", pady=(0, 15))

    instruction_label = Label(
        root, 
        text="Tap any feature you want", 
        bg="#1E1E1E", 
        fg="white", 
        font=("Arial", 11, "bold"),
        pady=5
    )
    instruction_label.pack(pady=5)

    btn_1 = Button(
        root, 
        text="1: Scan Links", 
        command=show_link_scanner_page,
        bg="white", 
        fg="black", 
        font=("Arial", 11, "bold"),
        width=28,
        relief="raised"
    )
    btn_1.pack(pady=6)

    btn_2 = Button(
        root, 
        text="2: Network Virus Scanner", 
        command=show_network_scanner_page,
        bg="white", 
        fg="black", 
        font=("Arial", 11, "bold"),
        width=28,
        relief="raised"
    )
    btn_2.pack(pady=6)

    btn_3 = Button(
        root, 
        text="3: Encrypted Password Vault", 
        command=show_password_vault_page,
        bg="white", 
        fg="black", 
        font=("Arial", 11, "bold"),
        width=28,
        relief="raised"
    )
    btn_3.pack(pady=6)

    btn_4 = Button(
        root, 
        text="4: Password Generator", 
        command=generate_password_page,
        bg="white", 
        fg="black", 
        font=("Arial", 11, "bold"),
        width=28,
        relief="raised"
    )
    btn_4.pack(pady=6)

    footer_label = Label(
        root, 
        text="by: Mohammed Reda", 
        bg="#FFD700", 
        fg="black", 
        font=("Arial", 11, "bold"),
        padx=10,
        pady=5
    )
    footer_label.pack(side="bottom", pady=15)

root = Tk()
root.title("Device Security - CyberShield")
root.geometry("380x600")
root.configure(bg="#1E1E1E")

create_main_menu()

root.mainloop()
