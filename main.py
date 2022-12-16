import random
import sys
from tkinter import ttk, Frame, Canvas, Label, StringVar, OptionMenu, Entry, Tk
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
        self.letter_pos = ord(letter) - ord("a")

    def __str__(self):
        return f"{self.letter} Position: {self.letter_pos} Points: {self.points}"


class Square:
    def __init__(self, position, point_x, point_y, is_blocked, type_square, path_Image):
        self.position = position
        self.point_x = point_x
        self.point_y = point_y
        self.is_blocked = is_blocked
        self.type_square = type_square
        self.path_image = path_Image


class Player:
    def __init__(self, name, points, letters):
        self.name = name
        self.points = points
        self.letters = letters
        self.has_given_up = False
        for i in letters:
            bag_with_all_letters.remove(i)


def initialize_dex():
    # fd = open(sys.argv[1], "rt")
    fd = open("Dictionaries/dictionary.txt", "rt", encoding="utf8")
    for word in fd:
        dex.append(word.strip("\n"))


def initialize_all_letters():
    def initialize_group_of_same_letter(letter, points, number_times):
        global dictionary_letters
        for i in range(number_times):
            bag_with_all_letters.append(Letter(letter, points))
        dictionary_letters.append(Letter(letter, points))
    def test_give_up_button():
        initialize_group_of_same_letter("i", 1, 2)
        initialize_group_of_same_letter("a", 1, 2)
        initialize_group_of_same_letter("e", 1, 2)
        initialize_group_of_same_letter("t", 1, 2)
        initialize_group_of_same_letter("n", 1, 2)
        initialize_group_of_same_letter("r", 1, 2)
        initialize_group_of_same_letter("s", 1, 2)
        initialize_group_of_same_letter("c", 1, 2)
        initialize_group_of_same_letter("l", 1, 2)
        initialize_group_of_same_letter("u", 1, 2)
        random.shuffle(bag_with_all_letters)
    #test give up button
    #test_give_up_button()
    #return

    initialize_group_of_same_letter("_", 0, 2)
    initialize_group_of_same_letter("i", 1, 11)
    initialize_group_of_same_letter("a", 1, 10)
    initialize_group_of_same_letter("e", 1, 9)
    initialize_group_of_same_letter("t", 1, 7)
    initialize_group_of_same_letter("n", 1, 6)
    initialize_group_of_same_letter("r", 1, 6)
    initialize_group_of_same_letter("s", 1, 6)
    initialize_group_of_same_letter("c", 1, 5)
    initialize_group_of_same_letter("l", 1, 5)
    initialize_group_of_same_letter("u", 1, 5)

    initialize_group_of_same_letter("o", 2, 5)
    initialize_group_of_same_letter("p", 2, 4)

    initialize_group_of_same_letter("d", 3, 4)

    initialize_group_of_same_letter("m", 4, 3)
    initialize_group_of_same_letter("f", 4, 2)
    initialize_group_of_same_letter("v", 4, 2)

    initialize_group_of_same_letter("b", 5, 2)

    initialize_group_of_same_letter("g", 6, 2)

    initialize_group_of_same_letter("h", 8, 1)
    initialize_group_of_same_letter("z", 8, 1)
    initialize_group_of_same_letter("j", 10, 1)
    initialize_group_of_same_letter("x", 10, 1)

    initialize_group_of_same_letter("w", 4, 0)
    initialize_group_of_same_letter("y", 4, 0)
    initialize_group_of_same_letter("k", 5, 0)
    initialize_group_of_same_letter("q", 10, 0)

    random.shuffle(bag_with_all_letters)


def display_direction(choice):
    global direction_input
    direction_input = choice


def color_selection(line_color_selection, column_color_selection, color):
    # TODO : de comentat pt proiectul final
    if place_word_button["state"] == "enable" or retry_letters_buttons["state"] == "enable":
        vertical_left = Frame(root, bg=color, height=50, width=2)
        vertical_right = Frame(root, bg=color, height=50, width=2)
        horizontal_up = Frame(root, bg=color, height=2, width=50)
        horizontal_down = Frame(root, bg=color, height=2, width=52)
        copy_square = matrix_squares[line_color_selection][column_color_selection]
        vertical_left.place(x=copy_square.point_x, y=copy_square.point_y)
        vertical_right.place(x=copy_square.point_x + 50, y=copy_square.point_y)
        horizontal_up.place(x=copy_square.point_x + 1, y=copy_square.point_y)
        horizontal_down.place(x=copy_square.point_x, y=copy_square.point_y + 50)


