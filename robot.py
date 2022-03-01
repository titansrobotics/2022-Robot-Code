import wpilib
from wpilib.drive import DifferentialDrive


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        # left_motor = wpilib.
        # right_monitor = wpilib.
        # self.drive = DifferentialDrive()
        print('Code is running...')


if __name__ == '__main__':
    wpilib.run(Robot)
