# language_model_obfuscator
The program obfuscates selected "Basic Latin" characters (mostly letters) from the Unicode range [0000; 007F]. Some or all characters from the above range are replaced with similar-looking characters either randomly or deterministically. While the obfuscated text still remains human-readable, language models will fail to use it for training.
