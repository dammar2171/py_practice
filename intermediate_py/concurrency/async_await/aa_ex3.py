import asyncio
import random
import time

class Restaurant:
    async def prepare_order(self, order):
        print(f"{order['customer']} → {order['food']} status: Preparing...")
        delay = random.uniform(2, 5)
        await asyncio.sleep(delay)
        order["status"] = "Ready"
        print(f"{order['customer']} → {order['food']} status: Ready (after {delay:.2f}s)")
        return order

class DeliveryAgent:
    async def deliver(self, order):
        print(f"{order['customer']} → {order['food']} status: Delivering...")
        delay = random.uniform(3, 7)
        await asyncio.sleep(delay)
        order["status"] = "Delivered"
        print(f"{order['customer']} → {order['food']} status: Delivered (after {delay:.2f}s)")
        return order

class OrderSystem:
    def __init__(self):
        self.restaurant = Restaurant()
        self.agent = DeliveryAgent()

    async def place_order(self, customer, food):
        order = {"customer": customer, "food": food, "status": "Placed"}
        print(f"{customer} placed order for {food} → Status: Placed")
        return order

    async def process_order(self, order):
        order = await self.restaurant.prepare_order(order)
        order = await self.agent.deliver(order)
        return order

    async def process_all_orders(self, orders):
        tasks = [self.process_order(order) for order in orders]
        results = await asyncio.gather(*tasks)
        return results

async def main():
    system = OrderSystem()

    customers = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
    foods = ["Pizza", "Burger", "Pasta", "Sushi", "Sandwich"]

    # Sequential execution
    start_seq = time.time()
    seq_orders = [await system.place_order(c, f) for c, f in zip(customers, foods)]
    for order in seq_orders:
        await system.process_order(order)
    end_seq = time.time()
    seq_time = end_seq - start_seq
    print(f"\nSequential time: {seq_time:.2f}s\n")

    # Concurrent execution
    start_par = time.time()
    par_orders = [await system.place_order(c, f) for c, f in zip(customers, foods)]
    await system.process_all_orders(par_orders)
    end_par = time.time()
    par_time = end_par - start_par
    print(f"\nConcurrent time: {par_time:.2f}s")
    print(f"Time saved: {seq_time - par_time:.2f}s")

asyncio.run(main())
