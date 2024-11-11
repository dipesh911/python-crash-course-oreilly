def make_car(manuf, model,**car_info):
    car_info['Manufacture']=manuf
    car_info['Model']=model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
car = make_car('kia', 'sonet', color='white', tow_package=True)
print(car)