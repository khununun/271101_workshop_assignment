import cv2
import mediapipe as mp
import pyfirmata

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        # print("Input is an integer number. Number = ", val)
        bv = True
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            # print("Input is a float  number. Number = ", val)
            bv = True
        except ValueError:
            # print("No.. input is not a number. It's a string")
            bv = False
    return bv            

cport = input('Enter the camera port: ')
while not (check_user_input(cport)):
    print('Please enter a number not string')
    cport = input('Enter the camera port: ')

comport = input('Enter the arduino board COM port: ')
while not (check_user_input(comport)):
    print('Please enter a number not string')
    comport = input('Enter the arduino board COM port: ')

board=pyfirmata.Arduino('COM'+comport)  
led_1=board.get_pin('d:13:o') #Set pin to output
led_2=board.get_pin('d:12:o')
led_3=board.get_pin('d:11:o')
led_4=board.get_pin('d:10:o')
led_5=board.get_pin('d:9:o')

video=cv2.VideoCapture(int(cport))

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

##################################################################

                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 2:
                    id2 = int(id)
                    cx2 = cx
                if id == 8:
                    id8 = int(id)
                    cy8 = cy
                if id == 6:
                    id6 = int(id)
                    cy6 = cy
                if id == 16:
                    id16 = int(id)
                    cy16 = cy
                if id == 14:
                    id14 = int(id)
                    cy14 = cy
                if id == 12:
                    id12 = int(id)
                    cy12 = cy
                if id == 10:
                    id10 = int(id)
                    cy10 = cy
                if id == 20:
                    id20 = int(id)
                    cy20 = cy
                if id == 18:
                    id18 = int(id)
                    cy18 = cy
                if id == 20:
                    id20 = int(id)
                    cx20 = cx

####################################################Thumb#########################################################

            if cx4 < cx20:
                if cx4 < cx2: 
                        led_1.write(1)
                else:
                    led_1.write(0)
            elif cx4 > cx20:
                if cx4 > cx2: 
                        led_1.write(1)
                else:
                    led_1.write(0)

####################################################Index#########################################################

            if cy8 < cy6:
                led_2.write(1)
            else:
                led_2.write(0)

####################################################Middle########################################################

            if cy12 < cy10:
                led_3.write(1)
            else:
                led_3.write(0)

####################################################Ring##########################################################

            if cy16 < cy14:
                led_4.write(1)
            else:
                led_4.write(0)

####################################################pinky#########################################################

            if cy20 < cy18:
                led_5.write(1)
            else:
                led_5.write(0)


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    k=cv2.waitKey(1)
    if k==ord('q'):  #press "q" to exit programe
        break
video.release()
cv2.destroyAllWindows()