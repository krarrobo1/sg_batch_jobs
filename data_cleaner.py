import unicodedata
# Normalise (normalize) unicode data in Python to remove umlauts, accents etc. 
def normalize(text):
    text = text.upper()
    normalized = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore')
    return normalized.decode('utf-8').strip()
 
# Removes connectors, and replace with '-'.
def id_maker(raw):
    raw = raw.lower()
    connectors = [' y ', ' o ', ' de ', ' la ', ' e ', ' u ', ' del ', ', ']
    for connector in connectors:
        idx = raw.find(connector)
        if(idx > 0):
            raw = raw.replace(connector,' ')

    return raw.replace(' ','-')