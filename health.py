import os
global name, gender, age, weight, height, itype

# def cls():
#     os.system('cls' if os.name=='nt' else 'clear')

# cls()

############################## Auxilary Funcions ###############################################
STEPS_TO_METRES = 0.75

def week_stats(dist_in_metres, time_in_seconds):
    
    metrics = {}
    award = 0

    for i in range(len(dist_in_metres) - 1, -1, -1):
        if dist_in_metres[i] == 0:
            award += 1
            dist_in_metres.pop(i)
            time_in_seconds.pop(i)

    speed_in_ms = [dist_in_metres[i]/time_in_seconds[i] for i in range(len(dist_in_metres))]
    metrics["max_speed"] = round(max(speed_in_ms), 2)
    metrics["max_dist"] = round(max(dist_in_metres), 2)
    metrics["min_speed"] = round(min(speed_in_ms), 2)
    metrics["min_dist"]= round(min(dist_in_metres), 2)
    metrics["avg_speed"] = round(sum(speed_in_ms)/len(speed_in_ms), 2)
    metrics["avg_dist"] = round(sum(dist_in_metres)/len(dist_in_metres), 2)

    return metrics, award

def month_stats(weeks_list):

    metrics = {}
    award = True
    count = 0
    result = 0

    for i in range(4):
        if weeks_list[i][1] > 2:
            count = 0
        else:
            count += 1
            result = max(result, count)
    
    if result < 2:
        award = False

    metrics["max_speed"] = max([weeks_list[i][0]["max_speed"] for i in range(4)])
    metrics["max_dist"] = max([weeks_list[i][0]["max_dist"] for i in range(4)])
    metrics["min_speed"] = min([weeks_list[i][0]["min_speed"] for i in range(4)])
    metrics["min_dist"]= min([weeks_list[i][0]["min_dist"] for i in range(4)])
    metrics["avg_speed"] = round(sum([weeks_list[i][0]["avg_speed"] for i in range(4)])/4, 2)
    metrics["avg_dist"] = round(sum([weeks_list[i][0]["avg_dist"] for i in range(4)])/4, 2)

    return metrics, award, result

def quadmonth_stats(months_list):

    metrics = {}
    award = True
    count = 0
    result = 0

    for i in range(4):
        if months_list[i][1] == False:
            count = 0
        else:
            count += 1
            result = max(result, count)
    
    if result < 2:
        award = False

    metrics["max_speed"] = max([months_list[i][0]["max_speed"] for i in range(4)])
    metrics["max_dist"] = max([months_list[i][0]["max_dist"] for i in range(4)])
    metrics["min_speed"] = min([months_list[i][0]["min_speed"] for i in range(4)])
    metrics["min_dist"]= min([months_list[i][0]["min_dist"] for i in range(4)])
    metrics["avg_speed"] = round(sum([months_list[i][0]["avg_speed"] for i in range(4)])/4, 2)
    metrics["avg_dist"] = round(sum([months_list[i][0]["avg_dist"] for i in range(4)])/4, 2)

    return metrics, award, result

def read_input_file(identify):

    check = True
    dist_in_metres = []
    time_in_seconds = []
    with open("data.txt", "r") as file:
        for line in file:
            if not line.strip():
                continue
            s, t = line.split(",")[1:]
            s = int(s) * STEPS_TO_METRES
            t = t.split(":")
            t = 3600 * int(t[0]) + 60 * int(t[1]) + int(t[2])
            dist_in_metres.append(s)
            time_in_seconds.append(t)
    
    if identify == "w":
        if len(dist_in_metres) != 7:
            check = False

    elif identify == "m":
        if len(dist_in_metres) != 28:
            check = False

    elif identify == "q":
        if len(dist_in_metres) != 112:
            check = False

    return dist_in_metres, time_in_seconds, check

######################################## Implementation ###############################################

def basic_details():
    global name, gender, age, weight, height, bmi
    print("Welcome to The Health Tracker APP\n")
    print("Please provide the following details:\n")
    name = input("Name: ")
    gender  = input("\nGender: ")
    age  = int(input("\nAge(Years): "))
    try:
        metric = input("\nDo You want to use the Metric System? Y or N\n")

        if metric.lower() == "n":
            print("\nUsing FPS System")
            weight  = int(input("\nWeight(pounds): "))
            height  = int(input("\nHeight(inches): "))

            weight = int(weight * 0.453592)
            height = int(height * 2.54)

        elif metric.lower() == "y":
            print("\nUsing Metric System")
            weight  = int(input("\nWeight(kg): "))
            height  = int(input("\nHeight(cms): "))

        else:
            assert(False)

        height = height/100
        assert(weight != 0)
        assert(height != 0)
    except:
        print("\nPlease enter valid height and weight input. TRY AGAIN\n\n")
        basic_details()

    bmi = round(weight/(height)**2, 2)
    choose_input_type()

