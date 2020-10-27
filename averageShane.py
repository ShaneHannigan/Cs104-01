Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> numberOfTests = 0
score = 0
total = 0
average = 0.0
scoreCount = 0
numberOfTests = int(input("Enter the number of tests you want to average: "))
#repeat these 3 lines using a while loop until scoreCount = numberOfTests
while scoreCount < numberOfTests:
    score = int(input("Enter a score: "))
    scoreCount = scoreCount + 1
    total += score
average = total/scoreCount
print("The average is ",average)