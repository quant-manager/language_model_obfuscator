#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2025 James James Johnson. All Rights Reserved.
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
# =============================================================================

###############################################################################
# The program obfuscates selected "Basic Latin" characters (mostly letters)
# from the Unicode range [0000; 007F]. Some or all characters from the
# above range are replaced with similar-looking characters either randomly or
# deterministically. While the obfuscated text still remains human-readable,
# language models will fail to use this obfuscated text for their productive
# training without reverse-obfuscation of this new text during their training
# set preprocessing. Thus, the copyright on the original text is more protected
# with this obfuscation.
###############################################################################

###############################################################################
# Useful links:
#
# https://docs.python.org/3/howto/unicode.html
# https://www.digitalocean.com/community/tutorials/
#         how-to-work-with-unicode-in-python
# https://symbl.cc/en/unicode-table/
# https://www.reuters.com/sustainability/boards-policy-regulation/
#         meta-fends-off-authors-us-copyright-lawsuit-over-ai-2025-06-25/
###############################################################################

# Sample usage:  python .\lmo.py -v 1 -t 4 -i in.txt -o out.txt

import argparse
from pathlib import Path
from random import seed, choice
from datetime import datetime


# 1. Obfuscator deterministic/full replacement
#    Replace "Basic Latin" (0000-007F) with "Fullwidth Form"(FF00-FFEF).
# https://en.wikipedia.org/wiki/Halfwidth_and_Fullwidth_Forms_(Unicode_block)
# https://symbl.cc/en/unicode-table/#halfwidth-and-fullwidth-forms
DICT_OBFUSCATOR_DETER_FULL_FWF = {
    ' \u0020' : '　\u3000',
    '!\u0021' : '！\uFF01',
    '"\u0022' : '＂\uFF02', # '“\u201C″\u2033〃\u3003〝\u301D〞\301E',
    '#\u0023' : '＃\uFF03',
    '$\u0024' : '＄\uFF04',
    '%\u0025' : '％\uFF05', # '⁒\u2052'
    '&\u0026' : '＆\uFF06',
    "'\u0027" : '＇\uFF07', # '‘\u2018'
    '(\u0028' : '（\uFF08',
    ')\u0029' : '）\uFF09',
    '*\u002A' : '＊\uFF0A', # '⁎\u204E⁕\u2055'
    '+\u002B' : '＋\uFF0B',
    ',\u002C' : '，\uFF0C', # '、\u3001',
    '-\u002D' : '－\uFF0D', # '‐\u2010⁃\u2043'
    '.\u002E' : '．\uFF0E',
    '/\u002F' : '／\uFF0F', # '⁄\u2044'
    '0\u0030' : '０\uFF10',
    '1\u0031' : '１\uFF11',
    '2\u0032' : '２\uFF12',
    '3\u0033' : '３\uFF13',
    '4\u0034' : '４\uFF14',
    '5\u0035' : '５\uFF15',
    '6\u0036' : '６\uFF16',
    '7\u0037' : '７\uFF17',
    '8\u0038' : '８\uFF18',
    '9\u0039' : '９\uFF19',
    ':\u003A' : '：\uFF1A',
    ';\u003B' : '；\uFF1B',
    '<\u003C' : '＜\uFF1C',
    '=\u003D' : '＝\uFF1D',
    '>\u003E' : '＞\uFF1E',
    '?\u003F' : '？\uFF1F',
    '@\u0040' : '＠\uFF20',
    #
    'A\u0041' : 'Ａ\uFF21',
    'B\u0042' : 'Ｂ\uFF22',
    'C\u0043' : 'Ｃ\uFF23',
    'D\u0044' : 'Ｄ\uFF24',
    'E\u0045' : 'Ｅ\uFF25',
    'F\u0046' : 'Ｆ\uFF26',
    'G\u0047' : 'Ｇ\uFF27',
    'H\u0048' : 'Ｈ\uFF28',
    'I\u0049' : 'Ｉ\uFF29',
    'J\u004A' : 'Ｊ\uFF2A',
    'K\u004B' : 'Ｋ\uFF2B',
    'L\u004C' : 'Ｌ\uFF2C',
    'M\u004D' : 'Ｍ\uFF2D',
    'N\u004E' : 'Ｎ\uFF2E',
    'O\u004F' : 'Ｏ\uFF2F',
    'P\u0050' : 'Ｐ\uFF30',
    'Q\u0051' : 'Ｑ\uFF31',
    'R\u0052' : 'Ｒ\uFF32',
    'S\u0053' : 'Ｓ\uFF33',
    'T\u0054' : 'Ｔ\uFF34',
    'U\u0055' : 'Ｕ\uFF35',
    'V\u0056' : 'Ｖ\uFF36',
    'W\u0057' : 'Ｗ\uFF37',
    'X\u0058' : 'Ｘ\uFF38',
    'Y\u0059' : 'Ｙ\uFF39',
    'Z\u005A' : 'Ｚ\uFF3A',
    #
    '[\u005B' : '［\uFF3B',
    '\\\u005C': '＼\uFF3C',
    ']\u005D' : '］\uFF3D',
    '^\u005E' : '＾\uFF3E',
    '_\u005F' : '＿\uFF3F',
    '`\u0060' : '｀\uFF40',
    #
    'a\u0061' : 'ａ\uFF41',
    'b\u0062' : 'ｂ\uFF42',
    'c\u0063' : 'ｃ\uFF43',
    'd\u0064' : 'ｄ\uFF44',
    'e\u0065' : 'ｅ\uFF45',
    'f\u0066' : 'ｆ\uFF46',
    'g\u0067' : 'ｇ\uFF47',
    'h\u0068' : 'ｈ\uFF48',
    'i\u0069' : 'ｉ\uFF49',
    'j\u006A' : 'ｊ\uFF4A',
    'k\u006B' : 'ｋ\uFF4B',
    'l\u006C' : 'ｌ\uFF4C',
    'm\u006D' : 'ｍ\uFF4D',
    'n\u006E' : 'ｎ\uFF4E',
    'o\u006F' : 'ｏ\uFF4F',
    'p\u0070' : 'ｐ\uFF50',
    'q\u0071' : 'ｑ\uFF51',
    'r\u0072' : 'ｒ\uFF52',
    's\u0073' : 'ｓ\uFF53',
    't\u0074' : 'ｔ\uFF54',
    'u\u0075' : 'ｕ\uFF55',
    'v\u0076' : 'ｖ\uFF56',
    'w\u0077' : 'ｗ\uFF57',
    'x\u0078' : 'ｘ\uFF58',
    'y\u0079' : 'ｙ\uFF59',
    'z\u007A' : 'ｚ\uFF5A',
    #
    '{\u007B' : '｛\uFF5B',
    '|\u007C' : '｜\uFF5C',
    '}\u007D' : '｝\uFF5D',
    '~\u007E' : '～\uFF5E', # '⁓\u2053〜\u301C'
    #
    '¢\u00A2' : '￠\uFFE0',
    '£\u00A3' : '￡\uFFE1',
    '¥\u00A5' : '￥\uFFE5',
    '·\u00B7' : '･\uFF65',
}

