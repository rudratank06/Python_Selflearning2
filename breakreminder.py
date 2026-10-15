import schedule
import time
from plyer import notification

def send_break_alert(title, message):
    """Trigger a native cross-platform OS toast notification."""
    notification.notify(
        title=title,
        message=message,
        timeout=5  # seconds the notification stays visible
    )

def hydration_alert():
    send_break_alert("Hydration Alert", "Time to drink some water!")

def posture_check():
    send_break_alert("Posture Check", "Sit up straight and relax your shoulders.")

# Scheduling triggers (using short intervals here for testing)
schedule.every(10).seconds.do(hydration_alert)   # In production: schedule.every(45).minutes.do(hydration_alert)
schedule.every(20).seconds.do(posture_check)

print("Health & Break Reminder Daemon started. Press Ctrl+C to stop.")

try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("\nDaemon stopped. Stay healthy!")