def sandwich(*items):
    print("Below ingredients are required:")
    for item in items:
        print(f" {item}")

sandwich('ham','peporini','salad')