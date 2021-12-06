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

def test_ichidan() :
    expected = {'stem': {'neutral': {'te_form': 'いて', 'i_stem': 'い'}}, 'plain': {'positive': {'nonpast': 'いる', 'past': 'いた', 'optative': 'いたい', 'past_optative': 'いたかった', 'optative_te_form': 'いたくて', 'volitional': 'いよう', 'ba_conditional': 'いれば', 'tara_conditional': 'いたら', 'receptive': 'いられる', 'causative': 'いらせる', 'potential': 'いられる', 'imperative': 'いろ', 'progressive': 'いている', 'past_progressive': 'いていた', 'past_presumptive': 'いたろう'}, 'negative': {'nonpast': 'いない', 'past': 'いなかった', 'optative': 'いたくない', 'past_optative': 'いたくなかった', 'optative_te_form': 'いたくなくて', 'ba_conditional': 'いなければ', 'tara_conditional': 'いなかったら', 'receptive': 'いられない', 'causative': 'いらせない', 'potential': 'いられない', 'imperative': 'いるな', 'progressive': 'いていない', 'past_progressive': 'いていなかった'}}, 'polite': {'positive': {'nonpast': 'います', 'past': 'いました', 'volitional': 'いましょう', 'tara_conditional': 'いましたら', 'receptive': 'いられます', 'causative': 'いらせます', 'potential': 'いられます', 'progressive': 'いています', 'past_progressive': 'いていました'}, 'negative': {'nonpast': 'いません', 'past': 'いませんでした', 'optative': 'いたくありません', 'tara_conditional': 'いませんでしたら', 'receptive': 'いられません', 'causative': 'いらせません', 'potential': 'いられません', 'imperative': 'いないで', 'progressive': 'いていません', 'past_progressive': 'いていませんでした'}}}
    
    c = conjugate.Verb("いる", True, True)
    
    c.forms.assert_equal(expected)

def test_adjective() :
    expected = {'stem': {'neutral': {'connective':'短く'}}, 'plain': {'positive': {'nonpast': '短い', 'past': '短かった', 'presumptive': '短いだろう', 'ba_conditional': '短ければ', 'te_form': '短くて'}, 'negative': {'nonpast': '短くない', 'past': '短くなかった', 'presumptive': '短かっただろう', 'ba_conditional': '短くなければ', 'te_form': '短くなくて'}}, 'polite': {'positive': {'nonpast': '短いです', 'past': '短かったです', 'presumptive': '短いでしょう'}, 'negative': {'nonpast': '短くありません', 'past': '短くありませんでした', 'presumptive': '短くないでしょう'}}}
    
    c = conjugate.Adjective("短い", True)

    c.forms.assert_equal(expected)

def test_ku_godan() :
    expected = {'stem': {'neutral': {'te_form': '欺いて', 'a_stem': '欺か', 'i_stem': '欺き', 'e_stem': '欺け', 'o_stem': '欺こ'}}, 'plain': {'positive': {'nonpast': '欺く', 'past': '欺いた', 'optative': '欺きたい', 'past_optative': '欺きたかった', 'optative_te_form': '欺きたくて', 'volitional': '欺こう', 'ba_conditional': '欺けば', 'tara_conditional': '欺いたら', 'receptive': '欺かれる', 'causative': '欺かせる', 'potential': '欺ける', 'imperative': '欺け', 'progressive': '欺いている', 'past_progressive': '欺いていた', 'past_presumptive': '欺いたろう'}, 'negative': {'nonpast': '欺かない', 'past': '欺かなかった', 'optative': '欺きたくない', 'past_optative': '欺きたくなかった', 'optative_te_form': '欺きたくなくて', 'ba_conditional': '欺かなければ', 'tara_conditional': '欺かなかったら', 'receptive': '欺かれない', 'causative': '欺かせない', 'potential': '欺けない', 'imperative': '欺くな', 'progressive': '欺いていない', 'past_progressive': '欺いていなかった'}}, 'polite': {'positive': {'nonpast': '欺きます', 'past': '欺きました', 'volitional': '欺きましょう', 'tara_conditional': '欺きましたら', 'receptive': '欺かれます', 'causative': '欺かせます', 'potential': '欺けます', 'progressive': '欺いています', 'past_progressive': '欺いていました'}, 'negative': {'nonpast': '欺きますせん', 'past': '欺きますせんでした', 'optative': '欺きたくありません', 'tara_conditional': '欺きますせんでしたら', 'receptive': '欺かれません', 'causative': '欺かせません', 'potential': '欺けません', 'imperative': '欺かないで', 'progressive': '欺いていません', 'past_progressive': '欺いていませんでした'}}}    
    
    c = conjugate.Verb("欺く", False, True)

    c.forms.assert_equal(expected)

