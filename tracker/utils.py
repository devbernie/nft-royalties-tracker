# tracker/utils.py

import json
import csv
import os
import logging
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def read_json(file_path):
    """
    Read JSON data from a file.
    Args:
        file_path (str): Path to the JSON file.
    Returns:
        dict: JSON data.
    """
    file_path = os.path.expanduser(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_csv(data, file_path):
    """
    Export data to a CSV file.
    Args:
        data (list): List of rows of data.
        file_path (str): Path to the output CSV file.
    """
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def write_pdf(data, file_path, title="Report"):
    """
    Export data to a PDF file.
    Args:
        data (list): Data to export (list of transactions or royalties).
        file_path (str): Path to the output PDF file.
        title (str): Title of the report.
    """
    c = canvas.Canvas(file_path, pagesize=letter)
    _, height = letter

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, title)

    # Data content
    c.setFont("Helvetica", 12)
    y = height - 100
    for row in data:
        text = ", ".join(f"{key}: {value}" for key, value in row.items())
        c.drawString(50, y, text)
        y -= 20
        if y < 50:  # If end of page
            c.showPage()
            y = height - 50

    c.save()


# Configure logging at the application level
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def log_message(message, level="info"):
    """
    Log messages for the application.
    Args:
        message (str): Log message.
        level (str): Log level (info, warning, error).
    """
    log_func = getattr(logging, level, logging.info)
    log_func(message)