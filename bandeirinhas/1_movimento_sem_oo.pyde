"""
Exemplo de movimentação de uma figura poligonal, ainda sem orientação a objetos
"""

def setup():
    """ Código de configuração, executado no início pelo Processing """
    global x, y
    size(100, 100)  # área de desenho
    x, y = width / 2, height / 2   # coordenadas do meio da área de desenho

def draw():
    """ Laço principal de repetição do Processing """
    global x, y
    background(0)  # atualização do desenho, fundo preto
    bandeirinha(x, y)  # desenha o polígono
    x += 1
    y += 1
    if x > width + 25:
        x = -25
    if y > height + 25:
        y = -25

def bandeirinha(px, py, tamanho=50):
    """ Desenha polígono em torno das coordenadas passadas, com tamanho padrão 50 """
    metade = tamanho / 2
    with pushMatrix():   # preseservando o sistema de coordenadas anterior
        translate(px, py)  # translada o sistema de coordenadas
        beginShape()  # inicia polígono
        vertex(-metade, -metade)
        vertex(-metade, metade)
        vertex(0, 0)
        vertex(metade, metade)
        vertex(metade, -metade)
        endShape(CLOSE)  # encerra polígono, fechando no primeiro vértice
