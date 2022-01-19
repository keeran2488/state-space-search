def heuristic(current, goal):
    h_value = 0
    for i in range(4):
        if(current[i] == goal[i]):
            h_value = h_value + i
        else:
            h_value = h_value - i
    return h_value

def main():
    current = ['B','A','C','D']
    goal = ['A','B','C','D']
    print("The current state is: ", end=" ")
    for i in current:
        print(i, end=" ")
    print("")
    h_value = heuristic(current, goal)
    print("The heuristic value of current state is: "+ str(h_value))
    

if __name__ == '__main__':
    main()