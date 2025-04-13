import os
import re
import csv 

def read_log_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return file.readlines()

def filter_log_lines(lines, keyword):
    return [line for line in lines if keyword.lower() in line.lower()]

def count_matches(lines, keyword):
    return sum(1 for line in lines if keyword.lower() in line.lower())

def parse_log_line(line):
    pattern = re.pattern(r"\[(.*?)\]\s+\[(.*?)\]\s+(.*)", line)
    if pattern:
        return {
            "timestamp": pattern.group(1),
            "level": pattern.group(2),
            "message": pattern.group(3)
        }
    return None

def export_logs_to_csv(log_lines, file_path):
    parsed_lines = [parse_log_line(line) for line in log_lines if parse_log_line(line)]
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['timestamp', 'level', 'message'])
        writer.writeheader()
        for row in parsed_lines:
            writer.writerow(row)
