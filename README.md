# Text Obfuscator

The program obfuscates selected "Basic Latin" characters (mostly letters) from the Unicode range \[0000; 007F]. Some or all characters from the above range are replaced with look-alike characters either randomly or deterministically. While the obfuscated text still remains human-readable, language models will fail to use this obfuscated text for their productive training without reverse-obfuscation of this new text during their training set preprocessing. Thus, the copyright on the original text is more protected with this obfuscation.

