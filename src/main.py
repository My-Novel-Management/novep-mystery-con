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
from config import ASSET
# import scenes
# from sceones import xxx


# Constant
TITLE = "ゴーストライター"
OUTLINE = "高校の文芸部がやっていたリレー小説に、誰も書いた覚えのない続きが書かれていた"
MAJOR, MINOR, MICRO = 0, 3, 0


# Episodes

# episodes
def ep_mystery(w: World):
    return w.episode('事件発生',
            "幽霊のような非科学的なものを信じるのは馬鹿のすることだ等と",
            "ほぼ部室だけで展開するようにする",
            w.plot_note("その部室（か校舎）には幽霊部員がいるという噂があった"),
            w.plot_note("$kiriが部室で一人小説を読んでいたところに、やってきた$natsuが騒ぎ出す", "幽霊がいると"),
            "友人の$yujiは文芸部だが書くことに興味はない",
            "$yujiは忘れっぽい",
            w.plot_note("事情を聞くとどうやら自分の番のはずが、誰かが既に小説の続きを書いていた", "しかも誰も書いた覚えがないらしい"),
            w.plot_note("世の中に不思議なことはないと言い張る$kiriは何故かその犯人を探すことになる"),
            outline="部員の一人がノートのリレー小説に誰も書いた覚えのない部分を発見する")

def ep_detective(w: World):
    return w.episode('犯人探し',
            "本当に幽霊がいるんじゃないか、とミスリードする内容を挿入",
            w.plot_note("リレー小説に参加している$natsuや$yujiたちからアリバイ及び証言を取る"),
            w.plot_note("話を聞いたところでは、誰もその小説を書いた者はいなかった"),
            w.plot_note("一週間後、再び幽霊文芸部員が出現した"),
            "ここで$yujiの姉の存在、顧問の存在を出しておく",
            "部室は鍵がかけられ、鍵は顧問の$tobeが管理している",
            outline="部室を閉め切り、誰が書いたのか犯人探しをする")

def ep_truningpoint(w: World):
    return w.episode('転換点',
            w.plot_note("結局監視カメラを設置してでも犯人を探したいと、$natsuが自腹でカメラを設置した"),
            w.plot_note("監視カメラに映っていたのは掃除のおばさん（$hatake）だった"),
            w.plot_note("$hatakeを呼び出して、リレー小説の続きを書いたのか尋ねる"),
            w.plot_note("$hatakeは学校のＯＧで図書部員だった", "小説好きでこっそりノートを読んだりしていたと証言する",
                "しかし彼女は書いたりしていなかった"),
            w.plot_note("$hatakeの証言で、顧問の$tobeがノートを持って帰っていたと分かる"),
            "$hatakeの字には特徴があった",
            outline="監視カメラを設置して犯人を探す。そこに浮かび上がったのは意外な人物だった")

def ep_truth(w: World):
    return w.episode('真相暴露',
            w.plot_note("久々にやってきた顧問の$tobeは幽霊部員の話に「そんなものいる訳ない」と$kiriと同じ答え"),
            w.plot_note("$tobeは文章の内容からどう考えても書き慣れた人物、しかも大学生以上と推理して、$yujiの姉はどうしてるんだ、と話を振った"),
            "筆無精で漫画やラノベが読みたいから部活参加している$yujiは、恋心を抱いている$natsuの提案に仕方なくのったが、リレー小説を書く気がなく、姉に適当に代わりに書いといてと言ったことも忘れてしまっていた",
            w.plot_note("実は$yujiの姉$shikiが、彼が宿題のリレー小説を書かないのをいいことに、勝手に続きを書き加えていた"),
            w.plot_note("後日、その話を姉にすると、$shikiは$kiriに「ぜひ一度大学のミステリ研究会に遊びにきて」とメッセージをくれた"),
            w.plot_note("しかし「ミステリは嫌いなんだ」と$kiriは答えたのだった"),
            outline="顧問の先生の証言で本当の犯人が彼の姉と分かる")


def ch_main(w: World):
    return w.chapter('main',
            ep_mystery(w),
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
    w.config.set_outline(f'{OUTLINE}')
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(ASSET)
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

