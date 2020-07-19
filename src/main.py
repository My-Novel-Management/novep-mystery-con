#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "A Ghost Writer"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from storybuilder.assets import common_rubi
from config import ASSET
# import scenes
from scenes import Clubroom


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Story structure - 1/8    :2k
#   4. Spec
#   5. Plot - 1/4               :4k
#   6. Scenes
#   7. Conte - 1/2              :8k
#   8. Layout
#   9. Draft - 1/1              :15k
#
################################################################


# Constant
TITLE = "ゴーストライター"
MAJOR, MINOR, MICRO = 0, 5, 0
COPY = "幽霊が小説を書いた、なんて不可思議は存在しない"
ONELINE = "約二万字の青春ミステリ短編。文芸部のリレー小説に誰も書いた覚えのない続きが書かれていた"
OUTLINE = "高校の文芸部に所属する$kiriは不可思議なことが嫌いだ。ある日、同じ文芸部員の$natsuが部員でやっていたリレー小説の中に自分たちが書いた覚えのない部分を発見する。それが幽霊の仕業だと言い出すが"
THEME = "不可思議というのはそういう風に観測しているだけで事実は実につまらないものだ"
GENRE = "ミステリ／学園"
TARGET = "10-30台（男女）"
SIZE = "〜20K"
CONTEST_INFO = "ノベルアッププラス・ミステリー短編コンテスト「日常の謎」"
CAUTION = ""
NOTE = ""
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
RELEASED = (7, 12, 2020)


# Episodes

# episodes
def ep_mystery(w: World):
    return w.episode('事件発生',
            w.plot_note("$kiriが入っている文芸部が部室として使わせてもらっている空き教室は、旧校舎にあった"),
            w.plot_note("その旧校舎では最近幽霊が出ると噂になっている"),
            w.plot_note("$kiriは謎を解くのは得意だが不思議が大嫌いだった"),
            w.plot_note("誰かが勘違いしているだけで世界には不思議などないと豪語している"),
            w.plot_note("部室にやってくると鍵が開いていた"),
            w.plot_note("中には同級生で同じ部員の$yujiがいて、ノートを気まずそうに置いていた"),
            w.plot_note("$yujiは$kiriに同じ部員の$natsuのことを相談してくる"),
            w.plot_note("$yujiは$natsuのことが好きでこの部に入ったのだった"),
            w.plot_note("三年生がほぼ抜けた後で、現在は二年生の$kiriたち三人だけになってしまっている"),
            w.plot_note("$kiriは本を読んでいるだけでも何も言われないこの部が気に入っていた"),
            w.plot_note("思い出したかのように$yujiにリレー小説のことを確認しようとすると、$natsuが入ってきた"),
            w.plot_note("$natsuは同級生で何かと不思議なことやオカルトが大好きな女子"),
            w.plot_note("現実派の$kiriとはいつも言い争いになっていた"),
            w.plot_note("「ねえ知ってる？」と$natsuのいつものが始まる"),
            w.plot_note("彼女が始めたのは旧校舎の幽霊部員の話だった"),
            w.plot_note("旧校舎では最近幽霊部員が出て、勝手に物を消したり、別の場所に移動させたり、落書きしてあったりと、好き放題しているらしい"),
            w.plot_note("だが$kiriは「幽霊なんていない」と断言する"),
            w.plot_note("分からない物事を幽霊やオカルト現象にして考えないのは人間の頭脳の敗北で、真実を知ろうとしない怠慢だと"),
            w.plot_note("$natsuはノートを見て、そこに奇妙な書き込みを見つける。赤字で正に幽霊が書いた小説だった"),
            "顧問の$tobeはほとんど顔を出さない",
            "$yujiには姉がいる",
            "$yujiは$natsuに惚れている",
            "リレー小説のルールがノート冒頭に書いてあるが、それについての注意書きというか、それを読む作業をどこかに",
            outline="部員の一人がノートのリレー小説に誰も書いた覚えのない部分を発見する")

