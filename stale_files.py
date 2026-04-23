import os
from datetime import datetime, timedelta

def get_details_of_stale_files(directories, stale_days):
    stale_files = []
    for directory in directories:
        for root,_,files in os.walk(directory):
            for file in files:
                filepath = os.path.join(root, file)
                try:
                    file_info = get_file_info(filepath)
                    if is_stale_file(file_info["last_modified_time"], stale_days):
                        stale_files.append(file_info)
                except:
                    print(f"Error getting info for file: {filepath}")
                    continue
    return stale_files                  

def get_file_info(filepath):
    stat_details = os.stat(filepath)
    return {
        "filepath": filepath,
        "name": os.path.basename(filepath),
        "size": stat_details.st_size,
        "type": os.path.splitext(filepath)[1],
        "last_modified_time": datetime.fromtimestamp(stat_details.st_mtime)
    }

def is_stale_file(last_modified_time, stale_days):
    stale_days_from_now = datetime.now() - timedelta(days=stale_days)
    return last_modified_time < stale_days_from_now

def print_stale_files_report(stale_files):
    report = {
        "total_stale_files": len(stale_files),
        "total_stale_files_size": sum(file["size"] for file in stale_files),
        "stale_files_details": stale_files
    }

    if report:
        if report["total_stale_files"] > 0:
            print(f"Total stale files: {report['total_stale_files']}")
            print(f"Total size of stale files: {report['total_stale_files_size']} bytes")
            print("Details of stale files:")
            for file in report["stale_files_details"]:
                print(f"Filepath: {file['filepath']}, Name: {file['name']}, Size: {file['size']} bytes, Type: {file['type']}, Last Modified Time: {file['last_modified_time']}")
        else:
            print("No stale files found.")
    else:
        print("No report generated.")                

if __name__ == "__main__":
    directories = ["D:/js"]
    stale_days = 30
    stale_files = get_details_of_stale_files(directories, stale_days)
    print_stale_files_report(stale_files)