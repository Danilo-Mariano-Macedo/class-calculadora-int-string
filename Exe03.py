# Crie uma classe chamada "Calculadora" com um método "somar" que pode somar dois números inteiros ou duas
# strings. Use o polimorfismo para implementar a sobrecarga do método "somar" para que ele funcione
# com diferentes tipos de entrada (números inteiros e strings). Crie exemplos de uso para demonstrar como a
# mesma função pode se comportar de maneira diferente com base nos tipos de entrada.

class Calculadora:
    def somar(self, a, b):
        # Verifica se a e b são inteiros
        if type(a) == int and type(b) == int:
            return a + b
        # Verifica se a e b são strings
        elif type(a) == str and type(b) == str:
            return a + b
        # Se os tipos forem diferentes, aparece a mensagem de erro
        else:
            return f'Erro! Os tipos de entrada são diferentes'
        
# Uso da classe
calcular = Calculadora()

# Somas de tipos int
soma_inteiro = calcular.somar(4, 6)
print('Soma dos inteiros é:', soma_inteiro)

# Soma de tipos str
soma_string = calcular.somar('Beba ', 'moderadamente' )
print('Soma das stings é:', soma_string)

# Somas de tipos diferentes
soma_inteiro = calcular.somar(2, '4')
print('Soma dos inteiros é:', soma_inteiro)

# Soma de tipos str
soma_string = calcular.somar('Mais ', 1)
print('Soma das stings é:', soma_string)