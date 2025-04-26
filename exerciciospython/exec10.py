din = (input('Quantos reais possui na conta?\n'))
din1 = float(din.replace(",", "."))

dinus = str(round(din1/6.03,2))
dines = str(round(din1/6.28,2))
print(f'R${din.replace(".", ",")}\n${dinus.replace(".", ",")}\n€{dines.replace(".", ",")}')
