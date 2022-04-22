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
    "AC", "AD", "AH", "AS",             # 0, 1, 2, 3
    "2C", "2D", "2H", "2S",             # 4, 5, 6, 7
    "3C", "3D", "3H", "3S",             # 8, 9, 10, 11
    "4C", "4D", "4H", "4S",             # 12, 13, 14, 15
    "5C", "5D", "5H", "5S",             # 16, 17, 18, 19
    "6C", "6D", "6H", "6S",             # 20, 21, 22, 23
    "7C", "7D", "7H", "7S",             # 24, 25, 26, 27
    "8C", "8D", "8H", "8S",             # 28, 29, 30, 31
    "9C", "9D", "9H", "9S",             # 32, 33, 34, 35
    "10C", "10D", "10H", "10S",         # 36, 37, 38, 39
    "JC", "JD", "JH", "JS",             # 40, 41, 42, 43
    "QC", "QD", "QH", "QS",             # 44, 45, 46, 47
    "KC", "KD", "KH", "KS",             # 48, 49, 50, 51
    "empty", "back"]                    # 52, 53      


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


def steps(i, direction):
    if direction == 0:
        start= i * 5
        end= start + 5
        step= 1
    else:
        start = i
        end = i + 21
        step = 5
    
    return (start, end, step)


def getHand(game, n, direction):
    
    jeu = game.copy()
    s = steps(n, direction)
    
    hand = []
    for i in range(s[0], s[1], s[2]):
        hand.append(jeu[i].card)
    
    return hand


def sortHand(hand):
    sort = hand.copy()
    
    for i in range(1, len(sort)):
        
        card = sort[i]
        
        j = i-1
        
        while j >= 0 and card < sort[j]:
            sort[j + 1] = sort[j]
            j -= 1
        sort[j + 1] = card
    
    return sort


def memeValeur(hand):
    c= 0
    
    for i in range(len(hand)):
        empty = hand[i] == 52
        same3 = False
        same2 = False
        
        if i + 2 < len(hand):
            same3 = hand[i+1] // 4 == hand[i+2] // 4
        if i + 1 < len(hand):
            same2 = hand[i] // 4 == hand[i+1] // 4
        
        if not empty and same2:
            c+= 1 if same3 else 2
    
    return c


def memeCouleur(hand):
    c= 0
    
    for i in range(len(hand)):
        empty = hand[i] == 52
        same3 = False
        same2 = False
        
        if i + 1 < len(hand) and hand[i+1] != 52:
            breakpoint()
            same2 = hand[i] % 4 == hand[i+1] % 4
        if i + 2 < len(hand) and hand[i+2] != 52:
            breakpoint()
            same3 = hand[i+1] % 4 == hand[i+2] % 4
        
        if not empty and same2:
            c+= 1 if same3 else 2
    
    return c

def points(hand):
    jeu = game.copy()
    
    for i in range(5):
        horizontalHand = sortHand(getHand(jeu, i, 0))
        verticalHand = sortHand(getHand(jeu, i, 1))
        
        nbMemeValeur = memeValeur(horizontalHand)
        nbMemeCouleur = memeCouleur(horizontalHand)
        
        #print(nbMemeValeur)

        
def mettrejeuAJour(game):
    jeu = game.copy()
    c=0
    for i in range(25):
        if jeu[i].card != 52:
            c+=1
    if c == 25:
        alert( " vous avez fini ")
        init()


def clic(id):
    
    clic = game[id]
    case = getCase(clic.id)
    
    selection(clic)
    
    drawCard(clic, case)
    
    placeCard(clic, case)
        
    highlight(clic, case)
    
    points(game)
    
    mettrejeuAJour(game)
    
    print('\n=======================')
    

    
def init():
    
    global game
    
    main = document.querySelector('#main')
    
    main.innerHTML = html + creerTable(5)
    
    game = makeGame()


init()