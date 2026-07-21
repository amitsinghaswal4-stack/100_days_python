#Here we use our decorator function 

def my_decorator(say_hello):
  def wrapper():
    print("something before function")
    say_hello()
    print("something after function")
  return wrapper

@my_decorator
def say_hell():
  print("hi how are you")

say_hell()