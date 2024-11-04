sandwich_orders=['tune','ham','normal']
finished_orders=[]
while sandwich_orders:
    sandwich_name=sandwich_orders.pop()
    finished_orders.append(sandwich_name)
    print(f"I made your {sandwich_name} sandwich")
for finished_order in finished_orders:
    print(f"{finished_order} sandwich has been made")