def add_match(matches):
    runs = int(input("Enter runs sscored :"))
    balls = int(input("Enetr balls faced :"))
    matches.append({"runs":runs,"balls":balls})

def batting_average(matches):
    total_runs = sum(match["runs"] for match in matches)
    return total_runs/len(matches)

def strike_rate(matches):
    total_runs = sum(match["runs"] for match in matches)
    total_balls = sum(match["balls"] for match in matches)
    return (total_runs / total_balls)*100

def best_score(matches):
    return max(match["runs"] for match in matches)

def consistancy(matches):
    avg = batting_average(matches)
    count = 0

    for match in matches:
        if match["runs"] >= avg:
            count+= 1

    return count 

def main():
    matches = []

    while True:
        print("\ncricket stats analyzer\n")
        print("1.add match stats")
        print("2.batting average")
        print("3.strike rate ")
        print("4.best score")
        print("5.consistant matches")
        print("6.Exit")

        choice = int(input("Enter your choice :"))

        if choice == 1:
            add_match(matches)
        elif choice == 2:
            if len(matches) == 0:
                print("no data available ")
            else:
                print("Batting average :",round(batting_average(matches),2))
        elif choice == 3:
            if len(matches) == 0:
                print("no data available")
            else:
                print("Bating strike rate :",round(strike_rate(matches),2))
        elif choice == 4:
            if len(matches) == 0:
                print("no data available")
            else:
                print("Best score :",round(best_score(matches),2))
        elif choice == 5:
            if len(matches) == 0:
                print("no data available")
            else:
                print("consistant matches :",consistancy(matches))
        elif choice == 6:
            print("Existing.....")
            break
        else:
            print("invalid choice !")

main()
