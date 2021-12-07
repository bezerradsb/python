def primo(n):
  d = n
  while n > 2:
    n = n - 1
    if d % n == 0:
      return False
  return True

def maior_primo(b):
    while primo(b) == False:
        b = b - 1
    print(b)
