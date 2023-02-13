from tkinter import *
from tkinter import messagebox
import requests

# set Main Window
window = Tk()

counter = 1


def closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()


def news():
    global counter

    def news_closing():
        news_window.destroy()
        global counter
        counter = 1

    if counter < 2:
        news_window = Toplevel(window)
        news_window.title("Investment News")
        news_window.geometry("300x300")
        counter += 1
        news_window.protocol("WM_DELETE_WINDOW", news_closing)


def portfolio():
    global counter

    def apply_information():
        total_value = 0
        symbol = add_stock_input.get()
        quantity = quantity_input.get()
        try:
            url = f'https://api.polygon.io/v1/open-close/{symbol}/2023-02-09?adjusted=false&apiKey=nrvGL4xwuciY3nX_QsmbypmmM8U_Nbnj'
            r = requests.get(url)
            data = r.json()
            stock_price = data["close"]
            textarea.configure(state=NORMAL)
            textarea.insert(END, '    Symbol\t    Counts of Shares\t    Current Price\t    Amount\n')
            textarea.insert(END, f"==============================================\n")
            textarea.delete(3.0, END)
            textarea.insert(END, f'\t\t{symbol}\t\t    {quantity}\t\t{stock_price}$\t  {(float(quantity) * stock_price):.2f}$\n')
            total_value += float(quantity)*stock_price
            textarea.insert(END, f"==============================================")
            textarea.configure(state=DISABLED)
        except:
            messagebox.askokcancel("Wrong Symbol!", "Enter a valid stock symbol")



    def clear_information():
        textarea.configure(state=NORMAL)
        textarea.delete("0.0", "end")
        textarea.configure(state=DISABLED)

    def portfolio_closing():
        portfolio_window.destroy()
        global counter
        counter = 1

    if counter < 2:
        portfolio_window = Toplevel(window)
        portfolio_window.title("Portfolio")
        portfolio_window.geometry("600x450")
        portfolio_window.resizable(False, False)
        counter += 1
        portfolio_window.protocol("WM_DELETE_WINDOW", portfolio_closing)

        title = Label(portfolio_window, pady=5, text="Your Stock Portfolio", bd=12, bg="sky blue", fg='white',
                      font=('times new roman', 35, 'bold'), relief=GROOVE, justify=CENTER)
        title.pack(fill=X)

        #################### Heading ####################
        buttons_frame = Frame(portfolio_window, bg="cyan", bd=15)
        buttons_frame.place(x=0, y=275, width=600, height=270)

        add_stock = Label(portfolio_window, text='Add Stock', font=('Helvetic', 12, 'bold', 'underline'),
                          fg='black', bg="cyan")
        add_stock.place(x=5, y=295)
        add_quantity = Label(portfolio_window, text='Add Quantity', font=('Helvetic', 12, 'bold', 'underline'),
                             fg='black', bg="cyan")
        add_quantity.place(x=110, y=295)
        remove_stock = Label(portfolio_window, text='Remove Stock', font=('Helvetic', 12, 'bold', 'underline'),
                             fg='black', bg="cyan")
        remove_stock.place(x=350, y=295)


        #################### EntryBoxes #####################
        add_stock_input = Entry(portfolio_window, width=12)
        add_stock_input.place(x=5, y=325)

        quantity_input = Entry(portfolio_window, width=12)
        quantity_input.place(x=110, y=325)

        remove_stock_input = Entry(portfolio_window, width=12)
        remove_stock_input.place(x=350, y=325)

        #################### Buttons ####################

        apply_button = Button(portfolio_window, text="Apply", width=10, bg="sky blue", border=3,
                              font=('times new roman', 12, 'bold'), command=apply_information)
        apply_button.place(x=225, y=325)
        clear_button = Button(portfolio_window, text="Clear All", width=10, bg="sky blue", border=3,
                              font=('times new roman', 12, 'bold'), command=clear_information)
        clear_button.place(x=475, y=325)
        back_button = Button(portfolio_window, text="Back", width=10, bg="sky blue", border=3,
                             font=('times new roman', 12, 'bold'), command=portfolio_closing)
        back_button.place(x=5, y=400)

        ################### Set TextArea ######################

        text_frame = Frame(portfolio_window, relief=GROOVE, bd=10)
        text_frame.place(x=0, y=90, width=600, height=200)
        scrol_y = Scrollbar(text_frame, orient=VERTICAL)
        scrol_y.pack(side=RIGHT, fill=Y)
        textarea = Text(text_frame, font='arial 15', yscrollcommand=scrol_y.set,state=DISABLED)
        textarea.pack(fill=BOTH)
        scrol_y.config(command=textarea.yview)


window.title("Stock's Portfolio")
window.geometry("600x300")
window.resizable(False, False)

# set background photo
bg_photo = PhotoImage(file="images/stock_bg.png")
bg_label = Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# set buttons
news_button = Button(window, text="NEWS", width=30, bg="sky blue", border=3,
                     font=('times new roman', 10, 'bold'), command=news)
news_button.place(x=190, y=45)

portfolio_button = Button(window, text="PORTFOLIO", width=30, bg="sky blue", border=3,
                          font=('times new roman', 10, 'bold'), command=portfolio)
portfolio_button.place(x=190, y=15)

window.protocol("WM_DELETE_WINDOW", closing)
window.mainloop()

window.mainloop()

