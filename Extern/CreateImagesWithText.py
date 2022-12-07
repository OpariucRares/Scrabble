from PIL import Image, ImageFont, ImageDraw, ImageTk

# TODO take the points from the dictionary template

letterPoints = [{"I": 1}, {"A": 1}, {"E": 1}, {"T": 1}, {"N": 1}, {"R": 1}, {"S": 1}, {"C": 1}, {"L": 1}, {"U": 1},
                {"O": 2}, {"P": 2}, {"D": 3}, {"M": 4}, {"F": 4}, {"V": 4}, {"B": 5}, {"G": 6}, {"H": 8}, {"Z": 8},
                {"J": 10}, {"X": 10}, {"W": 0}, {"Y": 0}, {"K": 0}, {"Q": 0}]

#img = Image.open(r"../Images/Letters/EmptyLetter.png") #background image
letterFont = ImageFont.truetype('../Images/Examples/Arimo-VariableFont_wght.ttf', 400)
pointsFont = ImageFont.truetype('../Images/Examples/Arimo-VariableFont_wght.ttf', 80)

sizeImage = 50
for i in letterPoints:
    copy = Image.open(r"../Images/Examples/EmptyLetter.png")
    I1 = ImageDraw.Draw(copy)
    letter = ""
    points = -1
    for key, value in i.items():
        letter = key
        points = value
    I1.text((60, 0), f"{letter}", font=letterFont, fill=(2, 99, 107))
    I1.text((365, 350), f"{points}", font= pointsFont, fill=(2, 99, 107))
    nameImage = ord(letter.lower()) - ord("a")
    copy.save(f"../Images/Letters/{nameImage}.png", 'PNG')
    image = Image.open(f"../Images/Letters/{nameImage}.png")
    copy = image.resize((sizeImage, sizeImage))
    copy.save(f"../Images/Letters/{nameImage}.png", 'PNG')

image = Image.open("../Images/Examples/EmptyLetter.png")
copy = image.resize((sizeImage, sizeImage))
copy.save(f"../Images/Letters/-2.png", 'PNG') #blank letter

otherCells = ["EmptyCell", "DoubleLetter", "DoubleWord", "TripleLetter", "TripleWord", "Start", "Background"]
for i in otherCells:
    image = Image.open(f"../Images/Examples/{i}.png")
    copy = image.resize((sizeImage, sizeImage))
    copy.save(f"../Images/Resize{i}.png", 'PNG')
