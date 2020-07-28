"""
The template of the main script of the machine learning process
"""

class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False
        self.ball_pre_x =0
        self.ball_pre_y =0
        self.window_width = 200
        self.platform_y = -1 

    def find_ball_landing_location(self , ballx , bally , direction ):
        if 'U' in direction:
            return -1
        
        if 'R' in direction:
            landing = False
            while not landing :
                diff = self.window_width-ballx
                targety = bally+diff
                # if targety > 
                # continue

    def get_ball_direction( self , ballx , bally ):
        ball_direction = ''
        if ballx > self.ball_pre_x :
                ball_direction='R'
        else:
            ball_direction='L'

        if bally > self.ball_pre_y :
            ball_direction='D'+ball_direction
        else:
            ball_direction='U'+ball_direction

        # print( '>> ball direction : ', ball_direction )
        return ball_direction


    def update(self, scene_info):
        """
        Generate the command according to the received `scene_info`.
        """
        # Make the caller to invoke `reset()` for the next round.
        if (scene_info["status"] == "GAME_OVER" or
            scene_info["status"] == "GAME_PASS"):
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            print('ball height : ',scene_info['ball'][1])
            command = "SERVE_TO_LEFT"
        else:
            # command = "MOVE_LEFT"        
            ballx = scene_info["ball"][0]
            bally = scene_info["ball"][1]
            pwidth = 40
            px = scene_info["platform"][0]+pwidth/2
            py = scene_info["platform"][0]
            

            # find the lowest bound
            lowest = 0
            for bks in scene_info['bricks']:
                # print('     bk : ', bks[1])
                if bks[1] > lowest:
                    lowest = bks[1]
            # print( '>> lowest : ', lowest )


            # find the orientation of the ball
            if bally>lowest :
                ball_direction = self.get_ball_direction(  ballx , bally)
                
            
            

            # set ball position
            self.ball_pre_x = ballx
            self.ball_pre_y = bally


            if ballx < px :
                command = "MOVE_LEFT"
            else:
                command = "MOVE_RIGHT"
                



        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
