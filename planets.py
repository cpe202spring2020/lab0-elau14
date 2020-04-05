def weight_on_planets():
   # write your code here
   weight = float(input('What do you weigh on earth? '))
   mars_weight = weight * 0.38
   jupiter_weight = weight * 2.34
   print('\nOn Mars you would weigh %0.2f pounds.'
         '\nOn Jupiter you would weigh %0.2f pounds.'
         % (mars_weight, jupiter_weight))
   
if __name__ == '__main__':
   weight_on_planets()