def test_gu_godan() :
    expected = {'stem': {'neutral': {'te_form': '仰いで', 'a_stem': '仰が', 'i_stem': '仰ぎ', 'e_stem': '仰げ', 'o_stem': '仰ご'}}, 'plain': {'positive': {'nonpast': '仰ぐ', 'past': '仰いだ', 'optative': '仰ぎたい', 'past_optative': '仰ぎたかった', 'optative_te_form': '仰ぎたくて', 'volitional': '仰ごう', 'ba_conditional': '仰げば', 'tara_conditional': '仰いだら', 'receptive': '仰がれる', 'causative': '仰がせる', 'potential': '仰げる', 'imperative': '仰げ', 'progressive': '仰いでいる', 'past_progressive': '仰いでいた', 'past_presumptive': '仰いだろう'}, 'negative': {'nonpast': '仰がない', 'past': '仰がなかった', 'optative': '仰ぎたくない', 'past_optative': '仰ぎたくなかった', 'optative_te_form': '仰ぎたくなくて', 'ba_conditional': '仰がなければ', 'tara_conditional': '仰がなかったら', 'receptive': '仰がれない', 'causative': '仰がせない', 'potential': '仰げない', 'imperative': '仰ぐな', 'progressive': '仰いでいない', 'past_progressive': '仰いでいなかった'}}, 'polite': {'positive': {'nonpast': '仰ぎます', 'past': '仰ぎました', 'volitional': '仰ぎましょう', 'tara_conditional': '仰ぎましたら', 'receptive': '仰がれます', 'causative': '仰がせます', 'potential': '仰げます', 'progressive': '仰いでいます', 'past_progressive': '仰いでいました'}, 'negative': {'nonpast': '仰ぎますせん', 'past': '仰ぎますせんでした', 'optative': '仰ぎたくありません', 'tara_conditional': '仰ぎますせんでしたら', 'receptive': '仰がれません', 'causative': '仰がせません', 'potential': '仰げません', 'imperative': '仰がないで', 'progressive': '仰いでいません', 'past_progressive': '仰いでいませんでした'}}}

    c = conjugate.Verb("仰ぐ", False, True)

    c.forms.assert_equal(expected)

def test_su_godan() :
    expected = {'stem': {'neutral': {'te_form': '済まして', 'a_stem': '済まさ', 'i_stem': '済まし', 'e_stem': '済ませ', 'o_stem': '済まそ'}}, 'plain': {'positive': {'nonpast': '済ます', 'past': '済ました', 'optative': '済ましたい', 'past_optative': '済ましたかった', 'optative_te_form': '済ましたくて', 'volitional': '済まそう', 'ba_conditional': '済ませば', 'tara_conditional': '済ましたら', 'receptive': '済まされる', 'causative': '済まさせる', 'potential': '済ませる', 'imperative': '済ませ', 'progressive': '済ましている', 'past_progressive': '済ましていた', 'past_presumptive': '済ましたろう'}, 'negative': {'nonpast': '済まさない', 'past': '済まさなかった', 'optative': '済ましたくない', 'past_optative': '済ましたくなかった', 'optative_te_form': '済ましたくなくて', 'ba_conditional': '済まさなければ', 'tara_conditional': '済まさなかったら', 'receptive': '済まされない', 'causative': '済まさせない', 'potential': '済ませない', 'imperative': '済ますな', 'progressive': '済ましていない', 'past_progressive': '済ましていなかった'}}, 'polite': {'positive': {'nonpast': '済まします', 'past': '済ましました', 'volitional': '済ましましょう', 'tara_conditional': '済ましましたら', 'receptive': '済まされます', 'causative': '済まさせます', 'potential': '済ませます', 'progressive': '済ましています', 'past_progressive': '済ましていました'}, 'negative': {'nonpast': '済ましますせん', 'past': '済ましますせんでした', 'optative': '済ましたくありません', 'tara_conditional': '済ましますせんでしたら', 'receptive': '済まされません', 'causative': '済まさせません', 'potential': '済ませません', 'imperative': '済まさないで', 'progressive': '済ましていません', 'past_progressive': '済ましていませんでした'}}}    
    
    c = conjugate.Verb("済ます", False, True)

    c.forms.assert_equal(expected)

