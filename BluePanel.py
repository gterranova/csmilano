# Copyright 2006 James Tauber and contributors
# Copyright (C) 2009 Luke Kenneth Casson Leighton <lkcl@lkcl.net>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __pyjamas__ import console
from pyjamas import Factory
from pyjamas import DOM

from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.ComplexPanel import ComplexPanel

class BlueClear(SimplePanel):
    def __init__(self, **ka):
        element = ka.pop('Element', None) or DOM.createDiv()
        self.setElement(element)
        ka['StyleName'] = "clear"
        SimplePanel.__init__(self, **ka)
        
class CSSPanel(ComplexPanel):
    def __init__(self, **ka):
        element = ka.pop('Element', None) or DOM.createDiv()
        self.setElement(element)
        ComplexPanel.__init__(self, **ka)        
        
    def add(self, widget, *attributes):
        ComplexPanel.add(self, widget, self.getElement())

    def setLast(self, value):
        if value:
            self.addStyleName("last")

    def setBox(self, value):
        if value:
            self.addStyleName("box")

    def setPrependTop(self, value):
        if value:
            self.addStyleName("prepend-top")

    def setAppendBottom(self, value):
        if value:
            self.addStyleName("append-bottom")

    def setColBorder(self, value):
        if value:
            self.addStyleName("colborder")

    def setSpan(self, value):
        self.addStyleName("span-%d" % value)

    def setPrepend(self, value):
        self.addStyleName("prepend-%d" % value)

    def setAppend(self, value):
        self.addStyleName("append-%d" % value)

    def setPull(self, value):
        self.addStyleName("pull-%d" % value)

    def setPush(self, value):
        self.addStyleName("push-%d" % value)

    def setHTML(self, value):
        self.getElement().innerHTML = value
        
class BlueContainer(CSSPanel):
    def __init__(self, **ka):
        CSSPanel.__init__(self, **ka)
        self.addStyleName("container")
        
    def add(self, widget, Last=None):
        widget.addStyleName("column")
        CSSPanel.add(self, widget, self.getElement())

class BlueColumn(CSSPanel):
    def __init__(self, **ka):
        CSSPanel.__init__(self, **ka)
        self.addStyleName("column")        
        
    def add(self, widget, Last=None):
        CSSPanel.add(self, widget, self.getElement())
