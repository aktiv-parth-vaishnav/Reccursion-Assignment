def fin(file_to_find, folder):
    for name, subfolder in folder.items():
        print(name)
        print(subfolder)
        if name == file_to_find:
            return "/" + name
        elif isinstance(subfolder, dict):
            path = fin(file_to_find, subfolder)
            if path:
                return "/" + name + path
    return None

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
            },
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

file_to_find = "music"
result = fin(file_to_find, file_system)

if result:
    print(f"File '{file_to_find}' found at: {result}")
else:
    print(f"File '{file_to_find}' not found.")
