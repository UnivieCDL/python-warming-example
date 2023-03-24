from warming.data.summary import Summary
from warming.plot.maps import World

def main():
    summary = Summary()
    world = World()
    world.show(summary.co2(), "CO2C")
    world.show(summary.ch4c(), "CH4C")
    world.show(summary.co2y(), "CO2Y")
    world.show(summary.ch4y(), "CH4Y")
    world.show(summary.n02y(), "NO2Y")


if __name__ == "__main__":
    main()