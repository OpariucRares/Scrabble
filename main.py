import random
import tkinter
from tkinter import *
from tkinter import ttk
from enum import Enum
from PIL import ImageTk, Image


class TypeCell(Enum):
    EMPTY = 1
    DOUBLE_LETTER = 2
    DOUBLE_WORD = 3
    TRIPLE_LETTER = 4
    TRIPLE_WORD = 5


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


def colorSelection(lineColorSelection, coloumnColorSelection, color):
    # TODO : de comentat pt proiectul final
    if placeWordButton["state"] == "enable" or retryLettersButtons["state"] == "enable":
        verticalLeft = Frame(root, bg=color, height=50, width=2)
        verticalRight = Frame(root, bg=color, height=50, width=2)
        horizontalUp = Frame(root, bg=color, height=2, width=50)
        horizontalDown = Frame(root, bg=color, height=2, width=52)
        copySquare = matrixSquares[lineColorSelection][coloumnColorSelection]
        verticalLeft.place(x=copySquare.pointX, y=copySquare.pointY)
        verticalRight.place(x=copySquare.pointX + 50, y=copySquare.pointY)
        horizontalUp.place(x=copySquare.pointX + 1, y=copySquare.pointY)
        horizontalDown.place(x=copySquare.pointX, y=copySquare.pointY + 50)
