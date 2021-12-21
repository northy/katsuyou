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

DEBUG = True

if DEBUG :
    import sys
    sys.path.insert(0, "..")

from katsuyou import conjugate
from katsuyou.util import matcher
from queue import Queue

def test_matcher() :
    word1 = conjugate.Verb("表示する", conjugateAll=True)
    word2 = conjugate.Verb("する", conjugateAll=True)

    dictionary = ["表示"]+list(word1.forms.unpack())+list(word2.forms.unpack())
    m = matcher.Matcher(words=dictionary)
    string = "表示しますしているし表示した表示"
    expected = Queue()
    expected.put([(0,2), "表示"])
    expected.put([(0,3), "表示し"])
    expected.put([(2,3), "し"])
    expected.put([(0,5), "表示します"])
    expected.put([(2,5), "します"])
    expected.put([(5,6), "し"])
    expected.put([(5,7), "して"])
    expected.put([(5,9), "している"])
    expected.put([(9,10), "し"])
    expected.put([(10,12), "表示"])
    expected.put([(10,13), "表示し"])
    expected.put([(12,13), "し"])
    expected.put([(10,14), "表示した"])
    expected.put([(12,14), "した"])
    expected.put([(14,16), "表示"])
    for s,e in m.matches(string) :
        assert not expected.empty(), "Missing: "+str(s)+' '+str(e)+' '+string[s:e]
        exp, exps = expected.get()
        assert (s,e) == exp, "Return/Expected: "+str(s)+' '+str(e)+' '+string[s:e]+' - '+' '+str(exp[0])+' '+str(exp[1])+' '+string[exp[0]:exp[1]]
        assert string[s:e] == exps, "Return/Expected: "+string[s:e]+" - "+exps
    assert expected.empty(), "Not enough returns"
    if DEBUG : print("OK")

def test_longest_matches() :
    word1 = conjugate.Verb("表示する", conjugateAll=True)
    word2 = conjugate.Verb("する", conjugateAll=True)

    dictionary = ["表示"]+list(word1.forms.unpack())+list(word2.forms.unpack())
    m = matcher.Matcher(words=dictionary)
    string = "表示しますしているし表示した表示"
    expected = Queue()
    expected.put([(0,5), "表示します"])
    expected.put([(5,9), "している"])
    expected.put([(9,10), "し"])
    expected.put([(10,14), "表示した"])
    expected.put([(14,16), "表示"])
    for s,e in m.longest_matches(string) :
        assert not expected.empty(), "Missing: "+str(s)+' '+str(e)+' '+string[s:e]
        exp, exps = expected.get()
        assert (s,e) == exp, "Return/Expected: "+str(s)+' '+str(e)+' '+string[s:e]+' - '+' '+str(exp[0])+' '+str(exp[1])+' '+string[exp[0]:exp[1]]
        assert string[s:e] == exps, "Return/Expected: "+string[s:e]+" - "+exps
    assert expected.empty(), "Not enough returns"
    if DEBUG : print("OK")

def test_1() :
    word1 = conjugate.Adjective("ぞろい", True)
    word2 = conjugate.Adjective("揃い", True)
    word3 = conjugate.Adjective("そろい", True)
    dictionary = list(word1.forms.unpack())+list(word2.forms.unpack())+list(word3.forms.unpack())
    m = matcher.Matcher(words=dictionary)

    string = "あのチームはつわものぞろいだ。"
    expected = Queue()
    expected.put([(10,13), "ぞろい"])
    for s,e in m.longest_matches(string) :
        assert not expected.empty(), "Missing: "+str(s)+' '+str(e)+' '+string[s:e]
        exp, exps = expected.get()
        assert (s,e) == exp, "Return/Expected: "+str(s)+' '+str(e)+' '+string[s:e]+' - '+' '+str(exp[0])+' '+str(exp[1])+' '+string[exp[0]:exp[1]]
        assert string[s:e] == exps, "Return/Expected: "+string[s:e]+" - "+exps
    assert expected.empty(), "Not enough returns"

    string = "みなさまがお揃いになったので、送別会を始められます"
    expected = Queue()
    expected.put([(6,8), "揃い"])
    for s,e in m.longest_matches(string) :
        assert not expected.empty(), "Missing: "+str(s)+' '+str(e)+' '+string[s:e]
        exp, exps = expected.get()
        assert (s,e) == exp, "Return/Expected: "+str(s)+' '+str(e)+' '+string[s:e]+' - '+' '+str(exp[0])+' '+str(exp[1])+' '+string[exp[0]:exp[1]]
        assert string[s:e] == exps, "Return/Expected: "+string[s:e]+" - "+exps
    assert expected.empty(), "Not enough returns"

    if DEBUG : print("OK")

if __name__=="__main__" :
    if DEBUG : print("---MATCHES---")
    test_matcher()
    if DEBUG : print("---LONGEST MATCHES---")
    test_longest_matches()
    if DEBUG : print("---TEST 1---")
    test_1()
