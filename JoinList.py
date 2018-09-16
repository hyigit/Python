sentence = ['Python', 'has', 'officially', 'been', 'searched', 'on', 'google', 'more', 'times', 'than', 'Michael', 'Jordan', 'in', '2018.']
#print(sentence)

#Uzun yol
final = ''
for word in sentence:
  final += word + ' '
#print(final)

#Join metodu ile kısa yol
final = ' '.join(sentence)
print(final)
