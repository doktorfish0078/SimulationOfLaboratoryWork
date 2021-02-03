import datetime


def creat_hash(a, p):
    s = 0
    k = 0
    z = 2 ** len(str(a))
    while a != 0:
        s += (a % 10) * p ** k
        s %= z
        k += 1
        a = a // 10
    buf = str(s)
    return 10**len(buf)*s+int(buf[::-1])


if __name__ == '__main__':
    now = datetime.datetime.now()
    # x = int(input())
    x = now.year
    if now.month >= 9:
        x = x*10 + 1
    else:
        x *= 10
    print(now)

    # print date in special format
    # print(x)

    saved = x
    l = len(str(x))
    x = x*(10**(l*2))+int(str(x)[::-1])*(10**l)+x
    x *= 1337

    # print crypted date
    # print(x)

    hahs = creat_hash(x, 228)
    step = saved % 100 % 3
    ans = ""
    i = 0
    while hahs != 0:
        i += 1
        curr = hahs % 10
        if i == step:
            step += 1
            i = 0
            abc = hahs % 10
            hahs = hahs // 10
            ans += chr(ord('a')+(curr*10+abc) % 26)
        ans += str(curr)
        hahs = hahs // 10
    final = [item for item in ans]
    k = 1
    dist = saved % 100 // 10
    while k + dist < len(final):
        final[k], final[k+dist] = final[k+dist], final[k]
        k += 1
    ans = ''
    for item in final:
        ans += item
    print("Your password: %s" % ans)
