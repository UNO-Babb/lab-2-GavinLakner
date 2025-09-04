#Magic8Ball.py
#Name: Gavin Lakner
#Date: 9/4/2025
#Assignment: Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
answers = [ "Why not" , "Go For IT" , "Might As Well" , "Heck No" , "That's A Silly Question" , "You Know The Answer" , "Trust Your Gut" , 
           "Meh" , "Woah There" , "Go Fishing Instead" , "Let Me Think About It" , "I'd Reconsider" , "Maybe Next Time" , "Goodluck" , "Ask Ai" , 
           "Flip A Coin" , "Try Meditating For Your Answer" , "Does Money Grow On Trees?" ,] 
  #Answer question randomly with one of the options from your earlier list.

length = len(answer) 
r = random.random()
r = int(r) 

print(r)
response = answers[r]
print(response)
if __name__ == '__main__':
  main()
