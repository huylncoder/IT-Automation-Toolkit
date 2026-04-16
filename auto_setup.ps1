# ====================== AUTO SETUP TOOL - CHỈ CÀI UNIKEY ======================
# FIX UTF-8 MẠNH NHẤT CHO WINDOWS POWERSHELL 5.1

# Buộc encoding UTF-8 từ đầu
chcp 65001 | Out-Null
$OutputEncoding = [System.Text.UTF8Encoding]::new()
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
[Console]::InputEncoding  = [System.Text.UTF8Encoding]::new()

Write-Host "=== IT Support - Auto Setup (Unikey Only) ===" -ForegroundColor Green
Write-Host "Mục tiêu: Tự động cài đặt UniKey - Bàn phím tiếng Việt`n" -ForegroundColor Cyan

# 1. Chocolatey
if (-not (Get-Command choco -ErrorAction SilentlyContinue)) {
    Write-Host "Chocolatey chưa được cài. Đang cài đặt..." -ForegroundColor Yellow
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    Write-Host "✅ Chocolatey đã cài thành công!" -ForegroundColor Green
} else {
    Write-Host "✅ Chocolatey đã được cài sẵn." -ForegroundColor Green
}

# 2. Unikey
Write-Host "`nĐang cài đặt / Cập nhật Unikey..." -ForegroundColor Yellow
choco install Unikey -y --force

if ($LASTEXITCODE -eq 0 -or $LASTEXITCODE -eq 3010) {
    Write-Host "`n✅ Cài đặt Unikey thành công!" -ForegroundColor Green
} else {
    Write-Host "`n⚠️ Có lỗi khi cài Unikey." -ForegroundColor Red
}

Write-Host "`nHoàn tất tự động hóa setup." -ForegroundColor Green
Write-Host "Thời gian hoàn thành: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor White
Write-Host "`nGợi ý: Mở Unikey → Chọn kiểu gõ Telex hoặc VNI." -ForegroundColor White