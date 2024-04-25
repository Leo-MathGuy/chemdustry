import imageio.v3 as iio
import numpy as np


def gen(name, disp, expl, flam, colr):
    canTmpl = iio.imread("templates/template-gas-can.png")

    if not all((name, disp, expl, flam, colr)):
        print("No")
        print((name, disp, expl, flam, colr))
        exit(1)

    color = tuple(int(colr[i : i + 2], 16) for i in (0, 2, 4)) + (255,)

    def procPix(pix):
        return pix if list(pix) != [0, 0, 0, 255] else color

    can = np.array(
        list(
            map(
                lambda row: tuple(map(procPix, row)),
                canTmpl,
            )
        ),
        np.uint8,
    )

    iio.imwrite("sprites/items/canisters/" + name + "-compressed.png", can)

    with open("content/liquids/" + name + ".hjson", "w") as f:
        f.write("type: Liquid\n")
        f.write("name: " + disp + "\n")
        f.write("gas: true\n")
        f.write("barColor: " + colr + "\n")
        f.write("explosiveness: " + expl + "\n")
        f.write("flammability: " + flam + "\n")

    with open("content/items/canisters/" + name + "-compressed.hjson", "w") as f:
        f.write("type: Item\n")
        f.write("name: Compressed " + disp + "\n")
        f.write("buildable: false\n")
        f.write("explosiveness: " + str(float(expl) + 0.5 * 1.3) + "\n")
        f.write("flammability: " + str(float(flam) / 2) + "\n")


if __name__ == "__main__":
    name = input("Gas Name: ")
    disp = input("Display Name: ")
    expl = input("Explosiveness: ")
    flam = input("Flammability: ")
    colr = input("Color: ")
    gen(name, disp, expl, flam, colr)
