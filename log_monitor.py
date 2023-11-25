# log_monitor.py
import time

def monitor_log(file_path, alert_keywords):
    with open(file_path, 'r') as f:
        # Move to the end of file
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            for keyword in alert_keywords:
                if keyword in line:
                    print(f"ALERT: Detected '{keyword}' in log.")
                    # Aquí puedes agregar acciones adicionales, como enviar un correo o notificación

if __name__ == "__main__":
    log_file = input("Enter path to log file: ")
    keywords = input("Enter alert keywords (separated by commas): ").split(',')
    keywords = [kw.strip() for kw in keywords]
    monitor_log(log_file, keywords)