def test_bu_godan() :
    expected = {'stem': {'neutral': {'te_form': '学んで', 'a_stem': '学ば', 'i_stem': '学び', 'e_stem': '学べ', 'o_stem': '学ぼ'}}, 'plain': {'positive': {'nonpast': '学ぶ', 'past': '学んだ', 'optative': '学びたい', 'past_optative': '学びたかった', 'optative_te_form': '学びたくて', 'volitional': '学ぼう', 'ba_conditional': '学べば', 'tara_conditional': '学んだら', 'receptive': '学ばれる', 'causative': '学ばせる', 'potential': '学べる', 'imperative': '学べ', 'progressive': '学んでいる', 'past_progressive': '学んでいた', 'past_presumptive': '学んだろう'}, 'negative': {'nonpast': '学ばない', 'past': '学ばなかった', 'optative': '学びたくない', 'past_optative': '学びたくなかった', 'optative_te_form': '学びたくなくて', 'ba_conditional': '学ばなければ', 'tara_conditional': '学ばなかったら', 'receptive': '学ばれない', 'causative': '学ばせない', 'potential': '学べない', 'imperative': '学ぶな', 'progressive': '学んでいない', 'past_progressive': '学んでいなかった'}}, 'polite': {'positive': {'nonpast': '学びます', 'past': '学びました', 'volitional': '学びましょう', 'tara_conditional': '学びましたら', 'receptive': '学ばれます', 'causative': '学ばせます', 'potential': '学べます', 'progressive': '学んでいます', 'past_progressive': '学んでいました'}, 'negative': {'nonpast': '学びますせん', 'past': '学びますせんでした', 'optative': '学びたくありません', 'tara_conditional': '学びますせんでしたら', 'receptive': '学ばれません', 'causative': '学ばせません', 'potential': '学べません', 'imperative': '学ばないで', 'progressive': '学んでいません', 'past_progressive': '学んでいませんでした'}}}
    
    c = conjugate.Verb("学ぶ", False, True)

    c.forms.assert_equal(expected)

def test_mu_godan() :
    expected = {'stem': {'neutral': {'te_form': '悴んで', 'a_stem': '悴ま', 'i_stem': '悴み', 'e_stem': '悴め', 'o_stem': '悴も'}}, 'plain': {'positive': {'nonpast': '悴む', 'past': '悴んだ', 'optative': '悴みたい', 'past_optative': '悴みたかった', 'optative_te_form': '悴みたくて', 'volitional': '悴もう', 'ba_conditional': '悴めば', 'tara_conditional': '悴んだら', 'receptive': '悴まれる', 'causative': '悴ませる', 'potential': '悴める', 'imperative': '悴め', 'progressive': '悴んでいる', 'past_progressive': '悴んでいた', 'past_presumptive': '悴んだろう'}, 'negative': {'nonpast': '悴まない', 'past': '悴まなかった', 'optative': '悴みたくない', 'past_optative': '悴みたくなかった', 'optative_te_form': '悴みたくなくて', 'ba_conditional': '悴まなければ', 'tara_conditional': '悴まなかったら', 'receptive': '悴まれない', 'causative': '悴ませない', 'potential': '悴めない', 'imperative': '悴むな', 'progressive': '悴んでいない', 'past_progressive': '悴んでいなかった'}}, 'polite': {'positive': {'nonpast': '悴みます', 'past': '悴みました', 'volitional': '悴みましょう', 'tara_conditional': '悴みましたら', 'receptive': '悴まれます', 'causative': '悴ませます', 'potential': '悴めます', 'progressive': '悴んでいます', 'past_progressive': '悴んでいました'}, 'negative': {'nonpast': '悴みますせん', 'past': '悴みますせんでした', 'optative': '悴みたくありません', 'tara_conditional': '悴みますせんでしたら', 'receptive': '悴まれません', 'causative': '悴ませません', 'potential': '悴めません', 'imperative': '悴まないで', 'progressive': '悴んでいません', 'past_progressive': '悴んでいませんでした'}}}

    c = conjugate.Verb("悴む", False, True)

    c.forms.assert_equal(expected)

def test_nu_godan() :
    expected = {'stem': {'neutral': {'te_form': '死んで', 'a_stem': '死な', 'i_stem': '死に', 'e_stem': '死ね', 'o_stem': '死の'}}, 'plain': {'positive': {'nonpast': '死ぬ', 'past': '死んだ', 'optative': '死にたい', 'past_optative': '死にたかった', 'optative_te_form': '死にたくて', 'volitional': '死のう', 'ba_conditional': '死ねば', 'tara_conditional': '死んだら', 'receptive': '死なれる', 'causative': '死なせる', 'potential': '死ねる', 'imperative': '死ね', 'progressive': '死んでいる', 'past_progressive': '死んでいた', 'past_presumptive': '死んだろう'}, 'negative': {'nonpast': '死なない', 'past': '死ななかった', 'optative': '死にたくない', 'past_optative': '死にたくなかった', 'optative_te_form': '死にたくなくて', 'ba_conditional': '死ななければ', 'tara_conditional': '死ななかったら', 'receptive': '死なれない', 'causative': '死なせない', 'potential': '死ねない', 'imperative': '死ぬな', 'progressive': '死んでいない', 'past_progressive': '死んでいなかった'}}, 'polite': {'positive': {'nonpast': '死にます', 'past': '死にました', 'volitional': '死にましょう', 'tara_conditional': '死にましたら', 'receptive': '死なれます', 'causative': '死なせます', 'potential': '死ねます', 'progressive': '死んでいます', 'past_progressive': '死んでいました'}, 'negative': {'nonpast': '死にますせん', 'past': '死にますせんでした', 'optative': '死にたくありません', 'tara_conditional': '死にますせんでしたら', 'receptive': '死なれません', 'causative': '死なせません', 'potential': '死ねません', 'imperative': '死なないで', 'progressive': '死んでいません', 'past_progressive': '死んでいませんでした'}}}
    
    c = conjugate.Verb("死ぬ", False, True)

    c.forms.assert_equal(expected)

