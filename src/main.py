import sys
from collections import defaultdict, deque


class Order:
    def __init__(self, oid, side, price, qty):
        self.id = oid
        self.side = side
        self.price = float(price)
        self.qty = int(qty)


class OrderBook:

    def __init__(self):
        self.bids = defaultdict(deque)
        self.asks = defaultdict(deque)
        self.orders = {}

    def best_bid(self):
        return max(self.bids.keys()) if self.bids else None

    def best_ask(self):
        return min(self.asks.keys()) if self.asks else None

    def add_order(self, order):
        if order.side == "BUY":
            self.match_buy(order)
        else:
            self.match_sell(order)

    def match_buy(self, order):

        if order.price == 0 and not self.asks:
            print("NO LIQUIDITY FOR MARKET BUY")
            return

        while order.qty > 0 and self.asks:

            best_price = self.best_ask()

            if order.price != 0 and order.price < best_price:
                break

            queue = self.asks[best_price]

            while queue and order.qty > 0:

                sell = queue[0]

                if sell.id == order.id:
                    break

                trade_qty = min(order.qty, sell.qty)

                print(f"TRADE {order.id} {sell.id} {best_price:.2f} {trade_qty}")

                order.qty -= trade_qty
                sell.qty -= trade_qty

                if sell.qty == 0:
                    queue.popleft()
                    del self.orders[sell.id]

            if not queue:
                del self.asks[best_price]

        if order.qty > 0 and order.price != 0:
            self.bids[order.price].append(order)
            self.orders[order.id] = order

    def match_sell(self, order):

        if order.price == 0 and not self.bids:
            print("NO LIQUIDITY FOR MARKET SELL")
            return

        while order.qty > 0 and self.bids:

            best_price = self.best_bid()

            if order.price != 0 and order.price > best_price:
                break

            queue = self.bids[best_price]

            while queue and order.qty > 0:

                buy = queue[0]

                if buy.id == order.id:
                    break

                trade_qty = min(order.qty, buy.qty)

                print(f"TRADE {buy.id} {order.id} {best_price:.2f} {trade_qty}")

                order.qty -= trade_qty
                buy.qty -= trade_qty

                if buy.qty == 0:
                    queue.popleft()
                    del self.orders[buy.id]

            if not queue:
                del self.bids[best_price]

        if order.qty > 0 and order.price != 0:
            self.asks[order.price].append(order)
            self.orders[order.id] = order

    def cancel(self, oid):

        if oid not in self.orders:
            return

        order = self.orders[oid]
        book = self.bids if order.side == "BUY" else self.asks

        queue = book[order.price]

        for i, o in enumerate(queue):
            if o.id == oid:
                del queue[i]
                break

        if not queue:
            del book[order.price]

        del self.orders[oid]

    def print_book(self):

        print("--- Book ---")

        asks = sorted(self.asks.keys())[:5]

        for p in asks:
            qty = sum(o.qty for o in self.asks[p])
            print(f"ASK: {p:.2f} x {qty}")

        bids = sorted(self.bids.keys(), reverse=True)[:5]

        if not bids:
            print("BID: (empty)")
        else:
            for p in bids:
                qty = sum(o.qty for o in self.bids[p])
                print(f"BID: {p:.2f} x {qty}")


def main():

    book = OrderBook()

    for line in sys.stdin:

        line = line.strip()

        if not line:
            continue

        parts = line.split()

        if len(parts) == 2 and parts[0] == "CANCEL":
            book.cancel(parts[1])

        elif len(parts) == 4:
            oid, side, price, qty = parts
            order = Order(oid, side, price, qty)
            book.add_order(order)

        else:
            print("INVALID INPUT:", line)

    book.print_book()


if __name__ == "__main__":
    main()