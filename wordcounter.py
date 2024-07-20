arquivo = "first.txt"
with open(arquivo, "r") as a:
    raw = a.read()
raw.lstrip()
raw = raw.split(" ")
print(f"Arquivo {arquivo} contém {len(raw)} palavras.")
print(len(raw))