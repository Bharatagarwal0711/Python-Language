#1
'''
Integer(int) = Stores +ve as well -ve Number without Decimal
Float(float) = Integers with Decimal 
String = Sequence of characters bounded with quotes
Boolean(bool) = Stores only 2 values , either true or false

'''


#2
name = "Bharat Agarwal"
age = 21
town = "Pilani"

print(f"Name : {name}")
print(f"Age : {age}")
print(f"Town : {town}")


#3
name = input("Enter Your Name : ")
print(f"Name = {name.upper()} ")
print(f"Number of Character = {len(name)}")


#4

'''
    Five Commonly used String Methods :

    String are Immutable in python, so majority functions returns the new string

    1. str.upper() - returns string with all character in uppercase
    2. str.lower() - returns string with all character in lowercase
    3. str.count("substring") - returns the number of substring present in the given string
    4. str.find("substring") - returns the index of the first occurence of Substring , if not found then returns -1
    5. str.replace("old","new") - returns the string where all old values are replaced with new value
'''

str = "Bharat Agarwal"
print(f"upper() --> {str.upper()}")
print(f"lower() --> {str.lower()}")
print(f"count() --> {str.count("bharat")}")  # case Doesn't Match that's why return 0
print(f"find() --> {str.find("Bharat")}")
print(f"replace() --> {str.replace('a','z')}")


#5
lst = ["Apple","Strawberry","Guava","Litchi","Mango"]
print(lst)
print(f"First Element = {lst[0]}")
print(f"Last Element = {lst[-1]}")
print(f"Length of List = {len(lst)}")


#6
lst = [10, 20, 30, 40, 50]  
lst.append(60)
lst.remove(20)
print(lst)


#7
'''
Aritifical Intelligence in simple words refers to a computer program or machine model that replicates Human brain.  
Artificial Intelligence is important because it helps machines perform tasks faster, more accurately, and often more efficiently than humans.

Application of AI 
1. ChatBots like chatGPT
2. Voice Assistant like Alexa/Bixby/Siri
3. Self Driving Cars 
4. Healthcare
5. Agriculture

'''

#8
'''
1.ChatGPT - Definitly a LLM. It understands questions and gives answers like humans do.
2.Google Maps route prediction - It predicts the best route using traffic and road data.
3.Calculator - Nope,Its not an example of AI as it only perform mathematical calculation based upon inputs given by the user. Technically its a static program
4.Netflix Recommendations - It suggests movies and serials based on your past search and watch history .
5.Alexa/Siri - They understand voice commands and answer questions. A Digital Assistant

'''

