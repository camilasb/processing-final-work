add_library('pdf')
salvar_pdf = False

firstPress = 0 #variavel que guarda se o mouse foi pressionado a primeira vez
linhas = [] #lista de valores (vazio)
barckgroundColor = 255

def setup():
    size(1000, 1000) #tamanho do board
    sorteio(5) #método que vai sortear onde as bolinhas vão ser plotadas
    x = 1 #coordenada X (para o primeiro ponto da linha)
    y = 1 #coordenada Y (para o primeiro ponto da linha)
    x0 = 1 #coordenada X (para o segundo ponto da linha)
    y0 = 1 #coordenada Y (para o segundo ponto da linha)

def sorteio(n): #método de sorteio onde vão ser plotadas as bolinhas
    global pontos
    pontos = [] #lista dos pontos a serem plotados
    for i in range(n): #loop que vai plotar as bolinhas
        margem = 50 #margem do board para que as bolinhas fiquem dentro dele
        x = random(margem, width - margem)
        y = random(margem, height - margem)
        pontos.append((x, y)) #colocar um valor dentro da lista de pontos
        
def draw():
    background (barckgroundColor) #limpa o background para que a linha plotada nao deixe rastro
    global salvar_pdf
    if salvar_pdf : #salvar_pdf == True
        beginRecord(PDF, "arquiv.pdf")
        
    for x, y in pontos:
        circle(x, y, 7) #plota as bolinhas
        fill(0, 0, 0) #coloca preenchimento preto nas bolinhas
       
    if firstPress == 1: #quando o mouse for pressionado a primeira vez
        line(x0, y0, mouseX, mouseY) #desenha uma linha

    for x1, y1, x2, y2 in linhas: #guarda as linhas que foram desenhadas na tela
        line(x1, y1, x2, y2) 
    
    if salvar_pdf:
        endRecord()
        salvar_pdf = False


def mousePressed(): 
    global firstPress, x0, y0

    if firstPress == 0: #se o mouse nao tiver sido pressionado pela primeira vez
        for x, y in pontos:
            if dist(x, y, mouseX, mouseY) < 10: #veja a distancia entre a proxima bolinha
                                                #para que nao seja possivel desenhar uma 
                                                #linha fora da bolinha
                firstPress = 1
                x0, y0 = x, y
                return

    if firstPress == 1: #mesma coisa de cima
        for x, y in pontos: 
            if dist(x, y, mouseX, mouseY) < 10:
                firstPress = 0
                linhas.append((x0, y0, x, y)) #colocar um valor dentro da lista de linhas

def keyPressed(): 
    
    if key == " ": #se o espaço for pressionado, novas bolinhas vao aparecer
        global barckgroundColor
        barckgroundColor = andom(256), random(256), random(256)
        background (barckgroundColor)
        print(barckgroundColor)
        sorteio(5)
        
    if key == DELETE: #se o delete for pressionado, as linhas anteriores irao ser deletadas
        linhas [:] = []
        #global linhas
        #linhas = []
    
    if key == 'p':
        salvar_pdf = True