def test_u_godan() :
    expected = {'stem': {'neutral': {'te_form': '救って', 'a_stem': '救わ', 'i_stem': '救い', 'e_stem': '救え', 'o_stem': '救お'}}, 'plain': {'positive': {'nonpast': '救う', 'past': '救った', 'optative': '救いたい', 'past_optative': '救いたかった', 'optative_te_form': '救いたくて', 'volitional': '救おう', 'ba_conditional': '救えば', 'tara_conditional': '救ったら', 'receptive': '救われる', 'causative': '救わせる', 'potential': '救える', 'imperative': '救え', 'progressive': '救っている', 'past_progressive': '救っていた', 'past_presumptive': '救ったろう'}, 'negative': {'nonpast': '救わない', 'past': '救わなかった', 'optative': '救いたくない', 'past_optative': '救いたくなかった', 'optative_te_form': '救いたくなくて', 'ba_conditional': '救わなければ', 'tara_conditional': '救わなかったら', 'receptive': '救われない', 'causative': '救わせない', 'potential': '救えない', 'imperative': '救うな', 'progressive': '救っていない', 'past_progressive': '救っていなかった'}}, 'polite': {'positive': {'nonpast': '救います', 'past': '救いました', 'volitional': '救いましょう', 'tara_conditional': '救いましたら', 'receptive': '救われます', 'causative': '救わせます', 'potential': '救えます', 'progressive': '救っています', 'past_progressive': '救っていました'}, 'negative': {'nonpast': '救いますせん', 'past': '救いますせんでした', 'optative': '救いたくありません', 'tara_conditional': '救いますせんでしたら', 'receptive': '救われません', 'causative': '救わせません', 'potential': '救えません', 'imperative': '救わないで', 'progressive': '救っていません', 'past_progressive': '救っていませんでした'}}}
    
    c = conjugate.Verb("救う", False, True)

    c.forms.assert_equal(expected)

def test_tsu_godan() :
    expected = {'stem': {'neutral': {'te_form': '待って', 'a_stem': '待た', 'i_stem': '待ち', 'e_stem': '待て', 'o_stem': '待と'}}, 'plain': {'positive': {'nonpast': '待つ', 'past': '待った', 'optative': '待ちたい', 'past_optative': '待ちたかった', 'optative_te_form': '待ちたくて', 'volitional': '待とう', 'ba_conditional': '待てば', 'tara_conditional': '待ったら', 'receptive': '待たれる', 'causative': '待たせる', 'potential': '待てる', 'imperative': '待て', 'progressive': '待っている', 'past_progressive': '待っていた', 'past_presumptive': '待ったろう'}, 'negative': {'nonpast': '待たない', 'past': '待たなかった', 'optative': '待ちたくない', 'past_optative': '待ちたくなかった', 'optative_te_form': '待ちたくなくて', 'ba_conditional': '待たなければ', 'tara_conditional': '待たなかったら', 'receptive': '待たれない', 'causative': '待たせない', 'potential': '待てない', 'imperative': '待つな', 'progressive': '待っていない', 'past_progressive': '待っていなかった'}}, 'polite': {'positive': {'nonpast': '待ちます', 'past': '待ちました', 'volitional': '待ちましょう', 'tara_conditional': '待ちましたら', 'receptive': '待たれます', 'causative': '待たせます', 'potential': '待てます', 'progressive': '待っています', 'past_progressive': '待っていました'}, 'negative': {'nonpast': '待ちますせん', 'past': '待ちますせんでした', 'optative': '待ちたくありません', 'tara_conditional': '待ちますせんでしたら', 'receptive': '待たれません', 'causative': '待たせません', 'potential': '待てません', 'imperative': '待たないで', 'progressive': '待っていません', 'past_progressive': '待っていませんでした'}}}
    
    c = conjugate.Verb("待つ", False, True)

    c.forms.assert_equal(expected)

