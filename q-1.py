def find_file(folder, filetofind, path=""):
    for name, content in folder.items():
        current_path = f"{path}/{name}"
        print(current_path)
        if name == filetofind:
            return current_path
        elif isinstance(content, dict):
            result = find_file(content, filetofind, current_path)
            if result:
                return result
    return None

filesystem = {
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

filetofind = "birthday.png"
result = find_file(filesystem, filetofind)
print(result)
