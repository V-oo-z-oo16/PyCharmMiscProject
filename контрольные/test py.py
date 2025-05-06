import tkinter as tk
from tkinter import messagebox
import requests
import random

API_URL = "https://restcountries.com/"

cities = ["Москва", "Париж", "Лондон", "Берлин", "Токио", "Нью-Йорк", "Сидней", "Рим"]
secret_city = ""
attempts = 3
score = 0


def main():
    country = entry.get()
    try:
        response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
        data = response.json()[0]
        result = f"Страна: {data['name']['common']}\nСтолица: {data.get('capital', ['нет'])[0]}\nНаселение: {data['population']}\nРегион: {data['region']}"
        output_label.config(text=result, foreground="purple")
    except Exception as error:
        messagebox.askyesno("Ошибка", f"Не удалось получить данные {error}, повторить ?")


def start_game():
    global secret_city, attempts, score
    secret_city = random.choice(cities)
    print(secret_city)
    attempts = 3
    score = 0
    game_label.config(text="Угадайте загаданый город! У вас 3 попытки.")
    guess_entry.delete(0, tk.END)


def check_guess():
    global attempts, score,secret_city
    guess = guess_entry.get()

    if guess == secret_city:
        score += 10
        messagebox.showinfo("Поздравляем!", f"Вы угадали город! Ваши очки: {score}")
        secret_city = random.choice(cities)
        print(secret_city)
    else:
        attempts -= 1
        if attempts > 0:
            messagebox.showwarning("Неправильно!", f"Неправильно! Осталось попыток: {attempts}")
        else:
            messagebox.showerror("Игра окончена!", f"Вы исчерпали все попытки. Загаданный город был: {secret_city}")
            #start_game()

def check_score():
    global score
    messagebox.showinfo("у вас", f"{score} очков, продолжайте в том же духе")


win = tk.Tk()
win.title("Информация о странах и игра")
win.geometry("400x500")

tk.Label(win, text="Введите название страны:", fg="blue").pack()
entry = tk.Entry(win)
entry.pack()

tk.Button(win, text="выдать информацию", command=main, foreground="blue").pack()

output_label = tk.Label(win, text="", justify=tk.LEFT, font=("Arial", 12))
output_label.pack()

tk.Label(win, text="Игра: Угадайте загаданый город", fg="green").pack(pady=10)
game_label = tk.Label(win, text="")
game_label.pack()


guess_entry = tk.Entry(win)
guess_entry.pack()

tk.Button(win, text="Начать игру", command=start_game, foreground="green").pack()
tk.Button(win, text="Угадать город", command=check_guess, foreground="green").pack()
tk.Button(win, text="Просмотр очков", command=check_score, foreground="green").pack()

win.mainloop()