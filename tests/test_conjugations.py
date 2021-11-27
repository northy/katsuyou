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

import difflib

def test_ichidan() :
    expected = {'stem': {'neutral': {'te_form': 'いて', 'i_stem': 'い'}}, 'plain': {'positive': {'nonpast': 'いる', 'past': 'いた', 'optative': 'いたい', 'optative_past': 'いたかった', 'optative_te_form': 'いたくて', 'volitional': 'いよう', 'ba_conditional': 'いれば', 'tara_conditional': 'いたら', 'receptive': 'いられる', 'causative': 'いらせる', 'potential': 'いられる', 'imperative': 'いろ', 'progressive': 'いている', 'past_progressive': 'いていた', 'past_presumptive': 'いたろう'}, 'negative': {'nonpast': 'いない', 'past': 'いなかった', 'optative': 'いたくない', 'optative_past': 'いたくなかった', 'optative_te_form': 'いたくなくて', 'ba_conditional': 'いなかっければ', 'tara_conditional': 'いなかったら', 'receptive': 'いられない', 'causative': 'いらせない', 'potential': 'いられない', 'imperative': 'いるな', 'progressive': 'いていない', 'past_progressive': 'いていなかった'}}, 'polite': {'positive': {'nonpast': 'います', 'past': 'いました', 'volitional': 'いましょう', 'tara_conditional': 'いましたら', 'receptive': 'いられます', 'causative': 'いらせます', 'potential': 'いられます', 'progressive': 'いています', 'past_progressive': 'いていました'}, 'negative': {'nonpast': 'いません', 'past': 'いませんでした', 'optative': 'いたくありません', 'tara_conditional': 'いませんでしたら', 'receptive': 'いられません', 'causative': 'いらせません', 'potential': 'いられません', 'imperative': 'いないで', 'progressive': 'いていません', 'past_progressive': 'いていませんでした'}}}
    
    c = conjugate.Verb("いる", True, True)
    
    assert c.forms==expected, "No match: "+str([li for li in difflib.ndiff(str(c.forms), str(expected)) if li[0] != ' '])

def test_adjective() :
    expected = {'plain': {'positive': {'nonpast': '短い', 'past': '短かった', 'presumptive': '短いだろう', 'ba_conditional': '短ければ', 'te_form': '短くて'}, 'negative': {'nonpast': '短くない', 'past': '短くなかった', 'presumptive': '短かっただろう', 'ba_conditional': '短かっければ', 'te_form': '短くなくて'}}, 'polite': {'positive': {'nonpast': '短いです', 'past': '短かったです', 'presumptive': '短いでしょう'}, 'negative': {'nonpast': '短くありません', 'past': '短くありませんでした', 'presumptive': '短くないでしょう'}}}
    
    c = conjugate.Adjective("短い", True)

    assert c.forms==expected, "No match: "+str([li for li in difflib.ndiff(str(c.forms), str(expected)) if li[0] != ' '])

def test_su_godan() :
    expected = {'stem': {'neutral': {'te_form': '済まして', 'a_stem': '済まさ', 'i_stem': '済まし', 'e_stem': '済ませ', 'o_stem': '済まそ'}}, 'plain': {'positive': {'nonpast': '済ます', 'past': '済ました', 'optative': '済ましたい', 'past_optative': '済ましたかった', 'optative_te_form': '済ましたくて', 'volitional': '済まそう', 'ba_conditional': '済ませば', 'tara_conditional': '済ましたら', 'receptive': '済まされる', 'causative': '済まさせる', 'potential': '済ませる', 'imperative': '済ませ', 'progressive': '済ましている', 'past_progressive': '済ましていた', 'past_presumptive': '済ましたろう'}, 'negative': {'nonpast': '済まさない', 'past': '済まさなかった', 'optative': '済ましたくない', 'past_optative': '済ましたくなかった', 'optative_te_form': '済ましたくなくて', 'ba_conditional': '済まさなかっければ', 'tara_conditional': '済まさなかったら', 'receptive': '済まされない', 'causative': '済まさせない', 'potential': '済ませない', 'imperative': '済ますな', 'progressive': '済ましていない', 'past_progressive': '済ましていなかった'}}, 'polite': {'positive': {'nonpast': '済まします', 'past': '済ましました', 'volitional': '済ましましょう', 'tara_conditional': '済ましましたら', 'receptive': '済まされます', 'causative': '済まさせます', 'potential': '済ませます', 'progressive': '済ましています', 'past_progressive': '済ましていました'}, 'negative': {'nonpast': '済ましますせん', 'past': '済ましますせんでした', 'optative': '済ましたくありません', 'tara_conditional': '済ましますせんでしたら', 'receptive': '済まされません', 'causative': '済まさせません', 'potential': '済ませません', 'imperative': '済まさないで', 'progressive': '済ましていません', 'past_progressive': '済ましていませんでした'}}}    
    
    c = conjugate.Verb("済ます", False, True)

    assert c.forms==expected, "No match: "+str([li for li in difflib.ndiff(str(c.forms), str(expected)) if li[0] != ' '])

def test_suru() :
    expected = {'stem': {'neutral': {'te_form': 'して', 'i_stem': 'し'}}, 'plain': {'positive': {'nonpast': 'する', 'past': 'した', 'optative': 'したい', 'past_optative': 'したかった', 'optative_te_form': 'したくて', 'volitional': 'しよう', 'ba_conditional': 'すれば', 'tara_conditional': 'したら', 'receptive': 'される', 'causative': 'させる', 'potential': 'できる', 'imperative': 'しろ', 'progressive': 'している', 'past_progressive': 'していた', 'past_presumptive': 'したろう'}, 'negative': {'nonpast': 'しない', 'past': 'しなかった', 'optative': 'したくない', 'past_optative': 'したくなかった', 'optative_te_form': 'したくなくて', 'ba_conditional': 'しなければ', 'tara_conditional': 'しなかったら', 'receptive': 'されない', 'causative': 'させない', 'potential': 'できない', 'imperative': 'するな', 'progressive': 'していない', 'past_progressive': 'していなかった'}}, 'polite': {'positive': {'nonpast': 'します', 'past': 'しました', 'volitional': 'しましょう', 'tara_conditional': 'しましたら', 'receptive': 'されます', 'causative': 'させます', 'potential': 'されます', 'progressive': 'しています', 'past_progressive': 'していました'}, 'negative': {'nonpast': 'しません', 'past': 'しませんでした', 'optative': 'したくありませんでした', 'tara_conditional': 'しませんでしたら', 'receptive': 'されません', 'causative': 'させません', 'potential': 'されません', 'imperative': 'しないで', 'progressive': 'していません', 'past_progressive': 'していました'}}}
    
    c = conjugate.Verb("する", conjugateAll=True)
    
    assert c.forms==expected, "No match: "+str([li for li in difflib.ndiff(str(c.forms), str(expected)) if li[0] != ' '])

if __name__=="__main__" :
    test_ichidan()
    test_adjective()
    test_su_godan()

    #irregulars
    test_suru()
    
