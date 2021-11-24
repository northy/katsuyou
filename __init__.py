# -*- coding: utf-8 -*-

# MIT License

# Copyright (c) 2021 Alexsandro Thomas

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import conjugate
from conjugate import ichidan_verb
from conjugate import godan_verb
from util import matcher

if __name__=="__main__" :
    #print("短い")
    #adjective = conjugate.Adjective("短い", True)
    #adjective.conjugate("plain","positive","*")
    #print(adjective.forms,'\n')

    #print("食べる")
    #verb_ichidan = conjugate.Verb("いる", True, True)
    #verb_ichidan.conjugate("polite","negative","*")
    #verb_ichidan.conjugate("*","*","te_form")
    #print(verb_ichidan.forms, '\n')

    #print("読む")
    #verb_godan = conjugate.Verb("すます", False, True)
    #verb_godan.conjugate("plain","positive","*")
    #verb_godan.conjugate("*","*","te_form")
    #print(verb_godan.forms, '\n')

    print("勉強する")
    verb_irreg = conjugate.Verb("勉強する", False, True)
    verb_irreg.conjugate()
    print(verb_irreg.forms, '\n')

    #dictionary = list(adjective.forms.unpack())+list(verb_ichidan.forms.unpack())+list(verb_godan.forms.unpack())
    #m = matcher.Matcher(words=dictionary)
    #string = "すましていてもいるよ"
    #for s,e in m.longest_matches(string) :
    #    print(s,e,string[s:e])
