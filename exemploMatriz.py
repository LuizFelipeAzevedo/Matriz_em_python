tab = []
tab.append(['']* 3)
tab.append(['']* 3)
tab.append(['']* 3)

tab[0][0]='X'
tab[1][1]='X'
tab[1][0]='O'
tab[0][2]='X'
for linha in tab:
    print(linha)
