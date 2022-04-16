html = """
<style>
        #main {
            padding: 1%;
        }
        #main table td {
            border: 0;
            padding: 1px 2px;
        }
        #main table td img {
            height: auto;
        }
        #main table td {
            width: 70px;
            height: 98px;
            text-align:
            center;
            font-size: 24px;
        }
        #main table td button {
            float: left;
            font-size: 14px;
            padding: 8%;
        }
    </style>
    <table>
        <tr>
            <td><button onclick="init();">Nouvelle partie</button></td>
            <td></td>
            <td id="case25" onclick="clic(25);"><img src="http://codeboot.org/cards/back.svg"></td>
            <td></td>
        </tr>
    </table>
"""

cartes = [
    "AC", "AD", "AH", "AS",
    "2C", "2D", "2H", "2S",
    "3C", "3D", "3H", "3S",
    "4C", "4D", "4H", "4S",
    "5C", "5D", "5H", "5S",
    "6C", "6D", "6H", "6S",
    "7C", "7D", "7H", "7S",
    "8C", "8D", "8H", "8S",
    "9C", "9D", "9H", "9S",
    "10C", "10D", "10H", "10S",
    "JC", "JD", "JH", "JS",
    "QC", "QD", "QH", "QS",
    "KC", "KD", "KH", "KS",
    "empty", "back"]                


def makeGame():
    game = []
    for i in range(26):
        game.append(struct(id=i, selected=False, card=52))
    game[-1].card=53
    return game


def img(num):
    return '<img src="http://codeboot.org/cards/' + cartes[num] + '.svg">'


def emptyCase(num):
    case = '<td id="case' + str(num) + '" onclick="clic('
    case += str(num) + ')">' + img(52) + '</td>'
    
    return case


def pointsCol(dimension):
    balise = ''
    for i in range(dimension):
        balise += '<td id="C' + str(i) + '">20</td>'
    
    return balise


def pointsRang(index):
    return '<td id="R' + str(index) + '">20</td></tr>'


def pointsTot():
    return '<td id="T">999</td>'


def tableauPoints(dimension):
    return '<tr>' + pointsCol(dimension) + pointsTot() + '</tr>'


def rangees(dimension):
    balise = ''
    c = 0
    for i in range(dimension):
        balise += '<tr>'
        for j in range(dimension):
            balise += emptyCase(c)
            c += 1
        balise += pointsRang(i)
    
    return balise


def tableauCartes(dimesion):
    balise = rangees(dimesion) + tableauPoints(dimesion)
    
    return balise


def creerTable(dimension):
    return '<table>' + tableauCartes(dimension) + '</table>'


def getCase(id):
    return document.querySelector('#case' + str(id))


def randomCard():
    return math.floor(random() * 52)


def drawCard(clic, case):
    if clic.id == 25 and clic.card == 53:
        card = randomCard()
        c = 0
        
        while c < 25:
            if card == game[c].card:
                card = randomCard()
                c = 0
            else:
                c +=1
                
        clic.card = card
        case.innerHTML = img(card)


def selection(clic):
    if clic.card != 52:
        clic.selected = False if clic.selected else True


def bgLime(case):
    case.setAttribute('style', 'background-color: lime')
    

def bgTransparent(case):
    case.setAttribute('style', 'background-color: none')
    

def highlight(clic, case):
    if clic.selected:
        # if there is a selected card that is not the clicked card : deselect
        for element in game:
            if element.selected and element != clic:
                selection(element)
                bgTransparent(getCase(element.id))
        bgLime(case)
    else:
        bgTransparent(case)


def placeCard(clic, case):
    deck = game[25]
    deckCase = getCase(deck.id)
    
    if deck.selected and clic.card == 52:        
        selection(deck)
        highlight(deck, deckCase)
        
        clic.card = deck.card
        deck.card = 53
        
        case.innerHTML = deckCase.innerHTML
        deckCase.innerHTML = img(53)
    
    elif not deck.selected and clic.card == 52:
        for element in game:
            if element.selected:
                elemCase = getCase(element.id)
                
                selection(element)
                highlight(element, elemCase)
                
                clic.card = element.card
                element.card = 52
                
                case.innerHTML = elemCase.innerHTML
                elemCase.innerHTML = img(52)
       
      
      
    if not deck.selected and clic.card != 52:
        for element in game:
            if element.selected and element.id != clic.id:
                elemCase = getCase(element.id)
                
                selection(element)
                highlight(element, elemCase)
                
                tempCard = clic.card
                tempHTML = case.innerHTML
                
                clic.card = element.card
                element.card = tempCard
                
                case.innerHTML = elemCase.innerHTML
                elemCase.innerHTML = tempHTML
                
                selection(clic)
                highlight(clic, case)


def steps(direction):
    if direction == 0:
            start = i * 5
            end = start + 4
            steps = 1
        else:
            start = i
            end = start + 21
            steps = 5
            
    return start, end, steps


def trier(game, direction): # tri bulle
    game = game.copy() 
    for i in range(5):
        echange = True
        
        start = direction(direction)[0]
        end = direction(direction)[1]
        steps = direction(direction)[2]
        
        while echange:
            echange = False
            for j in range(start, end):
                if game[j].card > game[j+1].card:
                    temp = game[j]
                    game[j] = game[j+1]
                    game[j+1] = temp
                    echange = True
    return game


def nbMemeValeur(game, direction):
    for i in range(5):        
        start = direction(direction)[0]
        end = direction(direction)[1]
        steps = direction(direction)[2]
        
        c = 0
        for j in range(start, end, steps):
            if game[j].card != 52 and game[j].card // 4 == game[j+steps].card // 4:
                if game[j+steps].card // 4 == game[j + 2 * steps].card // 4:
                    c+=1
                else:
                    c+=2

        print('ligne ' + str(i+1) + ' ' + str(c))
    print('\n=======================')


def clic(id):
    
    clic = game[id]
    case = getCase(clic.id)
    
    selection(clic)
    
    drawCard(clic, case)
    
    placeCard(clic, case)
        
    highlight(clic, case)
    
    sortedGame = trier(game)
    
    nbMemeValeur(sortedGame, 0)
    
    
    
    
def init():
    
    global game
    
    main = document.querySelector('#main')
    
    main.innerHTML = html + creerTable(5)
    
    game = makeGame()


init()