# 2. Obfuscator deterministic/full replacement
#    (using visually best replacement choice for each original letter).
DICT_OBFUSCATOR_DETER_FULL = {
    'A\u0041' : 'А\u0410',
    'B\u0042' : 'Β\u0392',
    'C\u0043' : 'ꓚ\uA4DA',
    'D\u0044' : 'ꓓ\uA4D3',
    'E\u0045' : 'Е\u0415',
    'F\u0046' : 'ꓝ\uA4DD',
    'G\u0047' : 'ꓖ\uA4D6',
    'H\u0048' : 'Η\u0397',
    'I\u0049' : 'І\u0406',
    'J\u004A' : 'Ј\u0408',
    'K\u004B' : 'Κ\u039A',
    'L\u004C' : 'ꓡ\uA4E1',
    'M\u004D' : 'М\u041C',
    'N\u004E' : 'Ν\u039D',
    'O\u004F' : 'О\u041E',
    'P\u0050' : 'Ρ\u03A1',
    'Q\u0051' : 'Ԛ\u051A',
    'R\u0052' : 'ꓣ\uA4E3',
    'S\u0053' : 'Ѕ\u0405',
    'T\u0054' : 'Т\u0422',
    'U\u0055' : 'ꓴ\uA4F4',
    'V\u0056' : 'ꓦ\uA4E6',
    'W\u0057' : 'Ԝ\u051C',
    'X\u0058' : 'ꓫ\uA4EB',
    'Y\u0059' : 'Ү\u04AE',
    'Z\u005A' : 'Ζ\u0396',
    #
    'a\u0061' : 'а\u0430',
    'b\u0062' : 'ɓ\u0253',
    'c\u0063' : 'с\u0441',
    'd\u0064' : 'ԁ\u0501',
    'e\u0065' : 'е\u0435',
    'f\u0066' : 'ꬵ\uAB35',
    'g\u0067' : 'ɡ\u0261',
    'h\u0068' : 'Ⴙ\u10B9',
    'i\u0069' : 'і\u0456',
    'j\u006A' : 'ј\u0458',
    'k\u006B' : 'ⲕ\u2C95',
    'l\u006C' : 'Ꙇ\uA646',
    'm\u006D' : 'ʍ\u028D',
    'n\u006E' : 'ɴ\u0274',
    'o\u006F' : 'о\u043E',
    'p\u0070' : 'р\u0440',
    'q\u0071' : 'ԛ\u051B',
    'r\u0072' : 'ɼ\u027C',
    's\u0073' : 'ѕ\u0455',
    't\u0074' : 'ʈ\u0288',
    'u\u0075' : 'υ\u03C5',
    'v\u0076' : 'ѵ\u0475',
    'w\u0077' : 'ѡ\u0461',
    'x\u0078' : 'х\u0445',
    'y\u0079' : 'γ\u03B3',
    'z\u007A' : 'ʐ\u0290',
}

