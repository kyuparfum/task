from random import randint
import os
import time

print("\033[33m-----------------------게임 설명--------------------- \n"
      "1.유저를 등록하면 랜덤한 power가 부여됩니다. \n"
      "2.power는 한번만 변경 할 수 있습니다. \n"
      "3.공격은 물리공격과 마법공격이 있으며, 이는 power에 비례합니다. \n"
      "4.게임종료 5초 후 콘솔이 리셋됩니다. \n"
      "----------------------------------------------------\033[0m\n")


# 캐릭터 클래스
class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """

    def __init__(self, name, power):
        self.name = name
        self.max_hp = 20000  # 내 캐릭터는 죽지않았으면해.....
        self.mp = 100
        self.power = power
        self.damage = self.power * randint(1, self.power * 10) * 2  # 물리공격
        self.magic = self.power * randint(1, self.power * 10) * 2  # 마법공격
        self.alive = True

    def show_info(self):
        print(f"\033[94m-------플레이어 정보---------\n"
              f"플레이어 : {self.name} \n"
              f"HP : {self.max_hp} \n"
              f"MP : {self.mp} \n"
              f"POWER : {self.power} \n"
              f"DAMAGE(물리) : {self.damage} \n"
              f"DAMAGE(마법) : {self.magic} \n"
              f"--------------------------\033[0m")

# 물리 마법 공격 및 상태출력
    def attack(self, select):
        if select == 1:
            user_damage = self.power * randint(1, self.damage * 1)
            damage_type = '물리'
            print(
                f"\033[30m{self.name}님이 몬스터에게 \033[90m{damage_type}\033[0m \033[30m{user_damage}데미지를 입혔습니다.\033[0m")
        elif select == 2:
            user_damage = self.power * randint(1, self.magic * 1)
            damage_type = '마법'
            print(
                f"\033[30m{self.name}님이 몬스터에게 \033[34m{damage_type}\033[0m \033[30m{user_damage}데미지를 입혔습니다.\033[0m")
        return user_damage

    def u_status(self, m_attack):
        self.max_hp -= m_attack
        print(f"플레이어의 남은 HP는 {self.max_hp}입니다.")
        if self.max_hp < 0:
            self.alive = False

# 몬스터 기본정보 및 대미지, 공격, 상태 체크함수


class Monster:
    def __init__(self, num):
        self.hp = randint(2000, 3500)
        self.damage = randint(10, 100)
        self.num = num
        self.alive = True
        print(
            f"\033[93m몬스터의 HP는 {self.hp} \n"
            f"몬스터의 기본 damage는 {self.damage}입니다.\033[0m \n \n")

    def m_damage(self, attack):
        self.hp -= attack
        if self.hp < 0:
            self.alive = False

    def m_attack(self):
        m_damage = randint(1, self.damage)
        print(f"\033[91m몬스터가 플레이어에게 {m_damage}데미지를 입혔습니다. \033[0m\n")
        return m_damage

    def status_check(self):
        if self.alive:
            print(f'몬스터의 남은 hp는 {self.hp}입니다. \n \n 몬스터가 공격합니다.')
        else:
            print('\033[96m WIN!!!!\033[0m')


# 유저 정보 입력
def make_player():
    player = input('\033[35m 플레이어의 이름을 정해주세요 :')
    return player


# 유저의 power 랜덤 재부여
def make_power():
    random_power = randint(1, 20)
    print(f"당신의 power는 {random_power}입니다. (1~20)")
    print("power를 다시 부여 받고 싶으신가요? \n 기회는 1번입니다")
    re_power = check_answer()
    if re_power == 1:
        random_power = randint(1, 20)
        print(f"power를 {random_power}로 다시 부여 받았습니다.")
        return random_power
    else:
        return random_power


# 몬스터 선택 이건뭐 임의로 생성하고 출력으로 이름만 뜨게 한 부분이라 나중에 각각 자신의 몬스터도 임의 생성되게 하고싶다.
def make_monster():
    user_monster = input("\033[96m 상대할 몬스터를 선택해 주세요. 포켓몬은 랜덤의 스텟을 가집니다.\033[0m\n"
                         "\033[33m  1. 피카츄 \033[0m\n \033[31m 2. 파이리\033[0m \n \033[34m 3. 꼬북이 \033[0m \n "
                         "\033[32m 4. 이상해씨 \033[0m \n \033[31m 5. 아차모 \033[0m \n \033[32m 6. 나무지기\033[0m \n \033[34m 7. 물짱이 \033[0m")
    if user_monster.isdigit() == False:
        print('숫자로만 입력해 주세요.')
        make_monster()
    elif int(user_monster) == 1:
        print('\033[33m 1. 피카츄를 선택하셨습니다.\033[0m')
    elif int(user_monster) == 2:
        print('\033[31m 2. 파이리를 선택하셨습니다.\033[0m')
    elif int(user_monster) == 3:
        print('\033[34m 3. 꼬북이를 선택하셨습니다.\033[0m')
    elif int(user_monster) == 4:
        print('\033[32m 4. 이상해씨를 선택하셨습니다.\033[0m')
    elif int(user_monster) == 5:
        print('\033[31m 5. 아차모를 선택하셨습니다.\033[0m')
    elif int(user_monster) == 6:
        print('\033[32m 6. 나무지기를 선택하셨습니다.\033[0m')
    elif int(user_monster) == 7:
        print('\033[34m 7. 물짱이를 선택하셨습니다.\033[0m')
    elif int(user_monster) == 1 or int(user_monster) > 8:
        print('선택할 수 있는 범위를 벗어났습니다.')
        make_monster()
    else:
        monster_num = int(user_monster)
        return monster_num


# 대답 유효성 판단 (핑핑이엄마의 도움으로 간단하게 선택을 만들 수 있었다.) 처음에는 문자로 하니깐 답도 없더니 이렇게 하니깐 오류없이 잘 진행됐다.
def check_answer():
    while True:
        check = input("\033[33m 1.예\033[0m \033[31m 2.아니오\033[0m \n")
        if check == '':
            print("\033[31m 입력된 값이 없습니다. 다시 입력해주세요.\033[0m \n")
        elif check.isdigit() == False:
            print('\033[31m숫자로만 입력해주세요.\033[0m')
        elif int(check) < 1 or int(check) > 2:
            print("1 또는 2 중에서 선택해주세요.\n")
        else:
            return int(check)


# 공격 방식 선택(다음번에는 원소(element)개념의 속성도넣고싶다.)
def select_attack():
    while True:
        select = input("공격 방법을 선택해 주세요. \n"
                       "\033[90m 1.물리 공격\033[0m \n"
                       "\033[34m 2.마법 공격\033[0m \n")
        if select == '':
            print("\033[31m다시 입력해주세요.\033[0m \n")
        elif select.isdigit() == False:
            print("\033[31m숫자로만 입력해 주세요.\033[0m")
        elif int(select) < 1 or int(select) > 2:
            print('\033[31m 1~2 사이로 선택해주세요.\033[0m')
        else:
            return int(select)


# 싸우자싸워~!
total = 0
name_receive = make_player()
power_receive = make_power()
user = Character(name_receive, power_receive)
user.show_info()
monster_receive = make_monster()
monster = Monster(monster_receive)
while True:
    if total == 0:
        print("몬스터에게 전투를 신청하시겠습니까? \n")
        game_start = check_answer()
    if game_start == 1:
        attack = select_attack()
        user_damage_give = user.attack(attack)
        monster.m_damage(user_damage_give)
        monster.status_check()
        attack = monster.m_attack()
        user.u_status(attack)
        total += 1
    else:
        break

    if not user.alive:
        print(f'\033[31m유저가 사망했습니다. 게임을 종료합니다.\033[0m')
        break
    if not monster.alive:
        print(f"\033[33m총 {total}번의 전투 끝에 승리했습니다!\033[0m")
        break
    if monster.alive:
        print("\033[32m다시 공격 하시겠습니까?\033[0m")
        re_attack = check_answer()
    if re_attack == 1:
        continue
    else:
        break

time.sleep(5)  # 5초후
os.system('clear')  # 콘솔창종료
