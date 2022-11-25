NAMES_PATH = 'Input/Names/invited_names.txt'
LETTER_PATH = 'Input/Letters/starting_letter.txt'
OUTPUT_PATH = 'Output/ReadyToSend'


with open(NAMES_PATH) as f:
  names = list(map(lambda _: _.strip(), f.readlines()))

with open(LETTER_PATH) as f:
  template = f.read()
  for name in names:
    with open(f"{OUTPUT_PATH}/letter_for_{name}.txt", 'w') as f:
      f.write(template.replace("[name]", name))
