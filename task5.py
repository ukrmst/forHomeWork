i = input(str("Введіть рядок: "))
vowels = ["а", "е", "и", "і", "о", "у", "я", "ю", "є", "ї"]
result = ""


for word in i.split(' '):
    if word.endswith(tuple(vowels)):
        word = word[:-1] + word[-1:].upper()
    result = result + word + " "        
        
print(result)
        