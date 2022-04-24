# 2022-04-24 
                                     #TP2#


# ilyas ....
# tarek mekki daouadji 20174482



                         ### JEU DE POKER SHUFFLE ###



html = """
<style>                                       # le style du tableau
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
                                            # on cree un tableau cinq par cinq pour mettre nos carte 
    <table>
        <tr>
            <td><button onclick="init();">Nouvelle partie</button></td>
            <td></td>
            <td id="case25" onclick="clic(25);"><img src="http://codeboot.org/cards/back.svg"></td>
            <td></td>
        </tr>
    </table>
"""
#___________________________________________________________________________# 
                    # tous les cartes du jeu
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
#___________________________________________________________________________# 
# La fonction makeGame ne prend pas de paramettre
# et retourne une structure qui contien l'id, si elle est selectionne 
# et le nombre de carte

def makeGame():
    game = []
    for i in range(26):
        game.append(struct(id=i, selected=False, card=52))
    game[-1].card=53
    return game
#___________________________________________________________________________# 
# La fonction img prend un entier comme paramettre (num)
# et retourne limage des carte 

def img(num):
    return '<img src="http://codeboot.org/cards/' + cartes[num] + '.svg">'

#___________________________________________________________________________# 
# La fonction emptyCase prend un entier comme paramettre (num)
# et retourne le tableau qui contien des cartes vide

def emptyCase(num):
    case = '<td id="case' + str(num) + '" onclick="clic('
    case += str(num) + ')">' + img(52) + '</td>'
    
    return case
#___________________________________________________________________________# 
# La fonction pointsCol prend un entier comme paramettre (dimension)
# et retourne les points des images de la colonne

def pointsCol(dimension):
    balise = ''
    for i in range(dimension):
        balise += '<td id="C' + str(i) + '">20</td>'
    
    return balise
#___________________________________________________________________________# 
# La fonction pointsRang prend un entier comme paramettre (index)
# et retourne les points des images de la range

def pointsRang(index):
    return '<td id="R' + str(index) + '">20</td></tr>'
#___________________________________________________________________________# 
# La fonction pointsTot ne prend pas de paramettre et retourne le nombre totale
# de points a cumuler des ligne et colonne du tableau

def pointsTot():
    return '<td id="T">999</td>'
#___________________________________________________________________________# 

# La fonction tableauPoints prend un entier comme paramettre (dimension)
# et retourne ne nombre de points dans une colone

def tableauPoints(dimension):
    return '<tr>' + pointsCol(dimension) + pointsTot() + '</tr>'
#___________________________________________________________________________# 
# La fonction rangees prend un entier comme paramettre (dimension)
# et retourne ne nombre de points dans la range

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
#___________________________________________________________________________# 
# La fonction tableauCartes prend un entier comme paramettre (dimension)
# et retourne les points de la rangees plus du tableau de points

def tableauCartes(dimesion):
    balise = rangees(dimesion) + tableauPoints(dimesion)
    
    return balise
#___________________________________________________________________________# 
# La fonction creerTable prend un entier comme paramettre (dimension)
# et retourne un tableau de carte

def creerTable(dimension):
    return '<table>' + tableauCartes(dimension) + '</table>'
#___________________________________________________________________________# 
# La fonction getCase prend un entier comme paramettre (id)
# et retourne ca casse avec son id

def getCase(id):
    return document.querySelector('#case' + str(id))
#___________________________________________________________________________# 
# La fonction randomCard ne prend pas de paramettre et retourne un chiffre
# entre 1 et 51 pour melege le deck

def randomCard():
    return math.floor(random() * 52)
#___________________________________________________________________________# 
# La fonction drawCard prend deux paramettre (clic) qui est la carte 
# puis (case) qui est l'id et sont tout les deux des entier

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
#___________________________________________________________________________# 
# La fonction selection prend un entier comme paramettre (clic)
# qui montre si la carte est selectionne ou pas

def selection(clic):
    if clic.card != 52:
        clic.selected = False if clic.selected else True
#___________________________________________________________________________# 
# La fonction bgLime prend un paramettre (case) et qui change de couleurs
# si on selectionne la carte en vert


