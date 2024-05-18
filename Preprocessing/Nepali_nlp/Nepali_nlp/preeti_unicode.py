import re

all_rules = {"post-rules": [["्ा", ""], ["(त्र|त्त)([^उभप]+?)m", "$1m$2"], ["त्रm", "क्र"], ["त्तm", "क्त"],
                            ["([^उभप]+?)m", "m$1"], ["उm", "ऊ"], ["भm", "झ"], ["पm", "फ"], ["इ{", "ई"],
                            ["ि((.्)*[^्])", "$1ि"], ["(.[ािीुूृेैोौंःँ]*?){", "{$1"], ["((.्)*){", "{$1"], ["{", "र्"],
                            ["([ाीुूृेैोौंःँ]+?)(्(.्)*[^्])", "$2$1"], ["्([ाीुूृेैोौंःँ]+?)((.्)*[^्])", "्$2$1"],
                            ["([ंँ])([ािीुूृेैोौः]*)", "$2$1"], ["ँँ", "ँ"], ["ंं", "ं"], ["ेे", "े"], ["ैै", "ै"],
                            ["ुु", "ु"], ["ूू", "ू"], ["^ः", ":"], ["टृ", "ट्ट"], ["ेा", "ाे"], ["ैा", "ाै"],
                            ["अाे", "ओ"], ["अाै", "औ"], ["अा", "आ"], ["एे", "ऐ"], ["ाे", "ो"], ["ाै", "ौ"]],

             "char-map": {
                 "÷": "/", "v": "ख", "r": "च", "\"": "ू", "~": "ञ्", "z": "श", "ç": "ॐ", "f": "ा", "b": "द", "n": "ल",
                 "j": "व", "×": "×", "V": "ख्", "R": "च्", "ß": "द्म", "^": "६", "Û": "!", "Z": "श्", "F": "ँ",
                 "B": "द्य", "N": "ल्", "Ë": "ङ्ग", "J": "व्", "6": "ट", "2": "द्द", "¿": "रू", ">": "श्र", ":": "स्",
                 "§": "ट्ट", "&": "७", "£": "घ्", "•": "ड्ड", ".": "।", "«": "्र", "*": "८", "„": "ध्र", "w": "ध",
                 "s": "क", "g": "न", "æ": "“", "c": "अ", "o": "य", "k": "प", "W": "ध्", "Ö": "=", "S": "क्", "Ò": "¨",
                 "_": ")", "[": "ृ", "Ú": "’", "G": "न्", "ˆ": "फ्", "C": "ऋ", "O": "इ", "Î": "ङ्ख", "K": "प्",
                 "7": "ठ", "¶": "ठ्ठ", "3": "घ", "9": "ढ", "?": "रु", ";": "स", "'": "ु", "#": "३", "¢": "द्घ",
                 "/": "र", "+": "ं", "ª": "ङ", "t": "त", "p": "उ", "|": "्र", "x": "ह", "å": "द्व", "d": "म", "`": "ञ",
                 "l": "ि", "h": "ज", "T": "त्", "P": "ए", "Ý": "ट्ठ", "\\": "्", "Ù": ";", "X": "ह्", "Å": "हृ",
                 "D": "म्", "@": "२", "Í": "ङ्क", "L": "ी", "H": "ज्", "4": "द्ध", "±": "+", "0": "ण्", "<": "?",
                 "8": "ड", "¥": "र्‍", "$": "४", "¡": "ज्ञ्", ",": ",", "©": "र", "(": "९", "‘": "ॅ", "u": "ग",
                 "q": "त्र", "}": "ै", "y": "थ", "e": "भ", "a": "ब", "i": "ष्", "‰": "झ्", "U": "ग्", "Q": "त्त",
                 "]": "े", "˜": "ऽ", "Y": "थ्", "Ø": "्य", "E": "भ्", "A": "ब्", "M": "ः", "Ì": "न्न", "I": "क्ष्",
                 "5": "छ", "´": "झ", "1": "ज्ञ", "°": "ङ्ढ", "=": ".", "Æ": "”", "‹": "ङ्घ", "%": "५", "¤": "झ्",
                 "!": "१", "-": "(", "›": "द्र", ")": "०", "…": "‘", "Ü": "%"
             }}


def preeti(words):
    output = ''
    for ind in range(len(words)):
        latter = words[ind]
        try:
            output = output + all_rules['char-map'][latter]
            # print('here')
        except:
            output = output + latter
    for ind in range(len(all_rules['post-rules'])):
        output = output.replace(all_rules['post-rules'][ind][0], all_rules['post-rules'][ind][1])

    return output
