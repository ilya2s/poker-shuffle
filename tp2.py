# 2022-04-24 
                                     #TP2#


# ilyas ....
# tarek mekki daouadji 20174482



                         ### JEU DE POKER SHUFFLE ###


 # on cree un tableau cinq par cinq pour mettre nos carte avec le style donne

html = """
<style>
        #main {
            padding: 0,5%;
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
            <td id="case25" onclick="clic(25);">
            <img src="http://codeboot.org/cards/back.svg"></td>
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

def img(num):#lien de la photo de la carte
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
        balise += '<td id="C' + str(i) + '"></td>'
    
    return balise
#___________________________________________________________________________# 
# La fonction pointsRang prend un entier comme paramettre (index)
# et retourne les points des images de la range

def pointsRang(index):
    return '<td id="R' + str(index) + '"></td></tr>'
#___________________________________________________________________________# 
# La fonction pointsTot ne prend pas de paramettre et retourne le nombre totale
# de points a cumuler des ligne et colonne du tableau

def pointsTot():
    return '<td id="T"></td>'
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
    for i in range(dimension): # ligne vide
        balise += '<tr>'
        for j in range(dimension): # colonne vide
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
# La fonction randomCardDEBUG ne prend pas de paramettre et retourne 
# une main de carte fix

def randomCardDEBUG(): # pour tester les fonctions 
    cards = [7, 9, 13, 17, 12]
    
    i= math.floor(random() * 5)
    return cards[i]
#___________________________________________________________________________# 
# La fonction drawCard prend deux paramettre (clic) qui est la carte 
# puis (case) qui est l'id et sont tout les deux des entier

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
        # si la carte est deja selectionne et on reclick ca la deselectionne
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
    
    if deck.selected and clic.card == 52: # le deck dois etre selectionne     
        selection(deck)                   # et une fois click dans la carte      
        highlight(deck, deckCase)         # on peu la mettre dans le jeux
        
        clic.card = deck.card
        deck.card = 53
        
        case.innerHTML = deckCase.innerHTML
        deckCase.innerHTML = img(53)
    
    elif not deck.selected and clic.card == 52:# si le jeux est vide on peu 
        for element in game:                  # le mettre une carte ou on veux
            if element.selected:
                elemCase = getCase(element.id)
                
                selection(element)
                highlight(element, elemCase)
                
                clic.card = element.card
                element.card = 52
                
                case.innerHTML = elemCase.innerHTML
                elemCase.innerHTML = img(52)
       
      
     # si une carte des selectionne avec une autre carte on switch leurs!!!!
     # position mais pas dans le deck
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
    if direction == 0:# on est dans les ligne
        start= i * 5
        end= start + 5
        step= 1
    else:# on est dans les colonne
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
    for i in range(s[0], s[1], s[2]):# on prends un tableau 
        hand.append(jeu[i].card) 
    
    return hand

#___________________________________________________________________________# 
# La fonction sortHand prend un paramettre (hand) un tableau 
# et qui retourne le tableau trier

def sortHand(hand):
    sort = hand.copy()
    
    for i in range(1, len(sort)):#on trie le tableau par leurs index 
        
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
    memeVal = []
    for i in range(len(hand)):
        for j in range(len(hand)):
            
            # si dans notre main on a que les deux element ou plus sont //4
            # alors ils sont de la meme valeurs
            same = i == j
            empty = hand[i] == 52 or hand[j] == 52
            sameValue = not same and not empty and hand[i] // 4 == hand[j] // 4
            
            seenFirst = hand[i] in memeVal
            seenSecond = hand[j] in memeVal
            
            if sameValue:
                if not seenFirst: memeVal.append(hand[i])
                if not seenSecond: memeVal.append(hand[j])
                
    return memeVal
        

#___________________________________________________________________________# 
# La fonction memeCouleur prend un paramettre (hand) et qui retourne
# un entier si les 5 cartes sont de la meme couleurs

def memeCouleur(hand):
    memeCoul = []
    for i in range(len(hand)):
        for j in range(len(hand)):
            # si dans notre main on a que les deux element ou plus sont %4
            # alors ils sont de la meme couleurs
            same = i == j
            empty = hand[i] == 52 or hand[j] == 52
            sameColor = not same and not empty and hand[i] % 4 == hand[j] % 4
                      
            seenFirst = hand[i] in memeCoul
            seenSecond = hand[j] in memeCoul
            
            if sameColor:
                if not seenFirst: memeCoul.append(hand[i])
                if not seenSecond: memeCoul.append(hand[j])
    
    return memeCoul

#___________________________________________________________________________# 
# La fonction memeSerie prend un paramettre (hand) et qui retourne
# un entier si on a une suite de carte

def memeSerie(hand):
    memeSer= []
    for i in range(len(hand)):
        for j in range(len(hand)):
            # si dans notre main on a que la difference entre nos carte sont
            # de 1 alors on a une serie
            if j-1 >= 0 and hand[j] // 4 ==  hand[j-1] // 4: continue
            same = i == j
            empty = hand[i] == 52 or hand[j] == 52
            
            suite = (hand[i] // 4) + 1 == hand[j] // 4
            serie = not same and not empty and suite
            

            # si dans notre main on a un as, un dix, un valet,une reine,un rois
            # alors c'est une flush
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

#___________________________________________________________________________# 
# La fonction getMemeValPoints prend un paramettre (hand) et qui retourne
# le calcule des points des cartes de la meme valeurs

def getMemeValPoints(hand):
    memeVal = memeValeur(hand)
    nMemeVal = len(memeVal)
        

    if nMemeVal == 2: #si deux carte de la meme valeurs(une Paire)
        return 2      # 2 points          
    elif nMemeVal == 3:#si deux carte de la meme valeurs(un Brelan)
        return 10     # 10 points
    elif nMemeVal == 4:
        memeVal.pop()
        memeVal = memeValeur(memeVal)
        
        if len(memeVal) != 2: #si quatre carte de la meme valeurs (un Carré)         
            return 50   # 50 points
    
        else:              #si on a deux paire (une Double Paire)
            return 5    # 5 points
            
    elif nMemeVal == 5: # si on a une paire et un Berlan (une Full House)
        return 25       # 25 points
    
    else:              # sinon on a rien
        return 0       # 0 points

#___________________________________________________________________________# 
# La fonction getMemeCoulPoints prend un paramettre (hand) et qui retourne
# le calcule des points des cartes de la couleurs

def getMemeCoulPoints(hand):
    memeCoul = memeCouleur(hand)
    nMemeCoul = len(memeCoul)
    couleur = False
    
    if nMemeCoul == 5: # on a 5 carte de la meme couleurs       
        memeCoul.pop()
        memeCoul = memeCouleur(memeCoul)
        
        if len(memeCoul) == 4:# on a 4 carte de la meme couleurs
            memeCoul.pop()
            memeCoul = memeCouleur(memeCoul)
            
            if len(memeCoul) == 3: # on a 3 carte de la meme couleurs
                couleur = True
                
    #si on a 5 carte de la meme couleurs alors +20 points            
    points = 20 if couleur else 0 
    
    return points
        

#___________________________________________________________________________# 
# La fonction getMemeSerPoints prend deux paramettre (hand) et (pointsMemeCoul) 
# et qui retourne le calcule des points des cartes si il y'a une suite
# et si ils sont tous de la meme couleurs 

def getMemeSerPoints(hand, pointsMemeCoul):
    serie = memeSerie(hand)
    memeSer = serie[0]
    royal = serie[1]
    nMemeSer = len(memeSer)
    points = 0
    serie = False
    
    if royal:# si on a une flush royal avec les meme couleurs alors +100 points
        
        points = 100 if pointsMemeCoul == 20 else 0
    
    if nMemeSer == 5:
        memeSer.pop()
        memeSer = memeSerie(memeSer)[0]

        if len(memeSer) == 4:
            memeSer.pop()
            memeSer = memeSerie(memeSer)[0]
            if len(memeSer) == 3:
                serie = True
        
    if serie: # si on a une serie avec de carte avec les couleurs +75 points
        # si ils sont pas de la meme couleurs +15 points
        points = 75 if pointsMemeCoul == 20 else 15

    return points

#___________________________________________________________________________# 
# La fonction updatePoints prend quatre paramettre position, direction, points
# et total et qui mettre la valeurs des points dans le tableau de jeux 

def updatePoints(position, direction, points, total):
    if not direction: pointsHTML = document.querySelector('#R' + str(position))
    else: pointsHTML = document.querySelector('#C' + str(position))
    totalHTML = document.querySelector('#T')
    
    pointsHTML.innerHTML = str(points) if points else ''
    totalHTML.innerHTML = str(total) if total else ''


#___________________________________________________________________________# 
# La fonction points prend un paramettre (hand) 
# et qui fait le calcul des points une fois qu'on a une serie, meme couleurs 
# et meme valeurs puis fait le calcule totale

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
            
            # on calcule le totale des points dans le jeux 
            # quand on a une serie, meme couleurs ou meme valeurs
            
            points = pValeur + pCouleur + pSerie
            
            total += points
            
            updatePoints(i, j, points, total)    
    
        
#___________________________________________________________________________#     
# La fonction mettrejeuAJour un paramettre (game) et qui relance le jeu 
# une fois la partie termine quand le tableau est rempli

def mettrejeuAJour(game):
    jeu = game.copy()
    c=0
    for i in range(25): # on regarde si le tableau est remplis
        if jeu[i].card != 52:
            c+=1
    if c == 25:# impime vous avez fini quand on fini le jeu
        alert( " vous avez fini avec")#ici on mets le nombre totale de points!!!!!!
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

def test ():#test unitaires
    game = makeGame()
    assert game[0]== struct(id=0, selected=False, card=52)
    assert game[-1]!= struct(id=0, selected=False, card=52)
    #assert game[1]== struct(id=0, selected=False, card=52)
    #assert game[25]== struct(id=0, selected=False, card=52)
    #assert game[10] != struct(id=0, selected=False, card=52)
    
    assert img(53) == '<img src="http://codeboot.org/cards/back.svg">'
    assert img(52) == '<img src="http://codeboot.org/cards/empty.svg">'
    assert img(0) == '<img src="http://codeboot.org/cards/AC.svg">'
    assert img(26) == '<img src="http://codeboot.org/cards/7H.svg">'
    assert img(39) == '<img src="http://codeboot.org/cards/10S.svg">'
    
    assert pointsCol(0) == ""
    assert pointsCol(1) =='<td id="C0"></td>'
    assert pointsCol(3)== '<td id="C0"></td><td id="C1"></td><td id="C2"></td>'
    assert pointsCol(-1)== ""
    assert pointsCol(-30)==""
    
    assert pointsRang(1)=='<td id="R1"></td></tr>'
    assert pointsRang(0)=='<td id="R0"></td></tr>'
    assert pointsRang(10)=='<td id="R10"></td></tr>'
    assert pointsRang(-1)=='<td id="R-1"></td></tr>'
    assert pointsRang(59)=='<td id="R59"></td></tr>'
    
    assert steps(0, 0)==(0, 5, 1)
    assert steps(1, 0)==(5, 10, 1)
    assert steps(0, 1)==(0, 21, 5)
    assert steps(-1, -1)==(-1, 20, 5)
    assert steps(5, 2)==(5, 26, 5)
    
    assert sortHand([0, 0, 0])==[0, 0, 0]
    assert sortHand([1, 2, 3])==[1, 2, 3]
    assert sortHand([5, 4, 3, 2, 1])==[1,2,3,4,5]
    assert sortHand([2, 4, -1])==[-1,2,4]
    assert sortHand([])==[]
    
    assert memeValeur([0])==[]
    assert memeValeur([1,5,9,14,19])==[]
    assert memeValeur([1,1,-1,-1])==[1, 1, -1, -1]
    assert memeValeur([])==[]
    assert memeValeur([1,2,3,4,5])==[1, 2, 3, 4, 5]
    
    assert memeCouleur([1, 2, 3, 4, 5])==[1, 5]
    assert memeCouleur([])==[]
    assert memeCouleur([0,1,2,3])==[]
    assert memeCouleur([4,5,6,7])==[]
    assert memeCouleur([0,0,0,0])==[0,0]
    
    assert memeSerie([0,0,0,0])==([], False)
    assert memeSerie([0,4,8,12])==([0, 4, 8, 12], False)
    assert memeSerie([])==([], False)
    assert memeSerie([1,2,3,4,5])==([1, 4, 2, 3], False) #je sais pas prk
    assert memeSerie([0,36,40,44,48])==([0, 36, 40, 44, 48], True)
    
    assert getMemeValPoints([1,2,3,4,5])==25
    assert getMemeValPoints([])==0
    assert getMemeValPoints([-1])==0
    assert getMemeValPoints([1,1,1,1,1])==2
    assert getMemeValPoints([1,1,2,2,3])==50
    
    assert getMemeCoulPoints([])==0
    assert getMemeCoulPoints([1, 2, 3, 4, 5])==0
    assert getMemeCoulPoints([1,1,1,1,1])==0
    assert getMemeCoulPoints([1,5,9,13,17])==20
    assert getMemeCoulPoints([2,18,46,42,26])==20

test()