def get_mouse_click_position(line, column):
    def func():  # func will be passed an event.
        global line_square_selected, column_square_selected, label_error_message, previous_square
        # print(69)
        is_previous_square_defined = True
        try:
            previous_square
        except NameError:
            is_previous_square_defined = False
        if is_previous_square_defined is True:
            if previous_square is not None:
                color_selection(previous_square[0], previous_square[1], '#F0F0F0')

        line_square_selected = line
        column_square_selected = column
        color_selection(line_square_selected, column_square_selected, 'red')
        # TODO : decomentat pt proiectul final
        if place_word_button["state"] == "enable" or retry_letters_buttons["state"] == "enable":
            label_error_message.config(
                text="Ati ales patratul de pe\nlinia " + str(line + 1) + " si coloana " + str(column + 1))
        previous_square = (line, column)

    return func


def initialize_background():
    begin_x = 50
    begin_y = 20
    count_squares = 0
    # add empty cells
    for i in range(15):
        row = list()
        for j in range(15):
            square = Square(count_squares, begin_x + j * 50, begin_y + i * 50, False, TypeCell.EMPTY,
                            "Images/ResizeEmptyCell.png")
            row.append(square)
        matrix_squares.append(row)
    for i in range(15):
        matrix_squares[i][i].path_image = "Images/ResizeDoubleWord.png"
        matrix_squares[i][i].type_square = TypeCell.DOUBLE_WORD
    for i in range(15):
        matrix_squares[i][14 - i].path_image = "Images/ResizeDoubleWord.png"
        matrix_squares[i][14 - i].type_square = TypeCell.DOUBLE_WORD
    # triple word
    for i in range(0, 15, 7):
        for j in range(0, 15, 7):
            matrix_squares[i][j].path_image = "Images/ResizeTripleWord.png"
            matrix_squares[i][j].type_square = TypeCell.TRIPLE_WORD
    # triple letter
    for i in [1, 5, 9, 13]:
        for j in [5, 9]:
            matrix_squares[i][j].path_image = "Images/ResizeTripleLetter.png"
            matrix_squares[i][j].type_square = TypeCell.TRIPLE_LETTER
    for j in [1, 13]:
        matrix_squares[5][j].path_image = "Images/ResizeTripleLetter.png"
        matrix_squares[9][j].path_image = "Images/ResizeTripleLetter.png"
        matrix_squares[5][j].type_square = TypeCell.TRIPLE_LETTER
        matrix_squares[9][j].type_square = TypeCell.TRIPLE_LETTER
    # double letter
    for i in [3, 11]:
        for j in [0, 7, 14]:
            matrix_squares[i][j].path_image = "Images/ResizeDoubleLetter.png"
            matrix_squares[i][j].type_square = TypeCell.DOUBLE_LETTER
    for i in [0, 7, 14]:
        for j in [3, 11]:
            matrix_squares[i][j].path_image = "Images/ResizeDoubleLetter.png"
            matrix_squares[i][j].type_square = TypeCell.DOUBLE_LETTER
    for i in [6, 8]:
        for j in [2, 6, 8, 12]:
            matrix_squares[i][j].path_image = "Images/ResizeDoubleLetter.png"
            matrix_squares[i][j].type_square = TypeCell.DOUBLE_LETTER
    for i in [2, 12]:
        for j in [6, 8]:
            matrix_squares[i][j].path_image = "Images/ResizeDoubleLetter.png"
            matrix_squares[i][j].type_square = TypeCell.DOUBLE_LETTER
    # center cell
    matrix_squares[7][7].path_image = "Images/ResizeStart.png"
    matrix_squares[7][7].type_square = TypeCell.DOUBLE_WORD
    # work for click function
    # text for error message

    pos_rectangle_x = 850
    pos_rectangle_y = 220
    canvas = Canvas(root, width=700, height=100, bg='#315399')
    # canvas.pack()
    canvas.create_rectangle(pos_rectangle_x, pos_rectangle_y, pos_rectangle_x + 100, pos_rectangle_y + 60, fill="red")
    canvas.place(x=pos_rectangle_x, y=pos_rectangle_y)

    global label_error_message
    label_error_message = Label(root, text="Sa inceapa jocul",
                                font=("Courier 15 bold"), justify='left')  # TODO: restructure the interface for the app
    label_error_message.place(x=880, y=240)

    # create the table
    for i in range(len(matrix_squares)):
        for j in range(len(matrix_squares[i])):
            image1 = Image.open(matrix_squares[i][j].path_image)
            test = ImageTk.PhotoImage(image1)
            label1 = Label(image=test)
            label1.bind('<Button-1>', get_mouse_click_position(i, j))
            label1.image = test
            label1.place(x=matrix_squares[i][j].point_x, y=matrix_squares[i][j].point_y)

    position_direction_x = 1300
    position_direction_y = 550

    label_print = Label(root, text="Direction of the word")
    label_print.place(x=position_direction_x, y=position_direction_y - 30)
    label_print.config(font=("Courier", 10))

    variable_direction = StringVar(root)
    variable_direction.set(direction_word[0])
    global direction_cb
    direction_cb = OptionMenu(root, variable_direction, *direction_word, command=display_direction)
    direction_cb.place(x=position_direction_x, y=position_direction_y)

    variable_column = StringVar(root)
    variable_column.set(columnPositionCell[0])

    variable_line = StringVar(root)
    variable_line.set(linePositionCell[0])

    # canvas.pack()

    # player scores
    position_x_player_name = 850
    position_y_player_name = 20
    font_player_name = 30
    label_print = Label(root, text="Player One:")
    label_print.place(x=position_x_player_name, y=position_y_player_name)
    label_print.config(font=("Courier", font_player_name))
    label_print = Label(root, text="Player Two:")
    label_print.place(x=position_x_player_name, y=position_y_player_name + 60)
    label_print.config(font=("Courier", font_player_name))
    label_print = Label(root, text="Number Letters:")
    label_print.place(x=position_x_player_name, y=position_y_player_name + 120)
    label_print.config(font=("Courier", font_player_name))

    global points_label_player_one
    global points_label_player_two
    global number_letters_bag
    position_x_points = position_x_player_name + 300
    points_label_player_one = Label(root, text="0")
    points_label_player_one.place(x=position_x_points, y=position_y_player_name)
    points_label_player_one.config(font=("Courier", font_player_name))

    points_label_player_two = Label(root, text="0")
    points_label_player_two.place(x=position_x_points, y=position_y_player_name + 60)
    points_label_player_two.config(font=("Courier", font_player_name))

    number_letters_bag = Label(root, text=str(len(bag_with_all_letters)))
    number_letters_bag.place(x=position_x_points + 100, y=position_y_player_name + 120)
    number_letters_bag.config(font=("Courier", font_player_name))
    button_width = 15

    global word_by_user
    word_by_user = Entry(root, width=40)
    word_by_user.focus_set()
    word_by_user_pos_x = 850
    word_by_user_pos_y = 550
    word_by_user.place(x=word_by_user_pos_x, y=word_by_user_pos_y)
    label_print = Label(root, text="Enter your word:")
    label_print.place(x=word_by_user_pos_x, y=word_by_user_pos_y - 40)
    label_print.config(font=("Courier", 15))

    place_buttons_start_pos_x = 850
    place_buttons_start_pos_y = 700
    distance_between_buttons = 110
    global place_word_button
    place_word_button = ttk.Button(root, text="Place Word", width=button_width, command=place_word)
    place_word_button.place(x=place_buttons_start_pos_x, y=place_buttons_start_pos_y)

    global retry_letters_buttons
    retry_letters_buttons = ttk.Button(root, text="Retry Letters", width=button_width, command=retry_fun)
    retry_letters_buttons.place(x=place_buttons_start_pos_x + distance_between_buttons, y=place_buttons_start_pos_y)

    global take_letters_after_placed_word_button
    take_letters_after_placed_word_button = ttk.Button(root, text="Take Letters", width=button_width, command=take_letters)
    take_letters_after_placed_word_button.place(x=place_buttons_start_pos_x + 2 * distance_between_buttons,
                                                y=place_buttons_start_pos_y)

    global hide_letters_button
    hide_letters_button = ttk.Button(root, text="Hide Letters", width=button_width, command=hide_letters)
    hide_letters_button.place(x=place_buttons_start_pos_x + 3 * distance_between_buttons, y=place_buttons_start_pos_y)

    global finish_turn_buttons
    finish_turn_buttons = ttk.Button(root, text="Finish turn", width=button_width, command=finish_turn_fun)
    finish_turn_buttons.place(x=place_buttons_start_pos_x + 4 * distance_between_buttons, y=place_buttons_start_pos_y)
    global give_up_button
    give_up_button = ttk.Button(root, text="Give up", width=button_width, command=give_up_fun)
    give_up_button.place(x=place_buttons_start_pos_x + 5 * distance_between_buttons, y=place_buttons_start_pos_y)
    give_up_button["state"] = "disabled"
    finish_turn_for_ui()
    change_activity_buttons(s_place_word="enable", s_retry_letters="enable")

