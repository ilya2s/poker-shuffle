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
    "KC", "KD", "KH", "KS", "empty", "back"]


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

<<<<<<< HEAD

def drawCard(clic, case):
    if clic.id == 25 and clic.card == 53:
        card = randomCard()
        for element in game:
            if card == element.card:
                card = randomCard()
                
        clic.card = card
        case.innerHTML = img(card)


def selection(clic):
    if clic.card != 52:
        clic.selected = False if clic.selected else True


def bgLime(case):
    case.setAttribute('style', 'background-color: lime')
    
=======
def clic(id):
    #je dois mettre une condition pour que juste les carte dans le tableau
    #et le paquet s'allume.
    #voir comment je pourrais juste enlever la couleur precedante sans iterer
    
    for i in range(26):        
        case = getCase(i)       
        if i == id:           
            case.setAttribute('style', 'background-color: lime')
            
        else:
            case.setAttribute('style', 'background-color: white')
        

    if id == 25:
        case.innerHTML = img(randomCard())
>>>>>>> 5b72ed4dd901e288ae1362e74b6a01d38a672458

def bgTransparent(case):
    case.setAttribute('style', 'background-color: none')
    

def highlight(clic, case):
    if clic.selected and clic.card != 52:
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

 
def clic(id):
    
    clic = game[id]
    case = getCase(clic.id)
    
    selection(clic)
    
    drawCard(clic, case)
    
    placeCard(clic, case)
        
    highlight(clic, case)
    

def init():
    
    global game
    
    main = document.querySelector('#main')
    
    main.innerHTML = html + creerTable(5)
<<<<<<< HEAD
    
    game = makeGame()
=======


init()
#---------------------------------------------------------------------------------------------------
# fonction pour ordonne les elements du tableau pour pouvoir les calculers (pas encore en marche)

#def trier(t): # tri bulle
   # t.copy()
   # echange = True
   # while echange:
        #echange = False
       # for i in range(5):
           # if t[i] > t[i+1]:
               # temp = t[i]
               # t[i] = t[i+1]
               # t[i+1] = temp
               # echange = True
               # for j in range (5):
                    #if t[i][j] > t[i][j+1]:
                        # temp = t[i][j]
                        # t[i][j] = t[i][j+1]
                        # t[i][j+1] = temp
                        # echange = True
    #une fois le tableau trier on passe au calcule des points(calculVal)

# def calculVal:

# ici le tableau est deja trier

# conteurlignecouleurs = 0
#conteurlignevaleurs = 0

#conteurcolonnecouleurs = 0
#conteurcolonnevaleurs =0

#   for i in range (5):

#       for j in range (5):

#           #if t[i][j]%4==t[i][j+1]%4:     # la meme couleurs de carte sur les lignes
                #conteurlignecouleurs +=1
            #elif t[i][j]//4==t[i][j+1]//4: # la meme valeurs de carte sur les lignes
                #conteurlignevaleurs +=1 

            #elif t[i]==t[j] and t[i][j]%4==t[i][j+1]%4:  # la meme couleurs de carte sur les colonnes
                #conteurcolonnecouleurs +=1
            #else t[i]==t[j] and t[i][j]//4==t[i][j+1]//4: # la meme valeurs de carte sur les colonnes
                #conteurcolonnevaleurs +=1

# apres on fait que multiplier les conteurs par la valeurs de leurs points dans chaque ligne et colonnes
#exemple #conteurlignecouleurs =4 et #conteurlignevaleurs = 2 ca veux dire Couleur ou  Flush(20 points) + Brelan(10 points) = 30 points pour la premier ligne 

# pas encore terminer.....



#100 points) Quinte Flush Royale : L'as, le roi, la dame, le valet et le 10 d'une même couleur (tous trèfle, tous pique, tous carreau, ou tous coeur).
#(75 points) Quinte Flush : Cinq cartes de même couleur qui se suivent (par exemple le 7, 8, 9, 10 et le valet, tous trèfle, tous pique, tous carreau, ou tous coeur).
#(50 points) Carré : Quatre cartes de même valeur (par exemple quatre valets).
#(25 points) Full House : Trois cartes de même valeur et une paire de cartes de même valeur (par exemple trois as et deux 9).
#(20 points) Couleur ou Flush : Toutes les cartes de même couleur (tous trèfle, tous pique, tous carreau, ou tous coeur).
#(15 points) Quinte : Cinq cartes qui se suivent (par exemple le 8, 9, 10, valet et dame). Il est à noter que l'as peut être le début ou la fin de la séquence.
#(10 points) Brelan : Trois cartes de même valeur (par exemple trois rois).
#(5 points) Double Paire : Une paire de cartes de même valeur et une autre paire de cartes de même valeur (par exemple deux rois et deux 7).
#(2 points) Une Paire : Une paire de cartes de même valeur (par exemple deux as).
>>>>>>> 5b72ed4dd901e288ae1362e74b6a01d38a672458