def test_ru_godan() :
    expected = {'stem': {'neutral': {'te_form': '勝って', 'a_stem': '勝ら', 'i_stem': '勝り', 'e_stem': '勝れ', 'o_stem': '勝ろ'}}, 'plain': {'positive': {'nonpast': '勝る', 'past': '勝った', 'optative': '勝りたい', 'past_optative': '勝りたかった', 'optative_te_form': '勝りたくて', 'volitional': '勝ろう', 'ba_conditional': '勝れば', 'tara_conditional': '勝ったら', 'receptive': '勝られる', 'causative': '勝らせる', 'potential': '勝れる', 'imperative': '勝れ', 'progressive': '勝っている', 'past_progressive': '勝っていた', 'past_presumptive': '勝ったろう'}, 'negative': {'nonpast': '勝らない', 'past': '勝らなかった', 'optative': '勝りたくない', 'past_optative': '勝りたくなかった', 'optative_te_form': '勝りたくなくて', 'ba_conditional': '勝らなければ', 'tara_conditional': '勝らなかったら', 'receptive': '勝られない', 'causative': '勝らせない', 'potential': '勝れない', 'imperative': '勝るな', 'progressive': '勝っていない', 'past_progressive': '勝っていなかった'}}, 'polite': {'positive': {'nonpast': '勝ります', 'past': '勝りました', 'volitional': '勝りましょう', 'tara_conditional': '勝りましたら', 'receptive': '勝られます', 'causative': '勝らせます', 'potential': '勝れます', 'progressive': '勝っています', 'past_progressive': '勝っていました'}, 'negative': {'nonpast': '勝りますせん', 'past': '勝りますせんでした', 'optative': '勝りたくありません', 'tara_conditional': '勝りますせんでしたら', 'receptive': '勝られません', 'causative': '勝らせません', 'potential': '勝れません', 'imperative': '勝らないで', 'progressive': '勝っていません', 'past_progressive': '勝っていませんでした'}}}

    c = conjugate.Verb("勝る", False, True)

    c.forms.assert_equal(expected)

def test_suru() :
    expected = {'stem': {'neutral': {'te_form': '勉強して', 'i_stem': '勉強し'}}, 'plain': {'positive': {'nonpast': '勉強する', 'past': '勉強した', 'optative': '勉強したい', 'past_optative': '勉強したかった', 'optative_te_form': '勉強したくて', 'volitional': '勉強しよう', 'ba_conditional': '勉強すれば', 'tara_conditional': '勉強したら', 'receptive': '勉強される', 'causative': '勉強させる', 'potential': '勉強できる', 'imperative': '勉強しろ', 'progressive': '勉強している', 'past_progressive': '勉強していた', 'past_presumptive': '勉強したろう'}, 'negative': {'nonpast': '勉強しない', 'past': '勉強しなかった', 'optative': '勉強したくない', 'past_optative': '勉強したくなかった', 'optative_te_form': '勉強したくなくて', 'ba_conditional': '勉強しなければ', 'tara_conditional': '勉強しなかったら', 'receptive': '勉強されない', 'causative': '勉強させない', 'potential': '勉強できない', 'imperative': '勉強するな', 'progressive': '勉強していない', 'past_progressive': '勉強していなかった'}}, 'polite': {'positive': {'nonpast': '勉強します', 'past': '勉強しました', 'volitional': '勉強しましょう', 'tara_conditional': '勉強しましたら', 'receptive': '勉強されます', 'causative': '勉強させます', 'potential': '勉強できます', 'progressive': '勉強しています', 'past_progressive': '勉強していました'}, 'negative': {'nonpast': '勉強しません', 'past': '勉強しませんでした', 'optative': '勉強したくありません', 'tara_conditional': '勉強しませんでしたら', 'receptive': '勉強されません', 'causative': '勉強させません', 'potential': '勉強できません', 'imperative': '勉強しないで', 'progressive': '勉強していません', 'past_progressive': '勉強していませんでした'}}}
    
    c = conjugate.Verb("勉強する", conjugateAll=True)

    c.forms.assert_equal(expected)

    expected = {'stem': {'neutral': {'te_form': '為て', 'i_stem': '為'}}, 'plain': {'positive': {'nonpast': '為る', 'past': '為た', 'optative': '為たい', 'past_optative': '為たかった', 'optative_te_form': '為たくて', 'volitional': '為よう', 'ba_conditional': '為れば', 'tara_conditional': '為たら', 'receptive': '為れる', 'causative': '為せる', 'potential': '出来る', 'imperative': '為ろ', 'progressive': '為ている', 'past_progressive': '為ていた', 'past_presumptive': '為たろう'}, 'negative': {'nonpast': '為ない', 'past': '為なかった', 'optative': '為たくない', 'past_optative': '為たくなかった', 'optative_te_form': '為たくなくて', 'ba_conditional': '為なければ', 'tara_conditional': '為なかったら', 'receptive': '為れない', 'causative': '為せない', 'potential': '出来ない', 'imperative': '為るな', 'progressive': '為ていない', 'past_progressive': '為ていなかった'}}, 'polite': {'positive': {'nonpast': '為ます', 'past': '為ました', 'volitional': '為ましょう', 'tara_conditional': '為ましたら', 'receptive': '為れます', 'causative': '為せます', 'potential': '出来ます', 'progressive': '為ています', 'past_progressive': '為ていました'}, 'negative': {'nonpast': '為ません', 'past': '為ませんでした', 'optative': '為たくありません', 'tara_conditional': '為ませんでしたら', 'receptive': '為れません', 'causative': '為せません', 'potential': '出来ません', 'imperative': '為ないで', 'progressive': '為ていません', 'past_progressive': '為ていませんでした'}}}

    c = conjugate.Verb("為る", conjugateAll=True)

    c.forms.assert_equal(expected)

