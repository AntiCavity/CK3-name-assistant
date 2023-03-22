import openai
import creds
import customtkinter

openai.api_key = creds.API_KEY
model = 'text-davinci-003'

'''Here is the  backend'''


def flavorize():

    language = langAns.get()

    location = provinceAns.get()

    prompt = 'How would someone who speaks %s pronounce and spell %s using the latin alphabet?' %(language, location)

    if language or location == '':
        retLabel.configure(text="Please fill out both entries")
    

    else:
        response = openai.Completion.create(
            prompt=prompt,
            model=model,
            max_tokens=1000,
            temperature=0.8,
    
        )


        for result in response.choices:
            retLabel.configure(text=result.text)

'''Here is the frontend'''

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")    #here is the size of the interface
root.title("CK3 Name Assistant")

    
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label=customtkinter.CTkLabel(master=frame, text="CK3 Name Assistant", font = ("Roboto", 24))
label.pack(pady=12,padx=10)

provinceAns = customtkinter.CTkEntry(master=frame, placeholder_text="Location")
provinceAns.pack(pady=12,padx=10)

langAns = customtkinter.CTkEntry(master=frame, placeholder_text="Language") 
langAns.pack(pady=12,padx=10)

button = customtkinter.CTkButton(master=frame, text="Generate Name", command=flavorize)
button.pack(pady=12,padx=10)

retLabel = customtkinter.CTkLabel(master=frame, text='', font = ("Roboto", 14))
retLabel.pack()

root.mainloop()

    
