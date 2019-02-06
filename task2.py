with open('running-config.cfg', "w") as file:

for words in file():
 replace= file.read() . replace('192', 10)
 replace= file.read() . replace('172', 10)
 replace= file.read() . replace('255.255.0.0', '255.0.0.0')
 replace= file.read() . replace('255.255.255.0', '255.0.0.0')

file.write(replace)
