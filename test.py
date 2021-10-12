from os import link
import requests,sys,webbrowser,bs4,time

print('Googling...')
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
time.sleep()
res.raise_for_status()

#Retrieve top search result links
soup = bs4.BeautifulSoup(res.text)

#Open a browser tab for each result
link_elems = soup.select('.r a')
num_open = min(5,len(link_elems))
for i in range(num_open):
    webbrowser.open('http://google.com'+link_elems[i].get('href'))
time.sleep()