def ep_ghostnote(w: World):
    return w.episode("幽霊の小説",
            "幽霊小説の中身",
            w.plot_note("幽霊が書いた小説はこんなものだった"),
            w.plot_note("それはまだ新校舎が建てられる前の、旧校舎が普通に校舎として使われていた時代"),
            w.plot_note("ある生徒が自殺した"),
            w.plot_note("原因はいじめだと言われているが、真相は誰も知らない"),
            w.plot_note("そのままその事件は忘れられ、新しい校舎が建ち、旧校舎は使われない空き教室になった"),
            w.plot_note("その旧校舎では夜な夜なピアノの音がしたり、誰かのうめき声がしたりして、幽霊が出ると噂になった"),
            w.plot_note("好奇心旺盛な生徒が本当に幽霊が出るかどうか調べようと、ある日、旧校舎に泊まり込みで番をする"),
            w.plot_note("しかし結局幽霊が出ることはなく、その生徒たちは朝を迎えた"),
            w.plot_note("だが翌日、学校では幽霊を見つけにいったその生徒たちが消えたと話題になっていた"),
            w.plot_note("それを確かめようと次々と生徒が旧校舎に入り、幽霊になってしまった"),
            w.plot_note("これはその幽霊の生徒の一人が書き残した記録である、という結び文になっている"),
            outline="幽霊が書いたと思われる小説の中身")

def ep_detective(w: World):
    return w.episode('犯人探し',
            w.plot_note("$kiriはその小説を見て「幽霊なんていない」と断言する"),
            w.plot_note("誰がやったものだと言う$kiriに、$natsuは説明を求める"),
            w.plot_note("$kiriはまずこのリレー小説のノートの存在を知っているのが現在の部員三名と顧問の$tobeだけであると示す"),
            w.plot_note("それから一人一人に誰もこれを書いていないか確かめる"),
            w.plot_note("$natsuはいつも自分の前の分だけ確認し、そこから構想をねって金曜日の締切までに書いておいておいたと"),
            w.plot_note("それに対して$yujiは自分はそんなものを書いた覚えはない、とだけ言うが、いつもと違い雰囲気がおかしい"),
            w.plot_note("$natsuに詰められ、$yujiは実はリレー小説を書いてこなかったと告白する"),
            w.plot_note("$natsuと$yujiの口論が始まるが、それに割って入り、誰も書いていないという証言を確認する"),
            w.plot_note("次に$kiriはノートの保管状況についてまとめる"),
            w.plot_note("まずはノートの冒頭に書いてあるリレー小説についての注意書きを読み上げる"),
            w.plot_note("リレー小説はこの学校を舞台とすること"),
            w.plot_note("小説は前の人が書いた内容を使ってもいいし、使わずに新しい話を書いてもいい"),
            w.plot_note("見開き一ページ、最低でも書くこと"),
            w.plot_note("次の人はページをめくった次の見開きページを使うこと"),
            w.plot_note("リレー小説が始まったのは２学期になってからで、最初はみんなしっかり書いていた"),
            w.plot_note("しかし今月に入ってから$yujiは自分が小説を書いていないと告白した"),
            w.plot_note("ノートを確認すると、けれど$yujiの回には彼が書いた覚えのない小説が書かれている"),
            w.plot_note("その文字は$yujiの綺麗な字によく似ていた。ただ彼も書いたかどうか覚えてないと言う"),
            w.plot_note("それを発見したことで、最初は誰かが悪戯で赤字の小説を書き込んだ、というところから、本格的な幽霊小説事件になった"),
            w.plot_note("けれど$kiriはそれでも慌てることなく、新しい情報が手に入ったので、より幽霊の可能性は低くなったと言う"),
            w.plot_note("$kiriは誰が書いたかは置いておいて、次にノートがどう管理されていたかを話す"),
            w.plot_note("ノートは各自担当の週は自宅に持ち帰ったり、自由なようにしていた"),
            w.plot_note("その間は誰でも自由に書き込める可能性があるが、誰かに見せたりしたか尋ねたが、三人とも見せていないと話す"),
            w.plot_note("次に部室の管理について話す"),
            w.plot_note("鍵は顧問の$tobeが保管しているが、ほとんど顔を出さないので、部員の誰かが鍵を持っていることが多い"),
            w.plot_note("犯行が行われたと想定される土曜に$yujiがノートを部室に置いてから、月曜に$kiriが部室を開けるまでの間"),
            w.plot_note("そこで$yujiが実は小説を書かずにそのまま出したと告白したが、次の順番の$natsuは急遽用事があってその日は部室にノートを取りに来られなかった"),
            w.plot_note("以上のことから、誰でも犯行可能であり、また部員三人は誰もやっていないという証言から外部犯であると"),
            w.plot_note("$kiriはそれで現実の証明は終わったと言うが、$natsuは納得しない"),
            w.plot_note("しかし翌週、再び幽霊小説が書かれていた"),
            outline="部室を閉め切り、誰が書いたのか犯人探しをする")

