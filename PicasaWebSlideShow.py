import pyjd # this is dummy in pyjs.

from pyjamas.JSONParser import JSONParser
from pyjamas.HTTPRequest import HTTPRequest
from pyjamas.ui.FocusPanel import FocusPanel
from BluePanel import BlueColumn

from __pyjamas__ import jsimport

jsimport("jquery.tools.min.js")

jq = jQuery

class PicasaWebSlideShow(BlueColumn):
    def __init__(self, **kwargs):
        x, y = kwargs.pop('PhotoSize', (950, 350))        
        kwargs['Width'] = self.photow = "%dpx" % x
        self.photoh = "%dpx" % y
        kwargs['Height'] = "%dpx" % (y + 20)
        BlueColumn.__init__(self, **kwargs)
        self.slideshow = FocusPanel(ID="slideshow", Height=self.photoh)      
        self.slidetabs = FocusPanel(ID="slidetabs")
        self.add(self.slideshow)
        self.add(self.slidetabs)

    def loadPicasaImages(self, userid, album):
        url = "http://picasaweb.google.com/data/feed/base/user/" + userid + "/albumid/" + album + "?alt=json&kind=photo&hl=en_US&fields=entry(title,gphoto:numphotos,media:group(media:content,media:thumbnail))"
        HTTPRequest().asyncImpl('GET', None, None, url, None, self, False, None, None)

    def parsePhotos(self, items):
        global jq
        ss = st = ""
        photos = JSONParser().parseJSON(items)
        photo_list = JSONParser().jsObjectToPyObject(photos.feed.entry)
        for i in range(len(photo_list)):
            index = "%s" % i
            url = photo_list[index]['media$group']['media$content']['0']['url']
            ss += "<img src='%s' width='%s' height='%s'/>\n" % (url, self.photow, self.photoh)
            st += "<a href='#'></a>\n"
        self.slideshow.getElement().innerHTML = ss
        self.slidetabs.getElement().innerHTML = st
        slt = jq(self.slidetabs.getElement())
        opts = Array()
        opts.effect = 'fade'
        opts.fadeOutSpeed = 'slow'
        opts.rotate = True    
        slt.tabs("#"+self.slideshow.getID()+" > img", opts).slideshow()
        slt.data("slideshow").play()

    def onCompletion(self, json):
        self.parsePhotos(json)
        
    def onError(self, text, code):
        print "error %s %s"  % (code,text)

    def onTimeout(self, text):
        print "timeout %s"  % text
    
