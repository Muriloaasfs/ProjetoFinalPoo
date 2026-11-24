from models.modelos_base import CadastroBase


class Pet(CadastroBase):
    """Subclasse 1: Representa o animal atendido no PetShop."""

    def __init__(self, codigo: int, nome: str, especie: str, raca: str, peso: float):
        super().__init__(codigo, nome)
        self.__especie = None
        self.__raca = None
        self.__peso = None
        self.set_especie(especie)
        self.set_raca(raca)
        self.set_peso(peso)

    def get_especie(self) -> str:
        return self.__especie

    def get_raca(self) -> str:
        return self.__raca

    def get_peso(self) -> float:
        return self.__peso

    def set_especie(self, especie: str):
        if especie and len(especie.strip()) >= 2:
            self.__especie = especie.strip()
        else:
            raise ValueError("Espécie inválida.")

    def set_raca(self, raca: str):
        self.__raca = raca.strip() if raca else "SRD"

    def set_peso(self, peso: float):
        if peso > 0:
            self.__peso = float(peso)
        else:
            raise ValueError("O peso do pet deve ser maior que zero.")

    # Sobrescrita de método (Polimorfismo)
    def exibir_ficha(self) -> str:
        return (
            f"PET | Cód: {self.get_codigo()} | Nome: {self.get_nome()} | "
            f"Espécie: {self.__especie} ({self.__raca}) | Peso: {self.__peso:.2f} kg"
        )


class Cliente(CadastroBase):
    """Subclasse 2: Representa o tutor responsável pelos pets."""

    def __init__(self, codigo: int, nome: str, telefone: str):
        super().__init__(codigo, nome)
        self.__telefone = None
        self.set_telefone(telefone)
        # Cardinalidade 1..* (Um cliente pode ter vários pets)
        self.pets = []

    def get_telefone(self) -> str:
        return self.__telefone

    def set_telefone(self, telefone: str):
        if telefone and len(telefone.strip()) >= 8:
            self.__telefone = telefone.strip()
        else:
            raise ValueError("Telefone inválido. Informe ao menos 8 dígitos.")

    def adicionar_pet(self, pet: Pet):
        self.pets.append(pet)

    # Sobrescrita de método (Polimorfismo)
    def exibir_ficha(self) -> str:
        nomes_pets = ", ".join([p.get_nome() for p in self.pets]) if self.pets else "Nenhum pet vinculado"
        return (
            f"CLIENTE | Cód: {self.get_codigo()} | Nome: {self.get_nome()} | "
            f"Tel: {self.__telefone} | Pets: [{nomes_pets}]"
        )