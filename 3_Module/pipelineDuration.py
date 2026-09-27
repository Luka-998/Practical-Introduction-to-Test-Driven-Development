# Pipeline duration function
import inspect
def calculate_duration(start,end):
    if not isinstance(start,(int,float)) or not isinstance(end,(int,float)):
        raise TypeError
    if start > end:
        raise ValueError
    if start == end:
        return 0

    return end - start

if __name__ == '__main__':
    z = calculate_duration(112,112)