# 3. Obfuscator random/full replacement.
DICT_OBFUSCATOR_RANDOM_FULL = {
    'A\u0041' : 'Α\u0391А\u0410ꓮ\uA4EE',
    'B\u0042' : 'Β\u0392В\u0412Ⲃ\u2C82ꓐ\uA4D0',
    'C\u0043' : 'Ϲ\u03F9С\u0421ꓚ\uA4DA',
    'D\u0044' : 'ꓓ\uA4D3',
    'E\u0045' : 'Ε\u0395Е\u0415ꓰ\uA4F0',
    'F\u0046' : 'ꓝ\uA4DD',
    'G\u0047' : 'Ԍ\u050Cꓖ\uA4D6',
    'H\u0048' : 'Η\u0397Н\u041DⲎ\u2C8Eꓧ\uA4E7',
    'I\u0049' : 'Ι\u0399І\u0406Ӏ\u04C0Ⲓ\u2C92ꓲ\uA4F2',
    'J\u004A' : 'Ј\u0408ꓙ\uA4D9',
    'K\u004B' : 'Κ\u039AК\u041AⲔ\u2C94ꓗ\uA4D7',
    'L\u004C' : 'ꓡ\uA4E1',
    'M\u004D' : 'Μ\u039CϺ\u03FAМ\u041Cꓟ\uA4DF',
    'N\u004E' : 'Ν\u039Dꓠ\uA4E0',
    'O\u004F' : 'Ο\u039FО\u041EՕ\u0555Ჿ\u1CBFꓳ\uA4F3',
    'P\u0050' : 'Ρ\u03A1Р\u0420ꓑ\uA4D1',
    'Q\u0051' : 'Ԛ\u051A',
    'R\u0052' : 'Ɍ\u024Cꓣ\uA4E3',
    'S\u0053' : 'Ѕ\u0405Տ\u054FᲽ\u1CBDꓢ\uA4E2Ꚃ\uA682',
    'T\u0054' : 'Τ\u03A4Т\u0422',
    'U\u0055' : '⋃\u22C3ꓴ\uA4F4',
    'V\u0056' : '⋁\u22C1ꓦ\uA4E6',
    'W\u0057' : 'Ԝ\u051Cꓪ\uA4EA',
    'X\u0058' : 'Χ\u03A7Х\u0425ꓫ\uA4EB',
    'Y\u0059' : 'Υ\u03A5Ү\u04AEꓬ\uA4EC',
    'Z\u005A' : 'Ζ\u0396Ⴭ\u10CDꓜ\uA4DC',
    #
    'a\u0061' : 'α\u03B1а\u0430',
    'b\u0062' : 'ƅ\u0185ɓ\u0253',
    'c\u0063' : 'ϲ\u03F2с\u0441',
    'd\u0064' : 'ԁ\u0501',
    'e\u0065' : 'е\u0435',
    'f\u0066' : 'ꬵ\uAB35',
    'g\u0067' : 'ɡ\u0261',
    'h\u0068' : 'Һ\u04BAႹ\u10B9',
    'i\u0069' : 'і\u0456',
    'j\u006A' : 'ϳ\u03F3ј\u0458',
    'k\u006B' : 'κ\u03BAк\u043Aⲕ\u2C95',
    'l\u006C' : 'Ꙇ\uA646',
    'm\u006D' : 'ʍ\u028Dм\u043C',
    'n\u006E' : 'ɴ\u0274',
    'o\u006F' : 'ο\u03BFо\u043Eჿ\u10FF',
    'p\u0070' : 'р\u0440',
    'q\u0071' : 'ԛ\u051B',
    'r\u0072' : 'ґ\u0491ɼ\u027Cɾ\u027E',
    's\u0073' : 'ѕ\u0455',
    't\u0074' : 'ʈ\u0288',
    'u\u0075' : 'υ\u03C5',
    'v\u0076' : 'ν\u03BDѵ\u0475',
    'w\u0077' : 'ѡ\u0461ԝ\u051D',
    'x\u0078' : 'х\u0445',
    'y\u0079' : 'γ\u03B3ү\u04AF',
    'z\u007A' : 'ȥ\u0225ɀ\u0240ʐ\u0290',
}


