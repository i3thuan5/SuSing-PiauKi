
'''
為了使TAICORP裡的語料能夠提供更多的訊息以便使用者做進一步的分析，在分詞的工作完成後，還要為每一個斷出的詞標上詞類標記。閩南語的詞類劃分的文獻雖然並不多，但由於閩南語和國語一樣，同屬於漢語語系，因此目前我們採用中研院詞庫小組的詞類標記，但是僅限於46個簡化標記，以避免詞類劃分過細時產生主觀強制性的歸類。
　
由於閩南語的詞類並非完全與國語一致，在建構本語料庫的過程當中，我們發現有兩個詞類為國語所沒有，一者為Di/T，另一為CIT，分別以「*」標示之。請參見下表。

'''

詞性表 = [
    'A', '非謂形容詞', 'non-predicative adjective',
    'Caa', '對等連接詞', 'coordinate conjunction',
    'Cab', '連接詞', 'listing conjunction',
    'Cba', '連接詞', 'conjunction occurring at the end of a sentence',
    'Cbb', '關聯連接詞', 'following a subject',
    'Da', '數量副詞', 'possibly preceding a noun',
    'Dfa', '動詞前程度副詞', 'preceding VH through VL',
    'Dfb', '動詞後程度副詞', 'following adverb',
    'Di', '時態標記', 'post-verbal',
    'Dk', '句副詞', 'sentence initial',
    'D', '副詞', 'adverbial',
    'Na', '普通名詞', 'common noun',
    'Nb', '專有名稱', 'proper noun',
    'Nc', '地方詞', 'location noun',
    'Ncd', '位置詞', 'localizer',
    'Nd', '時間詞', 'time noun',
    'Neu', '數詞定詞', 'numeral determiner',
    'Nes', '特指定詞', 'specific determiner',
    'Nep', '指代定詞', 'anaphoric determiner',
    'Neqa', '數量定詞', 'classifier determiner',
    'Neqb', '後置數量定詞', 'postposed classifier determiner',
    'Nf', '量詞', 'classifier',
    'Ng', '後置詞', 'postposition',
    'Nh', '代名詞', 'pronoun',
    'I', '感嘆詞', 'interjection',
    'P', '介詞', 'preposition',
    'T', '語助詞', 'particle',
    'VA', '動作不及物動詞', 'active intransitive verb',
    'VAC', '動作使動動詞', '',
    'VB', '動作類及物動詞', 'active pseudo-transitive verb',
    'VC', '動作及物動詞', 'active transitive verb',
    'VCL', '動作接地方賓語動詞', 'transitive verb taking a locative argument',
    'VD', '雙賓動詞', 'ditransitive verb',
    'VE', '動作句賓動詞', 'active transitive verb with sentential object',
    'VF', '動作謂賓動詞', 'active transitive verb with VP object',
    'VG', '分類動詞', 'classifactory verb',
    'VH', '狀態不及物動詞', 'stative intransitive verb',
    'VHC', '狀態使動動詞', 'stative causative verb',
    'VI', '狀態類及物動詞', 'stative pseudo-transitive verb',
    'VJ', '狀態及物動詞', 'stative transitive verb',
    'VK', '狀態句賓動詞', 'stative transitive verb with sentential object',
    'VL', '狀態謂賓動詞', 'stative transitive verb with VP object',
    'V_2', '有', '',
    'DE', '的', '*special tag for the word "的"',
    'SHI', '是', 'special tag for the word "是"',
    'FW', '外文標記', 'foreign words',
    '*Di/T', '*le01', '*marker following pseudo-transitive active verb',
    '*CIT', '*得2', '*special tag for the word "得2"',
    '*Comp', '*補語連詞', '*complementizer',
]

'''
Di/T 是「le01」之詞類標記。由於 le01都出現於動詞之後，並常常出現在語句之末尾，因此同時具有時態標記以及語尾助詞的特徵，因此以Di/T標記之。
例如： 你 坐 le01!
                         去 共 西瓜 切切 le01!
CIT是「得2」的詞類標記。「得2」表示能夠的意思，其不但能加在動詞之後，並能與主要動詞分開遠遠出現在句末的位置，由於國語並無此類詞，因此另外以CIT標示。
             例如：會1 提 得2
                        你 未使 去 偷挽 別人 辛苦 所 種 e0 果子 得2
Comp「補語連詞」是「得、甲1、了2、予3」的詞類標記。它的功用為連接兩個動詞，或前接一個動詞，後接一個子句。補語連詞並無貢獻任何語意，為一功能詞，此標記可以對應到國語的標記「DE」。但由於「補語連詞」不但可以標記閩南語的「得」，更可以標記「甲1」、「了2」、「予3」等其他詞，所以不採用「DE」，而使用「Comp」。
             例如： 活 得 真 健康
                         湊 甲1 按呢
                         排 了2 真 水2
                         穿 予3 水水2
       
此外，由於閩南語一部份的詞彙，其語法特性和國語不同，因此需將中研院詞庫小組所訂立之標記原則做一調整，調整之處如下所列：
　
＊重疊動詞：
此類動詞例如「食食」（ciah8ciah8），的詞類是依其後接的結果補語性質，以及其句法特性來判斷詞類標記。以「食食」（ciah8ciah8）為例，在「你緊共便當e0菜攏食食予3了」一句中，「食食」的詞類標記應為VB；然而在「等伊食食甲1飽就未哭a03」一句，「食食」則標予和未重覆前的原形動詞「食」相同的詞類，VC。
'''

詞性種類 = []
for 詞,華,英 in zip(詞性表[::3],詞性表[1::3],詞性表[2::3],):
    詞性種類.append('{}'.format(詞,華,英))
#     詞性種類.append('{} - {} - {}'.format(詞,華,英))
        