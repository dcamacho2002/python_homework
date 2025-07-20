# Write your code here.

#Task 1
def hello():
    return "Hello!"

print(hello())

#Task 2
def greet(name):
    return f"Hello, {name}"

print(greet("David"))

#Task 3
def calc(a, b, operation = "multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

print(calc(3, 3, "divide"))           

#Task 4
def data_type_conversion(value, dataName):
    try:
        if dataName == "float":
            return float(value)
        elif dataName == "str":
            return str(value)
        elif dataName == "int":
            return int(value)
    except ValueError:
        return f"You can't convert {value} into a {type}."
    
print(data_type_conversion(100, "float"))

#Task 5
def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except:
        return "Invalid data was provided."
    
print(grade(91, 73, 84, 96))

#Task 6
def repeat(string, count):
    result = ""
    for i in range(count):
        result += string
    return result

print(repeat("Hello", 3))

#Task 7

def student_scores(bestMean, **kwargs):
    if bestMean == "best":
        return max(kwargs, key = kwargs.get)
    elif bestMean == "mean":
        return sum(kwargs.values()) / len(kwargs)
    
print(student_scores("mean", David = 90, Adam = 93, Tim = 87))

#Task 8
def titleize(string):
    littleWords =  "a", "on", "an", "the", "of", "and", "is", "in"
    words = string.split()
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in littleWords: 
            words[i] = word.capitalize()
    return " ".join(words)

print(titleize("star wars: return of the jedi")) 

#Task 9
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result    

print(hangman("David", "ai"))

#Task 10
def pig_latin(sentence):
    words = sentence.split()
    result = []
    for word in words:
        if word[0] in "aeiou":
            result.append(word + "ay")
        elif word[0] == "q" and word[1] == "u":
            result.append(word[2:] + "quay")
        else:
            consonants = ""
            for letter in word:
                if letter in "aeiou":
                    break
                else:
                    consonants += letter
            result.append(word[len(consonants):] + consonants + "ay")
    return " ".join(result)

print(pig_latin("quick awesome shark"))