def bgLime(case):
    case.setAttribute('style', 'background-color: lime')
#___________________________________________________________________________#     
# La fonction bgTransparent prend un paramettre (case) et qui remets la couleur
# dorigine de la carte une fois deselectionne


def bgTransparent(case):
    case.setAttribute('style', 'background-color: none')
#___________________________________________________________________________#     
# La fonction highlight prend deux paramettre (clic) et (case) et qui fait
# en sort le change la couleurs de la carte une fois qu'on clic

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
#___________________________________________________________________________# 
# La fonction placeCard prend deux paramettre (clic) et (case) et qui fait
# en sort de mettre la carte dans le tableau et de change la position
# de deux carte dans le tableau

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
#___________________________________________________________________________# 
# La fonction steps prend deux paramettre (i) et (direction) et qui returne
# le debut, la fin et les pas des lignes et colones du tableau
 
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
#___________________________________________________________________________# 
# La fonction getHand prend trois paramettre (game), (n) et (direction) 
# et qui retourne un tableau qui contien une ligne ou une colonne de carte 
# qui est hand

def getHand(game, n, direction):
    
    jeu = game.copy()
    s = steps(n, direction)
    
    hand = []
    for i in range(s[0], s[1], s[2]):
        hand.append(jeu[i].card)
    
    return hand
#___________________________________________________________________________# 
# La fonction sortHand prend un paramettre (hand) et qui retourne
# le tableau(hand) trier en ordre

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
#___________________________________________________________________________# 
# La fonction memeValeur prend un paramettre (hand) et qui retourne
# un entier si deux carte ou plus on la meme valeurs

def memeValeur(hand):
    c= 0
    
    for i in range(len(hand)):
        empty = hand[i] == 52
        same3 = False
        same2 = False
        
        if i + 1 < len(hand):
            same2 = hand[i] // 4 == hand[i+1] // 4
        if i + 2 < len(hand):
            same3 = hand[i+1] // 4 == hand[i+2] // 4
        
        if not empty and same2:
            c+= 1 if same3 else 2
    
    return c
#___________________________________________________________________________# 
# La fonction memeCouleur prend un paramettre (hand) et qui retourne
# un entier si les 5 cartes sont de la meme couleurs

def memeCouleur(hand):
    explored = []
    for i in range(len(hand)):
        for j in range(len(hand)):
            same = i == j
            empty = hand[i] == 52 or hand[j] == 52
            sameColor = not same and not empty and hand[i] % 4 == hand[j] % 4
            
            seenFirst = hand[i] in explored
            seenSecond = hand[j] in explored
            seen = seenFirst and seenSecond
            
            if sameColor and not seen:
                if not seenFirst: explored.append(hand[i])
                if not seenSecond: explored.append(hand[j])
    
    nbSameColor = len(explored)
            
    return nbSameColor
#___________________________________________________________________________# 
# La fonction memeSerie prend un paramettre (hand) et qui retourne
# un entier si on a une suite de carte

