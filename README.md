# Task1: Airplane Control
   ## Run Instructions:
   ### Requirements:
   - Python 3.x
   - PyQt6: ```pip3 install PyQt6```
   - Qt libaries: ```sudo apt-get install --reinstall qt5-qmake qtbase5-dev qtchooser qtbase5-dev-tools```
   - X Server: [VCXSRV](https://vcxsrv.com/)

   ### Run the Application: 
   - ```python3 task1.py```

   - Use the Yaw and Speed Sliders to adjust yaw and speed respectively
   - Use the keyboard shortcuts listed on screen to adjust yaw and speed as well
   ## Trajectory Logic:
   - Each update cycle (every 100 ms), the airplane's position is updated based on its current speed and yaw angle. The yaw angle is converted
        from degrees to radians. The movement along the x axis is dx = speed * cos(angle). The movement along the y axis is dy = speed * sin(angle).
        The plane's new position is updated using airplane_x += dx and airplane_y += dy.

# Task2: Layup Sequence
   ## Run Instructions:
   ### Requirements:
   - matplotlib: ```pip3 install matplotlib```
   - X Server: [VCXSRV](https://vcxsrv.com/)

   ### Run the Application: 
   - ```python3 task2.py```

   ## Performance Evaluation:
   - Measure the runtime of your implementation: 0.00797414779663086 seconds
       - Run time calculated in main function of task2.py
   - Determine the time complexity of your solution: O(n)
       - Each value of S(n) is calculated once and stored in a dictionary for future reference. When the result of a value is needed again, the result is performed in O(1).
   - If possible, optimize the solution to reduce the computational overhead.
        - An iterative approach reduces computational overhead of recursive calls.
        - The optimal, iterative solution is implemented in task2.py.
        - The recursive solution with memoization is commented out in task2.py
   ## Explanation:
   - Provide a short explanation of the time complexity of your algorithm. You should provide a plot of N vs Runtime to backup your reasoning.
       - Each value of S(n) is calculated once and stored in a dictionary for future reference. When the result of a value is needed again, the result is performed in O(1).
       - N vs Runtime plot included in execution in task2.py
   - Discuss any optimizations applied and how they impact the runtime.
       - While the iterative and recursive approaches are both O(n), iterating reduces the overhead of recursion/stack maintenance. This can lead to lower memory usage for larger values of n. It also avoids stack overflow for large input values.