def test_gozaru() :
    expected = {'stem': {'neutral': {'te_form': 'ありがとうござって', 'a_stem': 'ありがとうござら', 'i_stem': 'ありがとうござい', 'e_stem': 'ありがとうござれ', 'o_stem': 'ありがとうござろ'}}, 'plain': {'positive': {'nonpast': 'ありがとうござる', 'past': 'ありがとうござった', 'optative': 'ありがとうございたい', 'past_optative': 'ありがとうございたかった', 'optative_te_form': 'ありがとうございたくて', 'volitional': 'ありがとうござろう', 'ba_conditional': 'ありがとうござれば', 'tara_conditional': 'ありがとうござったら', 'receptive': 'ありがとうござられる', 'causative': 'ありがとうござらせる', 'potential': 'ありがとうござれる', 'imperative': 'ありがとうござれ', 'progressive': 'ありがとうござっている', 'past_progressive': 'ありがとうござっていた', 'past_presumptive': 'ありがとうござったろう'}, 'negative': {'nonpast': 'ありがとうござらない', 'past': 'ありがとうござらなかった', 'optative': 'ありがとうございたくない', 'past_optative': 'ありがとうございたくなかった', 'optative_te_form': 'ありがとうございたくなくて', 'ba_conditional': 'ありがとうござらなければ', 'tara_conditional': 'ありがとうござらなかったら', 'receptive': 'ありがとうござられない', 'causative': 'ありがとうござらせない', 'potential': 'ありがとうござれない', 'imperative': 'ありがとうござるな', 'progressive': 'ありがとうござっていない', 'past_progressive': 'ありがとうござっていなかった'}}, 'polite': {'positive': {'nonpast': 'ありがとうございます', 'past': 'ありがとうございました', 'volitional': 'ありがとうございましょう', 'tara_conditional': 'ありがとうございましたら', 'receptive': 'ありがとうござられます', 'causative': 'ありがとうござらせます', 'potential': 'ありがとうござれます', 'progressive': 'ありがとうござっています', 'past_progressive': 'ありがとうござっていました'}, 'negative': {'nonpast': 'ありがとうございますせん', 'past': 'ありがとうございますせんでした', 'optative': 'ありがとうございたくありません', 'tara_conditional': 'ありがとうございますせんでしたら', 'receptive': 'ありがとうござられません', 'causative': 'ありがとうござらせません', 'potential': 'ありがとうござれません', 'imperative': 'ありがとうござらないで', 'progressive': 'ありがとうござっていません', 'past_progressive': 'ありがとうござっていませんでした'}}}
    
    c = conjugate.Verb("ありがとうござる", False, True)

    c.forms.assert_equal(expected)

    expected = {'stem': {'neutral': {'te_form': '御座って', 'a_stem': '御座ら', 'i_stem': "御座い", 'e_stem': '御座れ', 'o_stem': '御座ろ'}}, 'plain': {'positive': {'nonpast': '御座る', 'past': '御座った', 'optative': '御座いたい', 'past_optative': '御座いたかった', 'optative_te_form': '御座いたくて', 'volitional': '御座ろう', 'ba_conditional': '御座れば', 'tara_conditional': '御座ったら', 'receptive': '御座られる', 'causative': '御座らせる', 'potential': '御座れる', 'imperative': '御座れ', 'progressive': '御座っている', 'past_progressive': '御座っていた', 'past_presumptive': '御座ったろう'}, 'negative': {'nonpast': '御座らない', 'past': '御座らなかった', 'optative': '御座いたくない', 'past_optative': '御座いたくなかった', 'optative_te_form': '御座いたくなくて', 'ba_conditional': '御座らなければ', 'tara_conditional': '御座らなかったら', 'receptive': '御座られない', 'causative': '御座らせない', 'potential': '御座れない', 'imperative': '御座るな', 'progressive': '御座っていない', 'past_progressive': '御座っていなかった'}}, 'polite': {'positive': {'nonpast': '御座います', 'past': '御座いました', 'volitional': '御座いましょう', 'tara_conditional': '御座いましたら', 'receptive': '御座られます', 'causative': '御座らせます', 'potential': '御座れます', 'progressive': '御座っています', 'past_progressive': '御座っていました'}, 'negative': {'nonpast': '御座いますせん', 'past': '御座いますせんでした', 'optative': '御座いたくありません', 'tara_conditional': '御座いますせんでしたら', 'receptive': '御座られません', 'causative': '御座らせません', 'potential': '御座れません', 'imperative': '御座らないで', 'progressive': '御座っていません', 'past_progressive': '御座っていませんでした'}}}

    c = conjugate.Verb("御座る", False, True)

    c.forms.assert_equal(expected)

