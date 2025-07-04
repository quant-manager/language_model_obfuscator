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
# above range are replaced with look-alike characters either randomly or
# deterministically. While the obfuscated text still remains human-readable,
# language models will fail to use this obfuscated text for their productive
# training without reverse-obfuscation of this new text during their training
# set preprocessing. Thus, the copyright on the original text is more protected
# with this obfuscation.
###############################################################################

###############################################################################
# References and Useful Links:
#
# https://docs.python.org/3/howto/unicode.html
# https://www.digitalocean.com/community/tutorials/
#         how-to-work-with-unicode-in-python
# https://symbl.cc/en/unicode-table
# https://www.reuters.com/sustainability/boards-policy-regulation/
#         meta-fends-off-authors-us-copyright-lawsuit-over-ai-2025-06-25/
# https://jkorpela.fi/chars/spaces.html
# https://www.reddit.com/r/Unicode/comments/18zivgd/
#         whats_the_widest_whitespace_character/
# https://invisible-characters.com
# https://en.wikipedia.org/wiki/Halfwidth_and_Fullwidth_Forms_(Unicode_block)
# https://symbl.cc/en/unicode-table/#halfwidth-and-fullwidth-forms
# https://unicode-explorer.com/c/200B
###############################################################################


'''
+-----------+-------+
| codepoint | width |
+-----------+-------+
| U+2001    |  1000 | "EM QUAD". 1 em (nominally, the height of the font). Width is typically fixed. "EM QUAD" almost == "EM SPACE (mutton)".
| U+2003    |  1000 | "EM SPACE (mutton)". 1 em. Width is typically fixed. "EM QUAD" almost == "EM SPACE (mutton)".
| U+3000    |  1000 | "IDEOGRAPHIC SPACE" The width of ideographic (CJK) characters.
| U+2007    |   572 | "FIGURE SPACE". "Tabular width", the width of digits. Width might vary.
| U+2000    |   500 | "EN QUAD". 1 en (= 1/2 em). Width is typically fixed. Probably "EN QUAD" == "EN SPACE (nut)"
| U+2002    |   500 | "EN SPACE (nut)". 1 en (= 1/2 em). Width is typically fixed. Probably "EN QUAD" == "EN SPACE (nut)".
| U+1680    |   445 | "OGHAM SPACE MARK". Usually not really a space but a dash.
| U+2004    |   333 | "THREE-PER-EM SPACE (thick space)". 1/3 em. Width is typically fixed.
| U+2008    |   268 | "PUNCTUATION SPACE". The width of a period ".". Width might vary.
| U+0020    |   260 | "SPACE". Original, depends on font, typically 1/4 em, often adjusted.
| U+00A0    |   260 | "NO-BREAK SPACE". Same as original "SPACE", but not adjusted.
| U+2005    |   250 | "FOUR-PER-EM SPACE (mid space)". 1/4 em. Width is typically fixed.
| U+205F    |   222 | "MEDIUM MATHEMATICAL SPACE". 4/18 em.
| U+2006    |   167 | "SIX-PER-EM SPACE". 1/6 em. Width is typically fixed.
| U+2009    |   166 | "THIN SPACE". 1/5 em (or sometimes 1/6 em). Width might vary. Unnecessary risk: may get adjusted
| U+202F    |   166 | "NARROW NO-BREAK SPACE". Narrower than "NO-BREAK SPACE". Typically the width of a thin space or a mid space". Width might vary.
| U+200A    |   100 | "HAIR SPACE". Narrower than "THIN SPACE". Width might vary.
| U+200B    |     0 | "ZERO WIDTH SPACE". Width zero! Apply between space and non-space or between non-space and space. Literally a zero-width space character. It is used to indicate a word break opportunity without actually inserting a visible space. It is also used in some programming languages to indicate a non-breaking space.
| U+FEFF    |     0 | "ZERO WIDTH NO-BREAK SPACE". Width zero! Apply between non-space.
| U+180E    |     0 | "MONGOLIAN VOWEL SEPARATOR". Width zero!
+-----------+-------+
* The characters U+2000...U+2006, when implemented in a font, usually have the
  specific width defined for them.
** The characters U+2007...U+200A and U+202F have no exact width assigned to
   them in the standard, and implementations may deviate considerably even from
   the suggested widths.

Selected "spaces"" with fixed widths:
+-------+----------------------------------------------------------------------------------------------------------+
| width |                                             codepoints                                                   |
+-------+----------------------------------------------------------------------------------------------------------+
|  1000 | "EM QUAD" (U+2001); "EM SPACE (mutton)" (U+2003).                                                        |
|   500 | "EN QUAD" (U+2000); "EN SPACE (nut)" (U+2002).                                                           |
|   333 | "THREE-PER-EM SPACE (thick space)" (U+2004).                                                             |
|   260 | "SPACE" (U+0020); "NO-BREAK SPACE" (U+00A0).                                                             |
|   250 | "FOUR-PER-EM SPACE (mid space)" (U+2005).                                                                |
|   222 | "MEDIUM MATHEMATICAL SPACE" (U+205F).                                                                    |
|   167 | "SIX-PER-EM SPACE" (U+2006).                                                                             |
|   100 | "HAIR SPACE" (U+200A).                                                                                   |
|     0 | "ZERO WIDTH SPACE" (U+200B); "ZERO WIDTH NO-BREAK SPACE" (U+FEFF); "MONGOLIAN VOWEL SEPARATOR" (U+180E). |
+-------+----------------------------------------------------------------------------------------------------------+

Zero-Width Space (U+200B):
    Indicates a potential word break in text, particularly helpful in languages
    that don't typically use spaces between words. Allows for proper line
    wrapping of long words or URLs without visible spacing.

Zero-Width Non-Joiner (U+200C):
    Used in writing systems with ligatures (where characters combine visually)
    to prevent them from joining. For example, in Arabic, it can prevent
    letters from forming ligatures and ensure they appear in their final and
    initial forms respectively.

Zero-Width Joiner (U+200D):
    Conversely to the non-joiner, it encourages characters to be displayed in
    their connected forms, even if they wouldn't naturally join.
    Can be used to create certain emojis by combining multiple characters.

Zero-Width No-Break Space (U+FEFF):
    While originally intended to prevent line breaks, its modern use is
    primarily as a Byte Order Mark (BOM) at the beginning of Unicode text
    files.


# "BRAILLE PATTERN BLANK" '\u2800':
'\u2800'.isspace() == False
'\u2800'.isalpha() == False

# "FOUR-PER-EM SPACE" '\u2005':
'\u2005'.isspace() == True
'\u2005'.isalpha() == False

# "HALFWIDTH HANGUL FILLER" '\uFA00':
'\uFFA0'.isspace() == False
'\uFFA0'.isalpha() == True
'''


import argparse
from pathlib import Path
from random import seed, choice, random
from datetime import datetime


###############################################################################
# Typing special characters for the input file (see zero-width spaces below):
#
# Windows: hold "Alt"; type "+"; type in decimal on the right-side digits'
# keyboard, e.g. "9251" for "␣"; release "Alt".
#
###############################################################################


# 1. Obfuscator deterministic/full replacement of spaces only.
DICT_OBFUSCATOR_DETER_FULL_SPACES = {
    # "SPACE" -> {"HALFWIDTH HANGUL FILLER"}.
    ' \u0020' : 'ﾠ\uFFA0',
}


# 2. Obfuscator random/full replacement of spaces only.
DICT_OBFUSCATOR_RANDOM_FULL_SPACES = {
    # "SPACE" -> {"BRAILLE PATTERN BLANK"; "FOUR-PER-EM SPACE";
    #             "HALFWIDTH HANGUL FILLER"}.
    ' \u0020' : '⠀\u2800 \u2005ﾠ\uFFA0',
}


# 3. Obfuscator random/partial replacement of spaces only.
DICT_OBFUSCATOR_RANDOM_PARTIAL_SPACES = {
    # "SPACE" -> {"SPACE"; "BRAILLE PATTERN BLANK"; "FOUR-PER-EM SPACE";
    #             "HALFWIDTH HANGUL FILLER"}.
    ' \u0020' : ' \u0020⠀\u2800 \u2005ﾠ\uFFA0',
}

