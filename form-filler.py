from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
import random
from termcolor import colored



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('') # survey link

time.sleep(2)

# district
distval = "PURNEA"
district = driver.find_element(By.CLASS_NAME, "QR-QID1")
district.send_keys(distval)

# subdivision
subdval = "ARARIA"
subdivision = driver.find_element(By.CLASS_NAME, "QR-QID2")
subdivision.send_keys(subdval)

# anchal
anchalval = "PALASI"
anchal = driver.find_element(By.CLASS_NAME, "QR-QID3")
anchal.send_keys(anchalval)

# development block
devblockval = " "
devblock = driver.find_element(By.CLASS_NAME, "QR-QID33")
devblock.send_keys(devblockval)

# revenue thana
revval = "ARARIA-contd."
rev = driver.find_element(By.CLASS_NAME, "QR-QID4")
rev.send_keys(revval)

# village id
print(colored("enter village id", "green"))
vilidval = input()
vilid = driver.find_element(By.CLASS_NAME, "QR-QID6")
vilid.send_keys(vilidval)

# village name
print(colored("enter village name", "yellow"))
vilnameval = input()
vilname = driver.find_element(By.CLASS_NAME, "QR-QID5")
vilname.send_keys(vilnameval)

# area 
print(colored("enter area in acres", "blue"))
areaval = input()
area = driver.find_element(By.CLASS_NAME, "QR-QID7")
area.send_keys(areaval)

# number of occupied house
print(colored("enter number of occupied house", "red"))
houseval = input()
house = driver.find_element(By.CLASS_NAME, "QR-QID8")
house.send_keys(houseval)

# households
print(colored("enter number of occupied households", "yellow"))
householdval = input()
household = driver.find_element(By.CLASS_NAME, "QR-QID30")
household.send_keys(householdval)

#population
print(colored("Enter total population", "blue"))
pop = input()
print(colored("Enter male population", "green"))
male = input()
female = int(pop) - int(male);
population = driver.find_element(By.CLASS_NAME, "QR-QID10-1")
population.send_keys(pop)
malepopulation = driver.find_element(By.CLASS_NAME, "QR-QID10-2")
malepopulation.send_keys(male)
femalepopulation = driver.find_element(By.CLASS_NAME, "QR-QID10-3")
femalepopulation.send_keys(female)

#scheduled caste
print(colored("Enter male sc", "cyan"))
malesc = input()
print(colored("Enter female sc", "magenta"))
femalesc = input()
driver.find_element(By.CLASS_NAME, "QR-QID12-1").send_keys(malesc)
driver.find_element(By.CLASS_NAME, "QR-QID12-2").send_keys(femalesc)


## random ##


# literate and educated person
malelit = int(int(male)/(random.randint(4,7)))
femalelit = int(int(female)/(random.randint(4,8)))
driver.find_element(By.CLASS_NAME, "QR-QID32-1").send_keys(malelit)
driver.find_element(By.CLASS_NAME, "QR-QID32-2").send_keys(femalelit)


# total workers
totalmale = int(int(male)/(random.randint(2,3)))
driver.find_element(By.CLASS_NAME, "QR-QID15-1").send_keys(totalmale)
totalfemale = int(int(female)/(random.randint(4,5)))
driver.find_element(By.CLASS_NAME, "QR-QID15-2").send_keys(totalfemale)

# cultivator
malecul = int(int(totalmale)/(random.randint(2,3)))
driver.find_element(By.CLASS_NAME, "QR-QID16-1").send_keys(malecul)
femalecul = int(int(totalfemale)/3)
driver.find_element(By.CLASS_NAME, "QR-QID16-2").send_keys(femalecul)

# agriculture
maleag = random.randint(9, int(malecul))
driver.find_element(By.CLASS_NAME, "QR-QID17-1").send_keys(maleag)
femaleag = random.randint(0, int(femalecul))
driver.find_element(By.CLASS_NAME, "QR-QID17-2").send_keys(femaleag)

# mining
malemining = random.randint(4, int(int(malecul)/2))
driver.find_element(By.CLASS_NAME, "QR-QID31-1").send_keys(malemining)
femalemining = random.randint(0, int(int(femalecul)/2))
driver.find_element(By.CLASS_NAME, "QR-QID31-2").send_keys(femalemining)

# household industry
maleh = random.randint(0, int(int(malemining)/2))
driver.find_element(By.CLASS_NAME, "QR-QID19-1").send_keys(maleh)
femaleh = random.randint(0, int(int(femalemining)/2))
driver.find_element(By.CLASS_NAME, "QR-QID19-2").send_keys(femaleh)

# non workers
print(colored("Enter Male non workers", "yellow"))
malenon = input()
driver.find_element(By.CLASS_NAME, "QR-QID29-1").send_keys(malenon)
print(colored("Enter female non workers", "blue"))
femalenon = input()
driver.find_element(By.CLASS_NAME, "QR-QID29-2").send_keys(femalenon)


print(colored("Submit? 'Y' OR 'N' ", "white", "on_green"))
submission = input()
if(submission == 'Y'):
    driver.find_element(By.CLASS_NAME, "NextButton").click()
else:
    time.sleep(10)

time.sleep(1000)