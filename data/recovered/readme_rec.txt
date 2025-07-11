Text Obfuscator

James Johnson. July 11, 2025.

Tags: #obfuscator #text obfuscator #language model #copyright #search engine

Sharing text messages online may turn them into the subject of computerized processing. Message text obfuscation may prevent such cases of unauthorized use or processing of copyright-protected material. My open-source code in Johnson (2025) supports both forward obfuscation and reverse-obfuscation. However, the strength of text obfuscation is not only in the burden to revert-obfuscate non-deterministically jumbled but still human-readable text, but also in its ability to conceal the fact of obfuscation. Text obfuscation has these two objectives: 

1. Preserve the visual appearance of the original text as much as possible, or at least preserve some acceptable degree of human-readability of the obfuscated text, which retains the same language and words’ sequences.
2. Alter the byte sequences of the original text to a degree that computerized text processing would be impossible on this obfuscated text, which consists of random and noisy non-standard sequences of bytes with various Unicode characters.

In addition to ten modes of obfuscation, which will be summarized later, Text Obfuscator (Johnson, 2025) includes the following optionally activated features:

1. Random noise is the form of zero-width Unicode characters is inserted between words’ characters. The set of zero-width Unicode characters is as follows: “ZERO WIDTH NO-BREAK SPACE”, “MONGOLIAN VOWEL SEPARATOR”, and “ZERO WIDTH JOINER”.
2. The narrow gap character “HALFWIDTH HANGUL FILLER” is inserted between letter characters. The wide gap character “HANGUL FILLER” is inserted before the “NEW LINE”s. A random mix of special characters’ triplets from the following set replaces all “SPACE”s: “BRAILLE PATTERN BLANK”, “HALFWIDTH HANGUL FILLER”, and “HAIR SPACE”.

Any of the above optional features can be applied to any of the ten obfuscation modes, which can be subdivided into these groups:

1. Modes 1, 2, and 3 replace “SPACE”s only. Mode 1 maps them to “BRAILLE PATTERN BLANK”s. Mode 2 randomly maps them by adding “FOUR-PER-EM SPACE”s as a choice. Mode 3 either randomly retains them, or replaces as in Mode 1.
2. Modes 4, 5, 6, and 7 replace not only ”SPACE”s, but also letters and punctuations from the “Basic Latin” encoding (0000 - 007F) with their look-alikes in a wider Unicode range (0080 - FFFF). Mode 4 does this mapping deterministically. Mode 5 does it randomly with at least 2 choices. Mode 6 does it randomly with an option to retain the original “Basic Latin” symbol. Mode 7 does it randomly too, but and applies it to big sets of symbol choices, many of which may have significant visual deviations from the originals. 
3. Modes 8, 9, and 10 apply mapping from the “Basic Latin” encoding (0000 - 007F) to their respective alternative encoding: “Fullwidth Form” (mode 8). “Mathematical Sans-Serif” (mode 9), and “Mathematical Monospace” (mode 10).

References:
Johnson, J., (July 4, 2025). Text Obfuscator. Python Program. GitHub Repository. https://github.com/quant-manager/language_model_obfuscator