def ep_truningpoint(w: World):
    return w.episode('転換点',
            w.plot_note("再び書かれていた赤字の幽霊小説の内容は、まるで今の文芸部内の騒動を予見したものに見えた"),
            w.plot_note("$natsuは幽霊の仕業だと証明する為に部室に監視カメラを設置する"),
            w.plot_note("幽霊が監視カメラに映るかどうか気になる、と冗談なのか本気なのか分からない言葉で承諾した$kiri"),
            w.plot_note("週明け、部員全員揃ってから$kiriたちは監視カメラ映像を確認した"),
            w.plot_note("監視カメラに映っていたのは日曜に構内清掃に入る掃除のおばちゃんだった"),
            w.plot_note("彼女はノートを手に取り、何かしている。結構な時間何かをしていて、それからノートを元の場所に戻した"),
            w.plot_note("$natsuは自分のコネを利用して、その清掃員を突き止め、呼び出すことに成功する"),
            w.plot_note("清掃員の$hatakeを呼び出して、$kiriは監視カメラの映像を見せて、そこで何をしていたのか尋ねた"),
            w.plot_note("彼女は学校の$OGで元文芸部員だったが興味本位でノートを覗いたことはあっても、続きを書いたりはしていないと告白する"),
            w.plot_note("$natsuはそれでも監視カメラ映像から$hatakeが幽霊騒動の原因だった説を押す"),
            w.plot_note("$kiriは$natsuに字を書かせる。左利きだと監視カメラ映像から分かっていて、更にその字の傾きが特徴的だった"),
            w.plot_note("$hatakeの犯行説は否定されたが、彼女は自分がこのノートに気づいたのは顧問の$tobeが持ち出しているのを見たからだと証言する"),
            w.plot_note("その日は運悪く、$tobeは別の用事で学校におらず、確認することはできなかった"),
            w.plot_note("$kiriはもうこれ以上書かれることはないから安心していいと言う"),
            w.plot_note("その通りで、次の週明けには幽霊小説はなかった"),
            outline="監視カメラを設置して犯人を探す。そこに浮かび上がったのは意外な人物だった")

