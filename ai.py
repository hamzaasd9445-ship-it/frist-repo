# نظام تسجيل طلاب - franko version
# 7ot el code da w sh8'loh w 3del 3aleeh zy ma enta 3ayz

# list hat7ot fiha kol el talaba (kol taleb hayb2a dictionary)
students = []

# el program el asasy - hayesht8al continually 7atta y2ol 5rog
while True:
    # ========== el 2a'ema el ra2eesya ==========
    print("\n" + "="*40)
    print("          📚 4'war 3'er tanye")
    print("="*40)
    print("1. ➕ zyada taleb 7ded")
    print("2. 📋 3rd kol el talaba")
    print("3. 🔍 b7th 3an taleb")
    print("4. 📊 7sab mottawaset el daragat")
    print("5. 🚪 5rog")
    print("="*40)
    
    # nakhod ekhtyar el user
    choice = input("5tar mn 1: ")
    
    # ========== 1. zyada taleb 7ded ==========
    if choice == "1":
        print("\n--- zyada taleb ---")
        
        # nakhod data el taleb mn el user
        name = input("asem el taleb: ")
        age = input("sn el taleb: ")
        
        # nestakhdem try/except 3ashan net2aked en el grade raqm
        try:
            grade = float(input("darga el taleb: "))
            
            # na3mel dictionary lel taleb
            student = {
                "name": name,
                "age": age,
                "grade": grade
            }
            
            # nadeef el taleb lel list
            students.append(student)
            print(f"✅ tamt zyada {name}!")
            print(f"📊 3dad el talaba: {len(students)}")
            
        except ValueError:
            print("❌ 8alat: el degree lazem teb2a raqm!")
    
    # ========== 2. 3rd kol el talaba ==========
    elif choice == "2":
        print("\n--- kol el talaba ---")
        
        # law mafeesh talaba
        if len(students) == 0:
            print("❌ mafeesh talaba!")
        
        # law fe talaba
        else:
            print(f"3dad el talaba: {len(students)}")
            print("-" * 50)
            
            # handawer 3ala kol taleb
            for i, student in enumerate(students):
                print(f"{i+1}. {student['name']} | sn: {student['age']} | darga: {student['grade']}")
            
            print("-" * 50)
    
    # ========== 3. b7th 3an taleb ==========
    elif choice == "3":
        print("\n--- b7th 3an taleb ---")
        
        if len(students) == 0:
            print("❌ mafeesh talaba!")
        
        else:
            search_name = input("aktob asem el taleb: ")
            found = False
            
            for student in students:
                if student['name'].lower() == search_name.lower():
                    print(f"✅ talb mawgood:")
                    print(f"   asem: {student['name']}")
                    print(f"   sn: {student['age']}")
                    print(f"   darga: {student['grade']}")
                    found = True
                    break
            
            if not found:
                print(f"❌ mafeesh taleb be asem '{search_name}'")
    
    # ========== 4. 7sab mottawaset el daragat ==========
    elif choice == "4":
        print("\n--- mottawaset el daragat ---")
        
        if len(students) == 0:
            print("❌ mafeesh talaba!")
        
        else:
            total = 0
            
            for student in students:
                total = total + student['grade']
            
            average = total / len(students)
            
            print(f"📊 4'war el daragat: {total}")
            print(f"📊 3dad el talaba: {len(students)}")
            print(f"📊 el mottawaset: {average:.2f}")
            
            if average >= 90:
                print("🏆 7elw gedan!")
            elif average >= 80:
                print("🥇 kwayes!")
            elif average >= 70:
                print("🥈 mazboot!")
            elif average >= 60:
                print("🥉 tamam!")
            else:
                print("⚠️ mo7tag t3bea!")
    
    # ========== 5. 5rog mn el program ==========
    elif choice == "5":
        print("\n👋 thx for use 4'war el talaba!")
        print("📚 bye bye!")
        break
    
    # ========== law ekhtar raqm 8alat ==========
    else:
        print("❌ 8alat! 5tar mn 1 le 5")

print("\n✅ 4'war wa2f")