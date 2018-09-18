from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


# [MyPage:最初のページ…役割などを表示する]
class MyPage(Page):

    def is_displayed(self):
        return self.round_number == 1


# [student:順位入力ページ(学校すべてに対して順位をつける)]
class student(Page):


    form_model = models.Player
    form_fields = ['student_first_choice',
                   'student_second_choice',
                   'student_third_choice',
                   'student_fourth_choice'
                   ]

    # [error_message:重複チェック]
    def error_message(self,values):
        if values["student_first_choice"] == values["student_second_choice"]:
            return '第一希望と第二希望が重複しています。'
        elif values["student_first_choice"] == values["student_third_choice"]:
            return '第一希望と第三希望が重複しています。'
        elif values["student_first_choice"] == values["student_fourth_choice"]:
            return '第一希望と第四希望が重複しています。'
        elif values["student_second_choice"] == values["student_third_choice"]:
            return '第二希望と第三希望が重複しています。'
        elif values["student_second_choice"] == values["student_fourth_choice"]:
            return '第二希望と第四希望が重複しています。'
        elif values["student_third_choice"] == values["student_fourth_choice"]:
            return '第三希望と第四希望が重複しています。'




# [ResultsWaitPage2:マッチングを計算するページ]
class ResultsWaitPage2(WaitPage):
    def after_all_players_arrive(self):
        self.group.tekitou2()


# [Results:マッチング結果を表示するページ]
class Results(Page):


    timer_text = '30秒後に次のラウンドが始まります。'
    timeout_seconds =30

    pass


# [page_sequence:ページの表示順]
page_sequence = [
    MyPage,
    student,
    ResultsWaitPage2,
    Results,
]