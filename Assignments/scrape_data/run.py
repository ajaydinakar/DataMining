#*********************************************************************************
#             Ajay Dinakar Kandavalli
#             CMPS-5443 Data mining
#                 Assignment-1   
#         Scraping Data from a website     
#              Language :python3,
#   website choosed is www.allaboutcircuits.com(embedded systems projects website)  
#*********************************************************************************
#importing libraries
import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

f=open("projects.csv","w")
f.write("project Name, Published Time, Year, Author \n")
#interating multiple pages and
#getting the url stored in variable
for WPagenumb in range( 0, (5+1)*20, 20)[0:]:#as each page is multiple of 20
    WPagenumb=str(WPagenumb)                      #ex:p20,p40,p60 etc in url
    #first webpage
    if WPagenumb is 0:
        url="https://www.allaboutcircuits.com/projects/category/embedded/"
    #pages other than first webpage    
    else:    
        url="https://www.allaboutcircuits.com/projects/category/embedded/"+ "P" + WPagenumb + "/"
#opening connection and accessing the web page
    uclient=ureq(url)
    page_html=uclient.read()
    uclient.close()
#parse the html data
    page=soup(page_html,"html.parser")
    projects=page.findAll("div",{"class":"row archive-container"})
    
    for project in projects:
        projectTitle=(project.findNext("div",{"class":"col-lg-12 article-heading"}).h3.text)
        projectTime=(project.findNext("span",{"class":"meta-timespan"}).text)
        projectAuthor=(project.findNext("a",{"class":"article-author"}).text)
        f.write(projectTitle +", " + projectTime+", "+ projectAuthor + "\n")
f.close()
