import streamlit as st
from datetime import datetime, timedelta
from streamlit_autorefresh import st_autorefresh

# Otomatik yenileme (her 1 saniyede bir yenile)
st_autorefresh(interval=1000, key="counter")


now = datetime.now()
st.write(now)
# 5 Şubat 23:59:00 hedef zamanı
target_date = datetime(year=2025, month=2, day=5, hour=23, minute=59, second=59)

time_remaining = target_date - now

# Eğer süre dolduysa, sıfır yap
if time_remaining.total_seconds() <= 0:
    st.subheader("Süre doldu! 🚀")
else:
    # Gün, saat, dakika ve saniyeye böl
    days = time_remaining.days
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # HTML ile geri sayımı göster
    countdown_html = f"""
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; font-family: Arial, sans-serif; gap: 20px;">
        <h2 style="color: #ff6f61; font-size: 36px;">5 Şubat 23:59:59</h2>
        <h2 style="color: #ff6f61; font-size: 24px;">Geri Sayım</h2>
        <div style="display: flex; gap: 40px;"> <!-- Aralarına boşluk için gap -->
            <div style="text-align: center;">
                <div style="font-size: 48px; font-weight: bold; color: #333;">{days}</div>
                <div style="font-size: 16px; color: #777;">Gün</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 48px; font-weight: bold; color: #333;">{hours:02}</div>
                <div style="font-size: 16px; color: #777;">Saat</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 48px; font-weight: bold; color: #333;">{minutes:02}</div>
                <div style="font-size: 16px; color: #777;">Dakika</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 48px; font-weight: bold; color: #333;">{seconds:02}</div>
                <div style="font-size: 16px; color: #777;">Saniye</div>
            </div>
        </div>
    </div>
    """
    # HTML'yi Streamlit'e ekle
    st.markdown(countdown_html, unsafe_allow_html=True)

import random 
source_links = ["https://www.youtube.com/watch?v=Y1ohJumDYF4", "https://www.youtube.com/watch?v=AYPJhuidReg","https://www.youtube.com/watch?v=z9SzHvp7Lu0", "https://www.youtube.com/watch?v=fr54CX_6ERk", "https://www.youtube.com/watch?v=1yEeLRoWIhA"]
selected_link = random.choice(source_links)

if now.hour%2 == 0  and (now.minute == 47 or now.minute == 30 or now.minute == 15 or now.minute == 0):
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; font-family: Arial, sans-serif; gap: 20px; margin-top: 20px;">
            <h2 style="color: #ff6f61; font-size: 24px;">🎥 Özel YouTube Videosu</h2>
            <div style="border: 2px solid #ff6f61; border-radius: 10px; padding: 10px; background-color: #f9f9f9; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
                <a href="{selected_link}" target="_blank" style="text-decoration: none; color: #333;">
                    <img src="https://i.ytimg.com/vi/10WZLflapyI/mqdefault.jpg" alt="YouTube Video" style="width: 100%; border-radius: 8px;">
                    <p style="text-align: center; margin-top: 10px; font-size: 18px; font-weight: bold;">Bu özel videoyu izlemek için tıklayın!</p>
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )