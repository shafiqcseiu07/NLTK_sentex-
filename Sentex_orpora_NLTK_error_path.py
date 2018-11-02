import sys
import os
from django.urls import path
import nltk
print(nltk.__file__)
if sys.platform.startswith('win'):
    # Common locations on Windows:
    path += [
        str(r'C:\nltk_data'),
        os.path.join(sys.prefix, str('nltk_data')),
        os.path.join(sys.prefix, str('lib'), str('nltk_data')),
        #os.path.join(os.environ.get(str('APPDATA'), str('nltk_data')), str('nltk_data'))
       # os.path.join(os.environ.get(str('APPDATA'), str('C://nltk_data')), str('nltk_data'))
    ]
else:
    # Common locations on UNIX & OS X:
    path += [
        str('/usr/share/nltk_data'),
        str('/usr/local/share/nltk_data'),
        str('/usr/lib/nltk_data'),
        str('/usr/local/lib/nltk_data')
    ]
    from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer
    from nltk.corpus import gutenberg

    # sample text
    sample = gutenberg.raw("bible-kjv.txt")

    tok = sent_tokenize(sample)

    for x in range(5):
        print(tok[x])