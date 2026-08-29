import time
import psutil

def get_memory_available_mb():
    memory = psutil.virtual_memory()
    return memory.available / (1024 * 1024)

def get_temperature():
    temperature = psutil.sensors_temperatures()
    # Assuming you want the main CPU temperature
    if temperature:
        return list(temperature.values())[0][0].current
    return None

def get_cpu_percent():
    cpu_percent = psutil.cpu_percent(interval = None)
    return cpu_percent

def get_disk_free_gb():
    disk_usage = psutil.disk_usage('/')
    return disk_usage.free / (1024 ** 3)

def get_uptime_seconds():
    boot_time = psutil.boot_time()
    current_time = time.time()
    uptime_seconds = current_time - boot_time
    return uptime_seconds

def get_system_info():
    return {
        "hostname": psutil.users()[0].name,
        "temperature": get_temperature(),
        "cpu_percent": get_cpu_percent(),
        "memory_available_mb": get_memory_available_mb(),
        "disk_free_gb": get_disk_free_gb(),
        "uptime_seconds": get_uptime_seconds()
    }