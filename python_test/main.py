from time import sleep

def handler(robot_event):
  print(robot_event)
  print("Hello PowerFarm Cloudx2!")
  for i in range(100):
    sleep(1)
    print(f"I've been running for {i} seconds.")
