class MarsRovers(object):
	
	user_input = []    # to hold user's input of rover's initial position and instructions.                            
	x_corner = None    # to hold x co-ordinate of plateau's right upper corner.
	y_corner = None	   # to hold y co-ordinate of plateau's right upper corner. 
	
	
	"""Get the uppper-right co-ordinates of plateau from user, check if they are in correct and required format
			and return them. User is asked again to enter the co-ordinates if previous co-ordinates are in wrong format"""
	def get_corner(self):
		 
		while True:
			corner = raw_input('\nEnter the space-seperated upper-right co-ordinates of plateau  (X Y): ')
			if (len(corner.strip().split())!=2) or (('').join(corner.strip().split()).isdigit() == False):
				print "Wrong input! Two integer co-ordinates are required. \n"
				continue
			else: 
				return corner
	
	
	
	""" Check for the next instruction and change the location and/or orientation of the rover."""
	def act_as_per_instruction(self,instruction,current_location):
						
		placement=[(-1,0),(0,1),(1,0),(0,-1)]      	# all possible combinations of changes in a rover's location after one instruction.
		
		if instruction=='r':       
			return lambda x, y, orientation: (x, y, (orientation + 1) % 4)
		
		if instruction=='l':
			return lambda x, y, orientation: (x, y, (orientation - 1 + 4) % 4)
		
		if instruction=='m': 
			
			newX=current_location[0] + placement[current_location[2]][0] 
			newY=current_location[1] + placement[current_location[2]][1]
			
			#X co-ordinate of a rover can not be less than zero.
			if((current_location[0] + placement[current_location[2]][0])<0): 			    	
				newX=0
				
			#X co-ordinate of a rover can not go beyond given right-upper corner.	
			if((current_location[0] + placement[current_location[2]][0]) > self.x_corner):  	 
				newX=self.x_corner      
			
			#Y co-ordinate of a rover can not be less than zero.	
			if((current_location[1] + placement[current_location[2]][1])<0):				   
				newY=0
			
			#Y co-ordinate of a rover can not go beyond given right-upper corner.
			if((current_location[1] + placement[current_location[2]][1])>self.y_corner):     
				newY=self.y_corner
				
			
			return lambda x, y, orientation: (newX, newY, orientation)
		

	""" Iterate through the useer-specified instructions for each rover and change its position to get the final position."""	
	def get_final_position(self,user_input):
		
		final_position=[]
		reverse_direction = ['w','n','e','s']  		# all possible directions
		
		for i in range(1,len(user_input),2):        # get the starting position of each rover.
			user_input[i] = user_input[i].lower()
			user_input[i+1] = user_input[i+1].lower()
			current_position=[None]*3
			start_position = user_input[i].split()
			current_position[0],current_position[1],current_position[2]=int(start_position[0]),int(start_position[1]),start_position[2]
        
			current_position[2] = reverse_direction.index(current_position[2]) # convert the orientation into numerical form. 
			for j in range(len(user_input[i+1])):   # get the set of instructions for the current rover.
			
			    # decide the next as per the instruction.
				function = self.act_as_per_instruction(user_input[i+1][j],current_position)
				current_position = list(function(current_position[0],current_position[1],current_position[2]))
			
			current_position[2] = reverse_direction[current_position[2]]       # convert the orientation back into the string form.
			
			final_position.append(tuple(current_position))                     # save the rover's final position. 
		return final_position    



	
	"""Checks for the correctness of the rover's starting position specified by the user """	
	def check_position(self,rover_position):
		
		direction = ['n','s','e','w']  			# possible directions a rover can face
		rover_position = rover_position.strip().split()
		
		if(len(rover_position)!=3):   			#rover's starting position should have 3 parts (X,Y,Direction)
			print "Please enter 3 inputs."
			return False
			
		# rover's X and Y co-ordinates should be integers
		if((rover_position[0].isdigit() == False) or ( rover_position[1].isdigit() == False)):
			print "Either one or both the co-ordinates are not integer. Please enter rover's position again."
			return False
			
		# rover's X co-ordinate should be within specified plateau region	
		if((int(rover_position[0])>self.x_corner) or (int(rover_position[0])<0)):
			print "X co-ordinate is out of the plateau. Please enter rover's position again."
			return False
			
		# rover's Y co-ordinate should be within specified plateau region
		if((int(rover_position[1])>self.y_corner) or (int(rover_position[1])<0)):
			print "Y co-ordinate is out of the plateau. Please enter rover's position again."
			return False
			
		# rover's orientation should one of the specified directions.	
		if(rover_position[2].lower() not in direction):
			print "Rover's orientation is wrong. Please enter rover's position again."
			return False
			
		
		return True			# return true if all the above conditions are satisfied. 		
	
	
	""" Checks for the rover's movment instructions given by the user."""
	def check_instruction(self,instructions):
		moves = ['l','r','m']					# possible instructions that can be given to a rover to move
		
		if(set(instructions.lower()).issubset(set(moves))): # if the instrictions have only the specified moves.
			return True
		else: 
			print "Wrong instructions entered. Instructions should consist of L(l),R(r),M(m) only.Please enter instructions again. "
			return False
			
	""" Get the rover's starting position and the instruction from user to move the rover. """		
	def get_instruction(self):
		status = 'continue'
		
		while(True): 
		
			print "\nPlease enter at least one rover's initial position and orientation.[1 2 N 'OR' 3 3 E]"  
			print 'After entering initial position of atleast one rover, you can hit enter to exit or you can add for another rover also.\n'
			
			while(True):
				rover_position = raw_input("\nEnter rover's initial position(space-seperated):")
	
				if (rover_position==''):        				#users hit enter when they dont want to input another rover's position. 
					status = 'end' 
					break
				if(self.check_position(rover_position)): 		#check correctness for initial position, if its wrong ask user for it again.
					break
					
			if (status=='end'): 								#Done with all the inputs, exit the outer while loop. 
				break   
			
			else:
			
				self.user_input.append(rover_position)			# save the user's input about rover's position. 
			
			print 'Please enter instructions for this rover[LMLMLMLMM OR MMRMMRMRRM]'
			
			while(True):
				instruction = raw_input('Enter instructions for this rover:')
				if(self.check_instruction(instruction)):        # checking the correctness of instructions.
					break
        
			self.user_input.append(instruction) 

def main():

	mars_rovers = MarsRovers()

	corner = mars_rovers.get_corner()             # ask user for upper-right corner position of plateau.
	mars_rovers.user_input.append(corner)
 
	corner=corner.strip().split()
	mars_rovers.x_corner = int(corner[0])
	mars_rovers.y_corner = int(corner[1])

	mars_rovers.get_instruction()	              # ask user for rover's position and instructions.

	final_possition = mars_rovers.get_final_position(mars_rovers.user_input)

	print "\nFinal position of rovers:"
	for position in final_possition:                         # this has final positions of all the rovers.
		print position
			
			
if __name__ == '__main__':
	main()			
