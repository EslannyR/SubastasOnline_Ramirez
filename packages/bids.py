#- Pensado para el futuro -
class Bids:
    def __init__(self, bid_id, user_id, item_id, amount, bid_date):
        self.bid_id = bid_id
        self.user_id = user_id
        self.item_id = item_id
        self.amount = amount
        self.bid_date = bid_date