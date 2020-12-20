from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(
            title="please Take a break!!",
            message="Breaks help you to process and retain information.Taking regular breaks helps you be more productive.",
            app_icon='noun_relaxing.ico',
            timeout=10,
        )
        time.sleep(60*60)
