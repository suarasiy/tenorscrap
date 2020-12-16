import json
from tenorscrap import Tenor

tenor = Tenor()
tenor.search("Spongebob Squarepants", limit=3)
print(tenor.result())

data = json.loads(tenor.result())
