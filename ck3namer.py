import openai
import creds
import customtkinter

openai.api_key = creds.API_KEY
model = 'text-davinci-003'

'''Here is the  backend'''

def flavorize():

    language = input('What language does your character speak? ')

    location = input('What location do you wish to rename? ')

    prompt = 'How would someone who speaks %s pronounce and spell %s using the latin alphabet?' %(language, location)


    response = openai.Completion.create(
        prompt=prompt,
        model=model,
        max_tokens=1000,
        temperature=0.8,
    
    )

    for result in response.choices:
        print(result.text)
    

'''Here is the frontend'''

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")    #here is the size of the interface


    
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label=customtkinter.CTkLabel(master=frame, text="Login System or whateva", font = ("Roboto", 24))
label.pack(pady=12,padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12,padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*") 
entry2.pack(pady=12,padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=flavorize)
button.pack(pady=12,padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12,padx=10)

root.mainloop()

    
