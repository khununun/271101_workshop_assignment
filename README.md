หลักการทำงานของ Code "OpenCV Fingers"

ในส่วนนี้เป็นการเรียกใช้ Library
![image](https://user-images.githubusercontent.com/68842142/209473374-d6a9c7cb-4355-450c-9bf9-de12d0bfedb9.png)
 
ในส่วนนี้เป็นการอ่านค่าที่ได้จากตัวกล้องด้วยการใช้ OpenCV และ mediapipe 
![image](https://user-images.githubusercontent.com/68842142/209473190-e8c2f86e-42d2-467e-bac9-7b5ad42430ac.png)

ในส่วนนี้เป็นการนำค่าที่อ่านได้จากส่วนด้านบนมาเก็บไว้ในตัวแปรต่างที่สร้างขึ้นมาต่างส่วนต่างๆของมือตามรูปด้านล่าง
![image](https://user-images.githubusercontent.com/68842142/209473152-cb7563f3-0714-4565-8bd3-42792cdc1caf.png)
![image](https://user-images.githubusercontent.com/68842142/209472959-817a08de-3e62-43b4-ae78-34a550159150.png)

ในส่วนนี้เป็นการนำตัวแปรที่เก็บค่ามาแล้วมาใช้ในการคำนวณหาตำแหน่งของนิ้วมือแต่ละนิ้วโดยหลักการทำงานของนิ้วโป้งจะแตกต่างจากนิ้วอื่นเพราะนิ้วโป้งเป็นนิ้วที่เมื่อหุบนิ้วแล้วแกนที่จะนำมาใช้ได้เป็นแกน X 
ต่างจากนิ้วอื่นเมื่อหุบนิ้วแล้วแกนที่จะนำมาใช้ได้เป็นแกน Y ทำให้นิ้วโป้งจะต้องมีการจำแนกก่อนว่าเป็นมือซ้ายหรือมือขวาด้วยการนำค่าของนิ้วโป้ง(cx4)กับค่าของนิ้วก้อย(cx20)มาหาตำแหน่งซ้ายขวา
![image](https://user-images.githubusercontent.com/68842142/209473398-f2b2bc58-0915-4463-9c86-7d1a20126523.png)

