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

from .util.bundle import Bundle
from . import i_adjective

def stem_neutral_te_form(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("stem","neutral","te_form")
        if cache is not None : return cache

    ret = word[:-1]+"て"
    if forms is not None : forms.recursive_set("stem","neutral","te_form",ret)
    return ret

def stem_neutral_i_stem(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("stem","neutral","i_stem")
        if cache is not None : return cache

    ret = word[:-1]
    if forms is not None : forms.recursive_set("stem","neutral","i_stem",ret)
    return ret

def plain_positive_nonpast(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","positive","nonpast")
        if cache is not None : return cache

    ret = word
    if forms is not None : forms.recursive_set("plain","positive","nonpast",ret)
    return ret

def plain_positive_past(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","positive","past")
        if cache is not None : return cache

    ret = word[:-1]+"た"
    if forms is not None : forms.recursive_set("plain","positive","past",ret)
    return ret

def plain_positive_optative(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","positive","optative")
        if cache is not None : return cache

    ret = word[:-1]+"たい"
    if forms is not None : forms.recursive_set("plain","positive","optative",ret)
    return ret

def plain_positive_optative_past(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","positive","optative_past")
        if cache is not None : return cache

    ret = i_adjective.plain_positive_past(plain_positive_optative(word, forms), None)
    if forms is not None : forms.recursive_set("plain","positive","optative_past",ret)
    return ret

def plain_positive_optative_te_form(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","positive","optative_te_form")
        if cache is not None : return cache

    ret = i_adjective.plain_positive_te_form(plain_positive_optative(word, forms), None)
    if forms is not None : forms.recursive_set("plain","positive","optative_te_form",ret)
    return ret

def plain_positive_volitional(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","positive","volitional")
        if cache is not None : return cache

    ret = word[:-1]+"よう"
    if forms is not None : forms.recursive_set("plain","positive","volitional",ret)
    return ret

def plain_positive_ba_conditional(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","positive","ba_conditional")
        if cache is not None : return cache

    ret = word[:-1]+"れば"
    if forms is not None : forms.recursive_set("plain","positive","ba_conditional",ret)
    return ret

def plain_positive_tara_conditional(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","positive","tara_conditional")
        if cache is not None : return cache

    ret = plain_positive_past(word, forms)+"ら"
    if forms is not None : forms.recursive_set("plain","positive","tara_conditional",ret)
    return ret

def plain_positive_receptive(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","positive","receptive")
        if cache is not None : return cache

    ret = word[:-1]+"られる"
    if forms is not None : forms.recursive_set("plain","positive","receptive",ret)
    return ret

def plain_positive_causative(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","positive","causative")
        if cache is not None : return cache

    ret = word[:-1]+"らせる"
    if forms is not None : forms.recursive_set("plain","positive","causative",ret)
    return ret

def plain_positive_potential(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","positive","potential")
        if cache is not None : return cache

    ret = plain_positive_receptive(word, forms)
    if forms is not None : forms.recursive_set("plain","positive","potential",ret)
    return ret

def plain_positive_imperative(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","positive","imperative")
        if cache is not None : return cache

    ret = word[:-1]+"ろ"
    if forms is not None : forms.recursive_set("plain","positive","imperative",ret)
    return ret

def plain_positive_progressive(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","positive","progressive")
        if cache is not None : return cache

    ret = stem_neutral_te_form(word, forms)+"いる"
    if forms is not None : forms.recursive_set("plain","positive","progressive",ret)
    return ret

def plain_positive_past_progressive(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","positive","past_progressive")
        if cache is not None : return cache

    ret = plain_positive_past(plain_positive_progressive(word, forms), None)
    if forms is not None : forms.recursive_set("plain","positive","past_progressive",ret)
    return ret

def plain_positive_past_presumptive(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","positive","past_presumptive")
        if cache is not None : return cache

    ret = plain_positive_past(word, forms)+"ろう"
    if forms is not None : forms.recursive_set("plain","positive","past_presumptive",ret)
    return ret

def plain_negative_nonpast(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","negative","nonpast")
        if cache is not None : return cache

    ret = word[:-1]+"ない"
    if forms is not None : forms.recursive_set("plain","negative","nonpast",ret)
    return ret

def plain_negative_past(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","negative","past")
        if cache is not None : return cache

    ret = i_adjective.plain_positive_past(plain_negative_nonpast(word, forms), None)
    if forms is not None : forms.recursive_set("plain","negative","past",ret)
    return ret

def plain_negative_optative(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","negative","optative")
        if cache is not None : return cache

    ret = i_adjective.plain_negative_nonpast(plain_positive_optative(word, forms), None)
    if forms is not None : forms.recursive_set("plain","negative","optative",ret)
    return ret

def plain_negative_optative_past(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","negative","optative_past")
        if cache is not None : return cache

    ret = i_adjective.plain_negative_past(plain_positive_optative(word, forms), None)
    if forms is not None : forms.recursive_set("plain","negative","optative_past",ret)
    return ret

def plain_negative_optative_te_form(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","negative","optative_te_form")
        if cache is not None : return cache

    ret = i_adjective.plain_negative_te_form(plain_positive_optative(word, forms), None)
    if forms is not None : forms.recursive_set("plain","negative","optative_te_form",ret)
    return ret

def plain_negative_ba_conditional(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","negative","ba_conditional")
        if cache is not None : return cache

    ret = i_adjective.plain_positive_ba_conditional(plain_negative_past(word, forms), None)
    if forms is not None : forms.recursive_set("plain","negative","ba_conditional",ret)
    return ret

def plain_negative_tara_conditional(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","negative","tara_conditional")
        if cache is not None : return cache

    ret = plain_negative_past(word, forms)+"ら"
    if forms is not None : forms.recursive_set("plain","negative","tara_conditional",ret)
    return ret

def plain_negative_receptive(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","negative","receptive")
        if cache is not None : return cache

    ret = plain_negative_nonpast(plain_positive_receptive(word, forms), None)
    if forms is not None : forms.recursive_set("plain","negative","receptive",ret)
    return ret

def plain_negative_causative(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","negative","causative")
        if cache is not None : return cache

    ret = plain_negative_nonpast(plain_positive_causative(word, forms), None)
    if forms is not None : forms.recursive_set("plain","negative","causative",ret)
    return ret

def plain_negative_potential(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","negative","potential")
        if cache is not None : return cache

    ret = plain_negative_nonpast(plain_positive_potential(word, forms), None)
    if forms is not None : forms.recursive_set("plain","negative","potential",ret)
    return ret

def plain_negative_imperative(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","negative","imperative")
        if cache is not None : return cache

    ret = word+"な"
    if forms is not None : forms.recursive_set("plain","negative","imperative",ret)
    return ret

def plain_negative_progressive(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","negative","progressive")
        if cache is not None : return cache

    ret = plain_negative_nonpast(plain_positive_progressive(word, forms), None)
    if forms is not None : forms.recursive_set("plain","negative","progressive",ret)
    return ret

def plain_negative_past_progressive(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("plain","negative","past_progressive")
        if cache is not None : return cache

    ret = plain_negative_past(plain_positive_progressive(word, forms), None)
    if forms is not None : forms.recursive_set("plain","negative","past_progressive",ret)
    return ret

def polite_positive_nonpast(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("polite","positive","nonpast")
        if cache is not None : return cache

    ret = word[:-1]+"ます"
    if forms is not None : forms.recursive_set("polite","positive","nonpast",ret)
    return ret

def polite_positive_past(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("polite","positive","past")
        if cache is not None : return cache

    ret = word[:-1]+"ました"
    if forms is not None : forms.recursive_set("polite","positive","past",ret)
    return ret

def polite_positive_volitional(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("polite","positive","volitional")
        if cache is not None : return cache

    ret = word[:-1]+"ましょう"
    if forms is not None : forms.recursive_set("polite","positive","volitional",ret)
    return ret

def polite_positive_tara_conditional(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("polite","positive","tara_conditional")
        if cache is not None : return cache

    ret = polite_positive_past(word, forms)+"ら"
    if forms is not None : forms.recursive_set("polite","positive","tara_conditional",ret)
    return ret

def polite_positive_receptive(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("polite","positive","receptive")
        if cache is not None : return cache

    ret = polite_positive_nonpast(plain_positive_receptive(word, forms), None)
    if forms is not None : forms.recursive_set("polite","positive","receptive",ret)
    return ret

def polite_positive_causative(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("polite","positive","causative")
        if cache is not None : return cache

    ret = polite_positive_nonpast(plain_positive_causative(word, forms), None)
    if forms is not None : forms.recursive_set("polite","positive","causative",ret)
    return ret

def polite_positive_potential(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("polite","positive","potential")
        if cache is not None : return cache

    ret = polite_positive_nonpast(plain_positive_potential(word, forms), None)
    if forms is not None : forms.recursive_set("polite","positive","potential",ret)
    return ret

def polite_positive_progressive(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("polite","positive","progressive")
        if cache is not None : return cache

    ret = polite_positive_nonpast(plain_positive_progressive(word, forms), None)
    if forms is not None : forms.recursive_set("polite","positive","progressive",ret)
    return ret

def polite_positive_past_progressive(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("polite","positive","past_progressive")
        if cache is not None : return cache

    ret = polite_positive_past(plain_positive_progressive(word, forms), None)
    if forms is not None : forms.recursive_set("polite","positive","past_progressive",ret)
    return ret

def polite_negative_nonpast(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("polite","negative","nonpast")
        if cache is not None : return cache

    ret = word[:-1]+"ません"
    if forms is not None : forms.recursive_set("polite","negative","nonpast",ret)
    return ret

def polite_negative_past(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("polite","negative","past")
        if cache is not None : return cache

    ret = polite_negative_nonpast(word, forms)+"でした"
    if forms is not None : forms.recursive_set("polite","negative","past",ret)
    return ret

def polite_negative_optative(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("polite","negative","optative")
        if cache is not None : return cache

    ret = i_adjective.polite_negative_nonpast(plain_positive_optative(word, forms), None)
    if forms is not None : forms.recursive_set("polite","negative","optative",ret)
    return ret

def polite_negative_tara_conditional(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("polite","negative","tara_conditional")
        if cache is not None : return cache

    ret = polite_negative_past(word, forms)+"ら"
    if forms is not None : forms.recursive_set("polite","negative","tara_conditional",ret)
    return ret

def polite_negative_receptive(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("polite","negative","receptive")
        if cache is not None : return cache

    ret = polite_negative_nonpast(plain_positive_receptive(word, forms), None)
    if forms is not None : forms.recursive_set("polite","negative","receptive",ret)
    return ret

def polite_negative_causative(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("polite","negative","causative")
        if cache is not None : return cache

    ret = polite_negative_nonpast(plain_positive_causative(word, forms), None)
    if forms is not None : forms.recursive_set("polite","negative","causative",ret)
    return ret

def polite_negative_potential(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("polite","negative","potential")
        if cache is not None : return cache

    ret = polite_negative_nonpast(plain_positive_potential(word, forms), None)
    if forms is not None : forms.recursive_set("polite","negative","potential",ret)
    return ret

def polite_negative_imperative(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("polite","negative","imperative")
        if cache is not None : return cache

    ret = plain_negative_nonpast(word, forms)+"で"
    if forms is not None : forms.recursive_set("polite","negative","imperative",ret)
    return ret

def polite_negative_progressive(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("polite","negative","progressive")
        if cache is not None : return cache

    ret = polite_negative_nonpast(plain_positive_progressive(word, forms), None)
    if forms is not None : forms.recursive_set("polite","negative","progressive",ret)
    return ret

def polite_negative_past_progressive(word:str, forms:Bundle) :
    if forms is not None :
        cache = forms.recursive_get("polite","negative","past_progressive")
        if cache is not None : return cache

    ret = polite_negative_past(plain_positive_progressive(word, forms), None)
    if forms is not None : forms.recursive_set("polite","negative","past_progressive",ret)
    return ret

lookup = Bundle(
    stem = Bundle(
        neutral = Bundle(
            te_form = stem_neutral_te_form,
            i_stem = stem_neutral_i_stem
        )
    ),
    plain = Bundle(
        positive = Bundle(
            nonpast = plain_positive_nonpast,
            past = plain_positive_past,
            optative = plain_positive_optative,
            optative_past = plain_positive_optative_past,
            optative_te_form = plain_positive_optative_te_form,
            volitional = plain_positive_volitional,
            ba_conditional = plain_positive_ba_conditional,
            tara_conditional = plain_positive_tara_conditional,
            receptive = plain_positive_receptive,
            causative = plain_positive_causative,
            potential = plain_positive_potential,
            imperative = plain_positive_imperative,
            progressive = plain_positive_progressive,
            past_progressive = plain_positive_past_progressive,
            past_presumptive = plain_positive_past_presumptive
        ),
        negative = Bundle(
            nonpast = plain_negative_nonpast,
            past = plain_negative_past,
            optative = plain_negative_optative,
            optative_past = plain_negative_optative_past,
            optative_te_form = plain_negative_optative_te_form,
            ba_conditional = plain_negative_ba_conditional,
            tara_conditional = plain_negative_tara_conditional,
            receptive = plain_negative_receptive,
            causative = plain_negative_causative,
            potential = plain_negative_potential,
            imperative = plain_negative_imperative,
            progressive = plain_negative_progressive,
            past_progressive = plain_negative_past_progressive
        )
    ),

    polite = Bundle(
        positive = Bundle(
            nonpast = polite_positive_nonpast,
            past = polite_positive_past,
            volitional = polite_positive_volitional,
            tara_conditional = polite_positive_tara_conditional,
            receptive = polite_positive_receptive,
            causative = polite_positive_causative,
            potential = polite_positive_potential,
            progressive = polite_positive_progressive,
            past_progressive = polite_positive_past_progressive
        ),
        negative = Bundle(
            nonpast = polite_negative_nonpast,
            past = polite_negative_past,
            optative = polite_negative_optative,
            tara_conditional = polite_negative_tara_conditional,
            receptive = polite_negative_receptive,
            causative = polite_negative_causative,
            potential = polite_negative_potential,
            imperative = polite_negative_imperative,
            progressive = polite_negative_progressive,
            past_progressive = polite_negative_past_progressive
        )
    )
)
