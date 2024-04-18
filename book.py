import re

f = open("book.txt", "r")

resultado = []
DAT_ANTES = "\t03  FILLER						PIC X(013)\n									VALUE\n									\"STR_TO_DATE(\'\".\n"
DAT_DEPOIS = "\t03  FILLER						PIC X(014)\n									VALUE\n									\"\', \'$D.%M.%Y\')\".\n"
ASPAS = "\t03  FILLER						PIC X(01)\n									VALUE\n									\"'\".\n"

linhas = f.readlines()
for linha in linhas:
    proximo = False

    pic_timestamp = re.search("DAT-HOR", linha)
    if (pic_timestamp is not None):
        resultado.append(ASPAS)
        resultado.append(linha)
        resultado.append(ASPAS)
        proximo = True

    data_mask = re.search("DAT-", linha)
    if (data_mask is not None and proximo == False):
        resultado.append(DAT_ANTES)
        resultado.append(linha)
        resultado.append(DAT_DEPOIS)
        proximo = True

    resultado.append(linha)
    #pic_mask = re.search("PIC X", linha)


#print(f.read())
print("gerando arquivo...")
arquivo = open("book_result.txt", 'w')
for r in range(len(resultado)):
    print(resultado[r])
    arquivo.writelines(resultado[r])

arquivo.close()