def give_up_fun():
    global turn_player, line_square_selected, column_square_selected, previous_square
    start_count = turn_player
    player_list[turn_player].has_given_up = True
    turn_player = (turn_player + 1) % max_players
    while player_list[turn_player].has_given_up is True and start_count != turn_player:
        turn_player = (turn_player + 1) % max_players
    if turn_player == start_count:
        change_activity_buttons()
        give_up_button["state"] = "disabled"
        index_player_with_max_points = -1
        max_points = -sys.maxsize - 1
        for i in range(len(player_list)):
            if player_list[i].points > max_points:
                index_player_with_max_points = i
                max_points = player_list[i].points
        label_error_message.config(text="Castigatorul este " + player_list[index_player_with_max_points].name)
        return

    hide_letters()
    finish_turn_for_ui()
    change_activity_buttons(s_place_word="enable", s_retry_letters="enable")
    label_error_message.config(text="Jucatorul anterior s-a dat batut Randul " + player_list[turn_player].name)
    line_square_selected = None
    column_square_selected = None
    previous_square = None
def hide_letters():
    x_hide = 850
    y_hide = 400
    count = 0
    for i in range(7):
        image1 = Image.open(f"Images/ResizeBackground.png")
        test = ImageTk.PhotoImage(image1)
        label1 = Label(image=test)
        label1.image = test
        label1.place(x=x_hide + count * 50, y=y_hide)
        count += 1
    label_error_message.config(text="Randul urmatorului player")
    change_activity_buttons(s_finish_turn="enable")


