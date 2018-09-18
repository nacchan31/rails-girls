from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'ysquestion'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # 実験1のインストラクションは理解できましたか？5を理解できた、1を理解できなかったとして、5段階で評価してください。
    q_ex_11 = models.CharField(initial=None,
                              choices=['5', '4', '3', '2', '1'],
                              verbose_name='',
                              widget=widgets.RadioSelectHorizontal()
                              )
    # 実験1は何回目くらいから理解することができたか
    q_ex_12 = models.PositiveIntegerField(verbose_name='',
                                         choices=range(1, 6),
                                         initial=None,
                                         blank=True
                                         )

    # 実験1で、応募順位はどのように正直に申告しましたか？一番近いものを選んで下さい。
    q_ex_13 = models.CharField(verbose_name='',
                                         choices=['進学希望順位と同様にした', '自分の優先度が高い学類を上位にした', '他の参加者が選びそうな学類を上位にした','他の参加者が選らばなそうな学類を上位にした', 'その他'],
                                           widget=widgets.RadioSelectHorizontal(),
                                         initial=None,
                                         )

    # 他の学生の応募順位を予想しましたか？
    q_ex_14 = models.CharField(verbose_name='',
                                         choices=['予想した', '予想しなかった', '予想したときもあった'],
                                           widget=widgets.RadioSelectHorizontal(),
                                         initial=None,
                                         )

    # 実験2のインストラクションは理解できましたか？5を理解できた、1を理解できなかったとして、5段階で評価してください。
    q_ex_21 = models.CharField(initial=None,
                               choices=['5', '4', '3', '2', '1'],
                               verbose_name='',
                               widget=widgets.RadioSelectHorizontal()
                               )

    # 実験2は何回目くらいから理解することができたか
    q_ex_22 = models.PositiveIntegerField(verbose_name='',
                                         choices=range(1, 6),
                                         initial=None,
                                         blank=True
                                         )

    # 実験2で、応募順位はどのように正直に申告しましたか？一番近いものを選んで下さい。
    q_ex_23 = models.CharField(verbose_name='',
                                         choices=['進学希望順位と同様にした', '自分の優先度が高い学類を上位にした', '他の参加者が選びそうな学類を上位にした','他の参加者が選らばなそうな学類を上位にした', 'その他'],
                                         widget=widgets.RadioSelectHorizontal(),
                                         initial=None,
                                         )
    # 他の学生の応募順位を予想しましたか？
    q_ex_24 = models.CharField(verbose_name='',
                                         choices=['予想した', '予想しなかった', '予想したときもあった'],
                                           widget=widgets.RadioSelectHorizontal(),
                                         initial=None,
                                         )


    # 本実験ような配属決定において、あなたが一番重視する項目はなんですか？
    q_ex_7 = models.CharField(initial=None,
                              choices=['自分の学びたい分野ができる', '自分の好きな先生がいる', '友達と一緒になれる', '自分の成績ではいれる',
                                       '入学前から進学したかった学類', '単位取得が楽そう', 'その他'],
                              verbose_name='',
                              widget=widgets.RadioSelectHorizontal()
                              )

    # 性別
    q_gender = models.CharField(initial=None,
                                choices=['男', '女'],
                                verbose_name='',
                                widget=widgets.RadioSelectHorizontal()
                                )

    # ＤＡメカニズムを知っていますか？
    q_da = models.CharField(verbose_name='',
                                       choices=['メカニズムの手順・性質を知っている','聞いたことがある', '知らない'],
                                        initial=None,
                                        widget=widgets.RadioSelectHorizontal()
                            )
