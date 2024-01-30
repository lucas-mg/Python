import psutil
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage('/').percent

def analyze_saturation(cpu_threshold=80, memory_threshold=80, disk_threshold=80):
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()

    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print(f"Disk Usage: {disk_usage}%")

    if cpu_usage > cpu_threshold or memory_usage > memory_threshold or disk_usage > disk_threshold:
        print("System is saturated! Take action.")
    else:
        print("System is operating within normal limits.")

if __name__ == "__main__":
    while True:
        analyze_saturation()
        time.sleep(5)  # Adjust the sleep interval based on how frequently you want to check saturation
