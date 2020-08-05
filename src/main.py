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
MAJOR, MINOR, MICRO = 0, 7, 0
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
            Clubroom.old_school_ghost(w),
            Clubroom.find_ghost_novel(w),
            outline="部員の一人がノートのリレー小説に誰も書いた覚えのない部分を発見する")

def ep_ghostnote(w: World):
    return w.episode("幽霊の小説",
            Clubroom.a_ghost_novel(w),
            outline="幽霊が書いたと思われる小説の中身")

def ep_detective(w: World):
    return w.episode('犯人探し',
            Clubroom.detective(w),
            Clubroom.note_management(w),
            Clubroom.clubroom_management(w),
            outline="部室を閉め切り、誰が書いたのか犯人探しをする")

def ep_truningpoint(w: World):
    return w.episode('転換点',
            Clubroom.ghost_novel_again(w),
            Clubroom.surveillance_camera(w),
            Clubroom.interview_hatake(w),
            outline="監視カメラを設置して犯人を探す。そこに浮かび上がったのは意外な人物だった")

def ep_truth(w: World):
    return w.episode('真相暴露',
            Clubroom.testimony_tobe(w),
            Clubroom.truth(w),
            outline="顧問の先生の証言で本当の犯人が彼の姉と分かる")


def ch_main(w: World):
    return w.chapter('main',
            w.plot_setup("高校の文芸部", "旧校舎には幽霊の噂があった"),
            ep_mystery(w),
            ep_ghostnote(w),
            w.plot_turnpoint("幽霊小説を発見する"),
            w.plot_develop("誰がこの小説を書いたのか推理する"),
            ep_detective(w),
            w.plot_turnpoint("$tobeが初日にノートを確認して赤字が書かれていたと証言したことで、推理が覆る"),
            ep_truningpoint(w),
            w.plot_resolve("犯人は$yujiの姉だった", "噂に聞いた$kiriを試す目的で仕込んだが初日には気づかれず、幽霊が書いたと錯覚した"),
            ep_truth(w),
            w.symbol("（了）"),
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

