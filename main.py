from cpf_validator import CPFValidator

def main():
    cpf_fornecido = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")

    try:
        if CPFValidator(cpf_fornecido).validate():
            print("CPF é válido")
        else:
            print("CPF inválido")
    except ValueError as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()
