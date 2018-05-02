
from sys import stdin

from deepnlp import pos_tagger
import deepnlp
deepnlp.register_model('pos', 'tw')
tagger = pos_tagger.load_model(name='tw')

for text in stdin.readlines():
    tagging = tagger.predict(text.rstrip().split(" "))
    print(list(tagging))
