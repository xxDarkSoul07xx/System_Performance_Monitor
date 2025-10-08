# System Performance Monitor
# This is just a quick terminal tool that shows CPU, memory, and disk usage in real time

import psutil
import time
import os
import argparse

# grab system stats
def get_stats():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, mem, disk

# print system stats in a loop until user stops it
def monitor(interval):
    try:
        while True:
            # clear the screen each time for a "live" effect
            os.system('cls' if os.name == 'nt' else 'clear')

            cpu, mem, disk = get_stats()

            print("=== System Performance Monitor ===")
            print(f"CPU Usage: {cpu}%")
            print(f"Memory Usage: {mem}%")
            print(f"Disk Usage: {disk}%")

            # wait a bit before refreshing
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopped monitoring.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command-line system monitor.")
    parser.add_argument('--interval', type=int, default=1,
                        help="Refresh interval in seconds (default 1)")
    args = parser.parse_args()

    monitor(args.interval)
