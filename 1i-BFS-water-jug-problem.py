"""
Question 1:
Write a program in C/C++/Java to implement DFS/BFS on water jug problem. Given a 4 - liter jug filled with water & an empty 3 - liter Jug, how can one obtain exactly 2 liters in 4 liters jug. There is no measuring mark on any of them.

- Solution using BFS

Submitted by:
Name - Prajwal Chaudhary
CRN - 017-356

Submitted to - Krishna Bikram Shah

"""




from collections import deque

def BFS(jug1, jug2, target):
    m = {}
    isSolvable = False
    path = []

    # Queue to maintain states
    q = deque()

    # Initializing with initial state
    q.append((0,0))

    while (len(q) > 0):
        # Current state
        u = q.popleft()

        # If this state is already visited
        if((u[0], u[1]) in m):
            continue

        # Doesn't met jug constraints
        if((u[0] > jug1 or u[1] > jug2 or u[0] < 0 or u[1] < 0)):
            continue

        # Filling the vector for constructing the solution
        path.append([u[0], u[1]])

        # Marking current state as visited
        m[(u[0], u[1])] = 1

        # If we reach solution state, put ans = 1
        if(u[0] == target or u[1] == target):
            isSolvable = True

            if(u[0] == target):
                if(u[1] != 0):
                    # Fill the final state
                    path.append([u[0], 0])
            else:
                if(u[0] != 0):
                    # Fill the final state
                    path.append([0, u[1]])

            # Print the solution path
            size = len(path)
            for i in range(size):
                print(f"({path[i][0]}, {path[i][1]}) ")
            break

        # If we have not reached final state
        # then, start developing intermediate states
        # to reach solution state

        q.append([u[0], jug2]) # Fill jug2
        q.append([jug1, u[1]]) # Fill jug1

        for poured_amount in range(max(jug1, jug2) + 1):
            # Pour water poured_amount from Jug2 to Jug1
            jug1_temp = u[0] + poured_amount
            jug2_temp = u[1] - poured_amount

            # Check if this state is possible or not
            if(jug1_temp == jug1 or (jug2_temp == 0 and jug2_temp >= 0)):
                q.append([jug1_temp, jug2_temp])

             # Pour water poured_amount from Jug1 to Jug2
            jug1_temp = u[0] - poured_amount
            jug2_temp = u[1] + poured_amount

            # Check if this state is possible or not
            if(jug2_temp == jug2 or (jug1_temp == 0 and jug1_temp >= 0)):
                q.append([jug1_temp, jug2_temp])

        # Empty Jug2
        q.append([jug1, 0])

        # Empty Jug1
        q.append([0, jug2])

    # No Solution exists if ans = 0
    if(not isSolvable):
        print("No solution found.")


# Main Function
if __name__ == '__main__':
    jug1, jug2, target = 4, 3, 2
    print("Path from initial state to solution state :")

    BFS(jug1, jug2, target)

            



