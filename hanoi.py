#!/usr/bin/env python3

class HanoiStack:
    '''
    A stack used in the towers of hanoi problem
    meant as a stack of integers
    throws an error if an item to be added is bigger than the top
    '''
    def __init__(self):
        self._vals = []

    def push(self, val: int):
        '''
        Add an item to the top of the stack
        :val: the item to be added to the top
        throws an error if :val: is bigger than the top item
        '''
        if not self.is_empty() and self._vals[-1] < val:
            raise ValueError('cannot add a bigger item to the top of the stack')
        self._vals.append(val)

    def pop(self) -> int:
        '''
        Remove the top item from the stack
        throws an error if the stack is empty
        '''
        if self.is_empty():
            raise ValueError('Cannot pop from empty stack')
        return self._vals.pop()

    def is_empty(self) -> bool:
        '''returns true if the stack is empty'''
        return len(self._vals) == 0

    def __str__(self):
        '''Returns the stack as a string'''
        result = ''
        first = True
        for i in self._vals:
            if first:
                first = False
            else:
                result += ', '
            result += str(i)
        return result

def move_disks(n: int, src: HanoiStack, tmp: HanoiStack, dst: HanoiStack) -> int:
    '''
    Move disks from the tower of hanoi
    :n: number of disks to move
    :src: the source stack where the disks to move are
    :tmp: the temporary stack where the disks will be moved to temporarily
    :dst: the destination stack where the disks will be moved to finally
    :returns: number of moves taken
    '''
    if n == 0:
        return 0
    elif n == 1:
        dst.push(src.pop()) # move from source to destination
        return 1
    else:
        result = 1 # already at 1 beause of the move 2 lines below
        result += move_disks(n-1, src, dst, tmp)
        dst.push(src.pop()) # move from source to destination
        result += move_disks(n-1, tmp, src, dst)
        return result

def test_hanoi(n: int = 10):
    '''
    Test the hanoi problem and print results
    :n: number of disks to test
    '''
    s, t, d = (HanoiStack() for i in range(3))
    for i in reversed(range(n)):
        s.push(i)
    print('before:')
    print(f's: {s}')
    print(f't: {t}')
    print(f'd: {d}')
    print('-' * 50)
    print('after:')
    print('moves:', move_disks(n, s, t, d))
    print(f's: {s}')
    print(f't: {t}')
    print(f'd: {d}')

def main():
    '''driver code'''
    test_hanoi(10)

if __name__ == "__main__":
    main()
