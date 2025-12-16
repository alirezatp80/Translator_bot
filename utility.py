import re


def detect_lang(text:str):
    fa_count = 0
    en_count = 0
    
    for i in text:
        if re.search(r'[\u0600-\u06FF]',i):
            fa_count+=1
        if re.search(r'[A-Za-z]' , i):
            en_count+=1
    if fa_count>en_count:
        return 'fa'
    elif en_count>fa_count:
        return 'en'
    else:
        return 'en-fa'