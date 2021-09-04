# AI-trainer
Tired of changing gym buddies and having no one around to point out your wrong form  of exercise?
Cant afford a personal trainer and dont want some half-knowledge instructor to misguide you?
Want a trainer who counts each and every rep you done right without interferring or disturbing you?

Then here is your reliable new gym buddy (because If you cant afford something build one YOURSELF)

This is a python program that calculates the number of reps done in absolutely right form by estimating poses through plotting different landmarks defined in mediapipe framework and than tracking the user defined (##required_landmarks) landmarks and calculating the distance travelled by the points and then appending that information in a list that can be used to calculate the number of reps done for a particulaer exercise based on what points are marked and traced.   
##required_landmarks-- Values of the landmarks (https://google.github.io/mediapipe/solutions/pose.html) that can be used for calculation. For ex- For calculating no. of bicep curls done by right hand we need to trace the landmarks(12,14,16) i.e.(right_shoulder,right_elbow,right_wrist) so on and so forth.

Used Pycharm editor(community version) for writing code   
Interpreters Used:-    
opencv-python v-> 4.5.1.48     
mediapipe v-> 0.8.3.1     
numpy v-> 1.21.2

Shoutout to Murtaza Hasan of https://www.computervision.zone/ for helping
