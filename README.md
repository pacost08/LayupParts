Task1: Airplane Control
    - Run Instructions:
        a. Requirements:
            i. Python 3.x
            ii. PyQt6: pip3 install PyQt6
            iii. Qt libaries: sudo apt-get install --reinstall qt5-qmake qtbase5-dev qtchooser qtbase5-dev-tools
            iv. X Server: https://vcxsrv.com/
        b. Run the Application: "python3 task1.py"
            i. Use the Yaw and Speed Sliders to adjust yaw and speed respectively
            ii. Use the keyboard shortcuts listed on screen to adjust yaw and speed as well
    - Trajectory Logic:
        a. Each update cycle (every 100 ms), the airplane's position is updated based on its current speed and yaw angle. The yaw angle is converted
        from degrees to radians. The movement along the x axis is dx = speed * cos(angle). The movement along the y axis is dy = speed * sin(angle).
        The plane's new position is updated using airplane_x += dx and airplane_y += dy.

Task2: Layup Sequence
    - Run Instructions:
        a. Requirements:
            i. matplotlib: pip3 install matplotlib
            ii. X Server
        b. Run the Application: "python3 task2.py"
    - Performance Evaluation:
        a. Measure the runtime of your implementation: 0.00797414779663086 seconds
            i. run time calculated in main function of task2.py
        b. Determine the time complexity of your solution: O(n)
            i. Each value of S(n) is calculated once and stored in a dictionary for future reference.
               When the result of a value is needed again, the result is performed in O(1).
        c. If possible, optimize the solution to reduce the computational overhead.
            i. An iterative approach reduces computational overhead of recursive calls.
            ii. The optimal, iterative solution is implemented in task2.py.
            iii. The recursive solution with memoization is commented out in task2.py
    - Explanation:
        a. Provide a short explanation of the time complexity of your algorithm. You should provide a plot
           of N vs Runtime to backup your reasoning.
           i. Each value of S(n) is calculated once and stored in a dictionary for future reference.
               When the result of a value is needed again, the result is performed in O(1).
           ii. N vs Runtime plot included in execution in task2.py
        b. Discuss any optimizations applied and how they impact the runtime.
           i. While the iterative and recursive approaches are both O(n), iterating reduces the
              overhead of recursion/stack maintenance. This can lead to lower memory usage for larger values
              of n. It also avoids stack overflow for large input values.