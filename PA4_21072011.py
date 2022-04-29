# -*- coding: utf-8 -*-
import sys
from generators import *
import time
import random

all_lengths = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

class PRNG(object):
    def __init__(self, seed, length):
        self.seed = seed
        self.length = length

    def get_list_of_primes(self, max):
        primes = list()
        not_primes = list()
        for i in range(2, max + 1):
            if i not in not_primes:
                primes.append(i)
                for j in range(i * i, max + 1, i):
                    not_primes.append(j)
        return primes

    def are_coprimes(self, v1, v2):
        while v2 != 0:
            v1, v2 = v2, (v1 % v2)
        return v1 == 1

class BBS(PRNG):
    def __init__(self, seed, length):
        super(BBS, self).__init__(seed, length)

    def get_n(self):
        threshold = 7000
        primes = self.get_list_of_primes(10000)
        while True:
            p = random.choice(primes)
            if (((p % 4) == 3) and p > threshold):
                break
        while True:
            q = random.choice(primes)
            if (((q % 4) == 3) and q > threshold):
                if ((p != q) and self.are_coprimes(self.seed, p*q)):
                    break
        return p * q


    def generate_number(self, is_default=True):
        if is_default:
            p = 70891
            q = 85247
            n = p * q
        else:
            n = self.get_n()
        x = list()
        b = list()
        x.append((self.seed ** 2) % n)
        for i in range(self.length):
            x.append((x[-1]**2) % n)
            b.append(x[-1] % 2)

        self.generated_number = ''.join(map(str, b))
        return True


class LCG(PRNG):

    def __init__(self, length, m, a, c, x0):
        if m <= 0:
            raise ValueError('m must be > 0')
        if a <= 0:
            raise ValueError('a must be > 0')
        if a >= m:
            raise ValueError('a must be < m')
        if c < 0:
            raise ValueError('c must be >= 0')
        if c >= m:
            raise ValueError('c must be < m')
        if x0 < 0:
            raise ValueError('x0 must be >= 0')
        if c >= m:
            raise ValueError('x0 must be < m')
        self.m = m
        self.a = a
        self.c = c
        super(LCG, self).__init__(x0, length)

    def generate_number(self):
        x = list()
        x.append(self.seed)

        for i in range(self.length):
            x.append((self.a * x[-1] + self.c) % self.m)
        self.generated_number = ''.join(map(str,x))



class MT(PRNG):
    def __init__(self, seed):
        super(MT, self).__init__(seed)
        
if __name__ == "__main__":
    seed = 729150385
    for length in all_lengths:
        print('length:',length)
        start = time.time()
        print("----------------------------")
        bbs = BBS(seed, length)
        if bbs.generate_number():
            print(bbs.generated_number)
        else:
            print("Error generating number")
        end = time.time()
        print((end - start) * 1000)
        start = time.time()
        lcg = LCG(length, 32, 7, 0, seed)
        lcg.generate_number()
        print(lcg.generated_number)
        end = time.time()
        print((end - start) * 1000)
        print("----------------------------")
