from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import copy
import random



author = 'Your name here'

doc = """
Your app description
"""


# [値が変化しないものはここに書く。]
class Constants(BaseConstants):
    name_in_url = 'daplus'
    players_per_group = 6   # [参加者の人数(oTree/settings.py内のSESSION_CONFIGSも変更すること)]
    num_rounds = 6

    # [学生]
    student = ['student1', 'student2', 'student3', 'student4', 'student5', 'student6']

    # [先生]
    teacher = ['A', 'B', 'C', 'D']

    # [実験の役割リスト]
    role_list = [[0],[0,1,6,3,2,5,4],[0,2,1,4,5,3,6],[0,4,5,2,6,1,3],[0,3,2,1,4,6,5],[0,5,3,6,1,4,2],[0,6,4,5,3,2,1]]

    teacher_choices = {'A': ['student3', 'student1', 'student6', 'student5', 'student2', 'student4'],
                       'B': ['student4', 'student6', 'student5', 'student3', 'student2', 'student1'],
                       'C': ['student2', 'student5', 'student4', 'student3', 'student1', 'student6'],
                       'D': ['student5', 'student4', 'student2', 'student6', 'student3', 'student1']
                       }

    student_true_choices = {'student1': ['B', 'D', 'A', 'C'],
                            'student2': ['B', 'C', 'D', 'A'],
                            'student3': ['C', 'B', 'A', 'D'],
                            'student4': ['A', 'C', 'D', 'B'],
                            'student5': ['A', 'D', 'B', 'C'],
                            'student6': ['D', 'A', 'B', 'C']
                            }

##########ここからポイントの設定##########

    #第1志望とマッチした時
    match_1_payoff = c(19)

    #第2志望とマッチした時
    match_2_payoff = c(13)

    # 第3志望とマッチした時
    match_3_payoff = c(8)

    # 第4志望とマッチした時
    match_4_payoff = c(5)