def memeSerie(hand):
    explored= []
    for i in range(len(hand)):
        for j in range(len(hand)):
            same = i == j
            empty = hand[i] == 52 or hand[j] == 52
            #breakpoint()
            suite = (hand[i] // 4) + 1 == hand[j] // 4
            serie = not same and not empty and suite
            
            seenFirst = hand[i] in explored
            seenSecond = hand[j] in explored
            seen = seenFirst and seenSecond
            
            if serie and not seen:
                if not seenFirst: explored.append(hand[i])
                if not seenSecond: explored.append(hand[j])
            
    nbSerie = len(explored)
    
    return nbSerie
#___________________________________________________________________________# 
# La fonction flushRoyal prend un paramettre (hand) et qui retourne
# un entier si on a un as, 10 , J, Q ,K dans la main avec 5 meme couleurs

def flushRoyal(hand):
    explored= []
    for i in range(len(hand)):
        for j in range(len(hand)):
            same = i == j
            empty = hand[i] == 52 or hand[j] == 52
            
            suite =  hand[i] + 1 == hand[j]== (0 or 1 or 2 or 3) and  (36 or 37 or 38 or 39) and (40 or 41 or 42 or 43) and (44 or 45 or 46 or 47) and (48 or 49 or 50 or 51)
            # ca marche pas ici je voulais faire que la carte 1 c'est l'as, 2 c'est le 10, 3 c'est le J, 4 c'est la queen puis la 5 le king 
            # puis on dois aussi mettre la meme couleurs 
            
            """
            (hand[1] == 0 or 1 or 2 or 3) and
            (hand[2] == 36 or 37 or 38 or 39) and
            (hand[3] == 40 or 41 or 42 or 43) and 
            (hand[4] == 44 or 45 or 46 or 47)and 
            (hand[5] == 48 or 49 or 50 or 51)
            """
            serie = not same and not empty and suite
            
            seenFirst = hand[i] in explored
            seenSecond = hand[j] in explored
            seen = seenFirst and seenSecond
            
            if serie and not seen:
                if not seenFirst: explored.append(hand[i])
                if not seenSecond: explored.append(hand[j])
            
    flush = len(explored)
    
    return flush

#___________________________________________________________________________# 
# La fonction points prend un paramettre (hand) et qui calcule une colonne
# et une ligne du jeu

def points(hand):
    jeu = game.copy()
    
    for i in range(5):
        horizontalHand = sortHand(getHand(jeu, i, 0))
        verticalHand = sortHand(getHand(jeu, i, 1))
        
        nbMemeValeurHorizontal = memeValeur(horizontalHand)
        nbMemeValeurVertical = memeValeur(verticalHand)
        
        nbMemeCouleurHorizontal = memeCouleur(horizontalHand)
        nbMemeCouleurVertical = memeCouleur(verticalHand)
        
        nbMemeSerieHorizontal = memeSerie(horizontalHand)
        nbMemeSerieVertical = memeSerie(verticalHand)
        
        flushRoyalHorizontal = flushRoyal(horizontalHand)
        flushRoyalVertical = flushRoyal(verticalHand)
        
        
        print(flushRoyalHorizontal)
        
    print('==========================')
#___________________________________________________________________________#     
# La fonction mettrejeuAJour un paramettre (game) et qui relance le jeu 
# une fois la partie termine quand le tableau est rempli
       
def mettrejeuAJour(game):
    jeu = game.copy()
    c=0
    for i in range(25):
        if jeu[i].card != 52:
            c+=1
    if c == 25:
        alert( " vous avez fini ")
        init()
        
#___________________________________________________________________________#         
# La fonction clic un paramettre (id) et qui enrengiste les donnes lors
# d'un clic
  

def clic(id):
    
    clic = game[id]
    case = getCase(clic.id)
    
    selection(clic)
    
    drawCard(clic, case)
    
    placeCard(clic, case)
        
    highlight(clic, case)
    
    points(game)
    
    mettrejeuAJour(game)
    
#___________________________________________________________________________#    
# La fonction init ne prend pas de paramettre et c'est elle qui lance le jeu
    
def init():
    
    global game
    
    main = document.querySelector('#main')
    
    main.innerHTML = html + creerTable(5)
    
    game = makeGame()


init()
#___________________________________________________________________________#
#___________________________________________________________________________#
"""
def test ():#test unitaires
    assert makeGame()
    assert img(num)
    assert emptyCase(num)
    assert pointsCol(dimension)
    assert pointsRang(index)
    assert pointsTot()
    assert tableauPoints(dimension)
    assert rangees(dimension)
    assert tableauCartes(dimesion)
    assert creerTable(dimension)
    assert getCase(id)
    assert randomCard()
    assert drawCard(clic, case)
    assert selection(clic)
    assert bgLime(case)
    assert bgTransparent(case)
    assert highlight(clic, case)
    assert placeCard(clic, case)
    assert steps(i, direction)
    assert getHand(game, n, direction)
    assert sortHand(hand)
    assert memeValeur(hand)
    assert memeCouleur(hand)
    assert memeSerie(hand)
    assert flushRoyal(hand)
    assert points(hand)
    assert mettrejeuAJour(game)
    assert clic(id)
    assert init()

#test()
"""