def ep_truth(w: World):
    return w.episode('真相暴露',
            w.plot_note("その週末は$tobeに部室の鍵を預けていたので、$kiriは$tobeを連れ立って部室へとやってきた"),
            w.plot_note("部室に入ると、$tobeにノートのリレー小説に続きを書いたかどうか尋ねるが、$tobeはそんなことはしないと断言する"),
            w.plot_note("$kiriは$tobeに$natsuによって幽霊がリレー小説の続きを書いたとでっちあげられていると説明"),
            w.plot_note("だがノートを確認するとしっかり小説の続きが書かれている"),
            w.plot_note("ただし内容は繋がっていない"),
            w.plot_note("それを見て$kiriは犯人が分かったと言う"),
            w.plot_note("部員たちが揃うと$kiriはこの茶番を終わらせると宣言し、今回の事件について説明を始める"),
            w.plot_note("発端は$yujiがリレー小説をやりたいと言い出したことだった"),
            w.plot_note("それを思いついたのは$yujiではないだろう、と尋ねると、彼の姉$shikiが考えついたものだった"),
            w.plot_note("そうなった事情は伏せた（$yujiが$natsuともっと話す手段がないかとか尋ねたのだろう）が、今回の話を知っていたのは部員と顧問、清掃員を除くと、$yujiの姉$shikiもいたことになる"),
            w.plot_note("それに加えて、最初こそ何とか相手の気を引こうと小説を書いていた$yujiが書くのが面倒になり、書かなくなった"),
            w.plot_note("途中から$shikiが完全に$yujiの代わりを務めていたが$yujiはそれを知らず、書かなくても大丈夫なんだと思ってノートだけ持って帰るようになっていた"),
            w.plot_note("「でもそれなら文字を見て気づくんじゃない？」と$natsuがつっこむ"),
            w.plot_note("そこで$yujiに字を書かせる。性格に比べてやけに綺麗な字を書く。それは小さい頃から習字を習わされて、字だけは綺麗に書けたからだ"),
            w.plot_note("ぱっと見では見分けがつかない"),
            w.plot_note("ではなぜ$natsuがそれを「幽霊が書いた」と勘違いしたのか"),
            w.plot_note("赤字で、しかもホラー系のフォントを印字したものだったからだ。人間が書いたみたいな文字だが、造られたフォントだと説明する"),
            w.plot_note("$kiriは$yujiに頼んで$shikiに連絡を取ってもらう"),
            w.plot_note("連絡がつくと、$kiriに変わるように言われ、電話に出た"),
            w.plot_note("$shikiは$kiriに、あの幽霊小説がいつ書かれたものなのか、尋ねる"),
            w.plot_note("$kiriはそれがこのリレー小説を提案した時には既に作られていたことを指摘し、最初から書かれていたと言う"),
            w.plot_note("なぜ気づかなかったのか、$natsuは疑問を持つが、それに対して、最初の小説だけが書かれていたことを告げる"),
            w.plot_note("また巧妙にページが切られていることも"),
            w.plot_note("そこまで初日に知っていて何故指摘しなかったのか？　という$shikiの問いに「ちゃんと外部犯だと示した」と。それでＱＥＤのつもりだったと"),
            w.plot_note("謎は相手に分かるように説明しないといけないと$shikiは主張する"),
            w.plot_note("謎を解いていた$kiriのことを$shikiは気に入り、大学のミステリ研に来るよう要請するが、不思議を作る側は嫌いだと断った"),
            outline="顧問の先生の証言で本当の犯人が彼の姉と分かる")


def ch_main(w: World):
    return w.chapter('main',
            ep_mystery(w),
            ep_ghostnote(w),
            ep_detective(w),
            ep_truningpoint(w),
            ep_truth(w),
            )

# Note
def writer_note(w: World):
    return w.writer_note("作者意図",
            "学校の不思議につきものが「幽霊」や「七不思議」といった、噂話にまつわるものである",
            "それらの多くはどれも元になる逸話があったり、誰かの勘違いを発端とした都市伝説的な広まり方、伝わり方、残され方をしたものだったりで、",
            "本当に幽霊がいたり、怪奇現象が起こったりしている訳ではない",
            "心のどこかでは不思議を肯定したい人たちによって、それらの不思議は辛うじて存在しているが、",
            "現実主義の探偵基質な存在によって、その謎はただのつまらない現実へと引き戻されるのである",
            )

# Plot
def plot_notes(w: World):
    return (pl_main(w),
            pl_sub(w),
            )