# 4. Obfuscator random/partial replacement.
DICT_OBFUSCATOR_RANDOM_PARTIAL = {
    'A\u0041' : 'A\u0041Α\u0391А\u0410ꓮ\uA4EE',
    'B\u0042' : 'B\u0042Β\u0392В\u0412Ⲃ\u2C82ꓐ\uA4D0',
    'C\u0043' : 'C\u0043Ϲ\u03F9С\u0421ꓚ\uA4DA',
    'D\u0044' : 'D\u0044ꓓ\uA4D3',
    'E\u0045' : 'E\u0045Ε\u0395Е\u0415ꓰ\uA4F0',
    'F\u0046' : 'F\u0046ꓝ\uA4DD',
    'G\u0047' : 'G\u0047Ԍ\u050Cꓖ\uA4D6',
    'H\u0048' : 'H\u0048Η\u0397Н\u041Dꓧ\uA4E7',
    'I\u0049' : 'I\u0049Ι\u0399І\u0406Ӏ\u04C0',
    'J\u004A' : 'J\u004AЈ\u0408',
    'K\u004B' : 'K\u004BΚ\u039AК\u041Aꓗ\uA4D7',
    'L\u004C' : 'L\u004Cꓡ\uA4E1',
    'M\u004D' : 'M\u004DΜ\u039CМ\u041C',
    'N\u004E' : 'N\u004EΝ\u039Dꓠ\uA4E0',
    'O\u004F' : 'O\u004FΟ\u039FО\u041EՕ\u0555Ჿ\u1CBFꓳ\uA4F3',
    'P\u0050' : 'P\u0050Ρ\u03A1Р\u0420ꓑ\uA4D1',
    'Q\u0051' : 'Q\u0051Ԛ\u051A',
    'R\u0052' : 'R\u0052Ɍ\u024Cꓣ\uA4E3',
    'S\u0053' : 'S\u0053Ѕ\u0405Տ\u054FᲽ\u1CBDꓢ\uA4E2Ꚃ\uA682',
    'T\u0054' : 'T\u0054Τ\u03A4Т\u0422',
    'U\u0055' : 'U\u0055ꓴ\uA4F4',
    'V\u0056' : 'V\u0056ꓦ\uA4E6',
    'W\u0057' : 'W\u0057Ԝ\u051Cꓪ\uA4EA',
    'X\u0058' : 'X\u0058Χ\u03A7Х\u0425ꓫ\uA4EB',
    'Y\u0059' : 'Y\u0059Υ\u03A5Ү\u04AEꓬ\uA4EC',
    'Z\u005A' : 'Z\u005AΖ\u0396Ⴭ\u10CDꓜ\uA4DC',
    #
    'a\u0061' : 'a\u0061а\u0430',
    'b\u0062' : 'b\u0062',
    'c\u0063' : 'c\u0063ϲ\u03F2с\u0441',
    'd\u0064' : 'd\u0064ԁ\u0501',
    'e\u0065' : 'e\u0065е\u0435',
    'f\u0066' : 'f\u0066',
    'g\u0067' : 'g\u0067ɡ\u0261',
    'h\u0068' : 'h\u0068',
    'i\u0069' : 'i\u0069і\u0456',
    'j\u006A' : 'j\u006Aϳ\u03F3ј\u0458',
    'k\u006B' : 'k\u006B',
    'l\u006C' : 'l\u006C',
    'm\u006D' : 'm\u006D',
    'n\u006E' : 'n\u006E',
    'o\u006F' : 'o\u006Fο\u03BFо\u043Eჿ\u10FF',
    'p\u0070' : 'p\u0070р\u0440',
    'q\u0071' : 'q\u0071ԛ\u051B',
    'r\u0072' : 'r\u0072',
    's\u0073' : 's\u0073ѕ\u0455',
    't\u0074' : 't\u0074',
    'u\u0075' : 'u\u0075',
    'v\u0076' : 'v\u0076ν\u03BDѵ\u0475',
    'w\u0077' : 'w\u0077ѡ\u0461ԝ\u051D',
    'x\u0078' : 'x\u0078х\u0445',
    'y\u0079' : 'y\u0079',
    'z\u007A' : 'z\u007A',
}

