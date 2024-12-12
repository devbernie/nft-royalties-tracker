# File: tracker/utils.py

import json
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def read_json(file_path):
    """
    Đọc dữ liệu JSON từ file.
    Args:
        file_path (str): Đường dẫn file JSON.
    Returns:
        dict: Dữ liệu JSON.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_csv(data, file_path):
    """
    Xuất dữ liệu ra file CSV.
    Args:
        data (list): Danh sách các hàng dữ liệu.
        file_path (str): Đường dẫn file CSV xuất ra.
    """
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def write_pdf(data, file_path, title="Report"):
    """
    Xuất dữ liệu ra file PDF.
    Args:
        data (list): Dữ liệu cần xuất (danh sách giao dịch hoặc royalties).
        file_path (str): Đường dẫn file PDF xuất ra.
        title (str): Tiêu đề báo cáo.
    """
    c = canvas.Canvas(file_path, pagesize=letter)
    _, height = letter

    # Tiêu đề
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, title)

    # Nội dung dữ liệu
    c.setFont("Helvetica", 12)
    y = height - 100
    for row in data:
        text = ", ".join(f"{key}: {value}" for key, value in row.items())
        c.drawString(50, y, text)
        y -= 20
        if y < 50:  # Nếu hết trang
            c.showPage()
            y = height - 50

    c.save()


def format_currency(value, currency="ADA"):
    """
    Định dạng số thành chuỗi có gắn đơn vị tiền tệ.
    Args:
        value (float): Giá trị số.
        currency (str): Loại tiền tệ.
    Returns:
        str: Chuỗi định dạng tiền tệ.
    """
    return f"{value:,.2f} {currency}"


def validate_address(address):
    """
    Xác minh địa chỉ ví Cardano hợp lệ.
    Args:
        address (str): Địa chỉ ví Cardano.
    Returns:
        bool: True nếu hợp lệ, False nếu không hợp lệ.
    """
    return len(address) > 50 and address.startswith("addr")


def log_message(message, level="info"):
    """
    Ghi log cho ứng dụng.
    Args:
        message (str): Nội dung log.
        level (str): Mức độ log (info, warning, error).
    """
    levels = {"info": "INFO", "warning": "WARNING", "error": "ERROR"}
    print(f"[{levels.get(level, 'INFO')}] {message}")