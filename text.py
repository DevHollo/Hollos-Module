from hollosmodule import Text

text = Text()

for i in range(1, 300+1):
    print("\n\n\n")

print(text.red('red text'))
print(text.black("------"))
print(text.orange('orange text'))
print(text.black("------"))
print(text.yellow('yellow text'))
print(text.black("------"))
print(text.green('green text'))
print(text.black("------"))
print(text.blue('blue text'))
print(text.black("------"))
print(text.purple('purple text'))
print(text.black("------"))
print(text.cyan('cyan text'))
print(text.black("------"))
print(text.pink('pink text'))
print(text.black("------"))
print(text.custom_rgb('custom rgb text', (212,175,55)))
print(text.black("------"))
print(text.italic('italic text'))
print(text.black("------"))
print(text.bold('bold text'))
print(text.black("------"))
print(text.strikethrough('strikethrough text'))
print(text.black("------"))
print(text.blink('blinking text'))
print(text.black("------"))
print(text.underline('underlined text'))