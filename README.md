# IT Automation Toolkit

Công cụ tự động hóa hỗ trợ kỹ thuật IT (dành cho IT Support).

## Các tính năng đã triển khai

- **Script 1: System Health Check** – Kiểm tra ổ cứng, RAM, nhiệt độ CPU và xuất báo cáo.
- **Script 2: Auto Setup** – Tự động cài Unikey (và có thể mở rộng các phần mềm khác) bằng Chocolatey.
- **Script 3: Network Monitor** – Ping các thiết bị trong mạng nội bộ, báo cáo thiết bị offline.

## Công nghệ sử dụng
- Python (psutil, wmi)
- PowerShell + Chocolatey
- Git & GitHub

## Cách chạy
- Script 1 & 3: `python ten_file.py`
- Script 2: Chạy PowerShell as Administrator → `./auto_setup.ps1`

## Mục tiêu dự án
Tự động hóa các tác vụ lặp lại, giảm thời gian setup máy mới và kiểm tra hệ thống.
