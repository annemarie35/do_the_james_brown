class James():
  def ask(self, sentence):
    answer = ''
    sentence = sentence.strip()
    if sentence == "Are You Somebody?":
      answer = "Damn right. I am somebody"
    elif sentence == "How are you?":
      answer = "I feel Good !"
    else:
      answer = "Whatever"
    return answer