def choose_input_type():
    global itype
    print("\n\nDo you wish to enter weekly(w), monthly(m), or Quad-Monthly(q) data?")
    itype = input("Please choose either w, m or q as above. NOTE: Keep the data ready in data.txt file\n")
    
    if (itype not in ["w", "m", "q"]):
        print("\nPlease enter valid input. TRY AGAIN\n")
        choose_input_type()


def print_basic():
    global name, bmi
    # cls()
    print(f"Hi {name}")
    print(f"\nYour BMI is {bmi}. ")

    if bmi <= 18.5:
        print("Try to put on some weight!!\n")

    elif bmi >= 24.9:
        print("Try to lose on some weight!!\n")

    else:
        print("Your BMI is in healthy range!!\n")

def weekly():

    dist_in_metres, time_in_seconds, check = read_input_file("w")
    
    if check == False:
        print("\nPlease make sure complete data according to the chosen option is present in input.txt")
        print("\nCorrect input and restart the program")
        exit()

    metrics, award = week_stats(dist_in_metres, time_in_seconds)
    
    print_basic()
    print("\nYour weekly achievement is as follows:")
    print(f"\nYour fastest speed: { metrics['max_speed'] * 18/5} km/h")
    print(f"\nYour slowest speed: { metrics['min_speed'] * 18/5} km/h")
    print(f"\nYour longest distance: { metrics['max_dist']/1000} km")
    print(f"\nYour shortest distance: { metrics['min_dist']/1000} km")
    print(f"\nYour weekly average speed: { metrics['avg_speed'] * 18/5} km/h")
    print(f"\nYour weekly average distance is: { metrics['avg_dist']/ 1000} km")

    if award == 0:
        print("\nCongratulations! You have got a 7/7 award this week!\n")

    else:
        print("\nNo Awards this week, as there are breaks in the schedule!\n")


def monthly():
    
    dist_in_metres, time_in_seconds, check = read_input_file("m")
    
    if check == False:
        print("\nPlease make sure complete data according to the chosen option is present in input.txt")
        print("\nCorrect input and restart the program")
        exit()
        

    weeks_list = []

    for i in range(4):
        week_dist = dist_in_metres[i*7: i*7 + 7]
        week_time = time_in_seconds[i*7: i*7 + 7]
        weeks_list.append(week_stats(week_dist, week_time))

    metrics, award, result = month_stats(weeks_list)
    print_basic()
    print("\n*****************************************\n")
    print("Your monthly achievement is as follows:")
    print(f"\nYour fastest speed: { metrics['max_speed'] * 18/5} km/h")
    print(f"\nYour slowest speed: { metrics['min_speed'] * 18/5} km/h")
    print(f"\nYour longest distance: { metrics['max_dist']/1000} km")
    print(f"\nYour shortest distance: { metrics['min_dist']/1000} km")
    print(f"\nYour monthly average speed: { metrics['avg_speed'] * 18/5} km/h")
    print(f"\nYour monthly average distance is: { metrics['avg_dist']/ 1000} km")

    if award:
        print(f"\nCongrats! You have got {result} 7/7 award for this month\n")
    else:
        print(f"\nThere is no award this month, since you had no consecutive 7/7 weeks\n")

def quadmonth():

    dist_in_metres, time_in_seconds, check = read_input_file("q")
    
    if check == False:
        print("\nPlease make sure complete data according to the chosen option is present in input.txt")
        print("\nCorrect input and restart the program")
        exit()

    months_list = []

    for i in range(4):
        month_dist = dist_in_metres[i*28: i*28 + 28]
        month_time = time_in_seconds[i*28: i*28 + 28]
        weeks_list = []
        for i in range(4):
            week_dist = dist_in_metres[i*7: i*7 + 7]
            week_time = time_in_seconds[i*7: i*7 + 7]
            weeks_list.append(week_stats(week_dist, week_time))

        months_list.append(month_stats(weeks_list))

    metrics, award, result = quadmonth_stats(months_list)
    print_basic()
    print("\n*****************************************\n")
    print("Your quad-month achievement is as follows:")
    print(f"\nYour fastest speed: { metrics['max_speed'] * 18/5} km/h")
    print(f"\nYour slowest speed: { metrics['min_speed'] * 18/5} km/h")
    print(f"\nYour longest distance: { metrics['max_dist']/1000} km")
    print(f"\nYour shortest distance: { metrics['min_dist']/1000} km")
    print(f"\nYour quad-month average speed: { metrics['avg_speed'] * 18/5} km/h")
    print(f"\nYour quad-month average distance is: { metrics['avg_dist']/ 1000} km")

    if award:
        print(f"\nCongrats! You have got {result} M/M awards for this period\n")
    else:
        print(f"\nThere is no award this period, since you had no consecutive M/M months\n")


if __name__ == "__main__":
    try:
        basic_details()

    except:
        print("\nSorry, you have provided invalid input, please try again\n")
        basic_details()

    if itype == "w":
        weekly()

    elif itype == "m":
        monthly()

    elif itype == "q":
        quadmonth()

    temp = input("\nPress enter to exit")