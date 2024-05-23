import random

words  = ['chicken', 'cloud', 'python', 'computer', 'book']
word= random.choice(words)
hidden_word = ["_"]*len(word)
print(word)



guess_count = 0
max_guess = 5
while '_' in hidden_word and guess_count < max_guess: 
  guess  = input("Guess a letter: ")
  if guess in hidden_word:
    print('Bu harfi zaten tahmin ettiniz.')
    continue
  guess_count += 1
  for i, letter in enumerate(word):
    if letter == guess:
      hidden_word[i]= letter
      guess_count = guess_count - 1       
    continue
  print(' '.join(hidden_word))   # join the letters into one string with spaces


if '_' not in hidden_word:
    print(f'Tebrikler, sözcüğü tahmin ettiniz! Sözcük: {word}')
else:
    print(' '.join(hidden_word))
    print('Maalesef, sözcüğü tahmin edemediniz. Tahmin hakkınız kalmadı.')
