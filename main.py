print("===welcome to ride builders===")
print("bike menu: 1. bikes , 2. cars")
choice = int(input("enter your choice:"))
if choice == 1:
    print("now here are the options:")
    print("1. mountain bike")
    print("2. sports bike")
    print("3. super bike")
    bike_type = int(input("choose the bike you want:"))
    if bike_type == 1:
        print("A mountain motorcycle—commonly known as an adventure bike or dual-sport—is built specifically for rugged terrain, high-altitude paths, dirt tracks, and long-distance touring away from paved roads.")
    elif bike_type == 2:
        print("A sports bike is a high-performance motorcycle designed primarily for speed, rapid acceleration, sharp cornering, and hard braking on paved roads and racetracks")
    elif bike_type == 3:
        print("superbike is a high-performance motorcycle—typically featuring a 600cc to 1200cc engine—built for extreme speed, rapid acceleration, and razor-sharp handling on both the street and the race track.")
    else:
        print("===INVALID CHOICE MADE===")
elif choice == 2:
    print("now here are the options:")
    print("1. defender")
    print("2. creta")
    print("3. mercedes")
    car_type = int(input("choose the car you want:"))
    if car_type == 1:
        print("The Land Rover Defender is an iconic luxury off-road SUV known for its rugged heritage, boxy silhouette, and modern high-tech capabilities.")
    elif car_type == 2:
        print("The Hyundai Creta is a popular 5-door subcompact crossover SUV produced by Hyundai since 2014. Named after the Greek island of Crete, it is one of the highest-selling mid-size SUVs in India and global emerging markets.")
    elif car_type == 3:
        print("Mercedes-Benz is a world-famous German luxury automotive brand owned by Mercedes-Benz Group AG, with its corporate headquarters located in Stuttgart, Germany.")
    else:
        print("===INVALID CHOICE MADE===")
else:
    print("===INVALID CHOICES MADE===")