def test_kuru() :
    expected = {'stem': {'neutral': {'te_form': 'きて', 'i_stem': 'き'}}, 'plain': {'positive': {'presumptive': 'こよう', 'receptive': 'こられる', 'causative': 'こさせる', 'potential': 'こられる', 'imperative': 'こい', 'nonpast': 'くる', 'past': 'きた', 'optative': 'きたい', 'past_optative': 'きたかった', 'optative_te_form': 'きたくて', 'volitional': 'きよう', 'ba_conditional': 'くれば', 'tara_conditional': 'きたら', 'progressive': 'きている', 'past_progressive': 'きていた', 'past_presumptive': 'きたろう'}, 'negative': {'nonpast': 'こない', 'past': 'こなかった', 'optative': 'きたくない', 'past_optative': 'きたくなかった', 'optative_te_form': 'きたくなくて', 'ba_conditional': 'こなければ', 'tara_conditional': 'こなかったら', 'receptive': 'こられない', 'causative': 'こさせない', 'potential': 'こられない', 'imperative': 'くるな', 'progressive': 'きていない', 'past_progressive': 'きていなかった'}}, 'polite': {'positive': {'nonpast': 'きます', 'past': 'きました', 'volitional': 'きましょう', 'tara_conditional': 'きましたら', 'receptive': 'こられます', 'causative': 'こさせます', 'potential': 'こられます', 'progressive': 'きています', 'past_progressive': 'きていました'}, 'negative': {'nonpast': 'きません', 'past': 'きませんでした', 'optative': 'きたくありません', 'tara_conditional': 'きませんでしたら', 'receptive': 'こられません', 'causative': 'こさせません', 'potential': 'こられません', 'imperative': 'こないで', 'progressive': 'きていません', 'past_progressive': 'きていませんでした'}}}

    c = conjugate.Verb("くる", False, True)

    c.forms.assert_equal(expected)

    expected = {'stem': {'neutral': {'te_form': '来て', 'i_stem': '来'}}, 'plain': {'positive': {'presumptive': '来よう', 'receptive': '来られる', 'causative': '来させる', 'potential': '来られる', 'imperative': '来い', 'nonpast': '来る', 'past': '来た', 'optative': '来たい', 'past_optative': '来たかった', 'optative_te_form': '来たくて', 'volitional': '来よう', 'ba_conditional': '来れば', 'tara_conditional': '来たら', 'progressive': '来ている', 'past_progressive': '来ていた', 'past_presumptive': '来たろう'}, 'negative': {'nonpast': '来ない', 'past': '来なかった', 'optative': '来たくない', 'past_optative': '来たくなかった', 'optative_te_form': '来たくなくて', 'ba_conditional': '来なければ', 'tara_conditional': '来なかったら', 'receptive': '来られない', 'causative': '来させない', 'potential': '来られない', 'imperative': '来るな', 'progressive': '来ていない', 'past_progressive': '来ていなかった'}}, 'polite': {'positive': {'nonpast': '来ます', 'past': '来ました', 'volitional': '来ましょう', 'tara_conditional': '来ましたら', 'receptive': '来られます', 'causative': '来させます', 'potential': '来られます', 'progressive': '来ています', 'past_progressive': '来ていました'}, 'negative': {'nonpast': '来ません', 'past': '来ませんでした', 'optative': '来たくありません', 'tara_conditional': '来ませんでしたら', 'receptive': '来られません', 'causative': '来させません', 'potential': '来られません', 'imperative': '来ないで', 'progressive': '来ていません', 'past_progressive': '来ていませんでした'}}}

    c = conjugate.Verb("来る", False, True)

    c.forms.assert_equal(expected)
    
def test_ii() :
    expected = {'stem': {'neutral': {'connective': 'かっこよく'}}, 'plain': {'positive': {'past': 'かっこよかった', 'ba_conditional': 'かっこよければ', 'nonpast': 'かっこいい', 'presumptive': 'かっこいいだろう', 'te_form': 'かっこよくて'}, 'negative': {'nonpast': 'かっこよくない', 'past': 'かっこよくなかった', 'presumptive': 'かっこよかっただろう', 'ba_conditional': 'かっこよくなければ', 'te_form': 'かっこよくなくて'}}, 'polite': {'positive': {'nonpast': 'かっこいいです', 'past': 'かっこよかったです', 'presumptive': 'かっこいいでしょう'}, 'negative': {'nonpast': 'かっこよくありません', 'past': 'かっこよくありませんでした', 'presumptive': 'かっこよくないでしょう'}}}
    
    c = conjugate.Adjective("かっこいい", True)

    c.forms.assert_equal(expected)

    expected = {'stem': {'neutral': {'connective':'良く'}}, 'plain': {'positive': {'past': '良かった', 'ba_conditional': '良ければ', 'te_form': '良くて', 'nonpast': '良い', 'presumptive': '良いだろう'}, 'negative': {'nonpast': '良くない', 'past': '良くなかった', 'presumptive': '良かっただろう', 'ba_conditional': '良くなければ', 'te_form': '良くなくて'}}, 'polite': {'negative': {'nonpast': '良くありません', 'past': '良くありませんでした', 'presumptive': '良くないでしょう'}, 'positive': {'nonpast': '良いです', 'past': '良かったです', 'presumptive': '良いでしょう'}}}
    
    c = conjugate.Adjective("良い", True)

    c.forms.assert_equal(expected)

