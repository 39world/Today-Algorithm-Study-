## 프로그래머스 멀쩡한 사각형
from math import gcd
def solution(w,h):
    return w * h - (w + h - gcd(w, h))