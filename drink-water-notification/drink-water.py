from plyer import notification
import time

def drinkWaterNotificaton (title, message) :
    notification.notify(
        title = title,
        message = message,
        app_icon = "D:\\Workspace\\MyWork\\PythonProject\\LearnPython\\drink-water-notification\\water.ico",
        timeout = 5
    )


if __name__ == '__main__':
    while 1:
        title = "Drink Water Reminer"
        currTime = time.ctime()
        message = f"Drink Water Now\n" \
                  f"{currTime}"

        drinkWaterNotificaton(title, message)
        time.sleep(4*60*60*60)
