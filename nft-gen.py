print("No")
exit(1)

import creategas

for i in range(0, 256, 8):
    for j in range(0, 256, 8):
        print(f"{100*((i/256) + (j/256/32))}%")
        for k in range(0, 256, 8):
            name = "nft-" + "%02x%02x%02x" % (i, j, k)
            creategas.gen(name, name, "0", "0", "%02x%02x%02x" % (i, j, k))
