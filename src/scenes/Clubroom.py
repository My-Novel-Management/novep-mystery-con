# -*- cofing: utf-8 -*-
'''
Stage: Club room
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# scenes
def ghost_rumor(w: World):
    return w.scene("幽霊の噂",
            w.plot_note("高校の文芸部の部室として使わせてもらっているのは旧校舎の教室の一つ"),
            w.plot_note("そこに向かう一人の男子学生"),
            w.plot_note("旧校舎には幽霊が出るという噂があった"),
            "基本的に$yuji目線で物語は語られるが、三人称である",
            "幽霊のような非科学的なものを信じるのは馬鹿のすることだ等と",
            "ほぼ部室だけで展開するようにする",
            "幽霊部員の具体的な話が一つ欲しい",
            )

def yuji_thinking(w: World):
    return w.scene("$yujiの気持ち",
            w.plot_note("部室に入ってくる$yuji"),
            w.plot_note("先に$kiriがいて、彼は一人で読書をしている"),
            w.plot_note("$kiriが「今日はやけに早いじゃないか。さしずめ提出予定の連載小説を書いてこなかったんだろう？」と指摘"),
            "部室の様子",
            "スチール製の本棚に大量に文庫本（古いのも新しいのも）が並べられている",
            "$kiriの外見など",
            "読んでいる本はアガサクリスティあたり",
            )

def mystery_note(w: World):
    return w.scene("謎の小説を見つける",
            w.plot_note("$natsuが駆け込んでくる",
                "演劇部で幽霊が出たと騒動になっているらしい"),
            w.plot_note("$kiriは「幽霊などこの世にいない」といつもの調子で言う"),
            w.plot_note("$natsuはリレー小説を持ち出して、$kiriが現実主義すぎると非難する"),
            w.plot_note("そのリレー小説に謎の文章を見つけて$natsuは騒ぎ出す", "幽霊がいると"),
            "友人の$yujiは文芸部だが書くことに興味はない",
            "$yujiは忘れっぽい",
            "$natsuの外見。お嬢様だが男勝りな感じ。$kiriを意識してやや女っぽいおしゃれな部分も（制服の着方とか）",
            "$yujiと$natsuはいつも口論をしていて、その矛先が$kiriに向かう",
            "$kiriは他人や揉め事に興味がない",
            )

def ghost_novel(w: World):
    return w.scene("幽霊が書いた小説",
            w.plot_note("「幽霊はいないと言ったばかりだろう」と$kiriが確認する"),
            w.plot_note("そこには誰の筆跡でもなさそうな字で、とても高校生が書いたとは思えない質の高い掌編が書かれていた"),
            w.plot_note("事情を聞くとどうやら自分の番のはずが、誰かが既に小説の続きを書いていた", "しかも誰も書いた覚えがないらしい"),
            "ここの作品（掌編）そのものが今回の謎解きのヒントになっている",
            )

def detective(w: World):
    return w.scene("探偵をやることになる",
            w.plot_note("世の中に不思議なことはないと言い張る$kiriは何故かその犯人を探すことになる"),
            "$kiriは「またか」という思いだが、一度口から出したら引けなくなる",
            )

def members_witness(w: World):
    return w.scene("部員たちの証言",
            w.plot_note("$kiriはまず最初に部員たちから証言を集めると提案する"),
            w.plot_note("$yujiは最初はがんばって書いたものの、今回は書けなかったと告白する"),
            w.plot_note("$natsuは自分が書いたものを差し、それが書かれている小説と全く違うと言う"),
            "本当に幽霊がいるんじゃないか、とミスリードする内容を挿入",
            )

def nothing_criminal(w: World):
    return w.scene("犯人はいなかった",
            w.plot_note("話を聞いたところでは、誰もその小説を書いた者はいなかった"),
            w.plot_note("「やっぱり幽霊の仕業なのよ」と言い出す$natsuに対して、$kiriは外部犯の可能性を示唆する"),
            w.plot_note("$kiriは条件から外部犯の可能性しかないと言い切り、探偵を終わる"),
            "どうやれば外部犯が書くことができるのか、という思考実験を行う",
            )

def appear_second(w: World):
    return w.scene("幽霊部員再び",
            w.plot_note("翌日は何も起こらず、事件は忘れ去られた"),
            w.plot_note("一週間後、再び幽霊文芸部員が出現した"),
            "ここで$yujiの姉の存在、顧問の存在を出しておく",
            "部室は鍵がかけられ、鍵は顧問の$tobeが管理している",
            )

def consider_condition(w: World):
    return w.scene("条件を整理する",
            w.plot_note("$kiriは一度なら幽霊でもいいが二度起こったのは偶然じゃないと言い出し、",
                "条件を整理してこの謎を解くと言い出す"),
            )

def set_monitoring_cam(w: World):
    return w.scene("監視カメラを設置する",
            w.plot_note("結局監視カメラを設置してでも犯人を探したいと、$natsuが自腹でカメラを設置した"),
            )

def watch_cam_data(w: World):
    return w.scene("監視カメラに映っていたもの",
            w.plot_note("監視カメラに映っていたのは掃除のおばさん（$hatake）だった"),
            )

def hatake_witness(w: World):
    return w.scene("$hatakeの証言",
            w.plot_note("$hatakeを呼び出して、リレー小説の続きを書いたのか尋ねる"),
            w.plot_note("$hatakeは学校のＯＧで図書部員だった", "小説好きでこっそりノートを読んだりしていたと証言する",
                "しかし彼女は書いたりしていなかった"),
            w.plot_note("$hatakeの証言で、顧問の$tobeがノートを持って帰っていたと分かる"),
            "$hatakeの字には特徴があった",
            )

def tobe_advice(w: World):
    return w.scene("$tobeの助言",
            w.plot_note("久々にやってきた顧問の$tobeは幽霊部員の話に「そんなものいる訳ない」と$kiriと同じ答え"),
            w.plot_note("$tobeは文章の内容からどう考えても書き慣れた人物、しかも大学生以上と推理して、$yujiの姉はどうしてるんだ、と話を振った"),
            )

def yuji_confess(w: World):
    return w.scene("$yujiの告白",
            "筆無精で漫画やラノベが読みたいから部活参加している$yujiは、恋心を抱いている$natsuの提案に仕方なくのったが、リレー小説を書く気がなく、姉に適当に代わりに書いといてと言ったことも忘れてしまっていた",
            )

def ghost_writer(w: World):
    return w.scene("ゴーストライター",
            w.plot_note("実は$yujiの姉$shikiが、彼が宿題のリレー小説を書かないのをいいことに、勝手に続きを書き加えていた"),
            )

def epilogue(w: World):
    return w.scene("エピローグ",
            w.plot_note("後日、その話を姉にすると、$shikiは$kiriに「ぜひ一度大学のミステリ研究会に遊びにきて」とメッセージをくれた"),
            w.plot_note("しかし「ミステリは嫌いなんだ」と$kiriは答えたのだった"),
            "事件後、いつものように本を読んでいた$kiri",
            "そこにリレー小説の続きが書かれたノートが差し出される",
            "そこには$shikiから「大学に来たらぜひうちのサークルに入って」とお誘いが書かれていた",
            "しかし$kiriは「不可思議を生み出す側になるつもりはない」とぴしゃりと断った",
            )
