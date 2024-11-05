favorite_places={'A':['goa','timbaktoo'],
                 'B':['Nainital'],
                 'C':['manali','puri']
                 }
for name,place in favorite_places.items():
    print(f"{name}'s fav place is :")
    for places in place:
        print(places)