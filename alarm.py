import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "PLEASE TAKE A SHORT BREAK",
            message = "Its good to take short break after 25 minutes of work",
            app_icon = "D:\Projects\Alarm\pic_nxf_icon.ico",
            timeout = 10
            )
        time.sleep(1500)   
