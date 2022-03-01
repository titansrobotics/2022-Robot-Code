import wpilib
from wpilib.drive import DifferentialDrive
from constants import LEFT_MOTOR_ID, RIGHT_MOTOR_ID


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        left_motor = wpilib.PWMVictorSPX(LEFT_MOTOR_ID)
        right_motor = wpilib.PWMVictorSPX(RIGHT_MOTOR_ID)
        self.drive = DifferentialDrive(left_motor, right_motor)
        print('Robot initialized...')


if __name__ == '__main__':
    wpilib.run(Robot)
