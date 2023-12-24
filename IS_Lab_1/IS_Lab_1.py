from owlready2 import *

ont = get_ontology("http://example.org/KnowledgeBase")

with ont:
    class Scientist(Thing):
        def __repr__(self): return self.Name
    class Name(Scientist >> str, FunctionalProperty): pass
    class year_of_birth(Scientist >> int, FunctionalProperty): pass
    class number_of_works(Scientist >> int, FunctionalProperty): pass
    class place_of_work(Scientist >> str, FunctionalProperty): pass
    class scientific_interest(Scientist >> str, FunctionalProperty): pass  

    class is_younger_than(ObjectProperty, TransitiveProperty):
        domain = [Scientist]
        range = [Scientist]
    
    class is_smarter_than(ObjectProperty, TransitiveProperty):
        domain = [Scientist]
        range = [Scientist]
        
    class is_colleague_of(ObjectProperty):
        domain = [Scientist]
        range = [Scientist]
        
    class is_doctor_of_sciences(Scientist >> bool, FunctionalProperty): pass
    
    class is_efficient_scientist(Scientist >> bool, FunctionalProperty): pass

    r_younger = Imp()
    r_younger.set_as_rule("""Scientist(?s1), year_of_birth(?s1, ?y1), Scientist(?s2), year_of_birth(?s2, ?y2), greaterThan(?y1, ?y2) -> is_younger_than(?s1, ?s2)""")
     
    r_smarter = Imp()
    r_smarter.set_as_rule("""Scientist(?s1), number_of_works(?s1, ?n1), Scientist(?s2), number_of_works(?s2, ?n2), greaterThan(?n1, ?n2) -> is_smarter_than(?s1, ?s2)""")

    r_colleague = Imp()
    r_colleague.set_as_rule("""Scientist(?s1), place_of_work(?s1, ?p1), scientific_interest(?s1, ?i1), Name(?s1, ?n1), Scientist(?s2), place_of_work(?s2, ?p2), scientific_interest(?s2, ?i2), Name(?s2, ?n2), equal(?p1, ?p2), equal(?i1, ?i2), notEqual(?n1, ?n2) -> is_colleague_of(?s1, ?s2)""")
    
    r_doctor = Imp()
    r_doctor.set_as_rule("""Scientist(?s), number_of_works(?s, ?n), greaterThanOrEqual(?n, 10) -> is_doctor_of_sciences(?s, true)""")

    r_efficient = Imp()
    r_efficient.set_as_rule("""Scientist(?s), is_doctor_of_sciences(?s, ?d), year_of_birth(?s, ?y), equal(?d, true), greaterThanOrEqual(?y, 1983) -> is_efficient_scientist(?s, true)""")
    
    scientist1 = Scientist("Scientist1")
    scientist1.Name = "Scientist1"
    scientist1.year_of_birth = 1980
    scientist1.number_of_works = 8
    scientist1.place_of_work = "University1"
    scientist1.scientific_interest = "Informatics"
    
    scientist2 = Scientist("Scientist2")
    scientist2.Name = "Scientist2"
    scientist2.year_of_birth = 1965
    scientist2.number_of_works = 10
    scientist2.place_of_work = "University2"
    scientist2.scientific_interest = "Mathematics"
    
    scientist3 = Scientist("Scientist3")
    scientist3.Name = "Scientist3"
    scientist3.year_of_birth = 1987
    scientist3.number_of_works = 12
    scientist3.place_of_work = "University1"
    scientist3.scientific_interest = "Informatics"    

    scientist4 = Scientist("Scientist4")
    scientist4.Name = "Scientist4"
    scientist4.year_of_birth = 1972
    scientist4.number_of_works = 7
    scientist4.place_of_work = "University2"
    scientist4.scientific_interest = "Mathematics"
    
    scientist5 = Scientist("Scientist5")
    scientist5.Name = "Scientist5"
    scientist5.year_of_birth = 1960
    scientist5.number_of_works = 15
    scientist5.place_of_work = "University1"
    scientist5.scientific_interest = "Physics"

    sync_reasoner_pellet(infer_property_values = True, infer_data_property_values = True)
    
    ont.save("Ont.rtf")

    print()
    print("Scientist1 is younger than:", scientist1.is_younger_than)
    print("Scientist1 is smarter than:", scientist1.is_smarter_than)
    print("Scientist1 is colleague of:", scientist1.is_colleague_of)
    print()
    print("Scientist2 is younger than:", scientist2.is_younger_than)
    print("Scientist2 is smarter than:", scientist2.is_smarter_than)
    print("Scientist2 is colleague of:", scientist2.is_colleague_of)
    print()
    print("Scientist3 is younger than:", scientist3.is_younger_than)
    print("Scientist3 is smarter than:", scientist3.is_smarter_than)
    print("Scientist3 is colleague of:", scientist3.is_colleague_of)
    print()
    print("Scientist4 is younger than:", scientist4.is_younger_than)
    print("Scientist4 is smarter than:", scientist4.is_smarter_than)
    print("Scientist4 is colleague of:", scientist4.is_colleague_of)
    print()
    print("Scientist5 is younger than:", scientist5.is_younger_than)
    print("Scientist5 is smarter than:", scientist5.is_smarter_than)
    print("Scientist5 is colleague of:", scientist5.is_colleague_of)
    print()

    print("Doctors of sciences: ", end = '')
    if scientist1.is_doctor_of_sciences:
        print(scientist1.Name + " ", end = '')
    if scientist2.is_doctor_of_sciences:
        print(scientist2.Name + " ", end = '')
    if scientist3.is_doctor_of_sciences:
        print(scientist3.Name + " ", end = '')
    if scientist4.is_doctor_of_sciences:
        print(scientist4.Name + " ", end = '')
    if scientist5.is_doctor_of_sciences:
        print(scientist5.Name, end = '')
    
    print()

    print("Efficient scientists: ", end = '')
    if scientist1.is_efficient_scientist:
        print(scientist1.Name + " ", end = '')
    if scientist2.is_efficient_scientist:
        print(scientist2.Name + " ", end = '')
    if scientist3.is_efficient_scientist:
        print(scientist3.Name + " ", end = '')
    if scientist4.is_efficient_scientist:
        print(scientist4.Name + " ", end = '')
    if scientist5.is_efficient_scientist:
        print(scientist5.Name, end = '')
    
    print()