##########ここまでポイントの設定##########



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    student_choices = models.TextField()
    student_choices1 = models.TextField()
    student_choices2 = models.TextField()
    student_first_choices = models.TextField()
    student_second_choices = models.TextField()
    student_third_choices = models.TextField()
    start_studentStatus = models.TextField()
    start_teacherStatus = models.TextField()
    totyu_studentStatus = models.TextField()
    totyu_teacherStatus = models.TextField()
    zantei_studentStatus = models.TextField()
    zantei_teacherStatus = models.TextField()
    dummy_student_first_choices = models.TextField()
    dummy_student_second_choices = models.TextField()
    dummy_student_third_choices = models.TextField()
    dummy_student_fourth_choices = models.TextField()
    student1Status = models.CharField()
    student2Status = models.CharField()
    student3Status = models.CharField()
    student4Status = models.CharField()
    student5Status = models.CharField()
    student6Status = models.CharField()

    student1_1 = models.CharField()
    student1_2 = models.CharField()
    student1_3 = models.CharField()
    student1_4 = models.CharField()
    student2_1 = models.CharField()
    student2_2 = models.CharField()
    student2_3 = models.CharField()
    student2_4 = models.CharField()
    student3_1 = models.CharField()
    student3_2 = models.CharField()
    student3_3 = models.CharField()
    student3_4 = models.CharField()
    student4_1 = models.CharField()
    student4_2 = models.CharField()
    student4_3 = models.CharField()
    student4_4 = models.CharField()
    student5_1 = models.CharField()
    student5_2 = models.CharField()
    student5_3 = models.CharField()
    student5_4 = models.CharField()
    student6_1 = models.CharField()
    student6_2 = models.CharField()
    student6_3 = models.CharField()
    student6_4 = models.CharField()
    


    # [jyunbi:KKDAを動かすための準備]
    def jyunbi(self):
        # [定員の初期値]
        global start_t_lim
        start_t_lim = {'A': 2,
                       'B': 1,
                       'C': 2,
                       'D': 1
                       }
        # [途中定員（KKDAの途中で定員を更新するか比較するときに使う）]
        global totyu_t_lim
        totyu_t_lim = {'A': 2,
                       'B': 1,
                       'C': 2,
                       'D': 1
                       }

        # [暫定定員（KKDA終了時、これを定員として採用）]
        global zantei_t_lim
        zantei_t_lim = {'A': 2,
                        'B': 1,
                        'C': 2,
                        'D': 1
                        }

        # [受け入れ上限]
        global t_up
        t_up = {'A': 2,
                'B': 2,
                'C': 2,
                'D': 2
                }

        # [理工学群に属する学類]
        global riko
        riko = ['A', 'B']

        # [人文学群に属する学類]
        global jinbun
        jinbun = ['C', 'D']



        # [学生の先生に対する選好]
        global student_choices

        # [DAの中で使う]
        global student_choices1
        student_choices1 = copy.deepcopy(student_choices)

        # [KKDAで超過需要がある学類を探すのに使う]
        global student_choices2
        student_choices2 = copy.deepcopy(student_choices)

        # [学生のマッチング相手の初期値(誰ともマッチしていない状態)]
        global start_studentStatus
        start_studentStatus = {S: None for S in Constants.student}

        # [学校のマッチング相手の初期値(誰ともマッチしていない状態)]
        global start_teacherStatus
        start_teacherStatus = {T: [] for T in Constants.teacher}

        # [KKDAの中で使う。開始前はとりあえず初期値]
        global totyu_studentStatus
        totyu_studentStatus = {S: None for S in Constants.student}

        # [KKDAの中で使う。開始前はとりあえず初期値]
        global totyu_teacherStatus
        totyu_teacherStatus = {T: [] for T in Constants.teacher}

        # [KKDAでの暫定解。開始前はとりあえず初期値]
        global zantei_studentStatus
        zantei_studentStatus = {S: None for S in Constants.student}

        # [KKDAでの暫定解。開始前はとりあえず初期値]
        global zantei_teacherStatus
        zantei_teacherStatus = {T: [] for T in Constants.teacher}

        return True

    # DA。回す前にtotyu_studentStatus/totyu_teacherStatus/student_choices1を初期値に戻す処理をすること。
    def damatching(self):
        global totyu_studentStatus
        global totyu_teacherStatus
        global currentPartner

        for s in Constants.student:
            if totyu_studentStatus[s] is None:  # 相手が決まっていない学生がいれば・・・
                t = student_choices1[s].pop(0)  # まだ断られていない学類の中で一番選好の高い学類に申し込む
                if len(totyu_teacherStatus[t]) < totyu_t_lim[t]:  # 定員に空きがあれば・・・
                    totyu_teacherStatus[t].append(s)  # 先生のマッチング相手のリストに申し込んできた学生を追加
                    totyu_studentStatus[s] = t  # 学生のマッチング相手を更新
                elif len(totyu_teacherStatus[t]) == totyu_t_lim[t]:  # 定員がいっぱいなら
                    for x in totyu_teacherStatus[t]:  # 現在マッチしている学生の中で最も順位が低い学生をcurrentPartnerに
                        if totyu_teacherStatus[t].index(x) == 0:
                            currentPartner = x
                        elif Constants.teacher_choices[t].index(x) >= Constants.teacher_choices[t].index(currentPartner):
                            currentPartner = x
                    if Constants.teacher_choices[t].index(s) <= Constants.teacher_choices[t].index(currentPartner):  # currentPartnerより順位が高ければマッチング成功
                        totyu_teacherStatus[t].remove(currentPartner)  # currentPartnerを削除
                        totyu_studentStatus[currentPartner] = None  # currentPartnerだった学生のマッチングを解除
                        totyu_teacherStatus[t].append(s)  # 先生のマッチング相手のリストに申し込んできた学生を追加
                        totyu_studentStatus[s] = t  # 学生のマッチング相手を更新
        if len([1 for y in totyu_studentStatus if totyu_studentStatus[y] is None]) != 0:
            self.damatching()
        return True

    def tyoukajyuyou(self):
        global yoyu
        global tyouka
        global kouho

        yoyu = []  # 定員が学生上限一杯に達していない学類のリスト
        tyouka = []  # 超過需要がある学類のリスト
        kouho = []  # 定員を減らす学類の候補

        for t in Constants.teacher:  # 定員が学生上限に達していない学類を探す
            if zantei_t_lim[t] < t_up[t]:
                yoyu.append(t)
                print (yoyu)

        if len(yoyu) == 0:
            print('定員が学生上限に達していない学類はありません')

        elif len(yoyu) != 0:
            for t in yoyu:  # 超過需要がある学類を探す
                print(t)
                for s in Constants.student:
                    if student_choices2[s].index(t) < student_choices2[s].index(
                            zantei_studentStatus[s]):  # 学生sにとって暫定のパートナーより学類tの選好が高ければ、学類tは超過需要の学類
                        print(s + '超過需要あり')
                        if t not in tyouka:
                            tyouka.append(t)  # 超過需要がある学類のリストに学類tを追加
                            print(tyouka)
                            print('超過需要のある学類を追加しました')
                    else:
                        print(s + '超過需要なし')

        return True

    def daplusmatching(self):
        global totyu_studentStatus
        global totyu_teacherStatus
        global zantei_teacherStatus
        global zantei_studentStatus
        global student_choices
        global student_choices1
        global totyu_t_lim
        global zantei_t_lim
        global riko
        global jinbun
        global tyouka
        global koho
        global yoyu
        global currentPartner
        global tyoukairekae
        global tyouka2

        tyouka2 = []

        totyu_studentStatus = copy.deepcopy(start_studentStatus)

        totyu_teacherStatus = copy.deepcopy(start_teacherStatus)

        student_choices1 = copy.deepcopy(student_choices)

        totyu_t_lim = {'A': 2,
                       'B': 1,
                       'C': 2,
                       'D': 1
                       }

        # まずDAをまわして、暫定解を得る
        self.damatching()

        # 得られたマッチング(totyu_studentStatus/totyu_teacherStatus)を暫定解(zantei_studentStatus/zantei_teacherStatus)とする。
        zantei_studentStatus = copy.deepcopy(totyu_studentStatus)
        zantei_teacherStatus = copy.deepcopy(totyu_teacherStatus)

        print(zantei_studentStatus)

        # このときの定員を暫定の定員とする
        zantei_t_lim = copy.deepcopy(totyu_t_lim)

        step = 0

        while step < 10:

            self.tyoukajyuyou()

            tyoukairekae = random.sample(tyouka, len(tyouka))

            print (tyoukairekae)
            print ('の順で定員を変えてみます')

            if len(tyoukairekae) == 0:
                print('超過需要がないのでプログラムを終了します')
                break  # while文に対するbreak

            elif len(tyoukairekae) != 0:

                print ('超過需要があるのでマッチングを探します')

                for t in tyoukairekae:
                    print('超過需要はどこかな')
                    if t in riko:
                        print('超過需要は理工でした')
                        kouho = copy.deepcopy(riko)
                        kouho.remove(t)  # t学類が理工の学類だった場合、t以外の理工の学類を減らす候補とする

                    elif t in jinbun:
                        print('超過需要は人文でした')
                        kouho = copy.deepcopy(jinbun)
                        kouho.remove(t)

                    if len(kouho) == 0:
                        continue

                    elif len(kouho) != 0:
                        print('定員変えていきます')
                        for x in kouho:  # 候補の中から順に試していく
                            if zantei_t_lim[x] == 0:
                                continue

                            elif zantei_t_lim[x] != 0:  # 定員が1以上だったら減らしてみる。0のときはこれ以上減らせないのでやらない。
                                print('定員を増やします')
                                totyu_t_lim = copy.deepcopy(zantei_t_lim)

                                totyu_t_lim[t] += 1  # 超過需要がある学類tの定員を1人増やす
                                totyu_t_lim[x] -= 1  # 学類xの定員を一人減らす

                                # DAを回す準備をする。
                                student_choices1 = copy.deepcopy(student_choices)
                                totyu_studentStatus = copy.deepcopy(start_studentStatus)
                                totyu_teacherStatus = copy.deepcopy(start_teacherStatus)
                                currentPartner = None

                                print(totyu_studentStatus)
                                print(student_choices1)
                                print(zantei_studentStatus)

                                # 新しい定員でDAをまわし、解を得る。
                                self.damatching()

                                print(totyu_studentStatus)
                                print(zantei_studentStatus)

                                # ここでzantei_studentStatusとtotyu_studentStatusを比較する
                                # パレート支配していればzantei_studentStatus/zantei_teacherStatus/zantei_t_limを更新
                                if all(student_choices[s].index(totyu_studentStatus[s]) <= student_choices[s].index(
                                        zantei_studentStatus[s]) for s in Constants.student):
                                    print('ここはクリア')
                                    if any(student_choices[s].index(totyu_studentStatus[s]) < student_choices[s].index(
                                            zantei_studentStatus[s]) for s in Constants.student):
                                        print('パレート支配したのでマッチングを更新します')
                                        zantei_studentStatus = copy.deepcopy(totyu_studentStatus)
                                        zantei_teacherStatus = copy.deepcopy(totyu_teacherStatus)
                                        zantei_t_lim = copy.deepcopy(totyu_t_lim)
                                        print(zantei_studentStatus)

                                    break  # for x in kouho: を抜ける

                                else:
                                    print('パレート支配しませんでした')


                        else:
                            print('他の学類増やしてみます')
                            if t == tyoukairekae[-1]:
                                print('もう超過需要１つで試せるやつはありません')
                            continue

                        print('もう一回超過需要探します')
                        break


                else:
                    print('１つでパレート支配できなくなりました')
                    tyouka2 = copy.deepcopy(tyouka)
                    kouho2 = Constants.teacher.copy()

                    if len(tyouka2) == 1:
                        print('超過需要は1学群だけなので終了します')
                        break

                    elif len(tyouka2) == 2:
                        print('超過需要が2学群にあるので定員変えてみます')
                        kouho2.remove(tyouka2[0])
                        kouho2.remove(tyouka2[1])
                        totyu_t_lim = copy.deepcopy(zantei_t_lim)
                        totyu_t_lim[tyouka2[0]] += 1  # 超過需要がある学類tの定員を1人増やす
                        totyu_t_lim[tyouka2[1]] += 1  # 超過需要がある学類tの定員を1人増やす
                        totyu_t_lim[kouho2[0]] -= 1  # 学類xの定員を一人減らす
                        totyu_t_lim[kouho2[1]] -= 1  # 学類xの定員を一人減らす

                        # DAを回す準備をする。
                        student_choices1 = copy.deepcopy(student_choices)
                        totyu_studentStatus = copy.deepcopy(start_studentStatus)
                        totyu_teacherStatus = copy.deepcopy(start_teacherStatus)
                        currentPartner = None

                        # 新しい定員でDAをまわし、解を得る。
                        self.damatching()

                        # ここでzantei_studentStatusとtotyu_studentStatusを比較する
                        # パレート支配していればzantei_studentStatus/zantei_teacherStatus/zantei_t_limを更新
                        if all(student_choices[s].index(totyu_studentStatus[s]) <= student_choices[s].index(
                                zantei_studentStatus[s]) for s in Constants.student) and any(
                            student_choices[s].index(totyu_studentStatus[s]) < student_choices[s].index(
                                zantei_studentStatus[s]) for s in Constants.student):
                            print('パレート支配したのでマッチングを更新します')
                            zantei_studentStatus = copy.deepcopy(totyu_studentStatus)
                            zantei_teacherStatus = copy.deepcopy(totyu_teacherStatus)
                            zantei_t_lim = copy.deepcopy(totyu_t_lim)
                            print(zantei_studentStatus)
                        else:
                            break

        return True

    def tekitou2(group):
        global totyu_studentStatus
        global totyu_teacherStatus
        global zantei_teacherStatus
        global zantei_studentStatus
        global student_choices1
        global totyu_t_lim
        global zantei_t_lim
        global riko
        global jinbun
        global tyouka
        global koho
        global yoyu
        global currentPartner
        global tyoukairekae
        global yoyu
        global tyouka
        global kouho
        global start_t_lim
        global t_up
        global student_choices
        global student_choices2
        global start_studentStatus
        global start_teacherStatus





   #     players = group.get_players()

    #    student_first_choices = [p.student_first_choice for p in players]      #学生の第1志望のリスト

     #   student_second_choices = [p.student_second_choice for p in players]     #学生の第2志望のリスト

      #  student_third_choices = [p.student_third_choice for p in players]     #学生の第3志望のリスト

       # student_fourth_choices = [p.student_fourth_choice for p in players]  # 学生の第4志望のリスト

        #student_choices = {'student1': [student_first_choices[0], student_second_choices[0], student_third_choices[0], student_fourth_choices[0]],
         #                  'student2': [student_first_choices[1], student_second_choices[1], student_third_choices[1], student_fourth_choices[1]],
          #                 'student3': [student_first_choices[2], student_second_choices[2], student_third_choices[2], student_fourth_choices[2]],
           #                'student4': [student_first_choices[3], student_second_choices[3], student_third_choices[3], student_fourth_choices[3]],
            #               'student5': [student_first_choices[4], student_second_choices[4], student_third_choices[4], student_fourth_choices[4]],
             #              'student6': [student_first_choices[5], student_second_choices[5], student_third_choices[5], student_fourth_choices[5]]
        #}


        student1_part = group.get_player_by_role('student1')

        student2_part = group.get_player_by_role('student2')

        student3_part = group.get_player_by_role('student3')

        student4_part = group.get_player_by_role('student4')

        student5_part = group.get_player_by_role('student5')

        student6_part = group.get_player_by_role('student6')

        student_choices = {'student1': [student1_part.student_first_choice, student1_part.student_second_choice, student1_part.student_third_choice, student1_part.student_fourth_choice],
                           'student2': [student2_part.student_first_choice, student2_part.student_second_choice, student2_part.student_third_choice, student2_part.student_fourth_choice],
                           'student3': [student3_part.student_first_choice, student3_part.student_second_choice, student3_part.student_third_choice, student3_part.student_fourth_choice],
                           'student4': [student4_part.student_first_choice, student4_part.student_second_choice, student4_part.student_third_choice, student4_part.student_fourth_choice],
                           'student5': [student5_part.student_first_choice, student5_part.student_second_choice, student5_part.student_third_choice, student5_part.student_fourth_choice],
                           'student6': [student6_part.student_first_choice, student6_part.student_second_choice, student6_part.student_third_choice, student6_part.student_fourth_choice]
                           }

        #########################ここから全プレイヤーの入力を表示するための準備#######################

        group.student1_1 = student_choices['student1'][0]

        group.student1_2 = student_choices['student1'][1]

        group.student1_3 = student_choices['student1'][2]

        group.student1_4 = student_choices['student1'][3]

        group.student2_1 = student_choices['student2'][0]

        group.student2_2 = student_choices['student2'][1]

        group.student2_3 = student_choices['student2'][2]

        group.student2_4 = student_choices['student2'][3]

        group.student3_1 = student_choices['student3'][0]

        group.student3_2 = student_choices['student3'][1]

        group.student3_3 = student_choices['student3'][2]

        group.student3_4 = student_choices['student3'][3]

        group.student4_1 = student_choices['student4'][0]

        group.student4_2 = student_choices['student4'][1]

        group.student4_3 = student_choices['student4'][2]

        group.student4_4 = student_choices['student4'][3]

        group.student5_1 = student_choices['student5'][0]

        group.student5_2 = student_choices['student5'][1]

        group.student5_3 = student_choices['student5'][2]

        group.student5_4 = student_choices['student5'][3]

        group.student6_1 = student_choices['student6'][0]

        group.student6_2 = student_choices['student6'][1]

        group.student6_3 = student_choices['student6'][2]

        group.student6_4 = student_choices['student6'][3]

        ##########################ここまで全プレイヤーの入力を表示するための準備#######################

        group.jyunbi()
        group.daplusmatching()

        group.student1Status = zantei_studentStatus['student1']
        group.student2Status = zantei_studentStatus['student2']
        group.student3Status = zantei_studentStatus['student3']
        group.student4Status = zantei_studentStatus['student4']
        group.student5Status = zantei_studentStatus['student5']
        group.student6Status = zantei_studentStatus['student6']


        print(zantei_studentStatus)


        return zantei_studentStatus





