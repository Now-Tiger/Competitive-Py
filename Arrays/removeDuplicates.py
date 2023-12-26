#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
from __future__ import annotations

def brute_force_remove_duplicates(array: list) -> set[int]:
  return set(array)

def remove_duplicates(array: list[int]) -> int:
  i = 0
  for j in range(1, len(array)):
    if array[i] != array[j]:
      i += 1
      array[i] = array[j]
  return i + 1


def main() -> None:
  array = [2, 2, 4, 5, 5, 4, 8]
  print(array)
  k = remove_duplicates(array)
  for i in range(k):
    print(array[i], end=", ")


if __name__ == '__main__':
    main()