def finish_turn_for_ui():
    label_print = Label(root, text=player_list[turn_player].name)
    label_print.place(x=850, y=350)
    label_print.config(font=("Courier Bold", 15))
    show_letters_player(player_list[turn_player])


def create_list_with_class_letter(input_user):
    global dictionary_letters
    list_with_class_letter = list()
    for i in input_user:
        for j in dictionary_letters:
            if i == j.letter:
                list_with_class_letter.append(j)
                break
    return list_with_class_letter


def place_word():
    def is_input_user_build_with_valid_letters(input_user):
        global list_used_jokers
        list_used_jokers.clear()
        print(f"Input from isInputUserBuildWith {input_user}")
        place_word_list = list()
        copy_letters_player = player_list[turn_player].letters
        # print(copy_letters_player)
        copy_word = input_user
        for i in range(len(input_user)):
            for j in copy_letters_player:
                if input_user[i] == j.letter:
                    copy_word = copy_word.replace(input_user[i], "", 1)
                    place_word_list.append(j)
                    break
        if copy_word != "":
            for j in copy_letters_player:
                if j.letter == "_":
                    list_used_jokers.append(copy_word[0])
                    copy_word = copy_word.replace(copy_word[0], "", 1)
                    if copy_word == "":
                        break
        lista_output = list()
        for i in copy_letters_player:
            lista_output.append(i.letter)
        # print(lista_output)
        # print(inputUser)
        # created a word with other letters
        string_output = ""
        for i in place_word_list:
            string_output += i.letter
        print(f"Output {string_output}")
        if copy_word == "":
            label_error_message.config(text="Cuvantul nu este scris cu literele corecte")
            return True
        return False

    def check_new_letters_create_invalid_words(list_index_letters, direction):  # todo checking for later
        newWord = ""
        for line, column, letter in list_index_letters:
            print(f"linia {line} column {column} litera {letter}")
            newWord = ""
            if direction == "Vertical":
                find_left_index = column - 1
                if find_left_index >= 0:
                    while type(matrix_squares[line][find_left_index].is_blocked) is Letter:
                        newWord += matrix_squares[line][find_left_index].is_blocked.letter
                        find_left_index -= 1
                    newWord = newWord[::-1]
                newWord += letter
                findRightIndex = column + 1
                if findRightIndex <= 14:
                    while type(matrix_squares[line][findRightIndex].is_blocked) is Letter:
                        newWord += matrix_squares[line][findRightIndex].is_blocked.letter
                        findRightIndex += 1
                print(f"388 linia {line} column{column} leftIndex {find_left_index} rightIndex {findRightIndex}")
                if find_left_index + 1 != findRightIndex - 1:
                    list_new_words_for_player.append((line, find_left_index + 1, findRightIndex, "Horizontal"))
            else:
                find_left_index = line - 1
                if find_left_index >= 0:
                    while type(matrix_squares[find_left_index][column].is_blocked) is Letter:
                        newWord += matrix_squares[find_left_index][column].is_blocked.letter
                        find_left_index -= 1
                    newWord = newWord[::-1]
                newWord += letter
                findRightIndex = line + 1
                if findRightIndex <= 14:
                    while type(matrix_squares[findRightIndex][column].is_blocked) is Letter:
                        newWord += matrix_squares[findRightIndex][column].is_blocked.letter
                        findRightIndex += 1
                print(f"404 linie {line} column {column} leftIndex {find_left_index} rightIndex {findRightIndex}")
                if find_left_index + 1 != findRightIndex - 1:
                    list_new_words_for_player.append((find_left_index + 1, column, findRightIndex, "Vertical"))
            if newWord != letter and newWord not in dex:
                list_new_words_for_player.clear()
                string = "Nu exista cuvantul " + newWord
                label_error_message.config(text=string)
                return False
        return True

    def calculate_points_for_p_layer(listWords):
        points = 0
        listNewWords = list()

        for lineSquare, columnSquare, endPosition, direction in listWords:

            print(f"Calculam {points} {lineSquare} {columnSquare} {endPosition} {direction}")
            doubleWord = 0
            tripleWord = 0
            newWord = ""
            count = 0
            if direction == "Horizontal":
                for i in range(columnSquare, endPosition):
                    print(f"count {count}")
                    count += 1
                    newWord += matrix_squares[lineSquare][i].is_blocked.letter
                    copyLetterPoints = matrix_squares[lineSquare][i].is_blocked.points
                    points = points + copyLetterPoints
                    if matrix_squares[lineSquare][i].type_square == TypeCell.DOUBLE_LETTER:
                        points = points + copyLetterPoints
                    elif matrix_squares[lineSquare][i].type_square == TypeCell.TRIPLE_LETTER:
                        points = points + copyLetterPoints * 2
                    elif matrix_squares[lineSquare][i].type_square == TypeCell.DOUBLE_WORD:
                        doubleWord += 1
                    elif matrix_squares[lineSquare][i].type_square == TypeCell.TRIPLE_WORD:
                        tripleWord += 1
            else:
                for i in range(lineSquare, endPosition):
                    print(f"count {count}")
                    count += 1
                    newWord += matrix_squares[i][columnSquare].is_blocked.letter
                    copyLetterPoints = matrix_squares[i][columnSquare].is_blocked.points
                    points = points + copyLetterPoints
                    if matrix_squares[i][columnSquare].type_square == TypeCell.DOUBLE_LETTER:
                        points = points + copyLetterPoints
                    elif matrix_squares[i][columnSquare].type_square == TypeCell.TRIPLE_LETTER:
                        points = points + copyLetterPoints * 2
                    elif matrix_squares[i][columnSquare].type_square == TypeCell.DOUBLE_WORD:
                        doubleWord += 1
                    elif matrix_squares[i][columnSquare].type_square == TypeCell.TRIPLE_WORD:
                        tripleWord += 1
            for i in range(doubleWord):
                points *= 2
            for i in range(tripleWord):
                points *= 3
            listNewWords.append(newWord)
        player_list[turn_player].points += points
        if turn_player == 0:
            points_label_player_one.config(text=str(player_list[turn_player].points))
        else:
            points_label_player_two.config(text=str(player_list[turn_player].points))
        change_activity_buttons(s_take_letters="enable")
        succesMessage = "Cuvintele noi: "
        for i in listNewWords:
            succesMessage += i + " "
        succesMessage += "\nLuati litere noi"
        if len(list_used_jokers) > 0:
            succesMessage += " Ati folosit"
            for index, letter in enumerate(list_used_jokers):
                succesMessage += " joker" + str(index) + " pentru " + letter
        label_error_message.config(text=succesMessage)
        color_selection(previous_square[0], previous_square[1], '#F0F0F0')
        firstTurn = False

    def is_word_placement_valid(direction, lineSquare, columnSquare, limitSquarePlacement, inputUser):
        global list_new_words_for_player, first_turn
        print(f"is wordPLacementValid {inputUser}")

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
                while type(matrix_squares[lineSquare][startLine].is_blocked) is Letter:
                    print(matrix_squares[lineSquare][startLine].is_blocked)
                    newWord += matrix_squares[lineSquare][startLine].is_blocked.letter
                    startLine -= 1
            newWord = newWord[::-1]
            for i in range(columnSquare, limitSquarePlacement):
                print(f"linia {lineSquare} coloana {i} blocat {matrix_squares[lineSquare][i].is_blocked}")
                if type(matrix_squares[lineSquare][i].is_blocked) is Letter:
                    if inputUser[posString] != matrix_squares[lineSquare][i].is_blocked.letter:
                        label_error_message.config(text="Cuvantul dat nu se potriveste '\n'cu literele de pe tabla")
                        return False, ""
                    isConnected = True
                    newWord += inputUser[posString]
                    posString += 1
                    continue
                newWord += inputUser[posString]
                checkLettersForColision.append((lineSquare, i, inputUser[posString]))
                posString += 1
            endline = limitSquarePlacement
            if endline <= 14:
                while type(matrix_squares[lineSquare][endline].is_blocked) is Letter:
                    print(matrix_squares[lineSquare][endline].is_blocked)
                    newWord += matrix_squares[lineSquare][endline].is_blocked.letter
                    endline += 1
                if endline != limitSquarePlacement:
                    endline -= 1
            print(f"linie 517 {line_square_selected} {startLine + 1} {endline} {direction} {first_turn}")
            list_new_words_for_player.append((line_square_selected, startLine + 1, endline, direction))
        if direction == "Vertical":
            startLine = lineSquare - 1
            if startLine >= 0:
                while type(matrix_squares[startLine][columnSquare].is_blocked) is Letter:
                    print(matrix_squares[startLine][columnSquare].is_blocked)
                    newWord += matrix_squares[startLine][columnSquare].is_blocked.letter
                    startLine -= 1
            newWord = newWord[::-1]
            for i in range(lineSquare, limitSquarePlacement):
                print(f"linia {i} coloana {columnSquare} blocat {matrix_squares[i][columnSquare].is_blocked}")
                if type(matrix_squares[i][columnSquare].is_blocked) is Letter:
                    if inputUser[posString] != matrix_squares[i][columnSquare].is_blocked.letter:
                        label_error_message.config(text="Cuvantul dat nu se potriveste '\n'cu literele de pe tabla")
                        return False, ""
                    isConnected = True
                    newWord += inputUser[posString]
                    posString += 1
                    continue
                checkLettersForColision.append((i, columnSquare, inputUser[posString]))
                newWord += inputUser[posString]
                posString += 1
            endline = limitSquarePlacement
            if endline <= 14:
                while type(matrix_squares[endline][columnSquare].is_blocked) is Letter:
                    print(matrix_squares[endline][columnSquare].is_blocked)
                    newWord += matrix_squares[endline][columnSquare].is_blocked.letter
                    endline += 1
                if endline != limitSquarePlacement:
                    endline -= 1
            print(f"linie 548 {startLine + 1} {columnSquare} {endline} {direction} {first_turn}")
            list_new_words_for_player.append((startLine + 1, columnSquare, endline, direction))
        print(f"cuvant nou {newWord}")
        if newWord not in dex:
            string = "Nu exista cuvantul " + newWord
            label_error_message.config(text=string)
            return False, ""
        if newWord != inputUser or first_turn is True:
            isConnected = True

        print(f"{isConnected}")

        if len(checkLettersForColision) == 0:
            label_error_message.config(text="Nu ai folosit nicio litera noua")
            return False, ""
        if isConnected is False:
            label_error_message.config(text="Nu v-ati conectat la o litera")
            return False, ""
        wordForChecking = ""
        for line, column, letter in checkLettersForColision:
            wordForChecking += letter
        print(f"Litere noi {checkLettersForColision}")
        if first_turn is False:
            removeCollisionLetters = create_list_with_class_letter(wordForChecking)
        else:
            removeCollisionLetters = create_list_with_class_letter(newWord)
        stringOutput = list()
        for i in removeCollisionLetters:
            stringOutput.append(i.letter)
        print(f"literele ce au coliziune {stringOutput} playerturn {turn_player}")
        if check_new_letters_create_invalid_words(checkLettersForColision, direction) is False:
            return False, ""

        stringOutput.clear()
        isValid = is_input_user_build_with_valid_letters(wordForChecking)
        if isValid is False:
            return isValid, newWord
        for i in player_list[turn_player].letters:
            stringOutput.append(i.letter)
        print(f"Litere jucator {stringOutput}")
        for i in removeCollisionLetters:
            foundLetter = False
            for j in player_list[turn_player].letters:
                if j.letter == i.letter:
                    player_list[turn_player].letters.remove(j)
                    foundLetter = True
                    break
            if foundLetter is False:
                for _ in list_used_jokers:
                    for j in player_list[turn_player].letters:
                        if j.letter == "_":
                            player_list[turn_player].letters.remove(j)
                            break


        stringOutput = list()
        for i in player_list[turn_player].letters:
            stringOutput.append(i.letter)
        print(f"literele dupa ce au fost scoase {stringOutput} playerturn {turn_player}")
        first_turn = False
        return isValid, newWord

    def put_letters_on_board(listLetters):
        if direction_input == "Horizontal":
            indexColumn = column_square_selected
            for i in listLetters:
                image1 = Image.open(f"Images/Letters/{i.letter_pos}.png")
                test = ImageTk.PhotoImage(image1)
                label1 = Label(image=test)
                label1.image = test
                label1.bind('<Button-1>', get_mouse_click_position(line_square_selected, indexColumn))
                label1.place(x=matrix_squares[line_square_selected][indexColumn].point_x,
                             y=matrix_squares[line_square_selected][indexColumn].point_y)
                matrix_squares[line_square_selected][indexColumn].is_blocked = i

                indexColumn += 1
        else:
            indexLine = line_square_selected
            for i in listLetters:
                image1 = Image.open(f"Images/Letters/{i.letter_pos}.png")
                test = ImageTk.PhotoImage(image1)
                label1 = Label(image=test)
                label1.image = test
                label1.bind('<Button-1>', get_mouse_click_position(indexLine, column_square_selected))
                label1.place(x=matrix_squares[indexLine][column_square_selected].point_x,
                             y=matrix_squares[indexLine][column_square_selected].point_y)
                matrix_squares[indexLine][column_square_selected].is_blocked = i
                indexLine += 1

    global first_turn
    global list_new_words_for_player
    try:
        direction_input
    except NameError:
        label_error_message.config(text="Nu ati ales directia")
        return
    if direction_input == "Select direction":
        label_error_message.config(text="Nu ati ales directia")
        return
    try:
        line_square_selected
    except NameError:
        label_error_message.config(text="Nu ati ales patratul")
        return

    input1 = word_by_user.get()  # todo: use this case only the first turn

    # print(lineSquareSelected)
    # print(columnSquareSelected)
    # print(len(input1))
    # print(firstTurn)
    # print(lineSquareSelected > 7 or lineSquareSelected + len(input1) < 7)
    # print(columnSquareSelected)
    if line_square_selected is None:
        label_error_message.config(text="Nu ati ales patratul")
        return
    if direction_input == "Horizontal":
        if first_turn is True and (
                (column_square_selected > 7 or column_square_selected + len(input1) <= 7) or line_square_selected != 7):
            label_error_message.config(text="Trebuie sa va folositi de patratul din mijloc")
            return
    else:
        if first_turn is True and (
                (line_square_selected > 7 or line_square_selected + len(input1) <= 7) or column_square_selected != 7):
            label_error_message.config(text="Trebuie sa va folositi de patratul din mijloc")
            return

    limit_square = -1
    if direction_input == "Horizontal":
        limit_square = column_square_selected + len(input1)
    else:
        limit_square = line_square_selected + len(input1)
    # TODO de revizuit
    is_valid, show_new_word = is_word_placement_valid(direction_input, line_square_selected, column_square_selected, limit_square,
                                                   input1)
    print(f"isvalid {is_valid} listLetters {show_new_word}")
    if is_valid is False:
        return

    create_word_with_class_letter = create_list_with_class_letter(show_new_word)

    hide_letters()
    finish_turn_for_ui()

    print(create_word_with_class_letter)
    put_letters_on_board(create_word_with_class_letter)
    calculate_points_for_p_layer(list_new_words_for_player)
    list_new_words_for_player.clear()


