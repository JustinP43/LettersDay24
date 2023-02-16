PLACEHOLDER = "[name]"

with open("./names.txt",mode="r") as names:
    list_of_names = names.readlines()
    
with open("./letter.docx",mode="r") as file:
    letter = file.read()
    for person in list_of_names:
        stripped_name = person.strip()
        new_letter = letter.replace(PLACEHOLDER,stripped_name)
        
        with open(f"letter_to_{stripped_name}.txt",mode = "w") as file:
            file.write(new_letter)




            
                

                
            