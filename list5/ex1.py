import html.parser
import urllib.request

def pobierz_strone(adres):
    try:
        with urllib.request.urlopen(adres) as dane:
            return str(dane.read())
    except Exception:
        print ('Niepowodzenie')
        return None

def parsuj_strone(strona):
    hs = []
    class MyHTMLParser(html.parser.HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag == 'a':
                for (atr, val) in attrs:
                    if atr == 'href': 
                        hs.append(val)
    parser = MyHTMLParser()
    parser.feed(strona)
    return hs 

def przeszukaj_strone(f, adres, d, odwiedzone):
    if (d < 1): 
        return
    if adres in odwiedzone: 
        return
    odwiedzone.append(adres)
    strona = pobierz_strone(adres)
    if (strona == None): 
       return
    yield f(strona)
    hs = parsuj_strone(strona)
    for adr in hs:
        yield from przeszukaj_strone(f, adr, d-1, odwiedzone)

def pyton(strona):
    zdania = []
    class MyHTMLParser(html.parser.HTMLParser):
        def handle_data(self, dane):
            if 'Python' in dane:
                zdania.append(dane)
    myparser = MyHTMLParser()
    myparser.feed(strona)
    return zdania

def wypisz(f, adres, d):
    for zdania in przeszukaj_strone(f, adres, d, []):
        for zdanie in zdania: 
            print(zdanie)

wypisz(pyton, "https://www.python.org/", 1)