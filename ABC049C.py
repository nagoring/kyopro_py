def run():
    S = input()
 #   words = ["dreamer","dream","eraser","erase"]
    if(len(S) < 5):
        return False

    S = S.replace("eraser", "")
    S = S.replace("erase", "")
    S = S.replace("dreamer", "")
    T = S.replace("dream", "")
    if len(T) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    result = run()
    if result == True:
        print("YES")
    else:
        print("NO")
