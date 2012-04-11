import pyjd # this is dummy in pyjs.
#from pyjamas import DOM
from pyjamas.ui.RootPanel import RootPanel
#from pyjamas.ui.ComplexPanel import ComplexPanel 
#from pyjamas.ui.Button import Button
from pyjamas.ui.Image import Image
from pyjamas.ui.Hyperlink import Hyperlink
from pyjamas.ui.HyperlinkImage import HyperlinkImage
from pyjamas import History
from pyjamas.ui.HTML import HTML
#from pyjamas.ui.Label import Label
#from pyjamas import Window
#from pyjamas.JSONParser import JSONParser
from pyjamas.HTTPRequest import HTTPRequest

#from pyjamas.ui.Widget import Widget
#from pyjamas.ui.Panel import Panel
#from pyjamas.ui.FocusPanel import FocusPanel

from BluePanel import BlueContainer, BlueColumn
from PicasaWebSlideShow import PicasaWebSlideShow

class SlideLoader:
    def __init__(self, panel):
        self.panel = panel

    def onCompletion(self, text):
        self.panel.setSlide(text)

    def onError(self, text, code):
        print text, code
        #self.panel.onError(text, code)

    def onTimeout(self, text):
        #self.panel.onTimeout(text)
        print text
    
class BlueprintTest:

    def onHistoryChanged(self, token):
        if token == "":
            token = 'main'
        if token == 'main':
            self.picasa.setVisible(True)
        else:
            self.picasa.setVisible(False)
        self.loadPage(token)
        
    def __init__(self):
        page = BlueContainer(ID="page")
        doc = BlueColumn(Span=22, Prepend=1, Append=1, Last=True)
        page.add(doc)

        # Header
        header = BlueColumn(ID="header", Span=24, Pull=1, PrependTop=True)
        logo = HyperlinkImage(Image(Url='images/logo.png'),"#")
        col1 = BlueColumn(Span=7)
        col2 = BlueColumn(Span=12)
        col3 = BlueColumn(Span=5, Last=True)
        col1.add(logo)
        col2.add(HTML("<p>&nbsp;</p>")) 
        col3.add(HTML("<p>&nbsp;</p>")) 
        header.add(col1)
        header.add(col2)
        header.add(col3)
        doc.add(header)

        # Content
        content = BlueColumn(ID="content", Span=22, PrependTop=True, AppendBottom=True, Last=True)

#        self.picasa = PicasaWebSlideShow(Span=24, Last=True, Pull=1, PhotoSize=(950, 320))
#        content.add(self.picasa)
        
        main = BlueColumn(Span=14, ColBorder=True)
        self.picasa = PicasaWebSlideShow(Span=14, Last=True, PhotoSize=(560, 315))        
        main.add(self.picasa)

        c = BlueColumn(Span=14)
        self.pagecontent = HTML("")
        c.add(self.pagecontent)
        main.add(c)

##        threecol = BlueColumn(Span=14)
##        col1 = BlueColumn(Span=4, ColBorder=True, HTML="""<img class='right' src='images/maps.png'><h3>Where?</h3><p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Praesent aliquam, justo convallis luctus rutrum, erat nulla fermentum diam, at nonummy quam ante ac quam. </p>""")
##        col2 = BlueColumn(Span=4, ColBorder=True, HTML="""<img class='right' src='images/event.png'><h3>When?</h3><p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Praesent aliquam, justo convallis luctus rutrum, erat nulla fermentum diam, at nonummy quam ante ac quam. </p>""")
##        col3 = BlueColumn(Span=4, Last=True, HTML="""<img class='right' src='images/faq.png'><h3>Questions?</h3><p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Praesent aliquam, justo convallis luctus rutrum, erat nulla fermentum diam, at nonummy quam ante ac quam. </p>""")
##        for c in (col1, col2, col3):
##            threecol.add(c)
##        main.add(threecol)
        content.add(main)

        sidecol = BlueColumn(Span=7, Last=True)

        threecol = BlueColumn(Span=7)
        col1 = BlueColumn(Span=6, Last=True, Box=True, HTML="""<img class='right' src='images/maps.png'><h3>Where?</h3><p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Praesent aliquam, justo convallis luctus rutrum, erat nulla fermentum diam, at nonummy quam ante ac quam. <a href="#program"><p>Read more...</p></a></p>""")
        col2 = BlueColumn(Span=6, Last=True, Box=True, HTML="""<img class='right' src='images/event.png'><h3>When?</h3><p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Praesent aliquam, justo convallis luctus rutrum, erat nulla fermentum diam, at nonummy quam ante ac quam. <a href="#test"><p>Read more...</p></a></p>""")
        col3 = BlueColumn(Span=6, Last=True, Box=True, HTML="""<img class='right' src='images/faq.png'><h3>Questions?</h3><p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Praesent aliquam, justo convallis luctus rutrum, erat nulla fermentum diam, at nonummy quam ante ac quam. <a href="#test"><p>Read more...</p></a></p>""")
        for c in (col1, col2, col3):
            threecol.add(c)
        sidecol.add(threecol)
        
