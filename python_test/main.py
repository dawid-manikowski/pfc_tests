from time import sleep

def handler(robot_event):
  print(robot_event)
  print("Hello PowerFarm Cloudx3!")
  print("HABABABA")
  for i in range(100):
    sleep(1)
    print(f"I've been running for {i} seconds.")