# 5. Obfuscator random/partial replacement using all candidate symbols.
DICT_OBFUSCATOR_RANDOM_ALL = {
    'A\u0041' : 'A\u0041Α\u0391А\u0410ꓮ\uA4EEＡ\uFF21',
    'B\u0042' : 'B\u0042Β\u0392В\u0412Ⲃ\u2C82ꓐ\uA4D0Ｂ\uFF22',
    'C\u0043' : 'C\u0043Ϲ\u03F9С\u0421ꓚ\uA4DAＣ\uFF23',
    'D\u0044' : 'D\u0044ꓓ\uA4D3Ｄ\uFF24',
    'E\u0045' : 'E\u0045Ε\u0395Е\u0415ꓰ\uA4F0Ｅ\uFF25',
    'F\u0046' : 'F\u0046ꓝ\uA4DDＦ\uFF26',
    'G\u0047' : 'G\u0047Ԍ\u050Cꓖ\uA4D6Ｇ\uFF27',
    'H\u0048' : 'H\u0048Η\u0397Н\u041DⲎ\u2C8Eꓧ\uA4E7Ｈ\uFF28',
    'I\u0049' : 'I\u0049Ι\u0399І\u0406Ӏ\u04C0Ⲓ\u2C92ꓲ\uA4F2Ｉ\uFF29',
    'J\u004A' : 'J\u004AЈ\u0408ꓙ\uA4D9Ｊ\uFF2A',
    'K\u004B' : 'K\u004BΚ\u039AК\u041AⲔ\u2C94ꓗ\uA4D7Ｋ\uFF2B',
    'L\u004C' : 'L\u004Cꓡ\uA4E1Ｌ\uFF2C',
    'M\u004D' : 'M\u004DΜ\u039CϺ\u03FAМ\u041Cꓟ\uA4DFＭ\uFF2D',
    'N\u004E' : 'N\u004EΝ\u039Dꓠ\uA4E0Ｎ\uFF2E',
    'O\u004F' : 'O\u004FΟ\u039FО\u041EՕ\u0555Ჿ\u1CBFꓳ\uA4F3Ｏ\uFF2F',
    'P\u0050' : 'P\u0050Ρ\u03A1Р\u0420ꓑ\uA4D1Ｐ\uFF30',
    'Q\u0051' : 'Q\u0051Ԛ\u051AＱ\uFF31',
    'R\u0052' : 'R\u0052Ɍ\u024Cꓣ\uA4E3Ｒ\uFF32',
    'S\u0053' : 'S\u0053Ѕ\u0405Տ\u054FᲽ\u1CBDꓢ\uA4E2Ꚃ\uA682Ｓ\uFF33',
    'T\u0054' : 'T\u0054Τ\u03A4Т\u0422Ｔ\uFF34',
    'U\u0055' : 'U\u0055⋃\u22C3ꓴ\uA4F4Ｕ\uFF35',
    'V\u0056' : 'V\u0056⋁\u22C1ꓦ\uA4E6Ｖ\uFF36',
    'W\u0057' : 'W\u0057Ԝ\u051Cꓪ\uA4EAＷ\uFF37',
    'X\u0058' : 'X\u0058Χ\u03A7Х\u0425ꓫ\uA4EBＸ\uFF38',
    'Y\u0059' : 'Y\u0059Υ\u03A5Ү\u04AEꓬ\uA4ECＹ\uFF39',
    'Z\u005A' : 'Z\u005AΖ\u0396Ⴭ\u10CDꓜ\uA4DCＺ\uFF3A',
    #
    'a\u0061' : 'a\u0061α\u03B1а\u0430ａ\uFF41',
    'b\u0062' : 'b\u0062ƅ\u0185ɓ\u0253ｂ\uFF42',
    'c\u0063' : 'c\u0063ϲ\u03F2с\u0441ｃ\uFF43',
    'd\u0064' : 'd\u0064ԁ\u0501ｄ\uFF44',
    'e\u0065' : 'e\u0065е\u0435ｅ\uFF45',
    'f\u0066' : 'f\u0066ꬵ\uAB35ｆ\uFF46',
    'g\u0067' : 'g\u0067ɡ\u0261ｇ\uFF47',
    'h\u0068' : 'h\u0068Һ\u04BAႹ\u10B9ｈ\uFF48',
    'i\u0069' : 'i\u0069і\u0456ｉ\uFF49',
    'j\u006A' : 'j\u006Aϳ\u03F3ј\u0458ｊ\uFF4A',
    'k\u006B' : 'k\u006Bκ\u03BAк\u043Aⲕ\u2C95ｋ\uFF4B',
    'l\u006C' : 'l\u006CꙆ\uA646ｌ\uFF4C',
    'm\u006D' : 'm\u006Dʍ\u028Dм\u043Cｍ\uFF4D',
    'n\u006E' : 'n\u006Eɴ\u0274ｎ\uFF4E',
    'o\u006F' : 'o\u006Fο\u03BFо\u043Eჿ\u10FFｏ\uFF4F',
    'p\u0070' : 'p\u0070р\u0440ｐ\uFF50',
    'q\u0071' : 'q\u0071ԛ\u051Bｑ\uFF51',
    'r\u0072' : 'r\u0072ґ\u0491ɼ\u027Cɾ\u027Eｒ\uFF52',
    's\u0073' : 's\u0073ѕ\u0455ｓ\uFF53',
    't\u0074' : 't\u0074ʈ\u0288ｔ\uFF54',
    'u\u0075' : 'u\u0075υ\u03C5ｕ\uFF55',
    'v\u0076' : 'v\u0076ν\u03BDѵ\u0475ｖ\uFF56',
    'w\u0077' : 'w\u0077ѡ\u0461ԝ\u051Dｗ\uFF57',
    'x\u0078' : 'x\u0078х\u0445ｘ\uFF58',
    'y\u0079' : 'y\u0079γ\u03B3ү\u04AFｙ\uFF59',
    'z\u007A' : 'z\u007Aȥ\u0225ɀ\u0240ʐ\u0290ｚ\uFF5A',
}