def getMouseClickPosition(line, column):
    def func(e):  # func will be passed an event.
        global lineSquareSelected, columnSquareSelected, labelErrorMessage, previousSquare
        #print(69)
        isPreviousSquareDefined = True
        try:
            previousSquare
        except NameError:
            isPreviousSquareDefined = False
        if isPreviousSquareDefined is True:
            if previousSquare is not None:
                colorSelection(previousSquare[0], previousSquare[1], '#F0F0F0')


        lineSquareSelected = line
        columnSquareSelected = column
        colorSelection(lineSquareSelected, columnSquareSelected, 'red')
        # TODO : decomentat pt proiectul final
        #if placeWordButton["state"] == "enable" or retryLettersButtons["state"] == "enable":
        labelErrorMessage.config(text="Ati ales patratul de pe\nlinia " + str(line + 1) + " si coloana " + str(column + 1))
        previousSquare = (line, column)
    return func
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
        matrixSquares[i][14 - i].typeSquare = TypeCell.DOUBLE_WORD
    # triple word
    for i in range(0, 15, 7):
        for j in range(0, 15, 7):
            matrixSquares[i][j].pathImage = "Images/ResizeTripleWord.png"
            matrixSquares[i][j].typeSquare = TypeCell.TRIPLE_WORD
    # triple letter
    for i in [1, 5, 9, 13]:
        for j in [5, 9]:
            matrixSquares[i][j].pathImage = "Images/ResizeTripleLetter.png"
            matrixSquares[i][j].typeSquare = TypeCell.TRIPLE_LETTER
    for j in [1, 13]:
        matrixSquares[5][j].pathImage = "Images/ResizeTripleLetter.png"
        matrixSquares[9][j].pathImage = "Images/ResizeTripleLetter.png"
        matrixSquares[5][j].typeSquare = TypeCell.TRIPLE_LETTER
        matrixSquares[9][j].typeSquare = TypeCell.TRIPLE_LETTER
    # double letter
    for i in [3, 11]:
        for j in [0, 7, 14]:
            matrixSquares[i][j].pathImage = "Images/ResizeDoubleLetter.png"
            matrixSquares[i][j].typeSquare = TypeCell.DOUBLE_LETTER
    for i in [0, 7, 14]:
        for j in [3, 11]:
            matrixSquares[i][j].pathImage = "Images/ResizeDoubleLetter.png"
            matrixSquares[i][j].typeSquare = TypeCell.DOUBLE_LETTER
    for i in [6, 8]:
        for j in [2, 6, 8, 12]:
            matrixSquares[i][j].pathImage = "Images/ResizeDoubleLetter.png"
            matrixSquares[i][j].typeSquare = TypeCell.DOUBLE_LETTER
    for i in [2, 12]:
        for j in [6, 8]:
            matrixSquares[i][j].pathImage = "Images/ResizeDoubleLetter.png"
            matrixSquares[i][j].typeSquare = TypeCell.DOUBLE_LETTER
    # center cell
    matrixSquares[7][7].pathImage = "Images/ResizeStart.png"
    matrixSquares[7][7].typeSquare = TypeCell.DOUBLE_WORD
    #work for click function
    # text for error message

    posRectangleX = 850
    posRectangleY = 220
    canvas = Canvas(root, width=700, height=100, bg='#315399')
    # canvas.pack()
    canvas.create_rectangle(posRectangleX, posRectangleY, posRectangleX + 100, posRectangleY + 60, fill="red")
    canvas.place(x=posRectangleX, y=posRectangleY)

    global labelErrorMessage
    labelErrorMessage = Label(root, text="Sa inceapa jocul",
                              font=("Courier 15 bold"), justify='left')  # TODO: restructure the interface for the app
    labelErrorMessage.place(x=880, y=240)

    # create the table
    for i in range(len(matrixSquares)):
        for j in range(len(matrixSquares[i])):

            image1 = Image.open(matrixSquares[i][j].pathImage)
            test = ImageTk.PhotoImage(image1)
            label1 = tkinter.Label(image=test)
            label1.bind('<Button-1>', getMouseClickPosition(i, j))
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

    variableColumn = StringVar(root)
    variableColumn.set(columnPositionCell[0])

    variableLine = StringVar(root)
    variableLine.set(linePositionCell[0])




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
    labelPrint = Label(root, text="Number Letters:")
    labelPrint.place(x=positionXPlayerName, y=positionYPlayerName + 120)
    labelPrint.config(font=("Courier", fontPlayerName))




    global pointsLabelPlayerOne
    global pointsLabelPlayerTwo
    global numberLettersBag
    positionXPoints = positionXPlayerName + 300
    pointsLabelPlayerOne = Label(root, text="0")
    pointsLabelPlayerOne.place(x=positionXPoints, y=positionYPlayerName)
    pointsLabelPlayerOne.config(font=("Courier", fontPlayerName))

    pointsLabelPlayerTwo = Label(root, text="0")
    pointsLabelPlayerTwo.place(x=positionXPoints, y=positionYPlayerName + 60)
    pointsLabelPlayerTwo.config(font=("Courier", fontPlayerName))

    numberLettersBag = Label(root, text=str(len(bagWithAllLetters)))
    numberLettersBag.place(x=positionXPoints + 100, y=positionYPlayerName + 120)
    numberLettersBag.config(font=("Courier", fontPlayerName))
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
        print(f"Input from isInputUserBuildWith {inputUser}")
        placeWordList = list()
        copyLettersPlayer = playerList[turnPlayer].letters
        # print(copyLettersPlayer)
        copyWord = inputUser
        for i in range(len(inputUser)):
            for j in copyLettersPlayer:
                print(f"i j {inputUser[i]} {j.letter}")
                if inputUser[i] == j.letter:
                    copyWord = copyWord.replace(inputUser[i], "", 1)
                    placeWordList.append(j)
                    print(f"{inputUser} {inputUser[i]}")
                    break
        listaOutput = list()
        for i in copyLettersPlayer:
            listaOutput.append(i.letter)
        #print(listaOutput)
        #print(inputUser)
        # created a word with other letters
        stringOutput = ""
        for i in placeWordList:
            stringOutput += i.letter
        print(f"Output {stringOutput}")
        if copyWord == "":
            return True
        return False

    def checkNewLettersCreateInvalidWords(listIndexLetters, direction): #todo checking for later
        newWord = ""
        for pos, letter in listIndexLetters:
            newWord = ""
            if direction == "Vertical":
                findLeftIndex = columnSquareSelected - 1
                if findLeftIndex >= 0:
                    while type(matrixSquares[pos][findLeftIndex].IsBlocked) is Letter:
                        newWord += matrixSquares[pos][findLeftIndex].isBlocked.letter
                        findLeftIndex -= 1
                    newWord = newWord[::-1]
                newWord += listIndexLetters[1]
                findRightIndex = columnSquareSelected + 1
                if findRightIndex <= 14:
                    while type(matrixSquares[pos][findRightIndex].IsBlocked) is Letter:
                        newWord += matrixSquares[pos][findRightIndex].isBlocked.letter
                        findLeftIndex += 1
                listNewWordsForPlayer.append((pos, findLeftIndex, findRightIndex, "Horizontal"))
            else:
                findLeftIndex = lineSquareSelected - 1
                if findLeftIndex >= 0:
                    while type(matrixSquares[findLeftIndex][pos].IsBlocked) is Letter:
                        newWord += matrixSquares[findLeftIndex][pos].isBlocked.letter
                        findLeftIndex -= 1
                    newWord = newWord[::-1]
                newWord += listIndexLetters[1]
                findRightIndex = columnSquareSelected + 1
                if findRightIndex <= 14:
                    while type(matrixSquares[pos][findRightIndex].IsBlocked) is Letter:
                        newWord += matrixSquares[pos][findRightIndex].isBlocked.letter
                        findLeftIndex += 1
                listNewWordsForPlayer.append((pos, findLeftIndex, findRightIndex, "Vertical"))
            if newWord != listIndexLetters[1] and newWord not in dex:
                listNewWordsForPlayer.clear()
                string = "Nu exista cuvantul " + newWord
                labelErrorMessage.config(text=string)
                return False





    def isWordPlacementValid(direction, lineSquare, columnSquare, limitSquare, inputUser):
        global listNewWordsForPlayer
        print(f"is wordPLacementValid {inputUser}")

        if firstTurn is True:
            return isInputUserBuildWithValidLetters(inputUser), inputUser
        isConnected = False
        checkLettersForColision = list()
        listNewWords = list()

        numberLetter = 0
        newWord = ""
        startLine = -1
        endline = -1
        posString = 0
        # checkLettersForColision -> literele noi
        if direction == "Horizontal":
            startLine = columnSquare - 1  # TODO de verificat daca depasesc matricea
            if startLine >= 0:
                while type(matrixSquares[lineSquare][startLine].isBlocked) is Letter:
                    print(matrixSquares[lineSquare][startLine].isBlocked)
                    newWord += matrixSquares[lineSquare][startLine].isBlocked.letter
                    startLine -= 1
            newWord = newWord[::-1]
            for i in range(columnSquare, limitSquare):
                print(f"linia {lineSquare} coloana {i} blocat {matrixSquares[lineSquare][i].isBlocked}")
                if type(matrixSquares[lineSquare][i].isBlocked) is Letter:
                    if inputUser[posString] != matrixSquares[lineSquare][i].isBlocked.letter:
                        labelErrorMessage.config(text="Cuvantul dat nu se potriveste '\n'cu literele de pe tabla")
                        return False, list(), ""
                    isConnected = True
                    posString += 1
                    continue
                newWord += inputUser[posString]
                checkLettersForColision.append((i, inputUser[posString]))
                posString += 1
            endline = checkLettersForColision[len(checkLettersForColision) - 1][0] + 1  # TODO de verificat daca depasesc matricea
            if endline <= 14:
                while type(matrixSquares[lineSquare][endline].isBlocked) is Letter:
                    print(matrixSquares[lineSquare][endline].isBlocked)
                    newWord += matrixSquares[lineSquare][endline].isBlocked.letter
                    endline += 1

        if direction == "Vertical":
            startLine = lineSquare - 1
            if startLine >= 0:
                while type(matrixSquares[startLine][columnSquare].isBlocked) is Letter:
                    print(matrixSquares[startLine][columnSquare].isBlocked)
                    newWord += matrixSquares[startLine][columnSquare].isBlocked.letter
                    startLine -= 1
            newWord = newWord[::-1]
            for i in range(lineSquare, limitSquare):
                newWord += inputUser[posString]
                print(f"linia {i} coloana {columnSquare} blocat {matrixSquares[i][columnSquare].isBlocked}")
                if type(matrixSquares[i][columnSquare].isBlocked) is Letter:
                    if inputUser[posString] != matrixSquares[i][columnSquare].isBlocked.letter:
                        labelErrorMessage.config(text="Cuvantul dat nu se potriveste '\n'cu literele de pe tabla")
                        return False, list, ""
                    isConnected = True
                    posString += 1
                    continue
                checkLettersForColision.append((i, inputUser[posString]))
                posString += 1
            endline = checkLettersForColision[len(checkLettersForColision) - 1][0] + 1
            if endline <= 14:
                while type(matrixSquares[endline][columnSquare].isBlocked) is Letter:
                    print(matrixSquares[endline][columnSquare].isBlocked)
                    newWord += matrixSquares[endline][columnSquare].isBlocked.letter
                    endline += 1
        print(f"cuvant nou {newWord}")
        if newWord not in dex:
            string = "Nu exista cuvantul " + newWord
            labelErrorMessage.config(text=string)
            return False, list, ""
        if newWord != inputUser:
            isConnected = True
        listNewWordsForPlayer.append((lineSquare, columnSquare, endline, direction))
        print(f"{isConnected}")

        if len(checkLettersForColision) == 0:
            labelErrorMessage.config(text="Nu ai folosit nicio litera noua")
            return False, list, ""
        if isConnected is False:
            labelErrorMessage.config(text="Nu v-ati conectat la o litera")
            return False, list, ""
        wordForChecking = ""
        for pos, letter in checkLettersForColision:
            wordForChecking += (letter)
        print(f"Litere noi {checkLettersForColision}")
        isValid = isInputUserBuildWithValidLetters(wordForChecking)
        return isValid, newWord


    global firstTurn
    try:
        directionInput
    except NameError:
        labelErrorMessage.config(text="Nu ati ales directia")
        return
    try:
        lineSquareSelected
    except NameError:
        labelErrorMessage.config(text="Nu ati ales patratul")
        return



    input1 = wordByUser.get() # todo: use this case only the first turn

    #print(lineSquareSelected)
    #print(columnSquareSelected)
    #print(len(input1))
    #print(firstTurn)
    #print(lineSquareSelected > 7 or lineSquareSelected + len(input1) < 7)
    #print(columnSquareSelected)
    if lineSquareSelected is None:
        labelErrorMessage.config(text="Nu ati ales patratul")
        return
    if directionInput == "Horizontal":
        if firstTurn is True and ((columnSquareSelected > 7 or columnSquareSelected  + len(input1) < 7) or lineSquareSelected != 7):
            labelErrorMessage.config(text="Trebuie sa va folositi de patratul din mijloc")
            return
    else:
        if firstTurn is True and ((lineSquareSelected > 7 or lineSquareSelected + len(input1) < 7) or columnSquareSelected != 7):
            labelErrorMessage.config(text="Trebuie sa va folositi de patratul din mijloc")
            return


    limitSquare = -1
    if directionInput == "Horizontal":
        limitSquare = columnSquareSelected + len(input1)
    else:
        limitSquare = lineSquareSelected + len(input1)
    #TODO de revizuit
    isValid, listLetters, showNewWord = isWordPlacementValid(directionInput, lineSquareSelected, columnSquareSelected, limitSquare, input1)
    print(f"isvalid {isValid} listLetters {listLetters}")
    if isValid is False:
        labelErrorMessage.config(text="Cuvantul nu este scris cu literele corecte")
        return

    createWordWithClassLetter = listLetters



    for i in createWordWithClassLetter:
        playerList[turnPlayer].letters.remove(i)

    hideLetters()
    finishTurnForUI()
    triplePoints = 0
    doublePoints = 0
    player = playerList[turnPlayer]
    points = 0
    #todo make a function to paint it
    createWordWithClassLetter.clear()
    createWordWithClassLetter = isInputUserBuildWithValidLetters(showNewWord)[1]

    print(createWordWithClassLetter)
    if directionInput == "Horizontal":
        indexColumn = columnSquareSelected
        for i in createWordWithClassLetter:
            image1 = Image.open(f"Images/Letters/{i.letterPos}.png")
            test = ImageTk.PhotoImage(image1)
            label1 = tkinter.Label(image=test)
            label1.image = test
            label1.bind('<Button-1>', getMouseClickPosition(lineSquareSelected, indexColumn))
            label1.place(x=matrixSquares[lineSquareSelected][indexColumn].pointX, y=matrixSquares[lineSquareSelected][indexColumn].pointY)
            matrixSquares[lineSquareSelected][indexColumn].isBlocked = i
            points = points + i.points
            if matrixSquares[lineSquareSelected][indexColumn].typeSquare == TypeCell.DOUBLE_LETTER:
                points = points + i.points
            elif matrixSquares[lineSquareSelected][indexColumn].typeSquare == TypeCell.TRIPLE_LETTER:
                points = points + i.points * 2
            elif matrixSquares[lineSquareSelected][indexColumn].typeSquare == TypeCell.DOUBLE_WORD:
                doublePoints += 1
            elif matrixSquares[lineSquareSelected][indexColumn].typeSquare == TypeCell.TRIPLE_WORD:
                triplePoints += 1
            indexColumn += 1
    else:
        indexLine = lineSquareSelected
        for i in createWordWithClassLetter:
            image1 = Image.open(f"Images/Letters/{i.letterPos}.png")
            test = ImageTk.PhotoImage(image1)
            label1 = tkinter.Label(image=test)
            label1.image = test
            label1.bind('<Button-1>', getMouseClickPosition(indexLine, columnSquareSelected))
            label1.place(x=matrixSquares[indexLine][columnSquareSelected].pointX, y=matrixSquares[indexLine][columnSquareSelected].pointY)
            matrixSquares[indexLine][columnSquareSelected].isBlocked = i
            points = points + i.points
            if matrixSquares[indexLine][columnSquareSelected].typeSquare == TypeCell.DOUBLE_LETTER:
                points = points + i.points
            elif matrixSquares[indexLine][columnSquareSelected].typeSquare == TypeCell.TRIPLE_LETTER:
                points = points + i.points * 2
            elif matrixSquares[indexLine][columnSquareSelected].typeSquare == TypeCell.DOUBLE_WORD:
                doublePoints += 1
            elif matrixSquares[indexLine][columnSquareSelected].typeSquare == TypeCell.TRIPLE_WORD:
                triplePoints += 1
            indexLine += 1
    #print(doublePoints)
    #print(triplePoints)
    for i in range(doublePoints):
        points *= 2
    for i in range(triplePoints):
        points *= 3
    player.points = points
    if turnPlayer == 0:
        pointsLabelPlayerOne.config(text=str(points))
    else:
        pointsLabelPlayerTwo.config(text=str(points))
    changeActivityButtons(sTakeLetters="enable")
    labelErrorMessage.config(text="Luati litere noi")
    colorSelection(previousSquare[0], previousSquare[1], '#F0F0F0')
    firstTurn = False

