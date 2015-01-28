class James():
  def ask(self, sentence):
    answer = ''
    sentence = sentence.strip()
    if sentence == "":
      answer = "Weird"
    elif sentence == "Are You Somebody?":
      answer = "Damn right. I am somebody"
    elif sentence == sentence.upper() and sentence != sentence.lower():
      answer = "Woah"
    elif sentence[-1] == "?":
        answer = 'Sure'
    else:
      answer = "Whatever"
    return answer
