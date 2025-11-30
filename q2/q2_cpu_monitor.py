import time
import psutil

THRESHOLD = 80  # CPU usage percentage

def monitor_cpu(threshold: int = THRESHOLD):
    print("Monitoring CPU usage... (Press Ctrl+C to stop)")
    try:
        while True:
            # interval=1 means it waits 1 second and measures CPU usage over that second
            usage = psutil.cpu_percent(interval=1)

            if usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {usage}%")

            # Optional: small sleep, but cpu_percent already waited 1 second
            # time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"❌ An error occurred while monitoring CPU: {e}")


if __name__ == "__main__":
    monitor_cpu()
