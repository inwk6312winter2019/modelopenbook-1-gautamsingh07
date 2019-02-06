with open('running-config.cfg', "w") as file:

for words in file():
 replace= file.read() . replace('192', 10)
 replace= file.read() . replace('172', 10)

file.write(replace)
