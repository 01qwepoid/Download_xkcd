import os, webbrowser, bs4, requests

url = 'https://www.xkcd.com/10'
os.makedirs('C:\\Users\\Shubham\\Desktop\\Python Automate\\xkcd',exist_ok=True)

while not url.endswith('#'):
	#-------TODO (Download the page)
	print('Downlaoding the page %s... ' % url)
	res=requests.get(url)                  #requests.get(url) generates a txt file which can then be worked upon by bs4
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text)

	#-------TODO (Find Url of image)
	comicelem = soup.select('#comic img')
	if comicelem==[]:
		print('Could not find comic image.')
	else:
		comicurl = 'https:' + comicelem[0].get('src')

	#-------TODO (Download image)
		print('Downloading image %s ...' %(comicurl))
		res=requests.get(comicurl)
		res.raise_for_status()

	#-------TODO (Save image to folder ./xkcd)
	imagefile = open(os.path.join('C:\\Users\\Shubham\\Desktop\\Python Automate\\xkcd',os.path.basename(comicurl)),'wb')
	for chunk in res.iter_content(100000):
		imagefile.write(chunk)
	imagefile.close()

	#-------TODO (Get previous button's url)
	prevlink = soup.select('a[rel="prev"]')[0]  
	url = 'https://www.xkcd.com'+prevlink.get('href')

print('Done !')



