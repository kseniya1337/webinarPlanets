from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

planets = [('Меркурий', 2.646, 'img/Mercury.jpg'),
           ('Венера', 1.104, 'img/Venus.jpg'),
           ('Марс', 2.661, 'img/Mars.jpg'),
           ('Юпитер', 0.423, 'img/Jupiter.jpg'),
           ('Сатурн', 1.087, 'img/Saturn.jpg'),
           ('Уран', 1.125, 'img/Uran.jpg'),
           ('Нептун', 0.889, 'img/Neptune.jpg')]

planets_names = []
for planet in planets:
    planets_names.append(planet[0])


def calculate_weigth(_):
    global photo
    weight = earth_weight_ent.get()
    planet_name = planets_list_box.get()
    for planet in planets:
        if planet_name == planet[0]:
            planet_img = Image.open(planet[2])
            photo = ImageTk.PhotoImage(planet_img)
            planet_canvas.itemconfig(planet_canvas_img, image=photo)
            if weight == '':
                result_lb['text'] = 'Вы не ввели вес'
            else:
                result_lb['text'] = 'Ваш вес на планете ' + planet[0] + ' равен ' + str(
                    round(float(weight) / planet[1], 1)) + ' кг'


window = Tk()
window.title('Калькулятор веса на разных планетах')
window.geometry('350x400+800+320')

earth_weight_lb = Label(window, text='Введите вес на планете Земля:', font='Arial 14')
earth_weight_lb.pack()

earth_weight_ent = Entry(window, font='Arial 12')
earth_weight_ent.pack()

choose_planet_lb = Label(window, text='Выберите планету:', font='Arial 14')
choose_planet_lb.pack()

planets_list_box = ttk.Combobox(window, state='readonly', values=planets_names, font='Arial 12')
planets_list_box.current(0)
planets_list_box.bind('<<ComboboxSelected>>', calculate_weigth)
planets_list_box.pack()

planet_canvas = Canvas(window, height=200, width=200)
planet_canvas_img = planet_canvas.create_image(0, 0, anchor='nw')
planet_canvas.pack()

result_lb = Label(window, font='Arial 12')
result_lb.pack()
window.mainloop()
