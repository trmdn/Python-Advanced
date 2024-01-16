from collections import deque

bullet_price = int(input())
mag_max = int(input())

bullets = deque([int(b) for b in input().split()])
locks = deque([int(l) for l in input().split()])

reward = int(input())

bullet_in_mag = mag_max
bullet_shot = 0

while bullets in locks:
    bullet = bullets.pop()
    lock = locks.popleft()
    
    if bullet <= lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(lock)
    
    bullet_in_mag -= 1
    bullet_shot += 1

    if bullet_in_mag == 0 and bullets:
        bullets_in_mag = mag_max if len(bullets) >= mag_max else len(bullets)
        print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    earned_money = reward - (bullet_price * bullet_shot)
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")