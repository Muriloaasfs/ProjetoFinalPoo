from models.entidades import Cliente, Pet


def ler_inteiro(mensagem: str) -> int:
    """Garante que o usuário digite um número inteiro sem travar o programa."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: Digite apenas números inteiros válidos.")


def ler_float(mensagem: str) -> float:
    """Garante que o usuário digite um número decimal válido."""
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            return valor
        except ValueError:
            print("Erro: Digite um valor numérico válido (ex: 12.5).")


def buscar_por_codigo(lista_registros: list, codigo: int):
    """Busca sequencial pelo código único do registro."""
    for item in lista_registros:
        if item.get_codigo() == codigo:
            return item
    return None


def menu():
    # Lista heterogênea: armazena objetos das classes Cliente e Pet juntos
    registros_petshop = []

    while True:
        print("\n" + "=" * 40)
        print("      SISTEMA PETSHOP - MENU PRINCIPAL")
        print("=" * 40)
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Pet (vincular a um Cliente)")
        print("3. Listar Todos os Registros (Polimorfismo)")
        print("4. Buscar Registro por Código")
        print("5. Remover Registro por Código")
        print("0. Sair")
        print("=" * 40)

        opcao = ler_inteiro("Escolha uma opção: ")

        if opcao == 1:
            try:
                cod = ler_inteiro("Código do Cliente: ")
                if buscar_por_codigo(registros_petshop, cod):
                    print("Aviso: Já existe um registro com esse código.")
                    continue
                nome = input("Nome do Cliente: ")
                telefone = input("Telefone: ")
                novo_cliente = Cliente(cod, nome, telefone)
                registros_petshop.append(novo_cliente)
                print("Cliente cadastrado com sucesso!")
            except ValueError as erro:
                print(f"Não foi possível cadastrar: {erro}")

        elif opcao == 2:
            try:
                cod_tutor = ler_inteiro("Digite o código do Cliente (tutor): ")
                tutor = buscar_por_codigo(registros_petshop, cod_tutor)

                if not isinstance(tutor, Cliente):
                    print("Erro: Cliente não encontrado. Cadastre o tutor primeiro.")
                    continue

                cod_pet = ler_inteiro("Código do Pet: ")
                if buscar_por_codigo(registros_petshop, cod_pet):
                    print("Aviso: Já existe um registro com esse código.")
                    continue

                nome_pet = input("Nome do Pet: ")
                especie = input("Espécie (ex: Cachorro, Gato): ")
                raca = input("Raça: ")
                peso = ler_float("Peso (kg): ")

                novo_pet = Pet(cod_pet, nome_pet, especie, raca, peso)
                tutor.adicionar_pet(novo_pet)
                registros_petshop.append(novo_pet)
                print("Pet cadastrado e vinculado ao cliente com sucesso!")
            except ValueError as erro:
                print(f"Não foi possível cadastrar o pet: {erro}")

        elif opcao == 3:
            if not registros_petshop:
                print("Nenhum registro cadastrado no sistema.")
            else:
                print("\n--- LISTAGEM GERAL (POLIMORFISMO) ---")
                # Percorre a lista heterogênea chamando o mesmo método em classes diferentes
                for item in registros_petshop:
                    print(item.exibir_ficha())

        elif opcao == 4:
            cod = ler_inteiro("Digite o código para busca: ")
            encontrado = buscar_por_codigo(registros_petshop, cod)
            if encontrado:
                print("Registro encontrado:")
                print(encontrado.exibir_ficha())
            else:
                print("Nenhum registro encontrado com este código.")

        elif opcao == 5:
            cod = ler_inteiro("Digite o código para remover: ")
            encontrado = buscar_por_codigo(registros_petshop, cod)
            if encontrado:
                registros_petshop.remove(encontrado)
                print("Registro removido com sucesso!")
            else:
                print("Registro não encontrado para remoção.")

        elif opcao == 0:
            print("Encerrando o sistema do PetShop...")
            break

        else:
            print("Opção inválida! Escolha um número entre 0 e 5.")


if __name__ == "__main__":
    menu()