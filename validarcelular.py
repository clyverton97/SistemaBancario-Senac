def validarCelular():
    validar = input("Você deseja validar seu celular?").lower.strip()
    if validar == "sim" or validar == "s":
        print("Celular validado com sucesso")
    else:
        print("Autorização bloqueada")