class Player(BasePlayer):
    partner = models.CharField()
    role_number = models.IntegerField()





    def partner_deside(self):

        if Constants.role_list[self.subsession.round_number][self.participant.id_in_session] == 1:
            self.partner = self.group.student1Status

        elif Constants.role_list[self.subsession.round_number][self.participant.id_in_session] == 2:
            self.partner = self.group.student2Status

        elif Constants.role_list[self.subsession.round_number][self.participant.id_in_session] == 3:
            self.partner = self.group.student3Status

        elif Constants.role_list[self.subsession.round_number][self.participant.id_in_session] == 4:
            self.partner = self.group.student4Status

        elif Constants.role_list[self.subsession.round_number][self.participant.id_in_session] == 5:
            self.partner = self.group.student5Status

        elif Constants.role_list[self.subsession.round_number][self.participant.id_in_session] == 6:
            self.partner = self.group.student6Status

        return self.partner









    def this_round_role_and_preference(self):
        self.role_number = Constants.role_list[self.subsession.round_number][self.participant.id_in_session]

        return ""


    def role(self):
        if Constants.role_list[self.subsession.round_number][self.participant.id_in_session] == 1:
            return 'student1'

        elif Constants.role_list[self.subsession.round_number][self.participant.id_in_session] ==2:
            return 'student2'

        elif Constants.role_list[self.subsession.round_number][self.participant.id_in_session] ==3:
            return 'student3'

        elif Constants.role_list[self.subsession.round_number][self.participant.id_in_session] ==4:
            return 'student4'

        elif Constants.role_list[self.subsession.round_number][self.participant.id_in_session] ==5:
            return 'student5'

        elif Constants.role_list[self.subsession.round_number][self.participant.id_in_session] ==6:
            return 'student6'




    def set_payoff(self):

        if self.role_number == 1:
            if self.group.student1Status == Constants.student_true_choices['student1'][0]:
                self.payoff = Constants.match_1_payoff
            elif self.group.student1Status== Constants.student_true_choices['student1'][1]:
                self.payoff = Constants.match_2_payoff
            elif self.group.student1Status == Constants.student_true_choices['student1'][2]:
                self.payoff = Constants.match_3_payoff
            elif self.group.student1Status == Constants.student_true_choices['student1'][3]:
                self.payoff = Constants.match_4_payoff

        elif self.role_number == 2:
            if self.group.student2Status == Constants.student_true_choices['student2'][0]:
                self.payoff = Constants.match_1_payoff
            elif self.group.student2Status == Constants.student_true_choices['student2'][1]:
                self.payoff = Constants.match_2_payoff
            elif self.group.student2Status == Constants.student_true_choices['student2'][2]:
                self.payoff = Constants.match_3_payoff
            elif self.group.student2Status == Constants.student_true_choices['student2'][3]:
                self.payoff = Constants.match_4_payoff


        elif self.role_number == 3:
            if self.group.student3Status == Constants.student_true_choices['student3'][0]:
                self.payoff = Constants.match_1_payoff
            elif self.group.student3Status == Constants.student_true_choices['student3'][1]:
                self.payoff = Constants.match_2_payoff
            elif self.group.student3Status == Constants.student_true_choices['student3'][2]:
                self.payoff = Constants.match_3_payoff
            elif self.group.student3Status == Constants.student_true_choices['student3'][3]:
                self.payoff = Constants.match_4_payoff


        elif self.role_number == 4:
            if self.group.student4Status == Constants.student_true_choices['student4'][0]:
                self.payoff = Constants.match_1_payoff
            elif self.group.student4Status == Constants.student_true_choices['student4'][1]:
                self.payoff = Constants.match_2_payoff
            elif self.group.student4Status == Constants.student_true_choices['student4'][2]:
                self.payoff = Constants.match_3_payoff
            elif self.group.student4Status == Constants.student_true_choices['student4'][3]:
                self.payoff = Constants.match_4_payoff

        elif self.role_number == 5:
            if self.group.student5Status == Constants.student_true_choices['student5'][0]:
                self.payoff = Constants.match_1_payoff
            elif self.group.student5Status == Constants.student_true_choices['student5'][1]:
                self.payoff = Constants.match_2_payoff
            elif self.group.student5Status == Constants.student_true_choices['student5'][2]:
                self.payoff = Constants.match_3_payoff
            elif self.group.student5Status == Constants.student_true_choices['student5'][3]:
                self.payoff = Constants.match_4_payoff

        elif self.role_number == 6:
            if self.group.student6Status == Constants.student_true_choices['student6'][0]:
                self.payoff = Constants.match_1_payoff
            elif self.group.student6Status == Constants.student_true_choices['student6'][1]:
                self.payoff = Constants.match_2_payoff
            elif self.group.student6Status == Constants.student_true_choices['student6'][2]:
                self.payoff = Constants.match_3_payoff
            elif self.group.student6Status == Constants.student_true_choices['student6'][3]:
                self.payoff = Constants.match_4_payoff

        return ""




    # [プルダウンの選択肢　ここから]

    student_first_choice = models.CharField(verbose_name='',
                                            choices=Constants.teacher,
                                            initial=None)


    student_second_choice = models.CharField(verbose_name='',
                                             choices=Constants.teacher,
                                             initial=None)

    student_third_choice = models.CharField(verbose_name='',
                                            choices=Constants.teacher,
                                            initial=None)

    student_fourth_choice = models.CharField(verbose_name='',
                                            choices=Constants.teacher,
                                            initial=None)


    # [プルダウンの選択肢　ここまで]
