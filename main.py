# Movie Recommendation based off age.

def show_movies():
    print("______here are some movies we will be recommending and the age range for each of them")

    print("61 and above [movie names] ")
    print("41 --- 60 [movie names] ")
    print("21 --- 40 [movie names] ")
    print("11 --- 20 [movie names] ")
    print("0 --- 10 [movie names] ")

show_movies()

def movie_select():
    name = str(input("What's your name? "))
    your_age = int(input("How old are you? "))

    print("Welcome " + name)

    if your_age <= 10:
        print("They should be introduced to light movies and educative movies, like: ")

    elif your_age == 11 or your_age <= 20:
        print("They should be introduced to teen, coming of age, young adult movies, like: ")

    elif your_age == 21 or your_age <= 40:
        print("They should be introduced to young adult, new adult, coming of age, historical movies, like: ")

    elif your_age == 41 or your_age <= 60:
        print("They should be introduced to new adult, historical, magical, fantasy movies, like: ")

    elif your_age >= 61:
        print("They should be introduced to movies that make them feel young and vibrant, like: ")

    else:
        print("You picked the wrong thing bruh!")


movie_select()