def take_letters():
    string_new_letters = ""
    number_letters = 7 - len(player_list[turn_player].letters)
    copy_sample_player = list()
    if len(bag_with_all_letters) == 0:
        give_up_button["state"] = "enable"
    elif len(bag_with_all_letters) < number_letters:
        copy_sample_player = random.sample(bag_with_all_letters, len(bag_with_all_letters))
        give_up_button["state"] = "enable"
    else:
        copy_sample_player = random.sample(bag_with_all_letters, number_letters)
    if len(bag_with_all_letters) != 0:
        for i in copy_sample_player:
            player_list[turn_player].letters.append(i)
            string_new_letters = string_new_letters + i.letter
            string_new_letters += " "
            bag_with_all_letters.remove(i)

    show_letters_player(player_list[turn_player])
    change_activity_buttons(s_hide_letters="enable")
    label_error_message.config(
        text="Lierele noi sunt " + string_new_letters + "\nAscundeti literele ca sa vina urmatorul player")
    number_letters_bag.config(text=str(len(bag_with_all_letters)))


def retry_fun():
    for i in player_list[turn_player].letters:
        bag_with_all_letters.append(i)

    player_list[turn_player].letters.clear()
    copy_sample_player = random.sample(bag_with_all_letters, 7)
    for i in copy_sample_player:
        player_list[turn_player].letters.append(i)
        bag_with_all_letters.remove(i)
    show_letters_player(player_list[turn_player])
    try:
        color_selection(previous_square[0], previous_square[1], '#F0F0F0')
    except NameError as e:
        pass
    except TypeError as e:
        pass

    change_activity_buttons(s_hide_letters="enable")
    label_error_message.config(text="Ati luat litere noi. \nAscundeti literele si lasati urmatorul player")


