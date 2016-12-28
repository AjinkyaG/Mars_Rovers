# Mars_Rovers
This program does navigate rovers on mars and find their final positions.<br />
Programming language used is Python 2.7<br />
All the code is in MarsRovers.py file. <br />
To run the code, go to the files location on command prompt and execute the command 'python MarsRovers.py'.<br /><br />

After successfull run, first the user will be asked for Mars plateau's co-ordinates of right-upper corner with the help of get_corner() function.
This corner should consist of space-separated integers X and Y co-ordinates.E.g. 7 8. User will be asked again for input if the previous input is in wrong format. The left-bottom corner is assumed to be at 0,0.<br />

Next in get_instruction() function, user will be asked for rover's starting position on plateau. This starting position should in the form of space-seperated values
of rover's X, Y co-ordinates and its initial orientation i.e. the direction it is facing.
The integers X and Y co-ordinates should be within the above specified plateau's region, else user will be asked for the position again. 
Also the orientation can take one of the values W(w), S(s), N(n), E(e) only. <br />E.g 1 2 N or 3 3 E<br />
After this the user will be asked for rover's navigation instructions. These instruction shold be a sequence of commands like L(l) for rotating to Left, R(r) for rotating to Right or M(m) to move one grid ahed in same direction. Instruction example is LMLMLMLMM or MMRMMRMRRM<br />
If the instructions are in wrong format then user will be asked for them again.<br />
User can enter the initial position and navigation instructions for more than one rover also.
To end the input user need to hit enter when asked for rover's initial position.<br />

act_as_per_instruction(self,instruction,current_location) function navigates the rover as per the instruction provided by the user.
It handles the situation where the rover tries to go out of the plateau's region. If a rover tries to navigate out of the plateau, then it remains on the plateau's edge but can not go beyond that.



