from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.sum_basic import SumBasicSummarizer
from sumy.summarizers.reduction import ReductionSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.kl import KLSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.utils import get_stop_words
from sumy.nlp.tokenizers import Tokenizer
import spacy
import neologdn
import re
import emoji
import mojimoji
from janome.tokenizer import Tokenizer as JanomeTokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *

class JapaneseCorpus:
    # ①
    def __init__(self):
        self.nlp = spacy.load('ja_ginza')
        # ()「」、。は全てスペースに置き換える
        char_filters = [UnicodeNormalizeCharFilter(), RegexReplaceCharFilter(r'[(\)「」、。]', ' ')]
        # 名詞・形容詞・副詞・動詞の原型のみ
        token_filters = [POSKeepFilter(['名詞', '形容詞', '副詞', '動詞']), ExtractAttributeFilter('base_form')]
        self.analyzer = Analyzer(
            char_filters=char_filters, tokenizer=JanomeTokenizer(), token_filters=token_filters)
    # ②

    def preprocessing(self, text):
        text = re.sub(r'\n', '', text)
        text = re.sub(r'\r', '', text)
        text = re.sub(r'\s', '', text)
        text = text.lower()
        text = mojimoji.zen_to_han(text, kana=True)
        text = mojimoji.han_to_zen(text, digit=False, ascii=False)
        text = ''.join(c for c in text if c not in emoji.UNICODE_EMOJI)
        text = neologdn.normalize(text)
        return text
    # ③

    def make_sentence_list(self, sentences):
        doc = self.nlp(sentences)
        self.ginza_sents_object = doc.sents
        sentence_list = [s for s in doc.sents]
        return sentence_list
    # ④

    def make_corpus(self):
        corpus = [' '.join(self.analyzer.analyze(str(s))) +
                  '。' for s in self.ginza_sents_object]
        return corpus


class EnglishCorpus(JapaneseCorpus):
    # ①
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
    # ②

    def preprocessing(self, text):
        text = re.sub(r'\n', '', text)
        text = re.sub(r'\r', '', text)
        text = mojimoji.han_to_zen(text, digit=False, ascii=False)
        text = mojimoji.zen_to_han(text, kana=True)
        text = ''.join(c for c in text if c not in emoji.UNICODE_EMOJI)
        text = neologdn.normalize(text)
        return text
    # ④

    def make_corpus(self):
        corpus = []
        for s in self.ginza_sents_object:
            tokens = [str(t) for t in s]
            corpus.append(' '.join(tokens))
        return corpus


# algorithms
algorithm_dic = {"lex": LexRankSummarizer(), "tex": TextRankSummarizer(), "lsa": LsaSummarizer(),
                 "kl": KLSummarizer(), "luhn": LuhnSummarizer(), "redu": ReductionSummarizer(),
                 "sum": SumBasicSummarizer()}


def summarize_sentences(sentences, sentences_count=3, algorithm="lex", language="japanese"):
    # ①
    if language == "japanese":
        corpus_maker = JapaneseCorpus()
    else:
        corpus_maker = EnglishCorpus()
    preprocessed_sentences = corpus_maker.preprocessing(sentences)
    preprocessed_sentence_list = corpus_maker.make_sentence_list(
        preprocessed_sentences)
    corpus = corpus_maker.make_corpus()
    parser = PlaintextParser.from_string(" ".join(corpus), Tokenizer(language))
    # ②
    try:
        summarizer = algorithm_dic[algorithm]
    except KeyError:
        print("algorithm name:'{}'is not found.".format(algorithm))
    summarizer.stop_words = get_stop_words(language)
    summary = summarizer(document=parser.document,
                         sentences_count=sentences_count)
    # ③
    if language == "japanese":
        return "".join([str(preprocessed_sentence_list[corpus.index(sentence.__str__())]) for sentence in summary])
    else:
        return " ".join([sentence.__str__() for sentence in summary])


text = """今日は3分間でスピーチをすることを3分でまとめてみたいと思います 3分です すごい短い気がするじ
ゃないですか だから3分スピーチって言われるとすごい予定も刻んでなんだろう 必要なことを最初か
ら喋るしか時間がないよねって思っちゃうかもしれないんですけど そんなことないですよ3分があっ
たら人は感動します 凄い良いスピーチ だなって思ってもらうんだけど時間は自分で作ることができ
るんです だから3分ももらえたらラッキー ましてや 経営者の前で3分 しゃべっていいなんて言う 大
チャンスがあったらいいです 投資家の前で3分 しゃべっていいというチャンスがあったらありがたい
ことはないんです3分待って感動するんだもん だから 散歩 もらえたらしっかりと準備して反応させ
ましょう そのためのコツを三つに絞って今日はお話をしたいと思いますね ストーリーの靴です そう
に言ってね あのスピーチは大きく分けて ストーリーをしゃべると それについて 二つに分かれてる
んですよかかるか っていうことになるんですが ストーリーってね 一番単純に言えば単に決まればい
いんです 今何に困ってるかを伝えるだけなんです えーとね 例えば今のプロジェクトにすごく困って
いるとか 将来 こんな不安なやってくるとか困ってることをとにかく伝えることだったんですね 将来
の不安で例えば今は2020年にオリンピックの後 大きな業がやってくるんじゃないかってみんな恐れて
ますね そのことを例えば話します ちょっと具体的にどんな困難が次々にやってくるの勝手の花室用
があります そしてそこに共感して一緒に聞いてると困ったら今度それに対するソリューション解決さ
れるわけです ポイントは ここで 説得力をどうやって出すか なんですけど ここのポイントはない
今日はね 歴史に接続するってのが一般的な方法 なんですよ 歴史に接続するっていうのはどういうこ
とかというと 私たちはこれまでこういうことが得意こういう女の子じゃんだった時に こうやって乗
り越えてきたみたいなことを話す っていう意味です では二つ目に行きます 意見についてのコツです
そういうストーリーを語りました 私たちこうやって乗り越えましたよ っていうことを伝えましたそ
の後に じゃあ だから何が言えるのか っていうことを行きます 来られ 非常に シンプルでいいんで
す 3分しかないから答えはひとつでいいたいこと言えばいいんです 私に任せてください みたいな 非
常に シンプルなことでいいんです 私たちは困っていますですから これをやりましょうとかってシン
プルなことでいいんです それを言えば 意見としては最後に話し方のコツです 話し方のコツって言っ
たですね なんか あの3分って今 僕が喋ってみたいねすごい 急いで仕上げないと思うかもしれないん
ですが3分という時間はさっきみたいにすごく長いんです だから答えを 雄三 yuzo ってふりをしなが
らもったいぶって答えを言って これがポイントになるんでちっちゃなってこと話し方の一個大きなポ
イントになります 見積もり 持ってお話をしました"""
sentences_count = 10
algorithm = "lex"
language = "japanese"
sum_sentences = summarize_sentences(
    text, sentences_count=sentences_count, algorithm=algorithm, language=language)
print(sum_sentences)