def test_aru() :
    expected = {'stem': {'neutral': {'te_form': 'あって', 'a_stem': 'あら', 'i_stem': 'あり', 'e_stem': 'あれ', 'o_stem': 'あろ'}}, 'plain': {'positive': {'nonpast': 'ある', 'past': 'あった', 'optative': 'ありたい', 'past_optative': 'ありたかった', 'optative_te_form': 'ありたくて', 'volitional': 'あろう', 'ba_conditional': 'あれば', 'tara_conditional': 'あったら', 'receptive': 'あられる', 'causative': 'あらせる', 'potential': 'あれる', 'imperative': 'あれ', 'progressive': 'あっている', 'past_progressive': 'あっていた', 'past_presumptive': 'あったろう'}, 'negative': {'nonpast': 'ない', 'past': 'なかった', 'optative': 'ありたくない', 'past_optative': 'ありたくなかった', 'optative_te_form': 'ありたくなくて', 'ba_conditional': 'なければ', 'tara_conditional': 'なかったら', 'receptive': 'あられない', 'causative': 'あらせない', 'potential': 'あれない', 'imperative': 'あるな', 'progressive': 'あっていない', 'past_progressive': 'あっていなかった'}}, 'polite': {'positive': {'nonpast': 'あります', 'past': 'ありました', 'volitional': 'ありましょう', 'tara_conditional': 'ありましたら', 'receptive': 'あられます', 'causative': 'あらせます', 'potential': 'あれます', 'progressive': 'あっています', 'past_progressive': 'あっていました'}, 'negative': {'nonpast': 'ありますせん', 'past': 'ありますせんでした', 'optative': 'ありたくありません', 'tara_conditional': 'ありますせんでしたら', 'receptive': 'あられません', 'causative': 'あらせません', 'potential': 'あれません', 'imperative': 'ないで', 'progressive': 'あっていません', 'past_progressive': 'あっていませんでした'}}}

    c = conjugate.Verb("ある", False, True)
    
    c.forms.assert_equal(expected)

    expected = {'plain': {'negative': {'nonpast': '無い', 'past': '無かった', 'optative': '在りたくない', 'past_optative': '在りたくなかった', 'optative_te_form': '在りたくなくて', 'ba_conditional': '無ければ', 'tara_conditional': '無かったら', 'receptive': '在られない', 'causative': '在らせない', 'potential': '在れない', 'imperative': '在るな', 'progressive': '在っていない', 'past_progressive': '在っていなかった'}, 'positive': {'nonpast': '在る', 'past': '在った', 'optative': '在りたい', 'past_optative': '在りたかった', 'optative_te_form': '在りたくて', 'volitional': '在ろう', 'ba_conditional': '在れば', 'tara_conditional': '在ったら', 'receptive': '在られる', 'causative': '在らせる', 'potential': '在れる', 'imperative': '在れ', 'progressive': '在っている', 'past_progressive': '在っていた', 'past_presumptive': '在ったろう'}}, 'stem': {'neutral': {'te_form': '在って', 'a_stem': '在ら', 'i_stem': '在り', 'e_stem': '在れ', 'o_stem': '在ろ'}}, 'polite': {'positive': {'nonpast': '在ります', 'past': '在りました', 'volitional': '在りましょう', 'tara_conditional': '在りましたら', 'receptive': '在られます', 'causative': '在らせます', 'potential': '在れます', 'progressive': '在っています', 'past_progressive': '在っていました'}, 'negative': {'nonpast': '在りますせん', 'past': '在りますせんでした', 'optative': '在りたくありません', 'tara_conditional': '在りますせんでしたら', 'receptive': '在られません', 'causative': '在らせません', 'potential': '在れません', 'imperative': '無いで', 'progressive': '在っていません', 'past_progressive': '在っていませんでした'}}}

    c = conjugate.Verb("在る", False, True)
    
    c.forms.assert_equal(expected)

if __name__=="__main__" :
    test_ichidan()
    test_adjective()
    test_ku_godan()
    test_gu_godan()
    test_su_godan()
    test_bu_godan()
    test_mu_godan()
    test_nu_godan()
    test_u_godan()
    test_tsu_godan()
    test_ru_godan()

    #irregulars
    test_suru()
    test_gozaru()
    test_kuru()
    test_ii()
    test_aru()
