arquivo = ["first.txt", "second.txt"]
for a in arquivo:
    with open(a, "r") as arq:
        raw = arq.read()
        raw.lstrip()
        raw = raw.split(" ")
        print(f"Arquivo {a} contém {len(raw)} palavras!")