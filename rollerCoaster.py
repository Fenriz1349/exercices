places= 5
tours =3
file =[2,3,5,4]
profits=0
for i in range (tours):
    print("tour ",i+1)
    placesDispo=places
    groupe=file[0]
    while groupe<=placesDispo:
        print(file)
        placesDispo-=groupe
        print("placedispo ",placesDispo)
        profits+=groupe
        print("profits ",profits)
        file.append(groupe)
        file.remove(file[0])
        groupe=file[0]
print("le profit de la journée est de ",profits," €")

