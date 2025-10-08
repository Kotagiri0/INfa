for x in range(0,19):
    r = x
    if(r>=10):
        r = chr(x-10+65)

    x1 = int(f'98{r}79641',19)
    x2 = int(f'36{r}14',19)
    x3 = int(f'73{r}4', 19)
    if((x1+x2+x3)%18 == 0):
        print(x, (x1+x2+x3)/18)


x1 = int(f'98I641',19)
x2 = int(f'36I',19)
x3 = int(f'73I4',19)
print(x, (x1+x2+x3)/18)
