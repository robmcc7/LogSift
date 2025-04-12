import os

def read_log_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return file.readlines()

def filter_log_lines(lines, keyword):
    return [line for line in lines if keyword.lower() in line.lower()]

def count_matches(lines, keyword):
    return sum(1 for line in lines if keyword.lower() in line.lower())


