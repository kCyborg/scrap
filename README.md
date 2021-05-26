# scrap
## A little python script to scrap an amazing webserial and format it as an epub.

For a few months ago I have been reading an amazing web serial: [The Wondering Inn](https://wanderinginn.com/), but I would like to read it in epub format, so I gave myself the task to scrap the web and format it into epub.

To develop the script I use [Beautiful Soup](https://pypi.org/project/beautifulsoup4/) and [EbookLib](https://pypi.org/project/EbookLib/), so in order to run the script you will need them, just install them using pip:
```
python -m pip install ebooklib
python -m pip install beautifulsoup4
```

The whole idea is very simple: build your own epub just feeding the script with a few variables. If you wanna build an epub for just the Volumen2 you can, or if you decide to throw the entire web into a single epub, you also can.

The ussage is very simple: 
1. Run the script: ```/your/location/python3 script.py```
2. The script will ask you for a few details:
   - The url of the first chapter you wanna get. IE: https://wanderinginn.com/2021/01/10/8-00/
   - The number of chapters. IE: If you wanna get the Vol7 just count the number of Volumen 7's chapters and enter that number here
   - A little description. IE: `An inn is a place to rest, a place to talk and share stories, or a place to find adventures, a starting ground for quests and legends. In this world, at least. To Erin Solstice, an inn seems like a medieval relic from the past. But here she is, running from Goblins and trying to survive in a world full of monsters and magic. She’d be more excited about all of this if everything wasn’t trying to kill her. But an inn is what she found, and so that’s what she becomes. An innkeeper who serves drinks to heroes and monsters– Actually, mostly monsters. But it’s a living, right? This is the story of the Wandering Inn.`
   - The book name (the one that will be shown inside the epub)
   - The file name (the one that will be shown in your File Explorer app)
   - A full example can be:
 ```
 Hi, this little piece of code will format The Wondering Inn web serial into an epub
Enter the first chapter of the volumen url: https://wanderinginn.com/2021/01/10/8-00/
Enter the numbers of chapters you wanna scrap: 27
Enter a little description: This is the volumen 8 
Enter the book's name (inside the epub): Volumen 8
Enter the book's name (file name): Vol8
I will start the scraping now
```



3. Once you have feed the script, it will begin the scapaing and your terminal will look similar to:
```
8.00

https://wanderinginn.com/2021/01/13/8-01/

8.01

https://wanderinginn.com/2021/01/17/8-02/

8.02
....
https://wanderinginn.com/2021/01/20/8-03/

```

4. Once the script ends will prompt you with:
```
Your epub is saved now in: D:\Python\Scrap\scrap\Vol8.epub
```

As a feature I left you guys all the [epubs](https://github.com/kCyborg/scrap/tree/main/Books)


Greetings!