def takeLetters():
    stringNewLetters = ""
    numberLetters = 7 - len(playerList[turnPlayer].letters)
    copySamplePlayer = random.sample(bagWithAllLetters, numberLetters)
    for i in copySamplePlayer:
        playerList[turnPlayer].letters.append(i)
        stringNewLetters = stringNewLetters + i.letter
        stringNewLetters += " "
        bagWithAllLetters.remove(i)

    showLettersPlayer(playerList[turnPlayer])
    changeActivityButtons(sHideLetters="enable")
    labelErrorMessage.config(text="Lierele noi sunt " + stringNewLetters + "\nAscundeti literele ca sa vina urmatorul player")
    numberLettersBag.config(text=str(len(bagWithAllLetters)))
    #help
def retryFun():
    # changeActivityButtons("disabled")
    for i in player1.letters:
        bagWithAllLetters.append(i)
    playerList[turnPlayer].letters.clear()
    copySamplePlayer = random.sample(bagWithAllLetters, 7)
    for i in copySamplePlayer:
        playerList[turnPlayer].letters.append(i)
    showLettersPlayer(playerList[turnPlayer])
    colorSelection(previousSquare[0], previousSquare[1], '#F0F0F0')
    changeActivityButtons(sHideLetters="enable")
    labelErrorMessage.config(text="Ati luat litere noi. \nAscundeti literele si lasati urmatorul player")