def change_activity_buttons(s_place_word="disabled", s_retry_letters="disabled", s_take_letters="disabled",
                            s_hide_letters="disabled", s_finish_turn="disabled"):
    list_input = [s_place_word, s_retry_letters, s_take_letters, s_hide_letters, s_finish_turn]
    for sir in list_input:
        if sir not in ["disabled", "normal", "enable"]:
            return
    # TODO: testing passed, decomment when it is done
    place_word_button["state"] = s_place_word
    retry_letters_buttons["state"] = s_retry_letters
    take_letters_after_placed_word_button["state"] = s_take_letters
    hide_letters_button["state"] = s_hide_letters
    finish_turn_buttons["state"] = s_finish_turn


def finish_turn_fun():
    global turn_player, line_square_selected, column_square_selected, previous_square
    turn_player = (turn_player + 1) % max_players
    hide_letters()
    finish_turn_for_ui()
    change_activity_buttons(s_place_word="enable", s_retry_letters="enable")
    label_error_message.config(text="Randul " + player_list[turn_player].name)
    line_square_selected = None
    column_square_selected = None
    previous_square = None


def show_letters_player(player):
    count = 0
    show_letters_x = 850
    show_letters_y = 400
    for i in player.letters:
        index_imagine = ord(i.letter) - ord("a")
        image1 = Image.open(f"Images/Letters/{index_imagine}.png")
        test = ImageTk.PhotoImage(image1)
        label1 = Label(image=test)
        label1.image = test
        label1.place(x=show_letters_x + count * 50, y=show_letters_y)
        count += 1


root = Tk()
root.title("Scrabble")
root.geometry("800x600")
root.configure(bg='#315399')
frame = Frame(root, width=800, height=600)

dictionary_letters = list()
take_letters_for_player = 7
dex = list()
bag_with_all_letters = list()
matrix_squares = list(list())
# TODO: insert better starting message
direction_word = ["Select direction", "Horizontal", "Vertical"]
linePositionCell = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
columnPositionCell = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
list_used_jokers = list()
turn_player = 0
max_players = 2
mouseClickX, mouseClickY = -1, -1
initialize_dex()
initialize_all_letters()
player1 = Player("Player 1", 0, random.sample(bag_with_all_letters, 7))
player2 = Player("Player 2", 0, random.sample(bag_with_all_letters, 7))
player_list = [player1, player2]
# TODO: change to true for final project
first_turn = True
list_new_words_for_player = list()

initialize_background()

root.mainloop()

# if __name__ == '__main__':
#   print("hello")
