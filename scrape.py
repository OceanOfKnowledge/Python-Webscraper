from bs4 import BeautifulSoup
import requests
import csv

#make http request and convert to html text
source = requests.get('http://coreyms.com').text

#parse text into BeautifulSoup using lxml parser
soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

#Scrape the the returned data
for article in soup.find_all('article'):

	headline = article.h2.a.text.encode('utf8')
	print(headline)

	summary = article.find('div', class_='entry-content').p.text.encode('utf8')
	print(summary)

	try:		
		vid_src = article.find('iframe', class_='youtube-player')['src']

		vid_id = vid_src.split('/')[4]

		vid_id = vid_id.split('?')[0]

		yt_link = "https://youtube.com/watch?v={}".format(vid_id)
	except Exception as e:
		yt_link = None

	print(yt_link)

	print("")

	csv_writer.writerow([headline, summary, yt_link])
csv_file.close()
