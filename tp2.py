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


def tableauPoints(dimension):
    html = '<tr>'
    for i in range(dimension):
        html += '<td id="C' + str(i) + '">20</td>'
        
    html += '<td id="T">999</td>'
    html += '</tr>'
    
    return html


def tableauCartes(dimension):
    html = ''
    c = 0
    for i in range(dimension):
        html += '<tr>'
        for j in range(dimension):
            html += '<td id="case' + str(c) + '" onclick="clic(' + str(c) + ')"><img src="http://codeboot.org/cards/' + cartes[52] + '.svg"></td>'
            c += 1
        html += '<td id="R' + str(i) + '">20</td>'
        html += '</tr>'
    
    html += tableauPoints(dimension)
        
    return html


def creerTable(dimension):
    html = '<table>'
    html += tableauCartes(dimension)
    html+= '</table>'
    
    return html


def randomCard():
    return math.floor(random() * 52)


def clic(id):
    case = document.querySelector('#case' + str(id))
    case.setAttribute('style', 'background-color: lime')
    
    if id == 25:
        case.innerHTML = '<img src="http://codeboot.org/cards/' + cartes[randomCard()] + '.svg">'


def init():
    
    main = document.querySelector('#main')
    
    main.innerHTML = """
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
    """
    main.innerHTML += """
    <table>
        <tr>
            <td><button onclick="init();">Nouvelle partie</button></td>
            <td></td>
            <td id="case25" onclick="clic(25);"><img src="http://codeboot.org/cards/back.svg"></td>
            <td></td>
        </tr>
    </table>
    """
    
    main.innerHTML += creerTable(5)


init()
