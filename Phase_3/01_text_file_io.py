# ============================================
# 01 - TEXT FILE INPUT / OUTPUT
# ============================================

# Hinglish: File I/O ka matlab file se data read aur file me data write karna.
# with open(...) best practice hai kyunki file automatically close ho jaati hai.

file_name = "notes.txt"

# WRITE MODE: w purana content replace kar sakta hai.
with open(file_name, "w", encoding="utf-8") as file:
    file.write("Python is easy to learn.\n")
    file.write("File handling is useful.\n")

# READ MODE
with open(file_name, "r", encoding="utf-8") as file:
    content = file.read()

print(content)

# APPEND MODE: a existing file ke end me content add karta hai.
with open(file_name, "a", encoding="utf-8") as file:
    file.write("Practice makes you better.\n")

# Practice: line count aur word count nikaalo.
