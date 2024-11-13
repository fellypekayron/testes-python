# 1) Criar a classe 
# chamada "Calculadora"
class Calculadora:
    
    # 2) Criar um método
    # chamado "soma()"
    def soma(self, n1, n2):
        return n1 + n2
    
    # 3) Criar um método
    # chamado "subtração()"
    def subtracao(self, n1, n2):
        return n1 - n2
    
    # 4) Criar um método
    # chamado "multiplicação()"
    def multiplicacao(self, n1, n2):
        return n1 * n2
    
    # 5) Criar um método
    # chamado "diviisao()"
    def divisao(self, n1, n2):
        if n2 == 0:
            return "Divisão inválida"
        else: 
            return n1 / n2
       

