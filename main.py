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
    def __init__(self, letter, points):  # TODO: add image
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
    # fd = open(sys.argv[1], "rt")
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


def displayDirection(choice):
    global directionInput
    directionInput = choice


def displayLine(choice):
    global lineInput
    lineInput = int(choice)


def displayColumn(choice):
    global columnInput
    columnInput = int(choice)


def InitializeBackground():
    beginX = 50
    beginY = 20
    countSquares = 0
    # add empty cells
    for i in range(15):
        row = list()
        for j in range(15):
            square = Square(countSquares, beginX + j * 50, beginY + i * 50, False, TypeCell.EMPTY,
                            "Images/ResizeEmptyCell.png")
            row.append(square)
        matrixSquares.append(row)
    for i in range(15):
        matrixSquares[i][i].pathImage = "Images/ResizeDoubleWord.png"
        matrixSquares[i][i].typeSquare = TypeCell.DOUBLE_WORD
    for i in range(15):
        matrixSquares[i][14 - i].pathImage = "Images/ResizeDoubleWord.png"
        matrixSquares[i][i].typeSquare = TypeCell.DOUBLE_WORD
    # triple word
    for i in range(0, 15, 7):
        for j in range(0, 15, 7):
            matrixSquares[i][j].pathImage = "Images/ResizeTripleWord.png"
            matrixSquares[i][i].typeSquare = TypeCell.TRIPLE_WORD
    # triple letter
    for i in [1, 5, 9, 13]:
        for j in [5, 9]:
            matrixSquares[i][j].pathImage = "Images/ResizeTripleLetter.png"
            matrixSquares[i][i].typeSquare = TypeCell.TRIPLE_LETTER
    for j in [1, 13]:
        matrixSquares[5][j].pathImage = "Images/ResizeTripleLetter.png"
        matrixSquares[9][j].pathImage = "Images/ResizeTripleLetter.png"
        matrixSquares[i][i].typeSquare = TypeCell.TRIPLE_LETTER
    # double letter
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
    # center cell
    matrixSquares[7][7].pathImage = "Images/ResizeStart.png"
    matrixSquares[7][7].typeSquare = TypeCell.START_CELL
    # create the table
    for i in range(len(matrixSquares)):
        for j in range(len(matrixSquares[i])):
            image1 = Image.open(matrixSquares[i][j].pathImage)
            test = ImageTk.PhotoImage(image1)
            label1 = tkinter.Label(image=test)
            label1.image = test
            label1.place(x=matrixSquares[i][j].pointX, y=matrixSquares[i][j].pointY)

    positionDirectionX = 1300
    positionDirectionY = 550

    labelPrint = Label(root, text="Direction of the word")
    labelPrint.place(x=positionDirectionX, y=positionDirectionY - 30)
    labelPrint.config(font=("Courier", 10))

    variableDirection = StringVar(root)
    variableDirection.set(directionWord[0])
    global directionCB
    directionCB = OptionMenu(root, variableDirection, *directionWord, command=displayDirection)
    directionCB.place(x=positionDirectionX, y=positionDirectionY)

    labelPrint = Label(root, text="Column")
    labelPrint.place(x=positionDirectionX, y=positionDirectionY + 50)
    labelPrint.config(font=("Courier", 10))

    variableColumn = StringVar(root)
    variableColumn.set(columnPositionCell[0])
    global columnCB
    columnCB = OptionMenu(root, variableColumn, *columnPositionCell, command=displayColumn)
    columnCB.place(x=positionDirectionX, y=positionDirectionY + 80)

    labelPrint = Label(root, text="Line")
    labelPrint.place(x=positionDirectionX + 80, y=positionDirectionY + 50)
    labelPrint.config(font=("Courier", 10))

    variableLine = StringVar(root)
    variableLine.set(linePositionCell[0])
    global lineCB
    lineCB = OptionMenu(root, variableLine, *linePositionCell, command=displayLine)
    lineCB.place(x=positionDirectionX + 80, y=positionDirectionY + 80)

    # text for error message

    posRectangleX = 850
    posRectangleY = 180
    canvas = Canvas(root, width=700, height=100, bg='#315399')
    # canvas.pack()
    canvas.create_rectangle(posRectangleX, posRectangleY, posRectangleX + 100, posRectangleY + 60, fill="red")
    canvas.place(x=posRectangleX, y=posRectangleY)

    global labelErrorMessage
    labelErrorMessage = Label(root, text="Sa inceapa jocul",
                              font=("Courier 15 bold"), justify='left')  # TODO: restructure the interface for the app
    labelErrorMessage.place(x=880, y=200)
    # canvas.pack()

    # player scores
    positionXPlayerName = 850
    positionYPlayerName = 20
    fontPlayerName = 30
    labelPrint = Label(root, text="Player One:")
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

    buttonWidth = 15

    global wordByUser
    wordByUser = Entry(root, width=40)
    wordByUser.focus_set()
    wordByUserPosX = 850
    wordByUserPosY = 550
    wordByUser.place(x=wordByUserPosX, y=wordByUserPosY)
    labelPrint = Label(root, text="Enter your word:")
    labelPrint.place(x=wordByUserPosX, y=wordByUserPosY - 40)
    labelPrint.config(font=("Courier", 15))

    placeButtonsStartPosX = 850
    placeButtonsStartPosY = 700
    distanceBetweenButtons = 110
    global placeWordButton
    placeWordButton = ttk.Button(root, text="Place Word", width=buttonWidth, command=placeWord)
    placeWordButton.place(x=placeButtonsStartPosX, y=placeButtonsStartPosY)

    global retryLettersButtons
    retryLettersButtons = ttk.Button(root, text="Retry Letters", width=buttonWidth, command=retryFun)
    retryLettersButtons.place(x=placeButtonsStartPosX + distanceBetweenButtons, y=placeButtonsStartPosY)

    global takeLettersAfterPlacedWordButton
    takeLettersAfterPlacedWordButton = ttk.Button(root, text="Take Letters", width=buttonWidth, command=takeLetters)
    takeLettersAfterPlacedWordButton.place(x=placeButtonsStartPosX + 2 * distanceBetweenButtons,
                                           y=placeButtonsStartPosY)

    global hideLettersButton
    hideLettersButton = ttk.Button(root, text="Hide Letters", width=buttonWidth, command=hideLetters)
    hideLettersButton.place(x=placeButtonsStartPosX + 3 * distanceBetweenButtons, y=placeButtonsStartPosY)

    global finishTurnButtons
    finishTurnButtons = ttk.Button(root, text="Finish turn", width=buttonWidth, command=finishTurnFun)
    finishTurnButtons.place(x=placeButtonsStartPosX + 4 * distanceBetweenButtons, y=placeButtonsStartPosY)

    finishTurnForUI()
    changeActivityButtons(sPlaceWord="enable", sRetryLetters="enable")


