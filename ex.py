valores = [25, 40, 120, 84, 520, 1010, 960, 340, 252, 104]
letra = ["a)", "b)", "c)", "d)", "e)", "f)", "g)", "h)", "i)", "j)", ]
print("As respostas vão seguir o seguinte modelo : numerador/denominador=resultado(resto).(quantas veses forem "
      "necessárias) = binário(do ultimo resto ao primeiro)     ")
for i in range(0, len(valores)):
    print("")
    listaresto = []
    resto = 0
    for j in range(0, valores[i]):
        if valores[i] == 0:
            break
        resto = valores[i] % 2
        listaresto.append(resto)
        print(f"{letra[i]}- {valores[i]} : {valores[i]}/2 = {valores[i] // 2}({valores[i] % 2}) =.", end="")
        valores[i] = valores[i] // 2
    listabinarios = listaresto[::-1]
    for k in range(0, len(listabinarios)):
        print(f"{listabinarios[k]}", end="")
