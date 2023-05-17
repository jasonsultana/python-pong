class Utils:
    @staticmethod
    def angle_to_pixels(angle, velocity): 
        if angle <= 90:
            res = Utils.top_to_right(angle, velocity)
            return (res[0], 0 - res[1])
        
        elif angle > 90 and angle <= 180:
            return Utils.right_to_top(angle - 90, velocity)
        
        elif angle > 180 and angle <= 270:
            res = Utils.top_to_right(angle - 180, velocity)
            return (0 - res[0], res[1])
        
        elif angle > 270:
            res = Utils.right_to_top(angle - 270, velocity)
            return (0 - res[0], 0 - res[1])

    # the higher the angle, the less the object is moving vertically and the more the object is moving horizontally
    @staticmethod
    def top_to_right(angle, velocity):
        ratio = angle / 90
        yAmount = velocity * (1 - ratio)
        xAmount = velocity - yAmount

        return (xAmount, yAmount)
    
    # the higher the angle, the less the object is moving horizontally and the more the object is moving vertically
    @staticmethod
    def right_to_top(angle, velocity):
        ratio = angle / 90
        xAmount = velocity * (1 - ratio)
        yAmount = velocity - xAmount

        return (xAmount, yAmount)
