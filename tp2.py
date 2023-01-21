html = """
<style>
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
            text-align: center;
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
    "AC", "AD", "AH", "AS",             # 00, 01, 02, 03
    "2C", "2D", "2H", "2S",             # 04, 05, 06, 07
    "3C", "3D", "3H", "3S",             # 08, 09, 10, 11
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
        balise += '<td id="C' + str(i) + '"></td>'
    
    return balise


def pointsRang(index):
    return '<td id="R' + str(index) + '"></td></tr>'


def pointsTot():
    return '<td id="T"></td>'


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


def randomCardDEBUG():
    cards = [7, 9, 13, 17, 12]
    
    i= math.floor(random() * 5)
    return cards[i]


def drawCard(clic, case):
    if clic.id == 25 and clic.card == 53:
        card = randomCard()
        #card = randomCardDEBUG()
        c = 0
        
        while c < 25:
            if card == game[c].card:
                card = randomCard()
                #card = randomCardDEBUG()
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
    memeVal = []
    for i in range(len(hand)):
        for j in range(len(hand)):
            same = i == j
            empty = hand[i] == 52 or hand[j] == 52
            sameValue = not same and not empty and hand[i] // 4 == hand[j] // 4
            
            seenFirst = hand[i] in memeVal
            seenSecond = hand[j] in memeVal
            
            if sameValue:
                if not seenFirst: memeVal.append(hand[i])
                if not seenSecond: memeVal.append(hand[j])
                
    return memeVal
        


def memeCouleur(hand):
    memeCoul = []
    for i in range(len(hand)):
        for j in range(len(hand)):
            same = i == j
            empty = hand[i] == 52 or hand[j] == 52
            sameColor = not same and not empty and hand[i] % 4 == hand[j] % 4
                      
            seenFirst = hand[i] in memeCoul
            seenSecond = hand[j] in memeCoul
            
            if sameColor:
                if not seenFirst: memeCoul.append(hand[i])
                if not seenSecond: memeCoul.append(hand[j])
    
    return memeCoul


def memeSerie(hand):
    memeSer= []
    for i in range(len(hand)):
        for j in range(len(hand)):
            if j-1 >= 0 and hand[j] // 4 ==  hand[j-1] // 4: continue
            same = i == j
            empty = hand[i] == 52 or hand[j] == 52
            
            suite = (hand[i] // 4) + 1 == hand[j] // 4
            serie = not same and not empty and suite
            
            # Cas As à la fin
            if hand[0] in range(4):
                r = 1 < len(hand)
                ten = hand[1] if r and hand[1] in range(36, 40) else 0
                r = 2 < len(hand)
                valet = hand[2] if r and hand[2] in range(40, 44) else 0
                r = 3 < len(hand)
                queen = hand[3] if r and hand[3] in range(44, 48) else 0
                r = 4 < len(hand)
                king =  hand[4] if r and hand[4] in range(48, 52) else 0
                
                if ten and valet and queen and king:
                    royal = True
                    return [hand[0], ten, valet, queen, king], royal
            
            seenFirst = hand[i] in memeSer
            seenSecond = hand[j] in memeSer
            
            if serie:
                if not seenFirst: memeSer.append(hand[i])
                if not seenSecond: memeSer.append(hand[j])
    
    royal = False
    return memeSer, royal


def getMemeValPoints(hand):
    memeVal = memeValeur(hand)
    nMemeVal = len(memeVal)
        
    if nMemeVal == 2:
        return 2               # Paire
    elif nMemeVal == 3:
        return 10              # Brelan
    elif nMemeVal == 4:
        memeVal.pop()
        memeVal = memeValeur(memeVal)
        
        if len(memeVal) != 2:
            return 50          # Carré
        else:
            return 5           # Double Paire
            
    elif nMemeVal == 5:
        return 25              # Full House
    else:
        return 0


def getMemeCoulPoints(hand):
    memeCoul = memeCouleur(hand)
    nMemeCoul = len(memeCoul)
    couleur = False
    
    if nMemeCoul == 5:        
        memeCoul.pop()
        memeCoul = memeCouleur(memeCoul)
        
        if len(memeCoul) == 4:
            memeCoul.pop()
            memeCoul = memeCouleur(memeCoul)
            
            if len(memeCoul) == 3:
                couleur = True
              
    points = 20 if couleur else 0
    
    return points
        

def getMemeSerPoints(hand, pointsMemeCoul):
    serie = memeSerie(hand)
    memeSer = serie[0]
    royal = serie[1]
    nMemeSer = len(memeSer)
    points = 0
    serie = False
    
    if royal:
        points = 100 if pointsMemeCoul == 20 else 0
    
    if nMemeSer == 5:
        memeSer.pop()
        memeSer = memeSerie(memeSer)[0]

        if len(memeSer) == 4:
            memeSer.pop()
            memeSer = memeSerie(memeSer)[0]
            if len(memeSer) == 3:
                serie = True
        
    if serie:
        points = 75 if pointsMemeCoul == 20 else 15

    return points


def updatePoints(position, direction, points, total):
    if not direction: pointsHTML = document.querySelector('#R' + str(position))
    else: pointsHTML = document.querySelector('#C' + str(position))
    totalHTML = document.querySelector('#T')
    
    pointsHTML.innerHTML = str(points) if points else ''
    totalHTML.innerHTML = str(total) if total else ''



def points(hand):
    jeu = game.copy()
    
    total = 0
    for i in range(5):
        for j in range(2):
            hand = sortHand(getHand(jeu, i, j))
            
            pValeur = getMemeValPoints(hand)
            pCouleur = getMemeCoulPoints(hand)
            pSerie = getMemeSerPoints(hand, pCouleur)
            
            pCouleur = 0 if pSerie == 100 else pCouleur
            pCouleur = 0 if pSerie == 75 else pCouleur
            pSerie = 0 if pValeur == 50 else pSerie
            pSerie = 0 if pValeur == 25 else pSerie
            
            points = pValeur + pCouleur + pSerie
            
            total += points
            
            updatePoints(i, j, points, total)    
    
        
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
    

    
def init():
    
    global game
    
    main = document.querySelector('#main')
    
    main.innerHTML = html + creerTable(5)
    
    game = makeGame()


init()