import random
import tkinter
from tkinter import *
from tkinter import ttk
from enum import Enum
from PIL import ImageTk, Image

class TypeCell(Enum):
    START_CELL = 1
    EMPTY = 2
    DOUBLE_LETTER = 3
    DOUBLE_WORD = 4
    TRIPLE_LETTER = 5
    TRIPLE_WORD = 6

class Letter:
    def __init__(self, letter, points): #TODO: add image
        self.letter = letter
        self.points = points
        self.letterPos = ord(letter) - ord("a")
    def __str__(self):
        return f"{self.letter} Position: {self.letterPos} Points: {self.points}"
class Square:
    def __init__(self, position, pointX, pointY, isBlocked, typeSquare, pathImage):
        self.position = position
        self.pointX = pointX
        self.pointY = pointY
        self.isBlocked = isBlocked
        self.typeSquare = typeSquare
        self.pathImage = pathImage
class Player:
    def __init__(self, name, points, letters):
        self.name = name
        self.points = points
        self.letters = letters
        for i in letters:
            bagWithAllLetters.remove(i)

def initializeDex():
    #fd = open(sys.argv[1], "rt")
    fd = open("Dictionaries/dictionary.txt", "rt", encoding="utf8")
    for word in fd:
        dex.append(word.strip("\n"))
def initializeAllLetters():
    def initializeGroupOfSameLetter(letter, points, numberTimes):
        for i in range(numberTimes):
            bagWithAllLetters.append(Letter(letter, points))
    initializeGroupOfSameLetter("_", 0, 2)
    initializeGroupOfSameLetter("i", 1, 11)
    initializeGroupOfSameLetter("a", 1, 10)
    initializeGroupOfSameLetter("e", 1, 9)
    initializeGroupOfSameLetter("t", 1, 7)
    initializeGroupOfSameLetter("n", 1, 6)
    initializeGroupOfSameLetter("r", 1, 6)
    initializeGroupOfSameLetter("s", 1, 6)
    initializeGroupOfSameLetter("c", 1, 5)
    initializeGroupOfSameLetter("l", 1, 5)
    initializeGroupOfSameLetter("u", 1, 5)

    initializeGroupOfSameLetter("o", 2, 5)
    initializeGroupOfSameLetter("p", 2, 4)

    initializeGroupOfSameLetter("d", 3, 4)

    initializeGroupOfSameLetter("m", 4, 3)
    initializeGroupOfSameLetter("f", 4, 2)
    initializeGroupOfSameLetter("v", 4, 2)

    initializeGroupOfSameLetter("b", 5, 2)

    initializeGroupOfSameLetter("g", 6, 2)

    initializeGroupOfSameLetter("h", 8, 1)
    initializeGroupOfSameLetter("z", 8, 1)
    initializeGroupOfSameLetter("j", 10, 1)
    initializeGroupOfSameLetter("x", 10, 1)

    initializeGroupOfSameLetter("w", 4, 0)
    initializeGroupOfSameLetter("y", 4, 0)
    initializeGroupOfSameLetter("k", 5, 0)
    initializeGroupOfSameLetter("q", 10, 0)

    random.shuffle(bagWithAllLetters)