DICT_OBFUSCATOR_TYPES = {
    1 : "1. Deterministic full replacement with Fullwidth Form.",
    2 : "2. Deterministic full replacement with one similar symbol.",
    3 : "3. Random full replacement with various similar symbols.",
    4 : "4. Random partial replacement with various similar symbols.",
    5 : "5. Random partial replacement with all rougly similar symbols.",
}

'''
# Relative frequency in the English language (text)
# https://en.wikipedia.org/wiki/Letter_frequency
e : 12.7
t :  9.1
a :  8.2
o :  7.5
i :  7.0
n :  6.7
s :  6.3
h :  6.1
r :  6.0
d :  4.3
l :  4.0
c :  2.8
u :  2.8
m :  2.4
w :  2.4
f :  2.2
g :  2.0
y :  2.0
p :  1.9
b :  1.5
v :  0.98
k :  0.77
j :  0.15
x :  0.15
q :  0.095
z :  0.074
'''

# Validation:
def validate_obfuscator(dict_obfuscator) :
    for(key, value) in dict_obfuscator.items() :
        if len(key) != 2 or key[0] != key[1]:
            print ("Invalid key ", key)
        if len(value) % 2 != 0 :
            print ("Invalid value length", value)
        for i in range(0,len(value),2) :
            if value[i] != value[i+1]:
                print ("Invalid value ", value)
                break

