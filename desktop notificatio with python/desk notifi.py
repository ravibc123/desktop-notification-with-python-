import time
from plyer import notification 

if __name__== "__main__":
    while True:

        notification.notify (
        title="ALERT!!!",
        message="Take abreak !it has been an hour!!!",
        timeout=1100)

        time.sleep(3000)
