# with	Used to simplify exception handling

def writenote(note):
    with open("note.txt","w") as f:
        f.write(note)
    
    
note = writenote("Hello How are you")
        
        