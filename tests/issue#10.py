import sys
sys.path.append('../pokerlib')

import pokerlib
from pokerlib import enums
from pokerlib.implementations import TableWithChoiceToShowCards

class MyTable(TableWithChoiceToShowCards):
    def publicOut(self, out_id, **kwargs):
        print('table', out_id.name)
        if 'hand' in kwargs:
            kwargs['hand'] = list(kwargs['hand'])
        if out_id.name == enums.RoundPublicOutId.SMALLBLIND.name:
            print('DEALER', self.seats[self.round.current_index].id)
            kwargs['dealer_id'] = self.seats[self.round.current_index].id
        print("pub", out_id.name, kwargs)
    def privateOut(self, player_id, out_id, **kwargs):
        if 'hand' in kwargs:
            kwargs['hand'] = list(kwargs['hand'])
        print("private", out_id, kwargs)

table = MyTable(
    _id=1,
    seats = pokerlib.PlayerSeats([None, None, None]),
    buyin = 150,
    small_blind = 5,
    big_blind = 10,
)
player1 = pokerlib.Player(
    table_id = table.id,
    _id = 1,
    name = 'alice',
    money = table.buyin
)
player2 = pokerlib.Player(
    table_id = table.id,
    _id = 2,
    name = 'bob',
    money = table.buyin
)
player3 = pokerlib.Player(
    table_id = table.id,
    _id = 3,
    name = 'uncle joe',
    money = table.buyin
)

table += player1
table += player2

table.publicIn(player1.id, enums.TablePublicInId.STARTROUND)
print('start round')
table.publicIn(player1.id, table.round.PublicInId.CALL)
print('start call')
table.publicIn(player2.id, table.round.PublicInId.CHECK)
table.publicIn(player1.id, table.round.PublicInId.CHECK)
table.publicIn(player2.id, table.round.PublicInId.RAISE, raise_by=50)
table.publicIn(player1.id, table.round.PublicInId.CALL)
table.publicIn(player1.id, table.round.PublicInId.CALL)
# line bellow wil ignore
table.publicIn(player1.id, table.round.PublicInId.CALL)
table.publicIn(player2.id, table.round.PublicInId.CHECK)
table.publicIn(player1.id, table.round.PublicInId.RAISE, raise_by=50)
table.publicIn(player2.id, table.round.PublicInId.FOLD)