def InitializeBackground():
    beginX = 50
    beginY = 20
    countSquares = 0
    #add empty cells
    for i in range(15):
        row = list()
        for j in range(15):
            square = Square(countSquares, beginX + j * 50, beginY + i * 50, False, TypeCell.EMPTY, "Images/ResizeEmptyCell.png")
            row.append(square)
        matrixSquares.append(row)
    for i in range(15):
        matrixSquares[i][i].pathImage = "Images/ResizeDoubleWord.png"
        matrixSquares[i][i].typeSquare = TypeCell.DOUBLE_WORD
    for i in range(15):
        matrixSquares[i][14 - i].pathImage = "Images/ResizeDoubleWord.png"
        matrixSquares[i][i].typeSquare = TypeCell.DOUBLE_WORD
    #triple word
    for i in range(0, 15, 7):
        for j in range(0, 15, 7):
            matrixSquares[i][j].pathImage = "Images/ResizeTripleWord.png"
            matrixSquares[i][i].typeSquare = TypeCell.TRIPLE_WORD
    #triple letter
    for i in [1, 5, 9, 13]:
        for j in [5, 9]:
            matrixSquares[i][j].pathImage = "Images/ResizeTripleLetter.png"
            matrixSquares[i][i].typeSquare = TypeCell.TRIPLE_LETTER
    for j in [1, 13]:
        matrixSquares[5][j].pathImage = "Images/ResizeTripleLetter.png"
        matrixSquares[9][j].pathImage = "Images/ResizeTripleLetter.png"
        matrixSquares[i][i].typeSquare = TypeCell.TRIPLE_LETTER
    #double letter
    for i in [3, 11]:
        for j in [0, 7, 14]:
            matrixSquares[i][j].pathImage = "Images/ResizeDoubleLetter.png"
            matrixSquares[i][i].typeSquare = TypeCell.DOUBLE_LETTER
    for i in [0, 7, 14]:
        for j in [3, 11]:
            matrixSquares[i][j].pathImage = "Images/ResizeDoubleLetter.png"
            matrixSquares[i][i].typeSquare = TypeCell.DOUBLE_LETTER
    for i in [6, 8]:
        for j in [2, 6, 8, 12]:
            matrixSquares[i][j].pathImage = "Images/ResizeDoubleLetter.png"
            matrixSquares[i][i].typeSquare = TypeCell.DOUBLE_LETTER
    for i in [2, 12]:
        for j in [6, 8]:
            matrixSquares[i][j].pathImage = "Images/ResizeDoubleLetter.png"
            matrixSquares[i][i].typeSquare = TypeCell.DOUBLE_LETTER
    #center cell
    matrixSquares[7][7].pathImage = "Images/ResizeStart.png"
    matrixSquares[7][7].typeSquare = TypeCell.START_CELL
    #create the table
    for i in range(len(matrixSquares)):
        for j in range(len(matrixSquares[i])):
            image1 = Image.open(matrixSquares[i][j].pathImage)
            test = ImageTk.PhotoImage(image1)
            label1 = tkinter.Label(image=test)
            label1.image = test
            label1.place(x=matrixSquares[i][j].pointX, y=matrixSquares[i][j].pointY)

    positionDirectionX = 1300
    positionDirectionY = 600

    labelPrint = Label(root, text="Direction of the word")
    labelPrint.place(x=positionDirectionX, y=positionDirectionY - 30)
    labelPrint.config(font=("Courier", 10))

    variableDirection = StringVar(root)
    variableDirection.set(directionWord[0])
    global directionCB
    directionCB = OptionMenu(root, variableDirection, *directionWord)
    directionCB.place(x=positionDirectionX, y=positionDirectionY)

    labelPrint = Label(root, text="Column")
    labelPrint.place(x=positionDirectionX, y=positionDirectionY + 50)
    labelPrint.config(font=("Courier", 10))

    variableColumn = StringVar(root)
    variableColumn.set(columnPositionCell[0])
    global columnCB
    columnCB = OptionMenu(root, variableColumn, *columnPositionCell)
    columnCB.place(x=positionDirectionX, y=positionDirectionY + 80)

    labelPrint = Label(root, text="Line")
    labelPrint.place(x=positionDirectionX + 80, y=positionDirectionY + 50)
    labelPrint.config(font=("Courier", 10))

    variableLine = StringVar(root)
    variableLine.set(linePositionCell[0])
    global lineCB
    lineCB = OptionMenu(root, variableLine, *linePositionCell)
    lineCB.place(x=positionDirectionX + 80, y=positionDirectionY + 80)

    #text for error message

    posRectangleX = 850
    posRectangleY = 180
    canvas = Canvas(root, width=700, height=100, bg='#315399')
    #canvas.pack()
    canvas.create_rectangle(posRectangleX, posRectangleY, posRectangleX + 100, posRectangleY + 60, fill="red")
    canvas.place(x=posRectangleX, y=posRectangleY)

    global labelErrorMessage
    labelErrorMessage = Label(root, text="Urasc Tkinter", font=("Courier 15 bold"))  # TODO: restructure the interface for the app
    labelErrorMessage.place(x=880, y=200)
    #canvas.pack()

    #player scores
    positionXPlayerName = 850
    positionYPlayerName = 20
    fontPlayerName = 30
    labelPrint =Label(root, text="Player One:")
    labelPrint.place(x=positionXPlayerName, y=positionYPlayerName)
    labelPrint.config(font=("Courier", fontPlayerName))
    labelPrint = Label(root, text="Player Two:")
    labelPrint.place(x=positionXPlayerName, y=positionYPlayerName + 60)
    labelPrint.config(font=("Courier", fontPlayerName))

    global pointsLabelPlayerOne
    global pointsLabelPlayerTwo
    positionXPoints = positionXPlayerName + 300
    pointsLabelPlayerOne = Label(root, text="0")
    pointsLabelPlayerOne.place(x=positionXPoints, y=positionYPlayerName)
    pointsLabelPlayerOne.config(font=("Courier", fontPlayerName))

    pointsLabelPlayerTwo = Label(root, text="0")
    pointsLabelPlayerTwo.place(x=positionXPoints, y=positionYPlayerName + 60)
    pointsLabelPlayerTwo.config(font=("Courier", fontPlayerName))

    labelPrint = Label(root, text="Enter your word:")
    labelPrint.place(x=900, y=640)
    labelPrint.config(font=("Courier", 15))

    global wordByUser
    wordByUser = Entry(root, width=40)
    wordByUser.focus_set()
    wordByUser.place(x=900, y=680)

    global placeWordButton
    placeWordButton = ttk.Button(root, text="Place Word", width=20, command=placeWord)
    placeWordButton.place(x=1150, y=750)

    global retryLettersButtons
    retryLettersButtons = ttk.Button(root, text="Retry Letters", width=20, command=retryFun)
    retryLettersButtons.place(x=1000, y=750)

    global finishTurnButtons
    finishTurnButtons = ttk.Button(root, text="Finish turn", width=20, command=finishTurnFun)
    finishTurnButtons.place(x=1300, y=750)

    placeLetter()