# 4. Obfuscator deterministic/full replacement
#    Replace "Basic Latin" (0000-007F) with "Fullwidth Form"(FF00-FFEF).
DICT_OBFUSCATOR_DETER_FULL_FWF = {
    # "SPACE" -> {"IDEOGRAPHIC SPACE"}.
    ' \u0020' : '　\u3000',
    #
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


# 5. Obfuscator deterministic/full replacement
#    (using visually best replacement choice for each original letter).
DICT_OBFUSCATOR_DETER_FULL = {
    # "SPACE" -> {"HALFWIDTH HANGUL FILLER"}.
    ' \u0020' : 'ﾠ\uFFA0',
    #
    ',\u002C' : '‚\u201A', # 'ˏ\02CF¸\u00B8'
    '-\u002D' : '‐\u2010', # '‑\u2011⁃\u2043−\u2212'
    '.\u002E' : '․\u2024',
    ':\u003A' : '։\u0589', # '∶\u2236꞉\uA789'
    ';\u003B' : ';\u037E', # '⁏\u204F'
    #
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
    'f\u0066' : 'ƒ\u0192',
    'g\u0067' : 'ɡ\u0261',
    'h\u0068' : 'Ⴙ\u10B9',
    'i\u0069' : 'і\u0456',
    'j\u006A' : 'ј\u0458',
    'k\u006B' : 'ƙ\u0199',
    'l\u006C' : 'Ꙇ\uA646',
    'm\u006D' : 'ʍ\u028D',
    'n\u006E' : 'ɴ\u0274',
    'o\u006F' : 'о\u043E',
    'p\u0070' : 'р\u0440',
    'q\u0071' : 'ԛ\u051B',
    'r\u0072' : 'ɾ\u027E',
    's\u0073' : 'ѕ\u0455',
    't\u0074' : 'ᴛ\u1D1B',
    'u\u0075' : 'υ\u03C5',
    'v\u0076' : 'ѵ\u0475',
    'w\u0077' : 'ѡ\u0461',
    'x\u0078' : 'х\u0445',
    'y\u0079' : 'ƴ\u01B4',
    'z\u007A' : 'ᴢ\u1D22',
}


# 6. Obfuscator random/full replacement.
DICT_OBFUSCATOR_RANDOM_FULL = {
    # "SPACE" -> {"BRAILLE PATTERN BLANK"; "FOUR-PER-EM SPACE";
    #             "HALFWIDTH HANGUL FILLER"}.
    ' \u0020' : '⠀\u2800 \u2005ﾠ\uFFA0',
    #
    ',\u002C' : '‚\u201A', # 'ˏ\02CF¸\u00B8'
    '-\u002D' : '‐\u2010', # '‑\u2011⁃\u2043−\u2212'
    '.\u002E' : '․\u2024',
    ':\u003A' : '։\u0589', # '∶\u2236꞉\uA789'
    ';\u003B' : ';\u037E', # '⁏\u204F',
    #
    'A\u0041' : 'Α\u0391А\u0410ꓮ\uA4EE',
    'B\u0042' : 'Β\u0392В\u0412Ⲃ\u2C82ꓐ\uA4D0',
    'C\u0043' : 'Ϲ\u03F9С\u0421ꓚ\uA4DA',
    'D\u0044' : 'ꓓ\uA4D3Ɗ\u018A',
    'E\u0045' : 'Ε\u0395Е\u0415ꓰ\uA4F0',
    'F\u0046' : 'ꓝ\uA4DDƑ\u0191',
    'G\u0047' : 'Ԍ\u050Cꓖ\uA4D6',
    'H\u0048' : 'Η\u0397Н\u041DⲎ\u2C8Eꓧ\uA4E7',
    'I\u0049' : 'Ι\u0399І\u0406Ӏ\u04C0Ⲓ\u2C92ꓲ\uA4F2',
    'J\u004A' : 'Ј\u0408ꓙ\uA4D9',
    'K\u004B' : 'Κ\u039AК\u041AⲔ\u2C94ꓗ\uA4D7',
    'L\u004C' : 'ꓡ\uA4E1Լ\u053C',
    'M\u004D' : 'Μ\u039CϺ\u03FAМ\u041Cꓟ\uA4DF',
    'N\u004E' : 'Ν\u039Dꓠ\uA4E0',
    'O\u004F' : 'Ο\u039FО\u041EՕ\u0555Ჿ\u1CBFꓳ\uA4F3',
    'P\u0050' : 'Ρ\u03A1Р\u0420ꓑ\uA4D1',
    'Q\u0051' : 'Ԛ\u051AǪ\u01EA',
    'R\u0052' : 'Ɍ\u024Cꓣ\uA4E3',
    'S\u0053' : 'Ѕ\u0405Տ\u054FᲽ\u1CBDꓢ\uA4E2Ꚃ\uA682',
    'T\u0054' : 'Τ\u03A4Т\u0422',
    'U\u0055' : 'ꓴ\uA4F4Ս\u054D',
    'V\u0056' : 'ꓦ\uA4E6Ѵ\u0474',
    'W\u0057' : 'Ԝ\u051Cꓪ\uA4EA',
    'X\u0058' : 'Χ\u03A7Х\u0425ꓫ\uA4EB',
    'Y\u0059' : 'Υ\u03A5Ү\u04AEꓬ\uA4EC',
    'Z\u005A' : 'Ζ\u0396Ⴭ\u10CDꓜ\uA4DC',
    #
    'a\u0061' : 'а\u0430ɑ\u0251',
    'b\u0062' : 'ƅ\u0185ɓ\u0253',
    'c\u0063' : 'ϲ\u03F2с\u0441',
    'd\u0064' : 'ԁ\u0501ɗ\u0257',
    'e\u0065' : 'е\u0435ȩ\u0229',
    'f\u0066' : 'ƒ\u0192ꬵ\uAB35',
    'g\u0067' : 'ɡ\u0261ɠ\u0260',
    'h\u0068' : 'Һ\u04BAႹ\u10B9',
    'i\u0069' : 'і\u0456ί\u03AF',
    'j\u006A' : 'ϳ\u03F3ј\u0458',
    'k\u006B' : 'ƙ\u0199ᶄ\u1D84',
    'l\u006C' : 'ļ\u013CꙆ\uA646',
    'm\u006D' : 'ṃ\u1E43ɱ\u0271ᶆ\u1D86',
    'n\u006E' : 'ņ\u0146ṇ\u1E47',
    'o\u006F' : 'ο\u03BFо\u043Eჿ\u10FFᴏ\u1D0F',
    'p\u0070' : 'р\u0440ƿ\u01BF',
    'q\u0071' : 'ԛ\u051Bɋ\u024B',
    'r\u0072' : 'ŗ\u0157ɾ\u027E',
    's\u0073' : 'ѕ\u0455ş\u015F',
    't\u0074' : 'ţ\u0163ț\u021B',
    'u\u0075' : 'υ\u03C5ᴜ\u1D1C',
    'v\u0076' : 'ν\u03BDѵ\u0475',
    'w\u0077' : 'ѡ\u0461ԝ\u051D',
    'x\u0078' : 'х\u0445ҳ\u04B3',
    'y\u0079' : 'γ\u03B3ү\u04AFƴ\u01B4',
    'z\u007A' : 'ᴢ\u1D22ᵶ\u1D76',
}


# 7. Obfuscator random/partial replacement.
DICT_OBFUSCATOR_RANDOM_PARTIAL = {
    # "SPACE" -> {"SPACE"; "BRAILLE PATTERN BLANK"; "FOUR-PER-EM SPACE";
    #             "HALFWIDTH HANGUL FILLER"}.
    ' \u0020' : ' \u0020⠀\u2800 \u2005ﾠ\uFFA0',
    #
    ',\u002C' : ',\u002C‚\u201A', # 'ˏ\u02CF¸\u00B8'
    '-\u002D' : '-\u002D‐\u2010', # '‑\u2011⁃\u2043−\u2212'
    '.\u002E' : '.\u002E․\u2024',
    ':\u003A' : ':\u003A։\u0589', # '∶\u2236꞉\uA789'
    ';\u003B' : ';\u003B;\u037E', # '⁏\u204F',
    #
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
    'W\u0057' : 'W\u0057Ԝ\u051C',
    'X\u0058' : 'X\u0058Χ\u03A7Х\u0425ꓫ\uA4EB',
    'Y\u0059' : 'Y\u0059Υ\u03A5Ү\u04AEꓬ\uA4EC',
    'Z\u005A' : 'Z\u005AΖ\u0396Ⴭ\u10CDꓜ\uA4DC',
    #
    'a\u0061' : 'a\u0061а\u0430ɑ\u0251',
    'b\u0062' : 'b\u0062ɓ\u0253',
    'c\u0063' : 'c\u0063ϲ\u03F2с\u0441',
    'd\u0064' : 'd\u0064ԁ\u0501',
    'e\u0065' : 'e\u0065е\u0435',
    'f\u0066' : 'f\u0066ƒ\u0192',
    'g\u0067' : 'g\u0067ɡ\u0261',
    'h\u0068' : 'h\u0068Һ\u04BAႹ\u10B9',
    'i\u0069' : 'i\u0069і\u0456',
    'j\u006A' : 'j\u006Aϳ\u03F3ј\u0458',
    'k\u006B' : 'k\u006Bƙ\u0199',
    'l\u006C' : 'l\u006CꙆ\uA646',
    'm\u006D' : 'm\u006Dᶆ\u1D86',
    'n\u006E' : 'n\u006Eη\u03B7',
    'o\u006F' : 'o\u006Fο\u03BFо\u043Eჿ\u10FFᴏ\u1D0F',
    'p\u0070' : 'p\u0070р\u0440',
    'q\u0071' : 'q\u0071ԛ\u051B',
    'r\u0072' : 'r\u0072ɾ\u027E',
    's\u0073' : 's\u0073ѕ\u0455',
    't\u0074' : 't\u0074ţ\u0163',
    'u\u0075' : 'u\u0075υ\u03C5',
    'v\u0076' : 'v\u0076ν\u03BDѵ\u0475',
    'w\u0077' : 'w\u0077ԝ\u051D',
    'x\u0078' : 'x\u0078х\u0445',
    'y\u0079' : 'y\u0079ƴ\u01B4',
    'z\u007A' : 'z\u007Aᴢ\u1D22',
}

# 8. Obfuscator random/partial replacement using all candidate symbols.
DICT_OBFUSCATOR_RANDOM_ALL = {
    # Optionally insert these zero-width spaces between letters of a word:
    '␣\u2423' : '\u200C\u200C', # "OPEN BOX" (9251) -> "ZERO WIDTH NON-JOINER"
    #
    # "SPACE" -> {"SPACE"; "BRAILLE PATTERN BLANK"; "FOUR-PER-EM SPACE";
    #             "HALFWIDTH HANGUL FILLER"; "NO-BREAK SPACE"; "HANGUL FILLER"}.
    ' \u0020' : ' \u0020⠀\u2800 \u2005ﾠ\uFFA0\u00A0\u00A0ㅤ\u3164',
    #
    ',\u002C' : ',\u002C‚\u201Aˏ\u02CF¸\u00B8',
    '-\u002D' : '-\u002D‐\u2010‑\u2011⁃\u2043−\u2212',
    '.\u002E' : '.\u002E․\u2024',
    ':\u003A' : ':\u003A։\u0589∶\u2236꞉\uA789',
    ';\u003B' : ';\u003B;\u037E⁏\u204F',
    #
    'A\u0041' : 'A\u0041Α\u0391А\u0410ꓮ\uA4EEÀ\u00C0Á\u00C1Â\u00C2Ã\u00C3Ä\u00C4Å\u00C5Ā\u0100Ă\u0102Ą\u0104Ǎ\u01CDǞ\u01DEǠ\u01E0Ǻ\u01FAȀ\u0200Ȃ\u0202Ȧ\u0226Ⱥ\u023AΆ\u0386ά\u03ACӐ\u04D0Ӓ\u04D2Ḁ\u1E00Ạ\u1EA0Ả\u1EA2Ấ\u1EA4Ầ\u1EA6Ẩ\u1EA8Ẫ\u1EAAẬ\u1EACẮ\u1EAEẰ\u1EB0Ẳ\u1EB2Ẵ\u1EB4Ặ\u1EB6Ἀ\u1F08Ἁ\u1F09Ἂ\u1F0AἋ\u1F0BἌ\u1F0CἍ\u1F0DἎ\u1F0EἏ\u1F0FᾸ\u1FB8Ᾱ\u1FB9Ὰ\u1FBAΆ\u1FBBᾼ\u1FBCⱭ\u2C6DꞺ\uA7BA',
    'B\u0042' : 'B\u0042Β\u0392В\u0412Ⲃ\u2C82ꓐ\uA4D0Ɓ\u0181Ƀ\u0243Ḃ\u1E02Ḅ\u1E04Ḇ\u1E06ẞ\u1E9EꞖ\uA796Ꞵ\uA7B4',
    'C\u0043' : 'C\u0043Ϲ\u03F9С\u0421ꓚ\uA4DAÇ\u00C7Ć\u0106Ĉ\u0108Ċ\u010AČ\u010CƇ\u0187Ȼ\u023BҪ\u04AAḈ\u1E08Ⲥ\u2CA4',
    'D\u0044' : 'D\u0044ꓓ\uA4D3Ð\u00D0Ď\u010EĐ\u0110Ɖ\u0189Ɗ\u018AḊ\u1E0AḌ\u1E0CḎ\u1E0EḐ\u1E10Ḓ\u1E12',
    'E\u0045' : 'E\u0045Ε\u0395Е\u0415ꓰ\uA4F0È\u00C8É\u00C9Ê\u00CAË\u00CBĒ\u0112Ĕ\u0114Ė\u0116Ę\u0118Ě\u011AƐ\u0190Ʃ\u01A9Ȅ\u0204Ȇ\u0206Ȩ\u0228Ɇ\u0246Έ\u0388Σ\u03A3Ӗ\u04D6Ԑ\u0510Ḕ\u1E14Ḗ\u1E16Ḙ\u1E18Ḛ\u1E1AḜ\u1E1CẸ\u1EB8Ẻ\u1EBAẼ\u1EBCẾ\u1EBEỀ\u1EC0Ể\u1EC2Ễ\u1EC4Ệ\u1EC6Ἐ\u1F18Ἑ\u1F19Ἒ\u1F1AἛ\u1F1BἜ\u1F1CἝ\u1F1DῈ\u1FC8Έ\u1FC9Ⲉ\u2C88Ꜫ\uA72Aꜫ\uA72B',
    'F\u0046' : 'F\u0046ꓝ\uA4DDƑ\u0191Ḟ\u1E1E',
    'G\u0047' : 'G\u0047Ԍ\u050Cꓖ\uA4D6Ĝ\u011CĞ\u011EĠ\u0120Ģ\u0122Ɠ\u0193Ǥ\u01E4Ǧ\u01E6Ǵ\u01F4Ḡ\u1E20',
    'H\u0048' : 'H\u0048Η\u0397Н\u041DⲎ\u2C8Eꓧ\uA4E7Ĥ\u0124Ħ\u0126Ȟ\u021EΉ\u0389Ң\u04A2Ҥ\u04A4Ӈ\u04C7Ӊ\u04C9Ԋ\u050AḢ\u1E22Ḥ\u1E24Ḧ\u1E26Ḩ\u1E28Ḫ\u1E2AἨ\u1F28Ἡ\u1F29Ἢ\u1F2AἫ\u1F2BἬ\u1F2CἭ\u1F2DἮ\u1F2EἯ\u1F2FῊ\u1FCAΉ\u1FCBῌ\u1FCCⱧ\u2C67Ꜧ\uA726Ɦ\uA7AA',
    'I\u0049' : 'I\u0049Ι\u0399І\u0406Ӏ\u04C0Ⲓ\u2C92ꓲ\uA4F2Ì\u00CCÍ\u00CDÎ\u00CEÏ\u00CFĨ\u0128Ī\u012AĬ\u012CĮ\u012Eİ\u0130Ɨ\u0197Ǐ\u01CFȈ\u0208Ȋ\u020AΊ\u038AΪ\u03AAЇ\u0407ӏ\u04CFḬ\u1E2CḮ\u1E2EỈ\u1EC8Ị\u1ECAἸ\u1F38Ἱ\u1F39Ἲ\u1F3AἻ\u1F3BἼ\u1F3CἽ\u1F3DἾ\u1F3EἿ\u1F3FῘ\u1FD8Ῑ\u1FD9Ὶ\u1FDAΊ\u1FDBꞼ\uA7BC',
    'J\u004A' : 'J\u004AЈ\u0408ꓙ\uA4D9Ĵ\u0134Ɉ\u0248Ϳ\u037F',
    'K\u004B' : 'K\u004BΚ\u039AК\u041AⲔ\u2C94ꓗ\uA4D7Ķ\u0136Ƙ\u0198Ǩ\u01E8Ϗ\u03CFҚ\u049AҜ\u049CҞ\u049EҠ\u04A0Ӄ\u04C3Ԟ\u051EḰ\u1E30Ḳ\u1E32Ḵ\u1E34Ⱪ\u2C69Ꝁ\uA740Ꝃ\uA742Ꝅ\uA744Ꞣ\uA7A2',
    'L\u004C' : 'L\u004Cꓡ\uA4E1Ĺ\u0139Ļ\u013BĽ\u013DĿ\u013FŁ\u0141Ƚ\u023DԼ\u053CḶ\u1E36Ḹ\u1E38Ḻ\u1E3AḼ\u1E3CⱠ\u2C60Ɫ\u2C62Ⳑ\u2CD0Ꝇ\uA746Ꝉ\uA748Ɬ\uA7Ad',
    'M\u004D' : 'M\u004DΜ\u039CϺ\u03FAМ\u041Cꓟ\uA4DFӍ\u04CDḾ\u1E3EṀ\u1E40Ṃ\u1E42Ɱ\u2C6EⲘ\u2C98',
    'N\u004E' : 'N\u004EΝ\u039Dꓠ\uA4E0Ñ\u00D1Ń\u0143Ņ\u0145Ň\u0147Ŋ\u014AƝ\u019DǸ\u01F8Ṅ\u1E44Ṇ\u1E46Ṉ\u1E48Ṋ\u1E4AⲚ\u2C9AꞐ\uA790Ꞥ\uA7A4',
    'O\u004F' : 'O\u004FΟ\u039FО\u041EՕ\u0555Ჿ\u1CBFꓳ\uA4F3Ò\u00D2Ó\u00D3Ô\u00D4Õ\u00D5Ö\u00D6Ø\u00D8Ō\u014CŎ\u014EŐ\u0150Ơ\u01A0Ǒ\u01D1Ȍ\u020CȎ\u020EȪ\u022AȬ\u022CȮ\u022EȰ\u0230Ό\u038CӦ\u04E6Ṍ\u1E4CṎ\u1E4EṐ\u1E50Ṓ\u1E52Ọ\u1ECCỎ\u1ECEỐ\u1ED0Ồ\u1ED2Ổ\u1ED4Ỗ\u1ED6Ộ\u1ED8Ớ\u1EDAỜ\u1EDCỞ\u1EDEỠ\u1EE0Ợ\u1EE2Ὀ\u1F48Ὁ\u1F49Ὂ\u1F4AὋ\u1F4BὌ\u1F4CὍ\u1F4DῸ\u1FF8Ό\u1FF9Ⲟ\u2C9EꙨ\uA668Ꙫ\uA66AꝌ\uA74CꟀ\uA7C0',
    'P\u0050' : 'P\u0050Ρ\u03A1Р\u0420ꓑ\uA4D1Ƥ\u01A4Ƿ\u01F7Ҏ\u048EṔ\u1E54Ṗ\u1E56Ῥ\u1FECⱣ\u2C63Ⲣ\u2CA2Ꝑ\uA750Ꝓ\uA752Ꝥ\uA764Ꝧ\uA766',
    'Q\u0051' : 'Q\u0051Ԛ\u051AǪ\u01EAǬ\u01ECɊ\u024AႭ\u10ADꝖ\uA756Ꝙ\uA758',
    'R\u0052' : 'R\u0052Ɍ\u024Cꓣ\uA4E3Ŕ\u0154Ŗ\u0156Ř\u0158Ʀ\u01A6Ȑ\u0210Ȓ\u0212Ṙ\u1E58Ṛ\u1E5AṜ\u1E5CṞ\u1E5EⱤ\u2C64Ꞧ\uA7A6',
    'S\u0053' : 'S\u0053Ѕ\u0405Տ\u054FᲽ\u1CBDꓢ\uA4E2Ꚃ\uA682Ś\u015AŜ\u015CŞ\u015EŠ\u0160Ș\u0218Ⴝ\u10BDṠ\u1E60Ṣ\u1E62Ṥ\u1E64Ṧ\u1E66Ṩ\u1E68Ȿ\u2C7E',
    'T\u0054' : 'T\u0054Τ\u03A4Т\u0422Ţ\u0162Ť\u0164Ŧ\u0166Ƭ\u01ACƮ\u01AEȚ\u021AȾ\u023EͲ\u0372ͳ\u0373Ҭ\u04ACṪ\u1E6AṬ\u1E6CṮ\u1E6EṰ\u1E70Ⲧ\u2CA6Ꚍ\uA68CꚐ\uA690',
    'U\u0055' : 'U\u0055ꓴ\uA4F4Ù\u00D9Ú\u00DAÛ\u00DBÜ\u00DCŨ\u0168Ū\u016AŬ\u016CŮ\u016EŰ\u0170Ų\u0172Ư\u01AFƲ\u01B2Ǔ\u01D3Ǖ\u01D5Ǘ\u01D7Ǚ\u01D9Ǜ\u01DBȔ\u0214Ȗ\u0216Ʉ\u0244Մ\u0544Ս\u054DႮ\u10AEṲ\u1E72Ṵ\u1E74Ṷ\u1E76Ṹ\u1E78Ṻ\u1E7AỤ\u1EE4Ủ\u1EE6Ứ\u1EE8Ừ\u1EEAỬ\u1EECỮ\u1EEEỰ\u1EF0Ꞹ\uA7B8Ꞿ\uA7BE',
    'V\u0056' : 'V\u0056ꓦ\uA4E6Ѵ\u0474Ѷ\u0476Ṽ\u1E7CṾ\u1E7EꝞ\uA75E',
    'W\u0057' : 'W\u0057Ԝ\u051Cꓪ\uA4EAŴ\u0174Ẁ\u1E80Ẃ\u1E82Ẅ\u1E84Ẇ\u1E86Ẉ\u1E88Ⱳ\u2C72Ⲱ\u2CB0Ꙍ\uA64CꝠ\uA760Ꞷ\uA7B6',
    'X\u0058' : 'X\u0058Χ\u03A7Х\u0425ꓫ\uA4EBҲ\u04B2Ӽ\u04FCӾ\u04FEẊ\u1E8AẌ\u1E8CⲬ\u2CACꞳ\uA7B3',
    'Y\u0059' : 'Y\u0059Υ\u03A5Ү\u04AEꓬ\uA4EC¥\u00A5Ý\u00DDŶ\u0176Ÿ\u0178Ƴ\u01B3Ȳ\u0232Ɏ\u024EΎ\u038EΫ\u03ABϒ\u03D2ϓ\u03D3ϔ\u03D4Ұ\u04B0Ӯ\u04EEӰ\u04F0Ӳ\u04F2Ⴤ\u10C4Ẏ\u1E8EỲ\u1EF2Ỵ\u1EF4Ỷ\u1EF6Ỹ\u1EF8Ỿ\u1EFEὙ\u1F59Ὓ\u1F5BὝ\u1F5DὟ\u1F5FῨ\u1FE8Ῡ\u1FE9Ὺ\u1FEAΎ\u1FEBⲨ\u2CA8',
    'Z\u005A' : 'Z\u005AΖ\u0396Ⴭ\u10CDꓜ\uA4DCŹ\u0179Ż\u017BŽ\u017DƵ\u01B5Ȥ\u0224Ẑ\u1E90Ẓ\u1E92Ẕ\u1E94Ⱬ\u2C6BⱿ\u2C7FⲌ\u2C8CꙀ\uA640Ꙃ\uA642',
    #
    'a\u0061' : 'a\u0061α\u03B1а\u0430à\u00E0á\u00E1â\u00E2ã\u00E3ä\u00E4å\u00E5ā\u0101ă\u0103ą\u0105ǎ\u01CEǟ\u01DFǡ\u01E1ǻ\u01FBȁ\u0201ȃ\u0203ȧ\u0227ɑ\u0251ӑ\u04D1ӓ\u04D3ᴀ\u1D00ᶏ\u1D8Fᶐ\u1D90ḁ\u1E01ẚ\u1E9Aạ\u1EA1ả\u1EA3ấ\u1EA5ầ\u1EA7ẩ\u1EA9ẫ\u1EABậ\u1EADắ\u1EAFằ\u1EB1ẳ\u1EB3ẵ\u1EB5ặ\u1EB7ἀ\u1F00ἁ\u1F01ἂ\u1F02ἃ\u1F03ἄ\u1F04ἅ\u1F05ἆ\u1F06ἇ\u1F07ὰ\u1F70ά\u1F71ᾰ\u1FB0ᾱ\u1FB1ᾲ\u1FB2ᾳ\u1FB3ᾴ\u1FB4ᾶ\u1FB6ᾷ\u1FB7ⱥ\u2C65ꞻ\uA7BB',
    'b\u0062' : 'b\u0062ƅ\u0185ɓ\u0253ß\u00DFƀ\u0180ƃ\u0183Ƅ\u0184ʙ\u0299β\u03B2ᴃ\u1D03ᵬ\u1D6Cᶀ\u1D80ḃ\u1E03ḅ\u1E05ḇ\u1E07ⲃ\u2C83ꞗ\uA797ꞵ\uA7B5',
    'c\u0063' : 'c\u0063ϲ\u03F2с\u0441¢\u00A2ç\u00E7ć\u0107ĉ\u0109ċ\u010Bč\u010Dƈ\u0188ȼ\u023Cҫ\u04ABᴄ\u1D04ḉ\u1E09ⲥ\u2CA5',
    'd\u0064' : 'd\u0064ԁ\u0501ď\u010Fđ\u0111ƌ\u018Cɗ\u0257ᴅ\u1D05ᴆ\u1D06ᵭ\u1D6Dᶁ\u1D81ᶂ\u1D82ḋ\u1E0Bḍ\u1E0Dḏ\u1E0Fḑ\u1E11ḓ\u1E13',
    'e\u0065' : 'e\u0065е\u0435è\u00E8é\u00E9ê\u00EAë\u00EBē\u0113ĕ\u0115ė\u0117ę\u0119ě\u011Bȅ\u0205ȇ\u0207ȩ\u0229ɇ\u0247ɛ\u025Bέ\u03ADε\u03B5ϵ\u03F5ѐ\u0450ё\u0451є\u0454ҽ\u04BDӗ\u04D7ԑ\u0511ᴇ\u1D07ᶒ\u1D92ḕ\u1E15ḗ\u1E17ḙ\u1E19ḛ\u1E1Bḝ\u1E1Dẹ\u1EB9ẻ\u1EBBẽ\u1EBDế\u1EBFề\u1EC1ể\u1EC3ễ\u1EC5ệ\u1EC7ἐ\u1F10ἑ\u1F11ἒ\u1F12ἓ\u1F13ἔ\u1F14ἕ\u1F15ὲ\u1F72έ\u1F73ⱸ\u2C78ⲉ\u2C89ꬲ\uAB32',
    'f\u0066' : 'f\u0066ꬵ\uAB35ƒ\u0192ʄ\u0284ᵮ\u1D6Eḟ\u1E1Fẛ\u1E9Bẜ\u1E9Cẝ\u1E9Dꜰ\uA730',
    'g\u0067' : 'g\u0067ɡ\u0261ĝ\u011Dğ\u011Fġ\u0121ģ\u0123ǥ\u01E5ǧ\u01E7ǵ\u01F5ɠ\u0260ɢ\u0262ʛ\u029Bԍ\u050Dᶃ\u1D83ḡ\u1E21ꬶ\uAB36',
    'h\u0068' : 'h\u0068Һ\u04BAႹ\u10B9ĥ\u0125ħ\u0127ȟ\u021Fɦ\u0266ɧ\u0267ʜ\u029Cђ\u0452ћ\u045Bң\u04A3ҥ\u04A5һ\u04BBӈ\u04C8ӊ\u04CAԦ\u0526ḣ\u1E23ḥ\u1E25ḧ\u1E27ḩ\u1E29ḫ\u1E2Bẖ\u1E96ⱨ\u2C68ⲏ\u2C8Fꚕ\uA695ꜧ\uA727ꞕ\uA795',
    'i\u0069' : 'i\u0069і\u0456¡\u00A1ì\u00ECí\u00EDî\u00EEï\u00EFĩ\u0129ī\u012Bĭ\u012Dį\u012Fı\u0131ǐ\u01D0ȉ\u0209ȋ\u020Bɨ\u0268ɩ\u0269ɪ\u026Aΐ\u0390ί\u03AFι\u03B9ϊ\u03CAї\u0457ᶖ\u1D96ḭ\u1E2Dḯ\u1E2Fỉ\u1EC9ị\u1ECBἰ\u1F30ἱ\u1F31ἲ\u1F32ἳ\u1F33ἴ\u1F34ἵ\u1F35ἶ\u1F36ἷ\u1F37ὶ\u1F76ί\u1F77ῐ\u1FD0ῑ\u1FD1ῒ\u1FD2ΐ\u1FD3ῖ\u1FD6ῗ\u1FD7ꞽ\uA7BD',
    'j\u006A' : 'j\u006Aϳ\u03F3ј\u0458ĵ\u0135ǰ\u01F0ȷ\u0237ɉ\u0249ɟ\u025Fʝ\u029Dᴊ\u1D0A',
    'k\u006B' : 'k\u006Bκ\u03BAк\u043Aⲕ\u2C95ķ\u0137ĸ\u0138ƙ\u0199ǩ\u01E9ќ\u045Cқ\u049Bҝ\u049Dҟ\u049Fҡ\u04A1ӄ\u04C4ԟ\u051Fᴋ\u1D0Bᶄ\u1D84ḱ\u1E31ḳ\u1E33ḵ\u1E35ⱪ\u2C6Aꝁ\uA741ꝃ\uA743ꝅ\uA745ꞣ\uA7A3',
    'l\u006C' : 'l\u006CꙆ\uA646ĺ\u013Aļ\u013Cľ\u013Eŀ\u0140ȴ\u0234ɭ\u026Dʟ\u029Fᴌ\u1D0Cᶅ\u1D85ḷ\u1E37ḹ\u1E39ḻ\u1E3Bḽ\u1E3Dⳑ\u2CD1',
    'm\u006D' : 'm\u006Dʍ\u028Dм\u043Cɱ\u0271ϻ\u03FBӎ\u04CEᴍ\u1D0Dᵯ\u1D6Fᶆ\u1D86ḿ\u1E3Fṁ\u1E41ṃ\u1E43ⲙ\u2C99ꬺ\uAB3A',
    'n\u006E' : 'n\u006Eɴ\u0274ñ\u00F1ń\u0144ņ\u0146ň\u0148ŉ\u0149ŋ\u014Bǹ\u01F9ȵ\u0235ɲ\u0272ɳ\u0273ή\u03AEη\u03B7ᵰ\u1D70ᶇ\u1D87ṅ\u1E45ṇ\u1E47ṉ\u1E49ṋ\u1E4Bἠ\u1F20ἡ\u1F21ἢ\u1F22ἣ\u1F23ἤ\u1F24ἥ\u1F25ἦ\u1F26ἧ\u1F27ὴ\u1F74ή\u1F75ῂ\u1FC2ῃ\u1FC3ῄ\u1FC4ῆ\u1FC6ῇ\u1FC7ⲛ\u2C9Bꞑ\uA791ꞥ\uA7A5ꬻ\uAB3B',
    'o\u006F' : 'o\u006Fο\u03BFо\u043Eჿ\u10FFò\u00F2ó\u00F3ô\u00F4õ\u00F5ö\u00F6ø\u00F8ō\u014Dŏ\u014Fő\u0151ơ\u01A1ǒ\u01D2ȍ\u020Dȏ\u020Fȫ\u022Bȭ\u022Dȯ\u022Fȱ\u0231ό\u03CCӧ\u04E7ᴏ\u1D0Fṍ\u1E4Dṏ\u1E4Fṑ\u1E51ṓ\u1E53ọ\u1ECDỏ\u1ECFố\u1ED1ồ\u1ED3ổ\u1ED5ỗ\u1ED7ộ\u1ED9ớ\u1EDBờ\u1EDDở\u1EDFỡ\u1EE1ợ\u1EE3ὀ\u1F40ὁ\u1F41ὂ\u1F42ὃ\u1F43ὄ\u1F44ὅ\u1F45ὸ\u1F78ό\u1F79ⱺ\u2C7Aⲟ\u2C9Fꙩ\uA669ꙫ\uA66Bꝍ\uA74Dꟁ\uA7C1ꬽ\uAB3D',
    'p\u0070' : 'p\u0070р\u0440þ\u00FEƥ\u01A5ƿ\u01BFҏ\u048Fᴘ\u1D18ᴩ\u1D29ᵱ\u1D71ᵽ\u1D7Dᶈ\u1D88ṕ\u1E55ṗ\u1E57ⲣ\u2CA3ꝑ\uA751ꝓ\uA753ꝥ\uA765ꝧ\uA767',
    'q\u0071' : 'q\u0071ԛ\u051Bɋ\u024Bꝗ\uA757ꝙ\uA759',
    'r\u0072' : 'r\u0072ґ\u0491ɼ\u027Cɾ\u027Eŕ\u0155ŗ\u0157ř\u0159ȑ\u0211ȓ\u0213ɍ\u024Dʀ\u0280ᵲ\u1D72ᶉ\u1D89ṙ\u1E59ṛ\u1E5Bṝ\u1E5Dṟ\u1E5Fꞧ\uA7A7ꭆ\uAB46ꭇ\uAB47ꭈ\uAB48',
    's\u0073' : 's\u0073ѕ\u0455ś\u015Bŝ\u015Dş\u015Fš\u0161ș\u0219ȿ\u023Fʂ\u0282ᵴ\u1D74ᶊ\u1D8Aṡ\u1E61ṣ\u1E63ṥ\u1E65ṧ\u1E67ṩ\u1E69ꜱ\uA731',
    't\u0074' : 't\u0074ʈ\u0288ţ\u0163ť\u0165ŧ\u0167ƫ\u01ABƭ\u01ADț\u021Bȶ\u0236ᴛ\u1D1Bᵵ\u1D75ṫ\u1E6Bṭ\u1E6Dṯ\u1E6Fṱ\u1E71ẗ\u1E97ⱡ\u2C61ⱦ\u2C66ⲧ\u2CA7ꚍ\uA68Dꚑ\uA691',
    'u\u0075' : 'u\u0075υ\u03C5ù\u00F9ú\u00FAû\u00FBü\u00FCũ\u0169ū\u016Bŭ\u016Dů\u016Fű\u0171ų\u0173ư\u01B0ǔ\u01D4ǖ\u01D6ǘ\u01D8ǚ\u01DAǜ\u01DCȕ\u0215ȗ\u0217ύ\u03CDʋ\u028Bᴜ\u1D1Cᵾ\u1D7Eᶙ\u1D99ṳ\u1E73ṵ\u1E75ṷ\u1E77ṹ\u1E79ṻ\u1E7Bụ\u1EE5ủ\u1EE7ứ\u1EE9ừ\u1EEBử\u1EEDữ\u1EEFự\u1EF1ὐ\u1F50ὑ\u1F51ὒ\u1F52ὓ\u1F53ὔ\u1F54ὕ\u1F55ὖ\u1F56ὗ\u1F57ὺ\u1F7Aύ\u1F7Bῠ\u1FE0ῡ\u1FE1ῢ\u1FE2ΰ\u1FE3ῦ\u1FE6ῧ\u1FE7ꞹ\uA7B9ꞿ\uA7BFꭒ\uAB52',
    'v\u0076' : 'v\u0076ν\u03BDѵ\u0475ѷ\u0477ᴠ\u1D20ᶌ\u1D8Cṽ\u1E7Dṿ\u1E7Fⱱ\u2C71ⱴ\u2C74ꝟ\uA75F',
    'w\u0077' : 'w\u0077ѡ\u0461ԝ\u051Dŵ\u0175ɯ\u026Fω\u03C9ώ\u03CEѿ\u047Fᴡ\u1D21ẁ\u1E81ẃ\u1E83ẅ\u1E85ẇ\u1E87ẉ\u1E89ẘ\u1E98ὠ\u1F60ὡ\u1F61ὢ\u1F62ὣ\u1F63ὤ\u1F64ὥ\u1F65ὦ\u1F66ὧ\u1F67ὼ\u1F7Cώ\u1F7Dῲ\u1FF2ῳ\u1FF3ῴ\u1FF4ῶ\u1FF6ῷ\u1FF7ⱳ\u2C73ⲱ\u2CB1ꙍ\uA64Dꝡ\uA761ꞷ\uA7B7',
    'x\u0078' : 'x\u0078х\u0445χ\u03C7ҳ\u04B3ӽ\u04FDӿ\u04FFᶍ\u1D8Dẋ\u1E8Bẍ\u1E8Dⲭ\u2CADꭓ\uAB53ꭔ\uAB54ꭕ\uAB55',
    'y\u0079' : 'y\u0079γ\u03B3ү\u04AFý\u00FDÿ\u00FFŷ\u0177ƴ\u01B4ȳ\u0233ɏ\u024Fɣ\u0263ʏ\u028Fў\u045Eұ\u04B1ӯ\u04EFӱ\u04F1ӳ\u04F3ẏ\u1E8Fẙ\u1E99ỳ\u1EF3ỵ\u1EF5ỷ\u1EF7ỹ\u1EF9ỿ\u1EFFⲩ\u2CA9',
    'z\u007A' : 'z\u007Aȥ\u0225ɀ\u0240ʐ\u0290ź\u017Aż\u017Cž\u017Eƶ\u01B6ʑ\u0291ᴢ\u1D22ᵶ\u1D76ᶎ\u1D8Eẑ\u1E91ẓ\u1E93ẕ\u1E95ⱬ\u2C6Cⲍ\u2C8Dꙁ\uA641ꙃ\uA643',
}


DICT_OBFUSCATOR_TYPES = {
    1 : "1. Deterministic full replacement of spaces only.",
    2 : "2. Random full replacement of spaces only.",
    3 : "3. Random partial replacement of spaces only.",
    4 : "4. Deterministic full replacement with paired Fullwidth Form symbols.",
    5 : "5. Deterministic full replacement with the most look-alike symbols.",
    6 : "6. Random full replacement with various very look-alike symbols.",
    7 : "7. Random partial replacement with various very look-alike symbols.",
    8 : "8. Random partial replacement with various somewhat look-alike symbols.",
}

'''
# Relative frequency in the English language (text):
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

def validate_obfuscator(dict_obfuscator) :
    for(key, value) in dict_obfuscator.items() :
        if len(key) != 2 or key[0] != key[1]:
            print ("Invalid key ", key)
        if len(value) % 2 != 0 :
            print ("Invalid value length", value)
        if len(value) != len(set(value)) * 2 :
            print("Duplicate symbols in value ", value)
        for i in range(0,len(value),2) :
            if value[i] != value[i+1]:
                print ("Invalid value ", value)
                break


# Unit test for Obfuscators:
if False :
    validate_obfuscator(dict_obfuscator = DICT_OBFUSCATOR_DETER_FULL_SPACES)
    validate_obfuscator(dict_obfuscator = DICT_OBFUSCATOR_RANDOM_FULL_SPACES)
    validate_obfuscator(dict_obfuscator = DICT_OBFUSCATOR_RANDOM_PARTIAL_SPACES)
    validate_obfuscator(dict_obfuscator = DICT_OBFUSCATOR_DETER_FULL_FWF)
    validate_obfuscator(dict_obfuscator = DICT_OBFUSCATOR_DETER_FULL)
    validate_obfuscator(dict_obfuscator = DICT_OBFUSCATOR_RANDOM_FULL)
    validate_obfuscator(dict_obfuscator = DICT_OBFUSCATOR_RANDOM_PARTIAL)
    validate_obfuscator(dict_obfuscator = DICT_OBFUSCATOR_RANDOM_ALL)

    # seed(a = 12345)
    seed(datetime.now().timestamp())
    # str_in = 'ôcaoA'
    str_in = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz ,-.:;'
    str_out = ''.join(tuple(map(
        lambda x : choice(DICT_OBFUSCATOR_RANDOM_ALL.get(x + x, x)), str_in)))
    print(str_in)
    print(str_out)


# Unit test for Spaces:
if False :
    # Both "split" and "strip" recognize all "spaces" with positive width:
    print(len('\u2001'.strip())) # 0
    print(len('\u2003'.strip())) # 0
    print(len('\u2000'.strip())) # 0
    print(len('\u2002'.strip())) # 0
    print(len('\u2004'.strip())) # 0 "THREE-PER-EM SPACE (thick space)": third alternative to SPACE ('\u0020')
    print(len('\u0020'.strip())) # 0
    print(len('\u00A0'.strip())) # 0 "NO-BREAK SPACE": first (the best) alternative to SPACE ('\u0020')
    print(len('\u2005'.strip())) # 0 "FOUR-PER-EM SPACE (mid space)": second alternative to SPACE ('\u0020')
    print(len('\u205F'.strip())) # 0
    print(len('\u2006'.strip())) # 0
    print(len('\u200A'.strip())) # 0
    print(len('\u200B'.strip())) # 1 ZERO WIDTH SPACE ! https://unicode-explorer.com/c/200B
    print(len('\uFEFF'.strip())) # 1 ZERO WIDTH NO-BREAK SPACE obsolete, use WORD JOINER
    print(len('\u2060'.strip())) # 1 WORD JOINER: use instead of obsolete ZERO WIDTH NO-BREAK SPACE. https://unicode-explorer.com/c/2060
    print(len('\u200C'.strip())) # 1 Zero-Width Non-Joiner
    print(len('\u200D'.strip())) # 1 Zero-Width Joiner
    print(len('\u180E'.strip())) # 1
    print(len('\u3000'.strip())) # 0
    print(len('\u2007'.strip())) # 0
    print(len('\u2008'.strip())) # 0
    print(len('\u2009'.strip())) # 0
    print(len('\u200A'.strip())) # 0
    print(len('\u1680'.strip())) # 0
    print(len('\u202F'.strip())) # 0
    print(len('\u00AD'.strip())) # 1 # soft hyphen character
    print(len('\u2423'.strip())) # 1 '␣'
    print(len('\u2800'.strip())) # 1 BRAILLE PATTERN BLANK ! obfuscating alternative to SPACE ('\u0020')
    print(len('\u3164'.strip())) # 1 HANGUL FILLER ! too wide; obfuscating alternative to SPACE ('\u0020')
    print(len('\uFFA0'.strip())) # 1 HALFWIDTH HANGUL FILLER ! a bit too narrow, but can be used.
    print(len('\u00A0'.strip())) # 0
    #
    print("W\u0020W") # Original
    print("W\u200BW") # Insert between letters as fake word boundaries
    print("W\u2060W") # Insert between last letter of word and BRAILLE PATTERN BLANK (used to replace space)
    print("W\u2800W") # BRAILLE PATTERN BLANK
    print("W\u3164W") # HANGUL FILLER
    print("W\uFFA0W") # HALFWIDTH HANGUL FILLER


def add_noise(
        str_input,
        tpl_str_noise = (
            '\uFEFF', # ZERO WIDTH NO-BREAK SPACE
            '\u180E', # MONGOLIAN VOWEL SEPARATOR (zero width)
            '\u200D', # "ZERO WIDTH JOINER"
            ),
        set_non_alpha = {
            '\u2800', # "BRAILLE PATTERN BLANK" "isalpha" is False
            '\uFFA0', # "HALFWIDTH HANGUL FILLER" "isalpha" is True
            '\u3164', # "HANGUL FILLER" "isalpha" is True
            },
        str_gap = '\u200A', # "HAIR SPACE" width 100 vs "SPACE" width 260
        noise_insertion_percent = 0) :

    if len(tpl_str_noise) > 0 and noise_insertion_percent > 0 :
        flt_noise_insertion_prob = noise_insertion_percent / 100.
        str_output = ''.join('%s%s' % (
            str_input[i], choice(tpl_str_noise)
            if (((str_input[i].isalpha() and str_input[i] not in set_non_alpha)
                 or str_input[i] == str_gap) and
                (i + 1) < len(str_input) and
                (str_input[i+1].isalpha() and str_input[i+1] not in set_non_alpha) and
                random() <= flt_noise_insertion_prob) else '')
            for i in range(len(str_input)))
    else :
        str_output = str_input
    return str_output


def remove_noise(
        str_input,
        tpl_str_noise = (
            '\uFEFF', # ZERO WIDTH NO-BREAK SPACE
            '\u180E', # MONGOLIAN VOWEL SEPARATOR (zero width)
            '\u200D', # "ZERO WIDTH JOINER"
            ),
        ) :
    str_output = str_input
    if len(tpl_str_noise) > 0 :
        set_str_noise = set(tpl_str_noise)
        str_output = ''.join(str_output[i] if str_output[i] not in set_str_noise
                             else '' for i in range(len(str_output)))
    return str_output


def add_gaps(
        str_input,
        tpl_str_alt_spaces = (
            '\u2800\u200A\u200A', # "BRAILLE PATTERN BLANK" + "HAIR SPACE" (100) + "HAIR SPACE" (100)
            '\u200A\u2800\u200A', # "HAIR SPACE" (100) + "BRAILLE PATTERN BLANK" + "HAIR SPACE" (100)
            '\u200A\u200A\u2800', # "HAIR SPACE" (100) + "HAIR SPACE" (100) + "BRAILLE PATTERN BLANK"
            '\uFFA0\u200A\u200A', # "HALFWIDTH HANGUL FILLER" + "HAIR SPACE" (100) + "HAIR SPACE" (100)
            '\u200A\uFFA0\u200A', # "HAIR SPACE" (100) + "HALFWIDTH HANGUL FILLER" + "HAIR SPACE" (100)
            '\u200A\u200A\uFFA0', # "HAIR SPACE" (100) + "HAIR SPACE" (100) + "HALFWIDTH HANGUL FILLER"
            '\u3164',             # "HANGUL FILLER" (>300) is wider than "SPACE" (260)
            ),
        str_gap = '\u200A', # "HAIR SPACE" width 100 vs "SPACE" width 260
        set_str_orig_spaces = {'\u0020',}, # "SPACE" width 260
        ) :
    str_output = ''.join('%s%s' % (
        (choice(tpl_str_alt_spaces) if (
            str_input[i] in set_str_orig_spaces)
            else str_input[i]),
        (str_gap if (not str_input[i].isspace() and
                     (i + 1) < len(str_input) and
                     not str_input[i + 1].isspace()) else ''))
        for i in range(len(str_input)))
    return str_output


def remove_gaps(
        str_input,
        tpl_str_alt_spaces = (
            '\u2800\u200A\u200A', # "BRAILLE PATTERN BLANK" + "HAIR SPACE" (100) + "HAIR SPACE" (100)
            '\u200A\u2800\u200A', # "HAIR SPACE" (100) + "BRAILLE PATTERN BLANK" + "HAIR SPACE" (100)
            '\u200A\u200A\u2800', # "HAIR SPACE" (100) + "HAIR SPACE" (100) + "BRAILLE PATTERN BLANK"
            '\uFFA0\u200A\u200A', # "HALFWIDTH HANGUL FILLER" + "HAIR SPACE" (100) + "HAIR SPACE" (100)
            '\u200A\uFFA0\u200A', # "HAIR SPACE" (100) + "HALFWIDTH HANGUL FILLER" + "HAIR SPACE" (100)
            '\u200A\u200A\uFFA0', # "HAIR SPACE" (100) + "HAIR SPACE" (100) + "HALFWIDTH HANGUL FILLER"
            '\u3164',             # "HANGUL FILLER" (>300) is wider than "SPACE" (260)
            ),
        str_gap = '\u200A', # "HAIR SPACE" width 100 vs "SPACE" width 260
        str_orig_space = '\u0020', # "SPACE" width 260
        ) :
    set_str_alt_spaces = set("".join(tpl_str_alt_spaces))
    set_str_alt_spaces.remove(str_gap)
    str_output = str_input
    str_output = ''.join([
        str_orig_space if str_output[i] in set_str_alt_spaces else str_output[i]
        for i in range(len(str_output))])
    str_output = ''.join([
        '' if str_output[i] == str_gap else str_output[i]
        for i in range(len(str_output))])
    return str_output


def obfuscate(
        dict_obfuscator, integer_random_seed,
        input_file_name, output_file_name,
        gaps_insertion_flag = 0,
        noise_insertion_percent = 0,
        verbosity_flag = 0,
        reverse_obfuscation_flag = 0) :

    if integer_random_seed is None :
        seed(datetime.now().timestamp())
    else :
        seed(a = integer_random_seed)

    with open(input_file_name, 'r', encoding='utf-8') as file:
        str_input = file.read()

    str_output = str_input
    if gaps_insertion_flag :
        # Adding/removing gaps must be done before obfuscation.
        if reverse_obfuscation_flag :
            str_output = remove_gaps(str_input = str_output,)
        else :
            str_output = add_gaps(str_input = str_output,)

    if reverse_obfuscation_flag :
            str_output = remove_noise(str_input = str_output,)
    elif noise_insertion_percent > 0 :
        # Adding noise must be done before obfuscation.
        str_output = add_noise(
            str_input = str_output,
            noise_insertion_percent = noise_insertion_percent,)

    # Obfuscation:
    str_output = ''.join(tuple(map(lambda x : choice(
        dict_obfuscator.get(x + x, x)), str_output)))

    if verbosity_flag == 1 :
        print("Input file:\n")
        print(str_input)
        print("Output file:\n")
        print(str_output)
        print()

    with open(output_file_name, "w", encoding='utf-8') as file:
        file.write(str_output)


def revert_obfuscator(dict_obfuscator) :
    dict_reverse_obfuscator = {}
    for k in dict_obfuscator.keys() :
        for hv in set(dict_obfuscator[k]):
            dict_reverse_obfuscator[hv+hv] = k
    return dict_reverse_obfuscator


def main(
         obfuscator_type_index : int,
         input_file_name : str,
         output_file_name : str,
         integer_random_seed : int = None,
         gaps_insertion_flag : int = None,
         noise_insertion_percent : int = None,
         verbosity_flag : int = None,
         reverse_obfuscation_flag : int = None,
         ) :
    gaps_insertion_flag = 0 if gaps_insertion_flag is None else gaps_insertion_flag
    noise_insertion_percent = 0 if noise_insertion_percent is None else noise_insertion_percent
    verbosity_flag = 0 if verbosity_flag is None else verbosity_flag
    reverse_obfuscation_flag = 0 if reverse_obfuscation_flag is None else reverse_obfuscation_flag
    if 1 <= obfuscator_type_index <= 8 :
        if Path(input_file_name).is_file() :
            if not Path(output_file_name).is_dir() :
                if Path(output_file_name).is_file() :
                    Path(output_file_name).unlink()
                if not Path(output_file_name).is_file() :
                    if verbosity_flag == 1 :
                        print("Obfuscator type: " +
                              DICT_OBFUSCATOR_TYPES[obfuscator_type_index])
                        print("Input file name: " + input_file_name)
                        print("Output file name: " + output_file_name)
                        print()
                    lst_dict_obfuscators = [
                        DICT_OBFUSCATOR_DETER_FULL_SPACES,
                        DICT_OBFUSCATOR_RANDOM_FULL_SPACES,
                        DICT_OBFUSCATOR_RANDOM_PARTIAL_SPACES,
                        DICT_OBFUSCATOR_DETER_FULL_FWF,
                        DICT_OBFUSCATOR_DETER_FULL,
                        DICT_OBFUSCATOR_RANDOM_FULL,
                        DICT_OBFUSCATOR_RANDOM_PARTIAL,
                        DICT_OBFUSCATOR_RANDOM_ALL,
                        ]
                    dict_obfuscator = lst_dict_obfuscators[
                        obfuscator_type_index - 1]
                    validate_obfuscator(dict_obfuscator = dict_obfuscator)
                    if reverse_obfuscation_flag != 0 :
                        dict_obfuscator = revert_obfuscator(
                            dict_obfuscator = dict_obfuscator)
                    obfuscate(
                        dict_obfuscator = dict_obfuscator,
                        integer_random_seed = integer_random_seed,
                        input_file_name = input_file_name,
                        output_file_name = output_file_name,
                        gaps_insertion_flag = gaps_insertion_flag,
                        noise_insertion_percent = noise_insertion_percent,
                        verbosity_flag = verbosity_flag,
                        reverse_obfuscation_flag = reverse_obfuscation_flag,)
                else :
                    raise FileExistsError(
                        "Output text file cannot be removed.")
            else :
                raise FileExistsError(
                    "Output text file name is the directory name.")
        else :
            raise FileNotFoundError("Input text file does not exist.")
    else :
        raise ValueError("Obfuscator type index must be between 1 and 8.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--integer_random_seed",
        help = "Optional. Default: current time. A non-negative integer seed for random choices during obfuscation.",
        type = int,
        required = False,
    )
    parser.add_argument(
        "-g",
        "--gaps_insertion_flag",
        help = "Optional. Default: 0. Insert spaces of different types, and replace orginal spaces.",
        type = int,
        required = False,
    )
    parser.add_argument(
        "-n",
        "--noise_insertion_percent",
        help = "Optional. Default: 0. Range [0; 100]. Probabilty percent for ZERO WIDTH JOINER characters to be randomly inserted between each adjacent pair of letters.",
        type = int,
        required = False,
    )
    parser.add_argument(
        "-v",
        "--verbosity_flag",
        help = "Optional. Default: 0. Output verbosity integer at 0 for no traces and 1 for generating traces.",
        type = int,
        required = False,
    )
    parser.add_argument(
        "-r",
        "--reverse_obfuscation_flag",
        help = "Optional. Default: 0. Run reverse obfuscation to recover original text file (1) or forward obfuscation (0).",
        type = int,
        required = False,
    )
    parser.add_argument(
        "-t",
        "--obfuscator_type_index",
        help = '\n'.join((
            "Mandatory. The index of the obfuscator type in range from 1 to 6:",
            DICT_OBFUSCATOR_TYPES[1],
            DICT_OBFUSCATOR_TYPES[2],
            DICT_OBFUSCATOR_TYPES[3],
            DICT_OBFUSCATOR_TYPES[4],
            DICT_OBFUSCATOR_TYPES[5],
            DICT_OBFUSCATOR_TYPES[6],
            DICT_OBFUSCATOR_TYPES[7],
            DICT_OBFUSCATOR_TYPES[8],
            "\n")),
        type = int,
        required = True,
    )
    parser.add_argument(
        "-i",
        "--input_file_name",
        help = "Mandatory. The name of the input text file.",
        type = str,
        required = True,
    )
    parser.add_argument(
        "-o",
        "--output_file_name",
        help = "Mandatory. The name of the output text file.",
        type = str,
        required = True,
    )
    args = parser.parse_args()
    main(**vars(args))
