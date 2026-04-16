import subprocess
import platform
import datetime

# ====================== NETWORK MONITOR ======================
# Thay danh sách IP bên dưới bằng IP nội bộ của công ty/bạn

IP_LIST = [
    "192.168.1.1",      # Router thường
    "192.168.1.100",    # Máy 1
    "192.168.1.101",    # Máy 2
    # Thêm IP khác ở đây...
]

def ping_ip(ip):
    """Ping 1 lần, trả về True nếu online"""
    param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    try:
        output = subprocess.check_output(f"ping {param} {ip}", shell=True, stderr=subprocess.STDOUT)
        return "Reply from" in str(output) or "bytes from" in str(output)
    except subprocess.CalledProcessError:
        return False

def main():
    print("=== IT Support - Network Monitor ===")
    print(f"Thời gian: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    offline_devices = []
    
    for ip in IP_LIST:
        status = "✅ Online" if ping_ip(ip) else "❌ Offline"
        print(f"{ip:15} → {status}")
        if "Offline" in status:
            offline_devices.append(ip)
    
    # Xuất báo cáo
    with open("network_status_report.txt", "w", encoding="utf-8") as f:
        f.write("=== NETWORK STATUS REPORT ===\n")
        f.write(f"Thời gian: {datetime.datetime.now()}\n\n")
        for ip in IP_LIST:
            status = "Online" if ping_ip(ip) else "Offline"
            f.write(f"{ip:15} → {status}\n")
        if offline_devices:
            f.write("\n⚠️ Thiết bị offline:\n")
            for dev in offline_devices:
                f.write(f"   - {dev}\n")
    
    print(f"\n✅ Kiểm tra xong! Báo cáo: network_status_report.txt")
    if offline_devices:
        print(f"⚠️ Có {len(offline_devices)} thiết bị offline!")

if __name__ == "__main__":
    main()