'''
# Unit test:

validate_obfuscator(dict_obfuscator = DICT_OBFUSCATOR_DETER_FULL_FWF)
validate_obfuscator(dict_obfuscator = DICT_OBFUSCATOR_DETER_FULL)
validate_obfuscator(dict_obfuscator = DICT_OBFUSCATOR_RANDOM_FULL)
validate_obfuscator(dict_obfuscator = DICT_OBFUSCATOR_RANDOM_PARTIAL)
validate_obfuscator(dict_obfuscator = DICT_OBFUSCATOR_RANDOM_ALL)

# seed(a = 12345)
seed(datetime.now().timestamp())
# str_in = 'ôcaoA'
str_in = 'ABCDEFGHIJKLMNOPRSTUVWXYZ abcdefghijklmnoprstuvwxyz'
str_out = ''.join(tuple(map(
    lambda x: choice(DICT_OBFUSCATOR_RANDOM_ALL.get(x+x,x)),str_in)))
print(str_in)
print(str_out)
'''

def main(
         obfuscator_type_index : int,
         input_file_name : str,
         output_file_name : str,
         integer_random_seed : int = None,
         verbosity : int = 0,
         ) :
    if 1 <= obfuscator_type_index <= 5 :
        if Path(input_file_name).is_file() :
            if not Path(output_file_name).is_dir() :
                if Path(output_file_name).is_file() :
                    Path(output_file_name).unlink()
                if not Path(output_file_name).is_file() :
                    if verbosity == 1 :
                        print("Obfuscator type index: " +
                              DICT_OBFUSCATOR_TYPES[obfuscator_type_index])
                        print("Input file name: " + input_file_name)
                        print("Output file name: " + output_file_name)
                        print()
                    lst_dict_obfuscators = [
                        DICT_OBFUSCATOR_DETER_FULL_FWF,
                        DICT_OBFUSCATOR_DETER_FULL,
                        DICT_OBFUSCATOR_RANDOM_FULL,
                        DICT_OBFUSCATOR_RANDOM_PARTIAL,
                        DICT_OBFUSCATOR_RANDOM_ALL,
                        ]
                    for dict_obfuscator in lst_dict_obfuscators :
                        validate_obfuscator(
                            dict_obfuscator = dict_obfuscator)
                    dict_active_obfuscator = lst_dict_obfuscators[
                        obfuscator_type_index - 1]
                    if integer_random_seed is None :
                        seed(datetime.now().timestamp())
                    else :
                        seed(a = integer_random_seed)
                    with open(input_file_name, 'r', encoding='utf-8') as file:
                        str_in = file.read()
                    str_out = ''.join(tuple(map(lambda x: choice(
                        dict_active_obfuscator.get(x+x, x)), str_in)))
                    if verbosity == 1 :
                        print("Input file:\n")
                        print(str_in)
                        print("Output file:\n")
                        print(str_out)
                        print()
                    with open(output_file_name, "w", encoding='utf-8') as file:
                        file.write(str_out)
                else :
                    raise FileExistsError(
                        "Output text file cannot be removed.")
            else :
                raise FileExistsError(
                    "Output text file name is the directory name.")
        else :
            raise FileNotFoundError("Input text file does not exist.")
    else :
        raise ValueError("Obfuscator type index must be beterrn 1 and 5.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--integer_random_seed",
        help = "The integer seed for random choices during obfuscation.",
        type = int,
        required = False,
    )
    parser.add_argument(
        "-v",
        "--verbosity",
        help = "Output verbosity integer at 0 for no traces and 1 for traces.",
        type = int,
        required = False,
    )
    parser.add_argument(
        "-t",
        "--obfuscator_type_index",
        help = '\n'.join((
            "The index of the obfuscator type in range from 1 to 5:",
            DICT_OBFUSCATOR_TYPES[1],
            DICT_OBFUSCATOR_TYPES[2],
            DICT_OBFUSCATOR_TYPES[3],
            DICT_OBFUSCATOR_TYPES[4],
            DICT_OBFUSCATOR_TYPES[5],
            "\n")),
        type = int,
        required = True,
    )
    parser.add_argument(
        "-i",
        "--input_file_name",
        help = "The name of the input text file.",
        type = str,
        required = True,
    )
    parser.add_argument(
        "-o",
        "--output_file_name",
        help = "The name of the output text file.",
        type = str,
        required = True,
    )
    args = parser.parse_args()
    main(**vars(args))
