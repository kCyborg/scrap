from bs4 import BeautifulSoup as bs
import requests
from ebooklib import epub

next_url = "https://wanderinginn.com/2021/01/10/8-00/"

chapter_list = []

def scraping(url):
    #Get the webpage
    response = requests.get(url)
    html = response.content
    soup = bs(html, "lxml")

    #Get the title
    # global title
    title = soup.title.get_text()
    title = title.split('|')[0]
    title = title[:-1]
    #print(title)

    #Get the chapter
    # global chapter
    chapter = soup.find("div", class_="entry-content")
    chapter = str(chapter)
    #print(chapter)

    span = soup.find('span', class_="nav-next")
    a = span.find('a', href=True)
    # global next_url
    next_url = a['href']

    return (title, chapter, next_url)


#Create the epub and minimal  metadata requirements
book = epub.EpubBook()

book.set_identifier('id131313')
book.set_title('The Wondering Inn Volumen 8 (so far)')
book.set_language('en')

book.add_author('PirateAba')

c1 = epub.EpubHtml(title='Introduction', file_name="intro.xhtml", lang='en')
c1.content = 'An inn is a place to rest, a place to talk and share stories, or a place to find adventures, a starting ground for quests and legends. In this world, at least. To Erin Solstice, an inn seems like a medieval relic from the past. But here she is, running from Goblins and trying to survive in a world full of monsters and magic. She’d be more excited about all of this if everything wasn’t trying to kill her. But an inn is what she found, and so that’s what she becomes. An innkeeper who serves drinks to heroes and monsters– Actually, mostly monsters. But it’s a living, right? This is the story of the Wandering Inn.'
book.add_item(c1)

i=0
while i<=5:
    (title, chapter, next_url) = scraping(next_url)

    fle_name = "C" + str(i + 2) + ".xhtml"
    # print(fle_name)

    #Here you define chaper_list[i]
    chapter_list.append(epub.EpubHtml(title=title, file_name=fle_name, lang='hr'))
    chapter_list[i].content = chapter
    book.add_item(chapter_list[i])

    print(title)
    print(chapter)
    print (next_url)
    i=i+1



# define Table Of Contents
book.toc = (epub.Link('intro.xhtml', 'Introduction', 'intro'),
              (
                epub.Section('Chapters'),
                [c1] + chapter_list)
            )


# add default NCX and Nav file
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# define CSS style
style = 'BODY {color: white;}'
nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)

# add CSS file
book.add_item(nav_css)

# basic spine
book.spine = ['nav', c1] + chapter_list

# write to the file
epub.write_epub('The Wondering Inn Vol8 (so far).epub', book, {})






















