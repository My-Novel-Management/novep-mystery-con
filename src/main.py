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
from config import DAYS, ITEMS, PERSONS, RUBIS, STAGES, TIMES, WORDS


# episodes
def ep_mystery(w: World):
    return w.episode('事件発生',
            w.plot_note("$kiriが部室で一人小説を読んでいたところに、やってきた$natsuが騒ぎ出す", "幽霊がいると"),
            w.plot_note("事情を聞くとどうやら自分の番のはずが、誰かが既に小説の続きを書いていた", "しかも誰も書いた覚えがないらしい"),
            w.plot_note("世の中に不思議なことはないと言い張る$kiriは何故かその犯人を探すことになる"),
            outline="部員の一人がノートのリレー小説に誰も書いた覚えのない部分を発見する")

def ep_detective(w: World):
    return w.episode('犯人探し',
            w.plot_note("リレー小説に参加している$natsuや$yujiたちからアリバイ及び証言を取る"),
            w.plot_note("話を聞いたところでは、誰もその小説を書いた者はいなかった"),
            w.plot_note("一週間後、再び幽霊文芸部員が出現した"),
            w.comment("ここで$yujiの姉の存在、顧問の存在を出しておく"),
            w.comment("部室は鍵がかけられ、鍵は顧問の$tobeが管理している"),
            outline="部室を閉め切り、誰が書いたのか犯人探しをする")

def ep_truningpoint(w: World):
    return w.episode('転換点',
            w.plot_note("結局監視カメラを設置してでも犯人を探したいと、$natsuが自腹でカメラを設置した"),
            w.plot_note("監視カメラに映っていたのは掃除のおばさん（$hatake）だった"),
            w.plot_note("$hatakeの証言で、顧問の$tobeがノートを持って帰っていたと分かる"),
            outline="監視カメラを設置して犯人を探す。そこに浮かび上がったのは意外な人物だった")

def ep_truth(w: World):
    return w.episode('真相暴露',
            w.plot_note("実は$yujiの姉$sikiが、彼が宿題のリレー小説を書かないのをいいことに、勝手に続きを書き加えていた"),
            w.plot_note("後日、その話を姉にすると、$sikiは$kiriに「ぜひ一度大学のミステリ研究会に遊びにきて」とメッセージをくれた"),
            w.plot_note("しかし「ミステリは嫌いなんだ」と$kiriは答えたのだった"),
            outline="顧問の先生の証言で本当の犯人が彼の姉と分かる")


def ch_main(w: World):
    return w.chapter('main',
            ep_mystery(w),
            ep_detective(w),
            ep_truningpoint(w),
            ep_truth(w),
            )


def main(): # pragma: no cover
    w = World.create_world("ゴーストライター")
    w.config.set_outline('高校の文芸部でやっていたリレー小説に、誰も書いた覚えのない話が書き加えられていた')
    w.db.set_from_asset(basic.ASSET)
    w.db.build_db(PERSONS, STAGES, DAYS, TIMES, ITEMS, WORDS, RUBIS)
    return w.run(
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

