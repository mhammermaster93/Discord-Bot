import random

def get_response(message: str) -> str:
  p_message = message.lower()
  if p_message == 'hello':
    return 'hey!'
  if p_message == 'roll':
    #rolls a dice between one and six
    return str(random.randint(1,6))
  if p_message == '!help':
    return 'This is a standard help message you can modify'

  return 'I didn\'t understand what you wrote' + 'try typing !help'