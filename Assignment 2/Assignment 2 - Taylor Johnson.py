#Taylor Johnson
#Assignment 2
#August 29, 2016

#This function takes in three inputs: total distance, traveled distance, and time traveled
#Then it computes remaining distance, percentage of distance traveled,
#average speed, and estimated amount of hours to arrive
#Lastly, it outputs the computed values
def RoadTripCalculation():
    totalDistance, elapsedDistance, elapsedTime = eval(input("Enter the total distance, traveled distance, and time taken in minutes, separated by commas: "))

    percentageTraveled = elapsedDistance / totalDistance * 100
    remainingDistance = totalDistance - elapsedDistance
    elapsedTimeHours = elapsedTime / 60
    speed = elapsedDistance / elapsedTimeHours
    calculatedTime = remainingDistance / speed
    calculatedHours = calculatedTime // 1
    calculatedMinutes = calculatedTime * 60 % 60

    print("Percentage traveled ", percentageTraveled, " %")
    print("Remaining distance ", remainingDistance, " miles")
    print("Traveling time so far ", elapsedTimeHours, " hours")
    print("Speed ", speed, " mph")
    print("Time needed ", calculatedHours, " hours ", calculatedMinutes, " minutes ")
    input("Press enter to close program.")

RoadTripCalculation()
