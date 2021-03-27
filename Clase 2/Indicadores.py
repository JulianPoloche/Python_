from urllib.request import Request ,urlopen
from pyquery import PyQuery

class Indicadores():

    def indicadoresEconomicos(self):
            req = Request('https://www.dane.gov.co/index.php/indicadores-economicos',None,{'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
            contet = urlopen(req).read()
          ##  print(contet)
            pq = PyQuery(contet)

            trm = str([i.text() for i in pq('table').eq(1)('h1').items()][0]).replace('$','').replace('.','').replace(',','.')
            
            return trm