def calcular():
    while True:
        print("\nCalculadora Simples")
        print("Escolha a operação:")
        print("1. Soma (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Sair")
        
        escolha = input("Digite a opção (1/2/3/4/5): ")
        
        if escolha == '5':
            print("Encerrando a calculadora.")
            break
        
        if escolha in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Erro: Entrada inválida. Digite números válidos.")
                continue
            
            if escolha == '1':
                print(f"Resultado: {num1} + {num2} = {num1 + num2}")
            elif escolha == '2':
                print(f"Resultado: {num1} - {num2} = {num1 - num2}")
            elif escolha == '3':
                print(f"Resultado: {num1} * {num2} = {num1 * num2}")
            elif escolha == '4':
                if num2 == 0:
                    print("Erro: Divisão por zero não permitida.")
                else:
                    print(f"Resultado: {num1} / {num2} = {num1 / num2}")
        else:
            print("Opção inválida. Escolha um número entre 1 e 5.")
        
if __name__ == "__main__":
    calcular()