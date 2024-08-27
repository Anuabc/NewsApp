import requests

# Word
my_word = "abysmal"

# Get Info
req = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{my_word}")

# Print result
data = req.json()

for i in data[0]['meanings']:
  print(i['partOfSpeech'])
  for j in i['definitions']:
    print(j['definition'])
  print()