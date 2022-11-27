pqs = input("Pesquisa: ")
pqs = pqs.replace(" ", "%20")
pqs = pqs.replace("ç" or "Ç", "%C3%A7")
pqs = pqs.replace("á" or "Á", "%C3%A1")
pqs = pqs.replace("à" or "À", "%C3%A0")
pqs = pqs.replace("é" or "É", "%C3%A9")
pqs = pqs.replace("è" or "È", "%C3%A8")
pqs = pqs.replace("ã" or "Ã", "%C3%A3")
pqs = pqs.replace("õ" or "Õ", "%C3%B5")


print(pqs)