def repaintLetter(x, y):
    #850, 400
    count = 0
    for i in range(7):
        image1 = Image.open(f"Images/ResizeBackground.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=x + count * 50, y=y)
        count += 1
def placeLetter():
    if turnPlayer == 1:
        labelPrint = Label(root, text="Player 1 letters")
        labelPrint.place(x=850, y=350)
        labelPrint.config(font=("Courier Bold", 15))
        showLettersPlayer(player1, 850, 400)
    else:
        labelPrint = Label(root, text="Player 2 letters")
        labelPrint.place(x=850, y=350)
        labelPrint.config(font=("Courier Bold", 15))
        showLettersPlayer(player2, 850, 400)

def errorString():
    string = wordByUser.get()
    labelErrorMessage.configure(text=string)

def placeWord():
    input1 = wordByUser.get()
    #TODO validation word (after the checks, we can make the transition)
    if input1 not in dex:
        return False

    lettersPlayer = list()
    localPoint = 0
    if turnPlayer == 0:
        for i in player1.letters:
            lettersPlayer.append(i)
    else:
        for i in player2.letters:
            lettersPlayer.append(i)

    for i in input1:
        # find the letter
        for index in lettersPlayer:
            if i == index.letter:
                localPoint = localPoint + index.points
                lettersPlayer.remove(index)
                input1.replace(i, "")
                break

    takeLettersForPlayer = len(input1)
    return True


def retryFun():
    global turnPlayer
   # changeActivityButtons("disabled")
    if turnPlayer == 0:
        for i in player1.letters:
            bagWithAllLetters.append(i)
        player1.letters.clear()
        copySamplePlayer = random.sample(bagWithAllLetters, 7)
        for i in copySamplePlayer:
            player1.letters.append(i)
        turnPlayer = 1
        showLettersPlayer(player1, 850, 400)
    else:
        for i in player2.letters:
            bagWithAllLetters.append(i)
        player2.letters.clear()
        copySamplePlayer = random.sample(bagWithAllLetters, 7)
        for i in copySamplePlayer:
            player1.letters.append(i)
        turnPlayer = 0
        showLettersPlayer(player2, 850, 400)

def changeActivityButtons(sir):
    if sir not in ["disabled", "normal", "enable"]:
        return
    placeWordButton["state"] = sir
    retryLettersButtons["state"] = sir

def finishTurnFun():
    global turnPlayer
    if turnPlayer == 0:
        turnPlayer = 1
    else:
        turnPlayer = 0
    placeLetter()
    repaintLetter(850, 400)
    # 850, 400
    print(len(bagWithAllLetters))

def showLettersPlayer(player, x, y):
    count = 0
    for i in player.letters:
        indexImagine = ord(i.letter) - ord("a")
        image1 = Image.open(f"Images/Letters/{indexImagine}.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=x + count * 50, y=y)
        count += 1
root = Tk()
root.title("Scrabble")
root.geometry("800x600")
w = 1000
h = 1000
x = w / 2
y = h / 2
root.configure(bg='#315399')

takeLettersForPlayer = 7
dex = list()
bagWithAllLetters = list()
matrixSquares = list(list())
directionWord = ["Horizontal", "Vertical"]
linePositionCell = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
columnPositionCell = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
turnPlayer = 0

initializeDex()
initializeAllLetters()
player1 = Player("Player 1", 0, random.sample(bagWithAllLetters, 7))
player2 = Player("Player 2", 0, random.sample(bagWithAllLetters, 7))
InitializeBackground()




root.mainloop()

#if __name__ == '__main__':
 #   print("hello")
