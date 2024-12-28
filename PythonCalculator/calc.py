from tkinter import *
import math
from pygame import mixer
import speech_recognition as sr

mixer.init()

def click(value):
    ex = entryField.get()
    answer = ''
    
    try:
        if value == 'C':
            ex = entryField.get()
            ex = ex[0:len(ex)-1]
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return
        
        elif value == 'CE':
            entryField.delete(0, END)
        
        elif value == '√':
            answer = math.sqrt(eval(ex))
        
        elif value == 'π':
            answer = math.pi
        
        elif value == 'Cos θ':
            answer = math.cos(math.radians(eval(ex)))
        
        elif value == 'Sin θ':
            answer = math.sin(math.radians(eval(ex)))
        
        elif value == 'Tan θ':
            answer = math.tan(math.radians(eval(ex)))
        
        elif value == '2π':
            answer = 2 * math.pi
        
        elif value == 'Cosh':
            answer = math.cosh(eval(ex))
        
        elif value == 'Sinh':
            answer = math.sinh(eval(ex))
        
        elif value == 'Tanh':
            answer = math.tanh(eval(ex))
        
        elif value == '∛':
            answer = eval(ex) ** (1/3)
        
        elif value == 'x\u02b8':
            entryField.insert(END, '**')
            return
        
        elif value == 'x³':
            answer = eval(ex) ** 3
        
        elif value == ' x²':
            answer = eval(ex) ** 2
        
        elif value == 'ln':
            answer = math.log2(eval(ex))
        
        elif value == 'deg':
            answer = math.degrees(eval(ex))
        
        elif value == 'rad':
            answer = math.radians(eval(ex))
        
        elif value == 'e':
            answer = math.e
        
        elif value == 'log':
            answer = math.log10(eval(ex))
        
        elif value == 'x!':
            answer = math.factorial(eval(ex))
        
        elif value == '/':
            entryField.insert(END, "/")
            return
        
        elif value == '=':
            answer = eval(ex)
        
        else:
            entryField.insert(END, value)
            return
        
        entryField.delete(0, END)
        entryField.insert(0, answer)
    
    except SyntaxError:
        entryField.delete(0, END)
        entryField.insert(0, 'Syntax Error')
    except ValueError:
        entryField.delete(0, END)
        entryField.insert(0, 'Value Error')

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b 

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

def lcm(a, b):
    return math.lcm(a, b)

def hcf(a, b):
    return math.gcd(a, b)

operations = {
    'ADD': add, 'ADDITION': add, 'SUM': add, 'PLUS': add,
    'SUBTRACT': sub, 'DIFFERENCE': sub, 'MINUS': sub, 'SUBTRACTION': sub,
    'PRODUCT': mul, 'MULTIPLICATION': mul, 'MULTIPLY': mul,
    'DIVISION': div, 'DIV': div, 'DIVIDE': div,
    'LCM': lcm, 'HCF': hcf, 'MOD': mod, 'REMAINDER': mod, 'MODULUS': mod
}

number_words = {
    'ZERO': 0, 'ONE': 1, 'TWO': 2, 'THREE': 3, 'FOUR': 4, 'FIVE': 5,
    'SIX': 6, 'SEVEN': 7, 'EIGHT': 8, 'NINE': 9, 'TEN': 10,
    'ELEVEN': 11, 'TWELVE': 12, 'THIRTEEN': 13, 'FOURTEEN': 14, 'FIFTEEN': 15,
    'SIXTEEN': 16, 'SEVENTEEN': 17, 'EIGHTEEN': 18, 'NINETEEN': 19, 'TWENTY': 20
}

def findNumbers(text_list):
    numbers = []
    for word in text_list:
        if word.isdigit():
            numbers.append(int(word))
        elif word.upper() in number_words:
            numbers.append(number_words[word.upper()])
    return numbers 

def audio():
    mixer.music.load('music1.mp3')
    mixer.music.play()
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        try:
            recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            voice = recognizer.listen(mic)
            text = recognizer.recognize_google(voice)
            mixer.music.load('music2.mp3')
            mixer.music.play()
            text_list = text.split(' ')
            for word in text_list:
                if word.upper() in operations:
                    numbers = findNumbers(text_list)
                    if len(numbers) >= 2:
                        result = operations[word.upper()](numbers[0], numbers[1])
                        entryField.delete(0, END)
                        entryField.insert(END, result)
                        break
                else:
                    pass
        except sr.UnknownValueError:
            entryField.delete(0, END)
            entryField.insert(0, 'Could not understand the audio')
        except sr.RequestError:
            entryField.delete(0, END)
            entryField.insert(0, 'Request Error')
        except Exception as e:
            entryField.delete(0, END)
            entryField.insert(0, str(e))

root = Tk()
root.title('Scientific Calculator')
root.config(bg='SlateGray3')
root.geometry('680x486+100+100')

logoImage = PhotoImage(file='logo.png')
logoLabel = Label(root, image=logoImage, bg='SlateGray3')
logoLabel.grid(row=0, column=0)

entryField = Entry(root, font=('arial', 20, 'bold'), bg='mint cream', fg='Black', bd=10, relief=SUNKEN, width=30)
entryField.grid(row=0, column=0, columnspan=8)

micImage = PhotoImage(file='microphone.png')
micButton = Button(root, image=micImage, bd=0, bg='SlateGray3', activebackground="SlateGray3", command=audio)
micButton.grid(row=0, column=7)

button_text_list = ["C", "CE", "√", "+", "π", "Cos θ", "Sin θ", "Tan θ",
                    "1", "2", "3", "-", "2π", "Cosh", "Sinh", "Tanh",
                    "4", "5", "6", "*", " ∛", "x\u02b8", "x³", " x²",
                    "7", "8", "9", "/", "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log", "(", ")", "x!"]

rowvalue = 1
columnvalue = 0
for i in button_text_list:
    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='SlateGray3', fg='Black', font=('arial', 18, 'bold'), activebackground='SlateGray3', command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=1)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0

root.mainloop()
