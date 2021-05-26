from bs4 import BeautifulSoup as bs
import requests
from ebooklib import epub

print ("Hi, this little piece of code will format The Wondering Inn web serial \
into an epub")

next_url = input("Enter the first chapter of the volumen url: ")
n_chapters = int(input("Enter the numbers of chapters you wanna scrap: "))
n_chapters = n_chapters - 1
description = input("Enter a little description: ")
book_name_epub = input("Enter the book's name (inside the epub): ")
book_name_file = input("Enter the book's name (file name): ")

#next_url = "https://wanderinginn.com/2021/01/10/8-00/"

chapter_list = []

def scraping(url):
    #Get the webpage
    response = requests.get(url)
    html = response.content
    soup = bs(html, "lxml")

    #Get the title
    title = soup.title.get_text()
    title = title.split('|')[0]
    title = title[:-1]
    #print(title)

    #Get the chapter
    chapter = soup.find("div", class_="entry-content")
    chapter = str(chapter)
    #print(chapter)

    span = soup.find('span', class_="nav-next")
    a = span.find('a', href=True)
    next_url = a['href']

    return (title, chapter, next_url)


#Create the epub and minimal  metadata requirements
book = epub.EpubBook()

book.set_identifier('id131313')
book.set_title(book_name_epub)
book.set_language('en')

book.add_author('PirateAba')

c1 = epub.EpubHtml(title='Introduction', file_name="intro.xhtml", lang='en')
c1.content = description
book.add_item(c1)

i=0
while i<=n_chapters:
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
epub.write_epub(book_name_file+'.epub', book, {})






















