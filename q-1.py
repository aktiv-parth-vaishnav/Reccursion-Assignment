def find_file(folder, file_to_find, path=""):
    for name, content in folder.items():
        current_path = f"{path}/{name}"
        if name == file_to_find:
            return current_path
        elif isinstance(content, dict):
            result = find_file(content, file_to_find, current_path)
            if result:
                return result
    return None

# File system data
file_system = {
    "documents": {
        "work": {
            "report.docx": None,
            "summary.xlsx": None,
        },
        "personal": {
            "photos": {
                "vacation.jpg": None,
                "birthday.png": None,
            }
        },
    },
    "downloads": {
        "software": {
            "setup.exe": None,
        },
        "music": {
            "song.mp3": None,
        },
    },
}

file_to_find = "birthday.png"
result = find_file(file_system, file_to_find)

if result:
    print(f"File '{file_to_find}' found at: {result}")
else:
    print(f"File '{file_to_find}' not found.")
