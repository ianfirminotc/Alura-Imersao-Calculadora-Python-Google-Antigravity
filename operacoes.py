"""
Módulo de Operações Matemáticas
Contém as funções puras de cálculo utilizadas pela Calculadora.
"""

def somar(a: float, b: float) -> float:
    """Retorna a soma de a e b."""
    return a + b

def subtrair(a: float, b: float) -> float:
    """Retorna a subtração de b em relação a a."""
    return a - b

def multiplicar(a: float, b: float) -> float:
    """Retorna o produto de a e b."""
    return a * b

def dividir(a: float, b: float):
    """
    Retorna a divisão de a por b.
    Retorna uma mensagem de erro caso o divisor seja zero.
    """
    if b == 0:
        return "Erro: Não é possível dividir por zero!"
    return a / b

def porcentagem(a: float, b: float) -> float:
    """
    Calcula b por cento de a.
    Exemplo: porcentagem(200, 15) -> 30.0 (15% de 200).
    """
    return (a * b) / 100
