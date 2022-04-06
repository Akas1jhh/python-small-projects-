print('welcome to the quiz game')

playing = input("Do you want to play? ")

score = 0

if playing.lower() != 'yes':
  quit()

print('All question of 1 marks ')

answer = input("Capital of India? ").lower()
if answer == 'delhi':
  print('correct answer')
  score += 1
else:
  print('wrong answer')  

answer = input("prime minister of India? ").lower()
if answer == 'narendra modi':
  print('correct answer')
  score += 1
else:
  print('wrong answer') 

answer = input("National animal of India? ").lower()
if answer == 'tiger':
  print('correct answer')
  score += 1
else:
  print('wrong answer')     

answer = input("most played game of India? ").lower()
if answer == 'cricket':
  print('correct answer')
  score += 1
else:
  print('wrong answer')   

print("you got " + str(score) + " question correct ")  
print("you got " + str((score/4) * 100) +"%.")