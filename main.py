from warming.data.summary import Summary
from warming.plot.maps import World

def main():
    summary = Summary()
    world = World()
    world.show(summary.co2(), "CO2C")
    world.show(summary.ch4c(), "CH4C")

if __name__ == "__main__":
    main()