class Journal:
  def __init__(self, type, tag):
    self.type = type; self.tag = tag
  def log(self, msg):
    print("%s(%s) - %s" % (self.type, self.tag, msg))

def warning(tag): return Journal('warning', tag) 
def info(tag): return Journal('info', tag) 
