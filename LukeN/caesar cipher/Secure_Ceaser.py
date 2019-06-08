#!/usr/bin/python3
import hashlib

def isWord(inp):
  File=open("Words.txt","r")
  word=inp.rstrip().split(" ")
  for line in File:
    if line.rstrip().lower() in word:
      return True
  return False


def encrypt(message,Key):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  newmessage = ''
  for character in message:
    if character in alphabet:
      position = alphabet.find(character)
      newposition = (position + int(Key)) % 26
      newcharacter = alphabet[newposition]
      #print('The New Character is:', newcharacter)
      newmessage += newcharacter
    elif character in Alphabet:
      position = Alphabet.find(character)
      newposition = (position + int(Key)) % 26
      newcharacter = Alphabet[newposition]
      #print('The New Character is:', newcharacter)
      newmessage += newcharacter
    else:
      newmessage += character
  return newmessage
  
  
  
def decrypt(message,Key):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  newmessage = ''
  for character in message:
    if character in alphabet:
      position = alphabet.find(character)
      newposition = (position - int(Key)) % 26
      newcharacter = alphabet[newposition]
      #print('The New Character is:', newcharacter)
      newmessage += newcharacter
    elif character in Alphabet:
      position = Alphabet.find(character)
      newposition = (position - int(Key)) % 26
      newcharacter = Alphabet[newposition]
      #print('The New Character is:', newcharacter)
      newmessage += newcharacter
    else:
      newmessage += character
      
  return newmessage

def force_decrypt(message):
  for Key in range(1,26):
    if isWord(decrypt(message.lower(),Key)):
      print(decrypt(message.lower(),Key))

def user(username,password):
  username1=input('Please enter your Username: ')
  if username1==username:
    password1=input('Please enter your Password: ')
    if hashlib.sha512(password1.encode('utf-8')).hexdigest()==password:
      while True:
        mode=input('input mode: ')
        if mode=='encrypt':
          text=input('input message: ')
          while True:
            key=input('Please enter the encryption key: ')
            key=int(key)
            if key in range(1,26):
              break
            else:
              print('ERORR: invalid input')
          print('Your new message is {}'.format(encrypt(text,key)))
        elif mode=='decrypt':
          print('Your new message is {}'.format(decrypt(input('input message'),input('Please enter the encryption key'))))
        elif mode=='exit':
          break
        elif mode.lower()=='force decrypt':
          force_decrypt(input('input message: '))
        else:
          print('ERORR: invalid input')
    else:
      print('Incorrect')
      
try:
	File=open("Login.txt","r")
	loop = 1
	for line in File:
		if loop == 1:
			Username = line.rstrip()
		else:
			Password = line.rstrip()
		loop += 1
except:
	Username=input("Set Username: ")
	Password=hashlib.sha512(input("Set Password: ").encode('utf-8')).hexdigest()
	File=open("Login.txt","w")
	File.write("{}\n{}\n".format(Username, Password))
	File.close()
user(Username, Password)