def changeActivityButtons(sPlaceWord="disabled", sRetryLetters="disabled", sTakeLetters="disabled",
                          sHideLetters="disabled", sFinishTurn="disabled"):
    listInput = [sPlaceWord, sRetryLetters, sTakeLetters, sHideLetters, sFinishTurn]
    for sir in listInput:
        if sir not in ["disabled", "normal", "enable"]:
            return
    # TODO: testing passed, decomment when it is done
    placeWordButton["state"] = sPlaceWord
    retryLettersButtons["state"] = sRetryLetters
    takeLettersAfterPlacedWordButton["state"] = sTakeLetters
    hideLettersButton["state"] = sHideLetters
    finishTurnButtons["state"] = sFinishTurn


def finishTurnFun():
    global turnPlayer, lineSquareSelected, columnSquareSelected, previousSquare
    turnPlayer = (turnPlayer + 1) % maxPlayers
    hideLetters()
    finishTurnForUI()
    changeActivityButtons(sPlaceWord="enable", sRetryLetters="enable")
    labelErrorMessage.config(text="Randul " + playerList[turnPlayer].name)
    lineSquareSelected = None
    columnSquareSelected = None
    previousSquare = None

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
root.configure(bg='#315399')
frame = Frame(root, width=800, height=600)

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
mouseClickX, mouseClickY = -1, -1
initializeDex()
initializeAllLetters()
player1 = Player("Player 1", 0, random.sample(bagWithAllLetters, 7))
player2 = Player("Player 2", 0, random.sample(bagWithAllLetters, 7))
playerList = [player1, player2]
#TODO: change to true for final project
firstTurn = True
listNewWordsForPlayer = list()

InitializeBackground()

root.mainloop()

# if __name__ == '__main__':
#   print("hello")
