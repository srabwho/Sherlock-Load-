import yt_dlp
import requests
import time

# --- 1. رسمة شيرلوك المختصرة ---
def عرض_شيرلوك_ascii():
    sherlock_ascii = r'''
       ,_       
     ,'  `\,_   
     |_,-'_)    
     /##c '\  ( 
    ' |'  -{.  )
      /\__-' \[]
     /`-_`\     
     '     \    
    Sherlock Load
    '''
    print(sherlock_ascii)

# --- 2. واجهة وتعليمات ---
def عرض_الواجهة():
    print("=" * 60)
    عرض_شيرلوك_ascii()
    print("=" * 60)
    print("🕵️‍♂️ Tool Name: Sherlock Load")
    print("🔧 Developed by: Srab Al-Qahtani")
    print("📸 Instagram: @srvesthetic")
    print("=" * 60)
    print("🎯 Professional Media Downloader Tool")
    print("📥 Supports: TikTok, YouTube, Twitter, Instagram, Snapchat")
    print("💾 Output: /root/Downloads")
    print("❌ Exit anytime: type 'q'")
    print("=" * 60)
    time.sleep(1)

# --- 3. فك روابط مختصرة ---
def حل_رابط_مختصر(url):
    try:
        return requests.head(url, allow_redirects=True).url
    except:
        return url

# --- 4. تحميل الفيديو أو الصوت ---
def تحميل(الرابط, صوت=False, الجودة="best"):
    إعدادات = {
        'quiet': True,
        'format': 'bestaudio' if صوت else الجودة,
        'outtmpl': '/root/Downloads/%(title)s.%(ext)s',
    }

    if صوت:
        إعدادات['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    try:
        print("⏳ Downloading...")
        with yt_dlp.YoutubeDL(إعدادات) as ydl:
            ydl.download([الرابط])
        print("✅ Download completed!")
        print("📁 Saved to: /root/Downloads")
    except Exception as e:
        print(f"❌ Error: {e}")

# --- 5. واجهة المستخدم ---
def واجهة_المستخدم():
    عرض_الواجهة()
    while True:
        رابط = input("\n📎 Paste the link (or type 'q' to quit): ").strip()
        if رابط.lower() == "q":
            print("\n👋 Thank you for using Sherlock Load. Goodbye!")
            break

        if any(x in رابط for x in ["vm.tiktok.com", "bit.ly", "t.co"]):
            رابط = حل_رابط_مختصر(رابط)
            print(f"🔗 Resolved short link: {رابط}")

        صوت = input("🎧 Download audio only? (yes / no): ").strip().lower() == "yes"
        if not صوت:
            print("\n🎚️ Choose video quality:")
            print("1 - High (best)")
            print("2 - Medium (best[height<=720])")
            print("3 - Low (best[height<=480])")
            اختيار = input("👉 Enter 1/2/3: ").strip()
            if اختيار == "2":
                جودة = "best[height<=720]"
            elif اختيار == "3":
                جودة = "best[height<=480]"
            else:
                جودة = "best"
        else:
            جودة = "bestaudio"

        تحميل(رابط, صوت, جودة)

if __name__ == "__main__":
    واجهة_المستخدم()
