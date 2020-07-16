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
MAJOR, MINOR, MICRO = 0, 3, 2
COPY = "幽霊が小説を書いた、なんて不可思議は存在しない"
ONELINE = "文芸部のリレー小説に誰も書いた覚えのない続きが書かれていた"
OUTLINE = "青春ミステリ短編。高校の文芸部でやっていたリレー小説に、誰も書いた覚えのない部分があった。部員の一人は幽霊が書いたと言い出すが"
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
            w.plot_note("高校の文芸部に所属する$kiriは不思議が大嫌いだ",
                "誰かが勘違いしているだけで世界には不思議などないと豪語している"),
            w.plot_note("同級生で同じ部員の$yujiが、今日も文化部が部室で使っている旧校舎に幽霊が出たという噂を持ち込んだ"),
            w.plot_note("一方、文芸部では部活動としてリレー小説を行っていた",
                "その締切を守れなかった$yujiは黙ったままノートを置いておく"),
            w.plot_note("同じ部員で不可思議大好きな$natsuがやってきて$yujiが小説を書いていないだろうと勝手に決めつける"),
            w.plot_note("$natsuはノートを確認し、リレー小説に謎の続きを発見する"),
            w.plot_note("それが幽霊の仕業だと騒ぎ出した"),
            "顧問の$tobeはほとんど顔を出さない",
            "$yujiには姉がいる",
            "$yujiは$natsuに惚れている",
            outline="部員の一人がノートのリレー小説に誰も書いた覚えのない部分を発見する")

def ep_ghostnote(w: World):
    return w.episode("幽霊の小説",
            w.plot_note("幽霊が書いた小説はこんなものだった"),
            w.plot_note("リレー小説はこの高校を舞台としたもので、特に縛りはない（ノート冒頭に記してある）"),
            w.plot_note("高校の旧校舎には昔から幽霊の噂がある"),
            w.plot_note("そこの図書室に置かれたある本に、夜な夜な幽霊が書き込みをしているという"),
            w.plot_note("後悔を残して死んだ生徒たちの、あれがしたかった、これがしたかった、という願いが書き連ねられた古いノート"),
            w.plot_note("しかしある日を境に書かれなくなった"),
            w.plot_note("新学期になり、その犯人が転校していったからだった"),
            outline="幽霊が書いたと思われる小説の中身")

def ep_detective(w: World):
    return w.episode('犯人探し',
            w.plot_note("$kiriは幽霊の仕業ではないことを説明する"),
            w.plot_note("まず部員の中の誰もその小説を書いていないことを証言や文字から判別する"),
            w.plot_note("次にノートの保管状況について整理し、部室にノートがあるときで、鍵がかかっていない時間帯であれば、誰でも書き込み可能だったことを示す"),
            w.plot_note("鍵は顧問の$tobeが保管しているが、ほとんど顔を出さないので、部員の誰かが鍵を持っていることが多い"),
            w.plot_note("犯行が行われたと想定されるのは土曜に$yujiがノートを部室に置いてから、月曜に$kiriが部室を開けるまでの間"),
            w.plot_note("そこで$yujiが実は小説を書かずにそのまま出したと告白したが、次の順番の$natsuは急遽用事があってその日は部室にノートを取りに来られなかった"),
            w.plot_note("外部の愉快犯によるものだと論破し、$kiriはそれで終わらせようとしたが、"),
            w.plot_note("書かれていた短編小説は原稿用紙一枚程度の分量で、内容も文章も大人びている"),
            w.plot_note("$natsuはどうしても引き下がらず、犯人が幽霊だと証明すると言い出す"),
            w.plot_note("$natsuは幽霊が書いた証明がしたくて、監視カメラをつける"),
            outline="部室を閉め切り、誰が書いたのか犯人探しをする")

def ep_truningpoint(w: World):
    return w.episode('転換点',
            w.plot_note("週明け、部員全員揃ってから監視カメラ映像を確認する$kiriたち"),
            w.plot_note("監視カメラに映っていたのは日曜に構内清掃に入る掃除のおばちゃんだった"),
            w.plot_note("彼女はノートを手に取り、何かしている。結構な時間何かをしていて、それからノートを元の場所に戻した"),
            w.plot_note("清掃員の$hatakeを呼び出して、連載小説の続きを書いたのか尋ねる"),
            w.plot_note("彼女は学校の$OGで元文芸部員だったが興味本位でノートを覗いたことはあっても、続きを書いたりはしていないと告白する"),
            w.plot_note("その証拠に$hatakeは左利きでかなり字が傾いた特有の文字だった"),
            w.plot_note("$hatakeはノートを持ち出したのは顧問の$tobeだと告白する"),
            outline="監視カメラを設置して犯人を探す。そこに浮かび上がったのは意外な人物だった")

def ep_truth(w: World):
    return w.episode('真相暴露',
            w.plot_note("珍しく顔を出した$tobeに$kiriは連載小説を書いたか尋ねる"),
            w.plot_note("$tobeは幽霊の話を聞いて、一応ノートを保管しておく目的で持ち帰ったと証言する"),
            w.plot_note("それから、その文字を見て、$yujiの姉の字に似ていると指摘した"),
            w.plot_note("$yujiは思い出す。自分が小説の続きが全然浮かばなくて姉に考えてくれと食事の時に言ったことを"),
            w.plot_note("すぐに$yujiはその件を姉に問い合わせる"),
            w.plot_note("$yujiの姉$shikiは自分がやったと告白し、その連載小説にもヒントが書いてあると教える"),
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

def writer_note(w: World):
    return w.writer_note("作者意図",
            "学校の不思議につきものが「幽霊」や「七不思議」といった、噂話にまつわるものである",
            "それらの多くはどれも元になる逸話があったり、誰かの勘違いを発端とした都市伝説的な広まり方、伝わり方、残され方をしたものだったりで、",
            "本当に幽霊がいたり、怪奇現象が起こったりしている訳ではない",
            "心のどこかでは不思議を肯定したい人たちによって、それらの不思議は辛うじて存在しているが、",
            "現実主義の探偵基質な存在によって、その謎はただのつまらない現実へと引き戻されるのである",
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
            ch_main(w),
            chara_kiri(w),
            chara_natsu(w),
            chara_yuji(w),
            chara_shiki(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

