# This project was created to help me find another DNA's pair or mRNA's pair

import tkinter as tk

# Process


def finddnamrna():
    user_inp = input1.get()
    # 1
    pre_dna = user_inp.replace("A", "4").replace("T", "1").replace(
        "U", "1").replace("G", "2").replace("C", "3")
    prem_rna = user_inp.replace("A", "5").replace("T", "1").replace(
        "U", "1").replace("G", "2").replace("C", "3")
    # 2
    dna = pre_dna.replace("1",
                          "A").replace("2",
                                       "C").replace("3",
                                                    "G").replace("4", "T")
    m_rna = prem_rna.replace("1",
                             "A").replace("2",
                                          "C").replace("3",
                                                       "G").replace("5", "U")
    # Outout
    outputDNA.configure(text=dna)
    outputmRNA.configure(text=m_rna)


#UI
window = tk.Tk()

window.title('Converter')
window.minsize(width=400, height=200)

title_label = tk.Label(
    master=window,
    text=
    'Insert DNA or mRNA under here \n !!This thing works only with upper character !!',
    font="Time 14")
title_label.pack()

input1 = tk.Entry(master=window, font="Time 14", width=50)
input1.pack()

find_button = tk.Button(master=window, text='Find', command=finddnamrna)
find_button.pack()

DNA_lbl = tk.Label(master=window, text='\nDNA', font="Time 14")
DNA_lbl.pack()

outputDNA = tk.Label(master=window)
outputDNA.pack()

mRNAlbl = tk.Label(master=window, text='\nmRNA', font="Time 14")
mRNAlbl.pack()

outputmRNA = tk.Label(master=window)
outputmRNA.pack()

window.mainloop()
