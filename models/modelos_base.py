
class CadastroBase:
    """Superclasse que agrupa atributos e validações comuns do PetShop."""

    def __init__(self, codigo: int, nome: str):
        self.__codigo = None
        self.__nome = None
        # Redireciona o construtor para os setters validados
        self.set_codigo(codigo)
        self.set_nome(nome)

    # --- GETTERS ---
    def get_codigo(self) -> int:
        return self.__codigo

    def get_nome(self) -> str:
        return self.__nome

    # --- SETTERS COM REGRAS DE NEGÓCIO ---
    def set_codigo(self, codigo: int):
        if isinstance(codigo, int) and codigo > 0:
            self.__codigo = codigo
        else:
            raise ValueError("O código deve ser um número inteiro maior que zero.")

    def set_nome(self, nome: str):
        if isinstance(nome, str) and len(nome.strip()) >= 2:
            self.__nome = nome.strip()
        else:
            raise ValueError("O nome deve conter pelo menos 2 caracteres válidos.")

    # Método que será sobrescrito nas subclasses (Polimorfismo)
    def exibir_ficha(self) -> str:
        return f"[{self.__codigo}] {self.__nome}"