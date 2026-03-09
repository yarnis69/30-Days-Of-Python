#variables

distance_mi = 8
is_raining = False
has_bike = True
has_car = True
has_ride_share_app = False

#app logic

if not distance_mi:
    print('False')

if distance_mi <= 1 and not is_raining:
    print('True')
else:
    print('False')

if distance_mi > 1 and distance_mi <= 6 and has_bike and not is_raining:
    print('True')
else:
    print('False')

if distance_mi > 6 and (has_car or has_ride_share_app):
    print('True')
else:
    print('False')
