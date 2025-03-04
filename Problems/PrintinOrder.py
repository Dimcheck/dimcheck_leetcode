'''
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}

The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third().
Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().
We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering.
The input format you see is mainly to ensure our tests' comprehensiveness.

Example 1:
Input: nums = [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously.
The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.

Example 2:
Input: nums = [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.

Constraints:
    nums is a permutation of [1, 2, 3].
'''
from threading import Thread, Event
from typing import Callable


class Foo:
    def __init__(self):
        self.events = (Event(), Event())

    def first(self, printFirst: Callable[[], None]) -> None:
        printFirst("first")
        self.events[0].set()

    def second(self, printSecond: Callable[[], None]) -> None:
        self.events[0].wait()
        printSecond("second")
        self.events[1].set()

    def third(self, printThird: Callable[[], None]) -> None:
        self.events[1].wait()
        printThird("third")


def thread_manager(threads: list[Thread]):
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def print_data(args: str) -> None:
    print(args)


foo = Foo()
thread_manager((
    Thread(target=foo.first, args=(print_data,)),
    Thread(target=foo.second, args=(print_data,)),
    Thread(target=foo.third, args=(print_data,)),
))


