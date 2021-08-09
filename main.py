A = ['a','b', 'c']
bandera = True
TablaT = [[0,'a',1],[1,'a',1],[1,'b',2]]
TablaC = []
EF = [1]
E = 0
EA = E
CE = "aabbcc"
for c in CE:
    print(c)
    if c in A:
        print("Pertence")
        for f in TablaT:
            if c in f and EA in f:
                TablaC.append([EA,c,f[2]])
                EA = f[2]
                print("Estado Final: "+str(EA))
    else:
        print("Não pertence")
        bandera = False

if EA in EF and bandera == True:
    print("---------------------------------\n")
    print("Aceita!!!\n")
    print("-----Tabela de transição-------\n")
    for t in TablaC:
        print(t)
else:
    print("Rejeitada!\n")
    print("-----Tabela de transição-------\n")
    for t in TablaC:
        print(t)
