from bs4 import BeautifulSoup
import urllib2
import re


def get_soup(url):
    if url[:7] != "http://":
        url = "http://" + url
    html = urllib2.urlopen(url).read()
    return BeautifulSoup(html)


def get_story_links(soup):
    stories = []
    for i , a in enumerate(soup.find_all('area', href=True)):
        stories.append({
            'id': i,
            'url': "newser.com" + a['href'],
            'title': format_title(a['href']),
        })
    return stories



def format_title(title_str):
    title = title_str.split('/')
    title = title[-1][:-5]
    title = title.split('-')
    str = ""
    for i in title:
        if len(i) > 3:
            str += i.capitalize() + " "
        else:
            str += i + " "
    return str


def get_article(soup):
    paragraphs = []
    article = soup.findAll('p', {'class': 'storyParagraph'})
    for i in article:
        paragraphs.append(i.text.lstrip())
    return paragraphs

def display_choices():
    fp_stories = get_soup('newser.com')
    story_links = get_story_links(fp_stories)
    print "\n"
    for i in story_links:
        print i['id'], ":", i['title']
    print "\n"

def commander(choice):
    check = False
    fp_stories = get_soup('newser.com')
    story_links = get_story_links(fp_stories)
    print "\n"
    for i in story_links:
        if int(choice) == i['id']:
            check = True
            article = get_soup(i['url'])
            print "\n", i['title'], "\n\n"
            for a in get_article(article):
                print a
        check = True
    return check
        
    

if __name__ == "__main__":
    li = '''The MIT License (MIT)

Copyright (c) Oct, 11, 2014 Rylan Gotto

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.'''


    print li , "\n\n"

    print "Rylan CLI newser frontpage browser"

    END = False
    while not END:
        display_choices()
        choice = raw_input('Select a story or CTRL+C: ')
        if choice.upper is not 'Q':
            check = commander(choice)
            if check:
                raw_input("Press Enter to Continue")
            else:
                print "Not a valid selection"



		   
	
