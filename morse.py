converstions = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 
                'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 
                'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 
                'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 
                'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 
                'Z':'--..', '1':'.----', '2':'..---', '3':'...--', 
                '4':'....-', '5':'.....', '6':'-....', '7':'--...', 
                '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', 
                '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', 
                '(':'-.--.', ')':'-.--.-', '':''}
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ': 
            cipher += converstions[letter] + ' '
        else:
            cipher += ' ' 
    return cipher
def decrypt(message):
    message += ' '   
    decipher = ''    
    citext = ''
    for letter in message:
        if letter != ' ':
            i = 0 
            citext += letter 
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(converstions.keys())[list(converstions.values()).index(citext)]
                citext = ''
    return decipher
def main():
  eorm = int(input('\nMorse Code Converter\n\nWould you like to convert from \n(1) English to Morse\nor\n(2) Morse to English\nor\n(3) Morse to English **For Dummies**\n'))
  if eorm == 1:
    message = str(input('\n\nPlease print your message in ENGLISH below:\n'))
    print(encrypt(message.upper()) + '\n')
  elif eorm == 2:
    message = str(input('\n\nPlease print your message in MORSE below:\n'))
    print(decrypt(message.upper()) + '\n')
  elif eorm == 3:
    print(converstions)
    message = str(input('\n\nPlease print your message in MORSE below:\n'))
    print(decrypt(message.upper()) + '\n')
  else:
    return main()
while 1: 
  main()
  again = input('Would you like to continue the program? Y/N\n')
  if again in 'Yy':
    continue
  elif again in 'Nn':
    print('\nThank you\nGoodbye')
    break