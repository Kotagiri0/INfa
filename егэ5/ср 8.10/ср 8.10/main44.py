


ans = '0123456789ABCDEFGHI'
print(len(ans))
for x in ans:

    x1 = int(f'98{x}79641',19)
    x2 = int(f'36{x}14',19)
    x3 = int(f'73{x}4', 19)
    if((x1+x2+x3)%18 == 0):
        print(x, (x1+x2+x3)/18)


x1 = int(f'98I79641',19)
x2 = int(f'36I14',19)
x3 = int(f'73I4',19)
print(x, (x1+x2+x3)/18)
