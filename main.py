# Fortune teller

user_name = raw_input("What is your name?")
if user_name == "Alex":
    print "Hi", user_name
    
else: 
    print "nice to meet you", user_name
    
curiosities = raw_input("What curiosities bring your here?")

if curiosities == "future":
    print "The cristal ball will tell us about your"  , curiosities
  
else:
        print "The crystal ball will lead the way"
import random
color_types = ['red' ,'yellow' , 'blue' ,'white']

print " Is your favorite color... hmmm... green?"

fav_color = ("green")

if fav_color == "green":
    print "Yes!!!"
    print "that's my favorite color too."

if fav_color != random.choice(color_types):
 
    print " However, " +  random.choice(color_types) , "is a prettier color"
    
## The fortune teller is going to read the user 5 fortunes.
    
print " My dear friend, the crystal ball is ready to share the secrets of your fortunes for you."
print "I can see ..."
print " You have been rewarded with 5 fortunes."


fortune_1 = "A feather in the hand is better than a bird in the air."
fortune_2 = "A friend asks only for your time not your money."
fortune_3 = "A new perspective will come with the new year"
fortune_4 = "A pleasant surprise is waiting for you."
fortune_5 = "A truly rich life contains love and art in abundance."

if user_name.startswith("A"): 
    print fortune_1