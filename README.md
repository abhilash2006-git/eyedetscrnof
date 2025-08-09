<img width="3188" height="1202" alt="frame (3)" src="https://github.com/user-attachments/assets/517ad8e9-ad22-457d-9538-a9e62d137cd7" />


# Automated Screen Blackout via Eye Detection 


## Basic Details:
This project uses OpenCV for real-time eye detection from a webcam feed and Tkinter to create a full-screen black overlay window. The screen turns completely black when eyes are detected, and returns to normal when eyes are not detected.

### Team Name:Hairfallmeter


### Team Members
- Team Lead: Vysakh P Chandran - College of Engineering Trivandrum
- Member 2: Abhilash A -College of Enginnering Trivandrum


### Project Description
This is an eye detection–based real-time screen blackout system using OpenCV and Haar Cascade classifiers that can detect eyes and faces from a webcam stream, with optional image processing using CLAHE for improvements in accuracy in changing lighting conditions. On detecting eyes, a fullscreen black Tkinter window is shown over every other application, mimicking the effect of turning the screen off, and it becomes invisible when no eyes are detected.

### The Problem 
Think you’re spending too much time staring at your screen? Well, here’s a brilliantly unnecessary fix — a program that literally hides everything the moment you dare to look at it. Perfect for those who want to “use” their computer without actually seeing it

### The Solution
By combining OpenCV’s face-and-eye detection magic with a fullscreen black Tkinter window, the moment your eyes meet the webcam, your screen turns black. Stop looking, and it graciously returns, letting you wonder why you even opened it in the first place.



## Technical Details
### Technologies/Components Used
For Software:
Languages used: Python
Frameworks used: Tkinter (for GUI and fullscreen black screen display)
Libraries used: OpenCV (for face & eye detection), NumPy (for array operations)
Tools used: Haar Cascade Classifiers (for detecting faces and eyes), CLAHE (Contrast Limited Adaptive Histogram Equalization for better detection in varying lighting) and chatgpt/gemini for clean response.

For Hardware:
Built-in Camera present in laptop for eye detection

### Implementation
For Software:
# Installation
pip install opencv-python numpy tkinter

# Run
python eye_detection_black_screen.py

### Project Documentation
For Software:
This project uses OpenCV's Haar Cascade Classifiers to detect human faces and eyes through a webcam feed in real-time. When eyes are detected, a fullscreen black Tkinter window appears, simulating a “screen-off” effect without actually locking the system. If no eyes are detected, the black screen disappears, revealing the normal display. NumPy is used for basic array operations, and CLAHE is applied to improve contrast for better detection under different lighting conditions.

# Screenshots 

<img width="1920" height="1080" alt="Screenshot (4)" src="https://github.com/user-attachments/assets/55fe3649-7768-4e31-b9bf-56f2c691f871" />
Sample image of our Project code.


<img width="1920" height="1080" alt="Screenshot (7)" src="https://github.com/user-attachments/assets/a49cc049-8050-41ad-bd55-98a36123fe14" />
Screen stays on when the person isn't facing the screen.


<img width="1920" height="1080" alt="Screenshot (11)" src="https://github.com/user-attachments/assets/0ac43f18-45c7-48fd-8e95-8d5364dc1984" />
Screen stays turned on when the person's eyes are closed.



<img width="1920" height="1080" alt="Screenshot (9)" src="https://github.com/user-attachments/assets/21c18747-4ed0-4511-afbd-aabea8af6650" />
Rest of the cases where the webcam detects the users eyes and the screen turns black.



# Diagrams
<img width="1024" height="1536" alt="Uselessss Diagram" src="https://github.com/user-attachments/assets/700295e3-ca10-4e24-8b93-d2bf28d8a385" />



### Project Demo
# Video
since the video even after compressing 2 times it's still greater than 10 mb, a video ofn the name "Screen Recording 2025-08-09 155752 (1).mp4" is provided in the repository
Explanation:

The first 10 seconds showcase the entire code. Then, it shows a user looking away from the screen, so the screen remains visible. Next, the user closes their eyes while facing the screen; the screen stays visible since the eyes are closed. After positioning themselves facing the camera, the user opens their eyes, which is detected by OpenCV, causing the entire screen to turn black and making it impossible to work on the system while looking at the screen. The user then repeats this cycle looking in the opposite direction. Finally, the camera is physically disconnected, resulting in no eyes being detected, and the system returns to normal operation.



## Team Contributions
opencv implementation - Abhilash A

tkinter implementation - Vysakh P Chandran

Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--25-25?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)


