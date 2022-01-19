from deck import Deck
from player import Player
from dealer import Dealer
from rule import Rule


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.rule = None

    def start(self):
        print('==== 블랙잭 게임을 시작합니다. ===')
        print('==== 최초 기준 점수를 정하고 기준 점수에 가까운 쪽이 승리합니다.  ===')
        print('==== 플레이어가 기준점수를 초과하면 무조건 딜러의 승리 입니다.  ===')
        print('==== 기준 점수를 입력하세요 ===')
        ref_score = input()
        self.rule = Rule(21)

        print('=== 딜러 턴 입니다. ===')
        self.dealer.draw_card(self.deck.draw_card())
        self.dealer.draw_card(self.deck.draw_card())

        if self.dealer.get_total_score() <= 16:
            self.dealer.draw_card(self.deck.draw_card())

        print('=== 플레이어 턴입니다. === ')
        self.player.draw_card(self.deck.draw_card())
        self.player.draw_card(self.deck.draw_card())

        is_add = True

        while is_add:
            print(' === 카드를 추가로 더 뽑으려면 (A) 카드를 오픈하려면 (O) 를 입력하세요~!! ===')
            q = input()

            if q == 'A':
                self.player.draw_card(self.deck.draw_card())
            elif q == 'O':
                is_add = False

        self.rule.open(self.dealer, self.player)
        self.rule.result()

        print('=== 게임 종료 ===')




