import psutil
import wmi
import datetime
import platform

def get_cpu_temp():
    """Lấy nhiệt độ CPU qua WMI (Windows)"""
    try:
        w = wmi.WMI()
        for sensor in w.MSAcpi_ThermalZoneTemperature():
            temp_c = (sensor.CurrentTemperature / 10.0) - 273.15
            return f"{temp_c:.1f}°C"
        return "Không xác định"
    except Exception:
        return "Không lấy được (chạy với quyền Admin hoặc máy không hỗ trợ)"

def main():
    print("=== IT Support - System Health Check ===")
    report = []
    report.append(f"Thời gian: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"Hệ điều hành: {platform.system()} {platform.release()}\n")

    # 1. Thông tin ổ cứng
    report.append("=== Ổ CỨNG ===")
    for partition in psutil.disk_partitions(all=False):
        if 'cdrom' in partition.opts or partition.fstype == '':
            continue
        usage = psutil.disk_usage(partition.mountpoint)
        report.append(f"Ổ: {partition.device} ({partition.mountpoint})")
        report.append(f"   Dung lượng: {usage.total // (1024**3)} GB")
        report.append(f"   Đã dùng: {usage.used // (1024**3)} GB ({usage.percent}%)")
        report.append(f"   Còn trống: {usage.free // (1024**3)} GB\n")

    # 2. RAM
    ram = psutil.virtual_memory()
    report.append("=== RAM ===")
    report.append(f"Tổng RAM: {ram.total // (1024**3)} GB")
    report.append(f"Đã dùng: {ram.used // (1024**3)} GB ({ram.percent}%)")
    report.append(f"Còn trống: {ram.available // (1024**3)} GB\n")

    # 3. Nhiệt độ CPU
    report.append("=== CPU ===")
    report.append(f"Nhiệt độ CPU: {get_cpu_temp()}")
    report.append(f"Sử dụng CPU: {psutil.cpu_percent(interval=1)}%")

    # Xuất báo cáo
    with open("system_health_report.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(report))
    
    print("✅ Báo cáo đã được tạo: system_health_report.txt")
    print("Mở file để xem chi tiết!")

if __name__ == "__main__":
    main()
