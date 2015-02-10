class Dance():
  def jamesdance(self, dancestyle):
    answer = ""
    dance = dancestyle
    if dance == "Boogaloo":
        answer = "Boogaloo"
    elif dance == "CamelWalk":
        answer = "CamelWalk"
    elif dance == "FunkyChicken":
        answer = "FunkyChicken"
    elif dance == "MashedPotatoes":
        answer = "MashedPotatoes"
    elif dance == "Robot":
        answer = "Robot"
    else:
        answer = "Weird"
    return answer