##        sidecol_container = BlueColumn(Span=6, Last=True, Box=True)
##        p = BlueColumn(Span=6, Last=True, AppendBottom=True)
##        p.add(HTML("<h2>Sidebar Content</h2><p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Praesent aliquam, justo convallis luctus rutrum, erat nulla fermentum diam, at nonummy quam ante ac quam. </p>"))
##        p.add(Hyperlink("Read more...", TargetHistoryToken='Test'))
##        sidecol_container.add(p)
##        p = BlueColumn(Span=6, Last=True)
##        p.add(HTML("<h2>Sidebar Content</h2><p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Praesent aliquam, justo convallis luctus rutrum, erat nulla fermentum diam, at nonummy quam ante ac quam. </p>"))
##        sidecol_container.add(p)        
##        sidecol.add(sidecol_container)
        content.add(sidecol)
        doc.add(content)

        # Footer
        footer = BlueColumn(ID="footer", Span=24, Pull=1, Last=True)
        fourcol = BlueColumn(Span=23, Prepend=1, Append=1, PrependTop=True, AppendBottom=True, Last=True)

        def listWidget(title, items, Last=False):
            html = "<h3>%s</h3>" % title
            for item, url in items:
                html += "<li><a href='%s'>%s</a></li>" % (url, item)
            return BlueColumn(Span=5, ColBorder=(not Last), Last=Last, HTML=html)
                
        col1 = listWidget("What happened last year", [('link', 'http://www.google.it'), ('link', 'http://www.google.it'),('link', 'http://www.google.it')])
        col2 = listWidget("Links to cs", [('link', 'http://www.google.it'), ('link', 'http://www.google.it'),('link', 'http://www.google.it')])
        col3 = listWidget("Organizers", [('link', 'http://www.google.it'), ('link', 'http://www.google.it'),('link', 'http://www.google.it')])
        col4 = listWidget("Contacts", [('link', 'http://www.google.it'), ('link', 'http://www.google.it'),('link', 'http://www.google.it')], Last=True)
        for c in (col1, col2, col3, col4):
            fourcol.add(c)
        footer.add(fourcol)
        footer.add(HTML("<p class='light small'>&nbsp;&nbsp;&nbsp;&copy; 2011, Gianpaolo Terranova</p>"))
        doc.add(footer)
        
        RootPanel().add(page)
        
    def start(self):
        History.addHistoryListener(self)
        self.picasa.loadPicasaImages("milanocs","5512654378631416865")
        #Show the initial screen.
        initToken = History.getToken()
        print initToken
        if len(initToken):
            self.onHistoryChanged(initToken)
        else:
            self.loadPage("main")

    def loadPage(self, filename):
        HTTPRequest().asyncGet(filename+".txt", SlideLoader(self))

    def setSlide(self, text):
        self.pagecontent.setHTML(text)
                
if __name__ == '__main__':
    # for pyjd, set up a web server and load the HTML from there:
    # this convinces the browser engine that the AJAX will be loaded
    # from the same URI base as the URL, it's all a bit messy...
    pyjd.setup("public/main.html")
    app = BlueprintTest()
    app.start()
    pyjd.run()
