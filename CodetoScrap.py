from bs4 import BeautifulSoup
import requests
import csv
csv_file=open('csv_output_scrape.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['sno','Title','Date','Description','Link'])
source=requests.get("https://coreyms.com/").text
soup=BeautifulSoup(source,'lxml')
# print(soup.prettify())
# print(soup.title.text)
i=0
for article in soup.findAll('article'):

    heading=article.find('a',class_='entry-title-link').text
    date=article.find('time',class_='entry-time').text
    summary=article.find('div',class_='entry-content').p.text
    try:
        video_link=article.find('iframe',class_='youtube-player')['src']
    except:
        video_link = None
    i=i+1
    print(i)
    print(heading)
    print(date)
    print(summary)
    print(video_link)
    print('---------------------------------------------')
    csv_writer.writerow([i,heading,date,summary,video_link])

csv_file.close()