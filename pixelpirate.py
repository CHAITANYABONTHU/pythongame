import random

# Create grid and place ship, treasure, obstacle
grid = [['🌊']*5 for _ in range(5)]
ship, treasure = [2, 2], [random.randint(0,4), random.randint(0,4)]
obstacle = [random.randint(0,4), random.randint(0,4)]

while obstacle == ship or obstacle == treasure: 
    obstacle = [random.randint(0,4), random.randint(0,4)]

score = 0
print("PIXEL PIRATE\nFind treasure with WASD! (Q to quit)\nAvoid obstacles (⛔)!")

while True:
    print(f"\nScore: {score}")
    for y in range(5):
        for x in range(5):
            if [x, y] == ship:
                print('🚢', end='')
            elif [x, y] == treasure:
                print('💰', end='')
            elif [x, y] == obstacle:
                print('⛔', end='')
            else: 
                print('🌊', end='')
        print()

    if ship == treasure:
        score += 1
        treasure = [random.randint(0,4), random.randint(0,4)]
        while treasure == obstacle: treasure = [random.randint(0,4), random.randint(0,4)]

    if ship == obstacle:
        print("\nYou hit an obstacle! Game Over!")
        break

    cmd = input("Move: ").lower()
    if cmd == 'q': break
    if cmd == 'w' and ship[1] > 0: ship[1] -= 1
    if cmd == 'a' and ship[0] > 0: ship[0] -= 1
    if cmd == 's' and ship[1] < 4: ship[1] += 1
    if cmd == 'd' and ship[0] < 4: ship[0] += 1

print(f"\nFinal Score: {score}")