import csv
import json
import sqlite3
from pathlib import Path


class File:
    def __init__(self, file_name):
        self.file_name = file_name

    def create_json_folder(self):
        folder1 = input("ENTER FOLDER1 NAME>> ")
        file1 = input("ENTER FILE1 CONTENT>>  ")
        folder2 = input("ENTER FOLDER2 NAME>> ")
        file2 = input("ENTER FILE2 CONTENT>>  ")
        folder3 = input("ENTER FOLDER3 NAME>> ")
        file3 = input("ENTER FILE3 NAME>>    ")
        print(f"writing {self.file_name} into json file....")
        content = [{folder1: file1, folder2: file2, folder3: file3}]
        DataWrite = json.dumps(content)
        Path(f"{self.file_name}.json").write_text(DataWrite)
        find_folder = input("ENTER FOLDER NAME>>  ")
        if find_folder.lower() == folder1:
            print(file1)
        if find_folder.lower() == folder2:
            print(file2)
        if find_folder.lower() == folder3:
            print(file3)

    def create_csv_folder(self):
        folder1 = input("ENTER FOLDER1 NAME>> ")
        file1 = input("ENTER FILE1 CONTENT>>  ")
        folder2 = input("ENTER FOLDER2 NAME>> ")
        file2 = input("ENTER FILE2 CONTENT>>  ")
        folder3 = input("ENTER FOLDER3 NAME>> ")
        file3 = input("ENTER FILE3 NAME>>    ")
        print(f"writing {self.file_name} into CSV file....")
        with open(f"{self.file_name}.csv", "w") as DataCsvWriter:
            writer = csv.writer(DataCsvWriter)
            writer.writerow([folder1, folder2, folder3])
            writer.writerow([file1, file2, file3])
        find_folder = input("ENTER FOLDER NAME>>  ")
        if find_folder.lower() == folder1:
            print(file1)
        if find_folder.lower() == folder2:
            print(file2)
        if find_folder.lower() == folder3:
            print(file3)

    def create_sqlite_database(self):
        contents = json.loads(Path(f"{self.file_name}.json").read_text())
        with sqlite3.connect(f"{self.file_name}.sqlite3") as connection:
            command = f"INSERT INTO {self.file_name} VALUES(?, ?, ?)"
            for content in contents:
                connection.execute(command, tuple(content.values()))
            connection.commit()


file = File("james")
file.create_sqlite_database()
