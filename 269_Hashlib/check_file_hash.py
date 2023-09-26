import hashlib

CORRECT_HASH = "59f57803fa5235075c3e470e1006905a61236e491bb75a599d862cafcfbb529f"

with open("269_Hashlib/Everything-1.4.1.1024.x86-Setup.exe","rb") as f:
    file_bytes = f.read()
    h = hashlib.sha256()
    h.update(file_bytes)
    file_hash = h.hexdigest()

print(file_hash == CORRECT_HASH)

