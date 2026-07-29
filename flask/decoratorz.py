def make_bold(fn):
    def wrap():
         return f'<b>{fn()}</b>'
    return wrap

def make_underline(fn):
     def wrap():
          return f'<u>{fn()}</u>'
     return wrap