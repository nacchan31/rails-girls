from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models

class MyPage(Page):
    pass

class Questionnaire(Page):
    form_model = models.Player
    form_fields = [
                   'q_ex_11',
                    'q_ex_12',
                    'q_ex_13',
                    'q_ex_14',
                    'q_ex_21',
                    'q_ex_22',
                    'q_ex_23',
                    'q_ex_24',
                    'q_ex_7',
                    'q_gender',
                    'q_da'
                ]

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Questionnaire,
    ResultsWaitPage,
    Results
]
