from hollosmodule import Text

text = Text()

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

print(text.black("------"))

print(text.reverse('reversed text'))

print(text.black("------"))

print(f"Human readable number: {text.to_human_readable_number(100000000000000)}")