def hideLetters():
    xHide = 850
    yHide = 400
    count = 0
    for i in range(7):
        image1 = Image.open(f"Images/ResizeBackground.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=xHide + count * 50, y=yHide)
        count += 1
    labelErrorMessage.config(text="Randul urmatorului player")
    changeActivityButtons(sFinishTurn="enable")


def finishTurnForUI():
    labelPrint = Label(root, text=playerList[turnPlayer].name)
    labelPrint.place(x=850, y=350)
    labelPrint.config(font=("Courier Bold", 15))
    showLettersPlayer(playerList[turnPlayer])


def placeWord():
    def isInputUserBuildWithValidLetters(inputUser):
        placeWordList = list()
        copyLettersPlayer = playerList[turnPlayer].letters
        # print(copyLettersPlayer)
        for i in inputUser:
            for j in copyLettersPlayer:
                if i == j.letter:
                    inputUser = inputUser.replace(i, "", 1)
                    placeWordList.append(j)
                    break

        # created a word with other letters
        if inputUser == "":
            return True, placeWordList
        return False, list()

    input1 = wordByUser.get()
    if input1 not in dex:
        labelErrorMessage.config(text="Nu exista cuvantul")
        return
    if not isInputUserBuildWithValidLetters(input1)[0]:
        labelErrorMessage.config(text="Cuvantul nu este scris cu literele corecte")
        return
    createWordWithClassLetter = isInputUserBuildWithValidLetters(input1)[1]
    # finalCellWordLine = lineInput
    # finalCellWordColumn = columnInput
    try:
        directionInput
    except NameError:
        labelErrorMessage.config(text="Nu ati ales directia")
        return
    try:
        lineInput
    except NameError:
        labelErrorMessage.config(text="Nu ati ales linia primei litere")
        return
    try:
        columnInput
    except NameError:
        labelErrorMessage.config(text="Nu ati ales coloana primei litere")
        return
    for i in createWordWithClassLetter:
        playerList[turnPlayer].letters.remove(i)

    hideLetters()
    finishTurnForUI()
    if directionInput == "Horizontal":
        indexColumn = columnInput
        for i in createWordWithClassLetter:
            image1 = Image.open(f"Images/Letters/{i.letterPos}.png")
            test = ImageTk.PhotoImage(image1)
            label1 = tkinter.Label(image=test)
            label1.image = test
            label1.place(x=matrixSquares[lineInput][indexColumn].pointX, y=matrixSquares[lineInput][indexColumn].pointY)
            matrixSquares[lineInput][indexColumn].isBlocked = True
            matrixSquares[lineInput][indexColumn].typeSquare = i
            indexColumn += 1
    else:
        indexLine = lineInput
        for i in createWordWithClassLetter:
            image1 = Image.open(f"Images/Letters/{i.letterPos}.png")
            test = ImageTk.PhotoImage(image1)
            label1 = tkinter.Label(image=test)
            label1.image = test
            label1.place(x=matrixSquares[indexLine][columnInput].pointX, y=matrixSquares[indexLine][columnInput].pointY)
            matrixSquares[indexLine][columnInput].isBlocked = True
            matrixSquares[indexLine][columnInput].typeSquare = i
            indexLine += 1
    changeActivityButtons(sTakeLetters="enable")
    labelErrorMessage.config(text="Luati litere noi")


def takeLetters():
    stringNewLetters = ""
    numberLetters = 7 - len(playerList[turnPlayer].letters)
    copySamplePlayer = random.sample(bagWithAllLetters, numberLetters)
    for i in copySamplePlayer:
        playerList[turnPlayer].letters.append(i)
        stringNewLetters = stringNewLetters + i.letter
        stringNewLetters += " "
    showLettersPlayer(playerList[turnPlayer])
    changeActivityButtons(sHideLetters="enable")
    labelErrorMessage.config(text="Lierele noi sunt " + stringNewLetters + "\nAscundeti literele ca sa vina urmatorul player")

def retryFun():
    # changeActivityButtons("disabled")
    for i in player1.letters:
        bagWithAllLetters.append(i)
    playerList[turnPlayer].letters.clear()
    copySamplePlayer = random.sample(bagWithAllLetters, 7)
    for i in copySamplePlayer:
        playerList[turnPlayer].letters.append(i)
    showLettersPlayer(playerList[turnPlayer])
    changeActivityButtons(sHideLetters="enable")
    labelErrorMessage.config(text="Ati luat litere noi. \nAscundeti literele si lasati urmatorul player")


def changeActivityButtons(sPlaceWord="disabled", sRetryLetters="disabled", sTakeLetters="disabled",
                          sHideLetters="disabled", sFinishTurn="disabled"):
    listInput = [sPlaceWord, sRetryLetters, sTakeLetters, sHideLetters, sFinishTurn]
    for sir in listInput:
        if sir not in ["disabled", "normal", "enable"]:
            return
    # TODO: testing passed, decomment when it is done
    # placeWordButton["state"] = sPlaceWord
    # retryLettersButtons["state"] = sRetryLetters
    # takeLettersAfterPlacedWordButton["state"] = sTakeLetters
    # hideLettersButton["state"] = sHideLetters
    # finishTurnButtons["state"] = sFinishTurn


def finishTurnFun():
    global turnPlayer
    turnPlayer = (turnPlayer + 1) % maxPlayers
    hideLetters()
    finishTurnForUI()
    changeActivityButtons(sPlaceWord="enable", sRetryLetters="enable")
    labelErrorMessage.config(text="Randul " + playerList[turnPlayer].name)


def showLettersPlayer(player):
    count = 0
    showLettersX = 850
    showLettersY = 400
    for i in player.letters:
        indexImagine = ord(i.letter) - ord("a")
        image1 = Image.open(f"Images/Letters/{indexImagine}.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=test)
        label1.image = test
        label1.place(x=showLettersX + count * 50, y=showLettersY)
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
# TODO: insert better starting message
directionWord = ["Horizontal", "Vertical"]
linePositionCell = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
columnPositionCell = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
turnPlayer = 0
maxPlayers = 2
initializeDex()
initializeAllLetters()
player1 = Player("Player 1", 0, random.sample(bagWithAllLetters, 7))
player2 = Player("Player 2", 0, random.sample(bagWithAllLetters, 7))
playerList = [player1, player2]
InitializeBackground()

root.mainloop()

# if __name__ == '__main__':
#   print("hello")
