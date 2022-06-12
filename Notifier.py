from win10toast import ToastNotifier
import time
from plyer import notification

# One-time initialization
toaster = ToastNotifier()

# Show notification when needed
toaster.show_toast("Notification!", "Alert!", threaded=True, icon_path=None, duration=3) # 3 seconds

# check if notifications are active,
# use 'toaster.notification_active()'
while toaster.notification_active():
    time.sleep(0.1)

notification.notify(
    title='Here is the title',
    message='Here is the message',
    app_icon=None, # e.g. 'C:\\icon_32x32.ico'
    timeout=10, #seconds
)
