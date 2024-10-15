class Buffalo():
    def __init__(self, arm_length=18.0, leg_length=18.0):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.number_eyes = 2
        self.has_tail = True
        self.is_furry = True
    def print_attributes(self):
        print(f'This animal has arms {self.arm_length} inches long. Its legs are {self.leg_length} inches long.')
        print(f'It has {self.number_eyes} eyes.')
        print(f'Does it have a tail? {self.has_tail}')
        print(f'Does it have fur? {self.is_furry}')
        
def main():
    instance = Buffalo()
    instance.print_attributes()
    
if __name__ == '__main__':
    main()