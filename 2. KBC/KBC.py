def answer(UserAns, ANS, price):
    if UserAns == ANS:
        print("SAHI JAWAB!!!")
        return 0
    else:
        print("Aapka safar yahi tak tha Aap jite hai: Rs", price)
        return 1

def cases():
    print("\nDo you want to continue playing?")
    print("Press 0 to Continue\nPress 1 to EXIT")

print("\nWelcome to KAUN BANEGA CROREPATI!!!")
print("\nNOTE: Giving a Foul ANSWER will instantly make you disqualify.")

temp = 0
play = 1
price = 0

while temp <= 17:
    if play == 1:
        print("\nPehla prashna aapki computer screen pe:")
        print("Q-1 Price = Rs 1,000")
        print("Which of these is not a programming language?")
        print("1. Python\n2. Java\n3. Ruby\n4. Jupiter")
        UserAns = int(input("Uttar de:- "))
        ansret = answer(UserAns, 4, price)
        if ansret == 1:
            break 
        price =   1000  
        play = play + 1 
    cases()
    temp = int(input("Enter your choice: "))
    if temp == 1:
        print("Aapka safar yahi tak tha Aap jite hai: Rs", price)
        break
    if play == 2:
        print("\nDusra prashna aapki computer screen pe:")
        print("Q-2 Price = Rs 2,000")
        print("What is the capital of India?")
        print("1. Mumbai\n2. Delhi\n3. Kolkata\n4. Chennai")
        UserAns = int(input("Uttar de:- "))
        ansret = answer(UserAns, 2, price)
        if ansret == 1:
            break
        price = 2000
        play = play + 1  
    cases()
    temp = int(input("Enter your choice: "))
    if temp == 1:
        print("Aapka safar yahi tak tha Aap jite hai: Rs", price)
        break
    if play == 3:
        print("\nTeesra prashna aapki computer screen pe:")
        print("Q-3 Price = Rs 3,000")
        print("Which planet is known as the Red Planet?")
        print("1. Mars\n2. Venus\n3. Jupiter\n4. Saturn")
        UserAns = int(input("Uttar de:- "))
        ansret = answer(UserAns, 1, price)
        if ansret == 1:
            break
        price =  3000
        play = play + 1  
    cases()
    temp = int(input("Enter your choice: "))
    if temp == 1:
        print("Aapka safar yahi tak tha Aap jite hai: Rs", price)
        break
    if play == 4:
        print("\nchautha prashna aapki computer screen pe:")
        print("Q-4 Price = Rs 5,000")
        print("Lord Hanuman is Avatar of?")
        print("1. Lord Brahma\n2. Lord Shiva\n3. Lord Vishnu\n4. None of the Above")
        UserAns = int(input("Uttar de:- "))
        ansret = answer(UserAns, 2, price)
        if ansret == 1:
            break
        price =   5000
        play = play + 1  
    cases()
    temp = int(input("Enter your choice: "))
    if temp == 1:
        print("Aapka safar yahi tak tha Aap jite hai: Rs", price)
        break
    if play == 5:
        print("\nPachva prashna aapki computer screen pe:")
        print("Q-5 Price = Rs 10,000")
        print("What is the square root of 144?")
        print("1. 10\n2. 16\n3. 14\n4. 12")
        UserAns = int(input("Uttar de:- "))
        ansret = answer(UserAns, 4, price)
        if ansret == 1:
            break
        price =   10000
        play = play + 1  
    cases()
    temp = int(input("Enter your choice: "))
    if temp == 1:
        print("Aapka safar yahi tak tha Aap jite hai: Rs", price)
        break
    if play == 6:
        print("\nchattha prashna aapki computer screen pe:")
        print("Q-6 Price = Rs 20,000")
        print("Who wrote the national anthem of India?")
        print("1. Rabindranath Tagore\n2. Mahatma Gandhi\n3. Jawaharlal Nehru\n4. Subhash Chandra Bose")
        UserAns = int(input("Uttar de:- "))
        ansret = answer(UserAns, 1, price)
        if ansret == 1:
            break
        price =   20000
        play = play + 1  
    cases()
    temp = int(input("Enter your choice: "))
    if temp == 1:
        print("Aapka safar yahi tak tha Aap jite hai: Rs", price)
        break
    if play == 7:
        print("\nSatva prashna aapki computer screen pe:")
        print("Q-7 Price = Rs 40,000")
        print("What is the chemical symbol for water?")
        print("1. H2SO4\n2. O2\n3. CO2\n4. H2O")
        UserAns = int(input("Uttar de:- "))
        ansret = answer(UserAns, 4, price)
        if ansret == 1:
            break
        price =   40000
        play = play + 1  
    cases()
    temp = int(input("Enter your choice: "))
    if temp == 1:
        print("Aapka safar yahi tak tha Aap jite hai: Rs", price)
        break
    if play == 8:
        print("\nAathva prashna aaki computer screen pe:")
        print("Q-8 Price = Rs 80,000")
        print("Which sport is associated with the term \"Love\"?")
        print("1. Cricket\n2. Badminton\n3. Tennis\n4. Hockey")
        UserAns = int(input("Uttar de:- "))
        ansret = answer(UserAns, 3, price)
        if ansret == 1:
            break
        price =   80000
        play = play + 1  
    cases()
    temp = int(input("Enter your choice: "))
    if temp == 1:
        print("Aapka safar yahi tak tha Aap jite hai: Rs", price)
        break
    if play == 9:
        print("\nNavva prashna aapki computer screen pe:")
        print("Q-9 Price = Rs 1,60,000")
        print("Which country gifted the Statue of Liberty to the United States?")
        print("1. Germany\n2. France\n3. Italy\n4. England")
        UserAns = int(input("Uttar de:- "))
        ansret = answer(UserAns, 2, price)
        if ansret == 1:
            break
        price =   160000
        play = play + 1  
    cases()
    temp = int(input("Enter your choice: "))
    if temp == 1:
        print("Aapka safar yahi tak tha Aap jite hai: Rs", price)
        break
    if play == 10:
        print("\nDasva prashna aapki computer screen pe:")
        print("Q-10 Price = Rs 3,20,000")
        print("What does \"HTTP\" stand for in website addresses?")
        print("1. HyperText Transfer Protocol\n2. HyperText Transfer Path\n3. High Transfer Text Protocol\n4. Hyper Transfer Text Path")
        UserAns = int(input("Uttar de:- "))
        ansret = answer(UserAns,1, price)
        if ansret == 1:
            break
        price =   320000
        play = play + 1  
    cases()
    temp = int(input("Enter your choice: "))
    if temp == 1:
        print("Aapka safar yahi tak tha Aap jite hai: Rs", price)
        break
    if play == 11:
        print("\nIggarva prashna aapki computer screen pe:")
        print("Q-11 Price = Rs 6,40,000")
        print("Who was the first Indian woman to win a Nobel Prize?")
        print("1. Indira Gandhi\n2. Mother Teresa\n3. Sarojini Naidu\n4. Amartya Sen")
        UserAns = int(input("Uttar de:- "))
        ansret = answer(UserAns, 2, price)
        if ansret == 1:
            break
        price =   640000
        play = play + 1  
    cases()
    temp = int(input("Enter your choice: "))
    if temp == 1:
        print("Aapka safar yahi tak tha Aap jite hai: Rs", price)
        break
    if play == 12:
        print("\nBarva prashna aapki computer screen pe:")
        print("Q-12 Price = Rs 12,50,000")
        print("Which gas is most abundant in Earth's atmosphere?")
        print("1. Oxygen\n2. Nitrogen\n3. Carbon Dioxide\n4. Hydrogen")
        UserAns = int(input("Uttar de:- "))
        ansret = answer(UserAns, 2, price)
        if ansret == 1:
            break
        price =   1250000
        play = play + 1  
    cases()
    temp = int(input("Enter your choice: "))
    if temp == 1:
        print("Aapka safar yahi tak tha Aap jite hai: Rs", price)
        break
    if play == 13:
        print("\nTeerva prashna aapki computer screen pe:")
        print("Q-13 Price = Rs 25,00,000")
        print("Which is the largest mammal in the world?")
        print("1. Elephant\n2. Blue Whale\n3. Giraffe\n4. Orca")
        UserAns = int(input("Uttar de:- "))
        ansret = answer(UserAns, 2, price)
        if ansret == 1:
            break
        price =   2500000
        play = play + 1  
    cases()
    temp = int(input("Enter your choice: "))
    if temp == 1:
        print("Aapka safar yahi tak tha Aap jite hai: Rs", price)
        break
    if play == 14:
        print("\nChaudva prashna aapki computer screen pe:")
        print("Q-14 Price = Rs 50,00,000")
        print("Who is known as the Missile Man of India?")
        print("1. C. V. Raman\n2. Homi Bhabha\n3. A. P. J. Abdul Kalam\n4. Vikram Sarabhai")
        UserAns = int(input("Uttar de:- "))
        ansret = answer(UserAns, 3, price)
        if ansret == 1:
            break
        price =   5000000
        play = play + 1  
    cases()
    temp = int(input("Enter your choice: "))
    if temp == 1:
        print("Aapka safar yahi tak tha Aap jite hai: Rs", price)
        break
    if play == 15:
        print("\nPandrava prashna aapki computer screen pe:")
        print("Q-15 Price = Rs 75,00,000")
        print("Which Indian city is also known as the \"Pink City\"?")
        print("1. Udaipur\n2. Jodhpur\n3. Jaipur\n4. Ahmedabad")
        UserAns = int(input("Uttar de:- "))
        ansret = answer(UserAns, 3, price)
        if ansret == 1:
            break
        price =   7500000
        play = play + 1  
    cases()
    temp = int(input("Enter your choice: "))
    if temp == 1:
        print("Aapka safar yahi tak tha Aap jite hai: Rs", price)
        break
    if play == 16:
        print("\nSoolva prashna aapki computer screen pe:")
        print("Q-16 Price = Rs 10000000")
        print("What is the SI unit of electric current?")
        print("1.  Volt\n2. Ampere\n3. Ohm\n4. Watt")
        UserAns = int(input("Uttar de:- "))
        ansret = answer(UserAns, 2, price)
        if ansret == 1:
            break
        price =   10000000
        play = play + 1  
    cases()
    temp = int(input("Enter your choice: "))
    if temp == 1:
        print("Aapka safar yahi tak tha Aap jite hai: Rs", price)
        break
    if play == 17:
        print("\nSaatrava prashna aapki computer screen pe:")
        print("Q-17 Price = Rs 75000000")
        print("Who was the first person to step on the moon?")
        print("1. Neil Armstrong\n2. Buzz Aldrin\n3. Yuri Gagarin\n4. Michael Collins")
        UserAns = int(input("Uttar de:- "))
        ansret = answer(UserAns, 1, price)
        if ansret == 1:
            break
        price =   75000000
        play = play + 1  
    cases()
    temp = int(input("Enter your choice: "))
    if temp == 1:
        print("Aapka safar yahi tak tha Aap jite hai: Rs", price)
        break