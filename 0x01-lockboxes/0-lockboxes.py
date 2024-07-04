#!/usr/bin/python3
'''LockBoxes Challenge'''

def canUnlockAll(boxes):
  """
  Checks if all the boxes can be opened using the keys provided.

  Args:
      boxes: A list of lists, where each inner list represents the keys found in a box.

  Returns:
      True if all boxes can be opened, False otherwise.
  """

  N = len(boxes)
  opened = [False] * N

  opened[0] = True

  while True:
    opened_something = False

    for i in range(N):
      if opened[i] or not boxes[i]:
        continue

      for key in boxes[i]:
        if not opened[key]:
          opened[key] = True
          opened_something = True
          break

    if not opened_something:
      break

  return all(opened)