def pl_main(w: World):
    return w.writer_note("main",
            "幽霊小説について",
            "幽霊小説の犯人は？",
            w.plot_note("幽霊小説の犯人は「$shiki」"),
            "どうやってノートを手に入れたか？",
            w.plot_note("$yujiが家に持って帰った時に部屋に入って借りた"),
            "いつ幽霊小説（赤字）を書き込んだか？",
            w.plot_note("一番最初に「これを使えば？」と$yujiにノートを渡した時に"),
            "最初の日にひと月後の小説を仕込んでおいた",
            "初日に見つけられていたなら、それでよかったという話",
            "追加の文章は、ヒントとして与えたもの",
            "幽霊小説の話を$yujiから聞いて、同じ細工をした",
            )

def pl_sub(w: World):
    return w.writer_note("sub",
            "校舎の幽霊騒動",
            "$shikiが二年の時に噂を流した",
            "元々は旧校舎を解体して新しい施設を建てようという話があったのを邪魔するためだった",
            "そのことは追加のリレー小説で書かれた内容から察せられる",
            )

# Characters
def chara_notes(w: World):
    return (chara_kiri(w),
            chara_natsu(w),
            chara_yuji(w),
            chara_shiki(w),
            )

def chara_kiri(w: World):
    return w.chara_note("$kiriの履歴書",
            "学者の父と、看護師の母の下に生まれる",
            "小さい頃から知的好奇心が旺盛で、気になることはとにかく知りたがった",
            "本が読めるようになってからは父親の書庫にこもりがちになり、",
            "近所の図書館では常連になった",
            "小学生でPCのC言語の基礎をマスターし、自分でプログラムを組むようになる",
            "中学の時、ある事件に関わったことをきっかけに、他人と距離を置くようになる",
            "高校では幼馴染の$yujiに誘われて仕方なく文芸部に入る",
            )

def chara_natsu(w: World):
    return w.chara_note("$natsuの履歴書",
            "破天荒な旅行ライターの母と、堅実な役所勤めの父の下に生まれる",
            "よく動いて怪我をする娘だった",
            "家庭教師をつけたが、よく喧嘩になり、すぐに辞めさせてしまった",
            "学校では男子とよく口論をして、取っ組み合いの喧嘩をするような女子で、一目置かれていた",
            "高学年になり力でかなわなくなると、今度は口や金、政治力にものを言わせるようになる",
            "中学に入り、先輩に初恋をしたことで女らしさを磨き始める",
            "高校に入り、同じクラスの$kiriが気になり、彼と一緒の部活に入る",
            )

def chara_yuji(w: World):
    return w.chara_note("$yujiの履歴書",
            "精密機器の会社員である父と、事務パートの母の下に生まれる",
            "近所だった$kiriとは保育園時代からの腐れ縁で、何かと迷惑をかけては彼に解決してもらった",
            "とにかくめんどくさがりな割に何かと首をつっこみたがる",
            "また女関係にだらしなくて、すぐに誰かを好きになり、それがトラブルの種になった",
            "高校で文芸部に入ったのはどこかの部活に入らなければならないけれど体育系部活は嫌だったこと、",
            "またその当時の三年生の先輩が美人だったこと（$shikiの後輩だった）が主な理由である",
            "最近は同じ部活の$natsuが気になっている",
            )

def chara_shiki(w: World):
    return w.chara_note("$shikiの履歴書",
            "$yujiの三つ上の姉",
            "才女で、小さい頃からパズルや謎解きが得意だった",
            "人に謎解きを仕掛けるのも好きで、$yujiはその犠牲者になっていた",
            "それが現在の$yujiのトラウマになっているが本人は気にしていない",
            "$yujiが文芸部に入ったと知り、将来ミステリ作家を目指している$shikiは、",
            "何かと動向を気にしている",
            "今回、リレー小説の話を小耳に挟み、また$yujiに言われたこともあって、一計を考えた",
            )

def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_released(*RELEASED)
    return w.run(
            writer_note(w),
            *plot_notes(w),
            *chara_notes(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

