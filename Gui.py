import os
from tkinter import *
from crawl import *
from plot import histPlot, boxPlot
from PIL import ImageTk, Image
import pickle
import webbrowser

sorted_item_list = []
img_hist = None
img_box = None


def yviews(*args):
    listbox_No.yview(*args)
    listbox_platform.yview(*args)
    listbox_title.yview(*args)
    listbox_price.yview(*args)


def setslide(first, last):
    slide.set(first, last)
    args = ('moveto', str(first))
    yviews(*args)


def search():
    keyword = entry_keyword.get()
    if not keyword:
        return
    item_list = []
    for item in jdItem(keyword, 9222):
        item_list.append(item)
    for item in amzItem(keyword, 9223):
        item_list.append(item)
    for item in pddItem(keyword, 9224):
        item_list.append(item)
    global listbox_No, listbox_platform, listbox_title, listbox_price, sorted_item_list
    sorted_item_list = sorted(item_list, key=lambda item: item["price"])

    items = sorted_item_list
    for idx in range(len(items)):
        listbox_No.insert(END, str(idx + 1))
        listbox_platform.insert(END, str(items[idx]["platform"]))
        listbox_title.insert(END, str(items[idx]["title"]))
        listbox_price.insert(END, str(items[idx]["price"]))

    histPlot(items)
    global img_hist, canvas_hist
    img_hist = Image.open("{p}\hist.png".format(p=os.getcwd()))
    img_hist = img_hist.resize((canvas_hist.winfo_width(), canvas_hist.winfo_height()), Image.ANTIALIAS)
    img_hist = ImageTk.PhotoImage(img_hist)
    canvas_hist.create_image(0, 0, anchor=NW, image=img_hist)

    boxPlot(items)
    global img_box, canvas_box
    img_box = Image.open(r"{p}\box.png".format(p=os.getcwd()))
    img_box = img_box.resize((canvas_box.winfo_width(), canvas_box.winfo_height()), Image.ANTIALIAS)
    img_box = ImageTk.PhotoImage(img_box)
    canvas_box.create_image(0, 0, anchor=NW, image=img_box)
    return


def goto_link(event):
    idx = listbox_title.curselection()[0]
    item_selected = sorted_item_list[idx]
    link = item_selected["link"]
    webbrowser.open(link)


main_window = Tk()
main_window.title("网购平台比价系统")
main_window.geometry("900x600")
main_window.resizable(False, False)

frame_upper = Frame(main_window, borderwidth=1, relief="solid", height="50", bg="gray")
frame_middle = Frame(main_window, borderwidth=1, relief="solid", height="268", bg="yellow")
frame_bottom = Frame(main_window, borderwidth=1, relief="solid", height="300", bg="blue")

# top section start
label_keyword = Label(frame_upper, text="输入关键词")
entry_keyword = Entry(frame_upper)
button_search = Button(frame_upper, text="开始比价", command=search)
# top section end

# mid section start
frame_middle_1 = Frame(frame_middle, borderwidth=1, relief="solid", width="225", height="300")
frame_middle_2 = Frame(frame_middle, borderwidth=1, relief="solid", width="225", height="300")
frame_middle_3 = Frame(frame_middle, borderwidth=1, relief="solid", width="225", height="300")
frame_middle_4 = Frame(frame_middle, borderwidth=1, relief="solid", width="225", height="300")

label_No = Label(frame_middle_1, text="序号")
label_platform = Label(frame_middle_2, text="平台")
label_title = Label(frame_middle_3, text="商品名称")
label_price = Label(frame_middle_4, text="商品价格")

slide = Scrollbar(frame_middle, orient=VERTICAL)
listbox_No = Listbox(frame_middle_1, height=15, width=1, yscrollcommand=setslide)
listbox_platform = Listbox(frame_middle_2, height=15, width=1, yscrollcommand=setslide)
listbox_title = Listbox(frame_middle_3, height=15, width=50, yscrollcommand=setslide); listbox_title.bind('<Double-1>', goto_link)
listbox_price = Listbox(frame_middle_4, height=15, width=1, yscrollcommand=setslide)
slide.config(command=yviews)
# mid section end

# bottom section start
canvas_hist = Canvas(frame_bottom, width="450", borderwidth=1, relief="solid")
canvas_box = Canvas(frame_bottom, width="450", borderwidth=1, relief="solid")
# bottom section end

# placement start
frame_upper.pack(side=TOP, fill=X, expand=False)
frame_middle.pack(side=TOP, fill=X, expand=True)
frame_bottom.pack(side=TOP, fill=X, expand=True)

label_keyword.pack(side=LEFT)
entry_keyword.pack(side=LEFT)
button_search.pack(side=LEFT)

frame_middle_1.pack(side=LEFT, fill=BOTH, expand=True)
frame_middle_2.pack(side=LEFT, fill=BOTH, expand=True)
frame_middle_3.pack(side=LEFT, fill=BOTH, expand=True)
frame_middle_4.pack(side=LEFT, fill=BOTH, expand=True)
slide.pack(side=RIGHT, fill=Y)

listbox_No.pack(side=BOTTOM, fill=BOTH, expand=True)
listbox_platform.pack(side=BOTTOM, fill=BOTH, expand=True)
listbox_title.pack(side=BOTTOM, fill=BOTH, expand=True)
listbox_price.pack(side=BOTTOM, fill=BOTH, expand=True)

label_No.pack(side=TOP, fill=BOTH)
label_platform.pack(side=TOP, fill=BOTH)
label_title.pack(side=TOP, fill=BOTH)
label_price.pack(side=TOP, fill=BOTH)

canvas_hist.pack(side=LEFT, fill=Y, expand=True)
canvas_box.pack(side=LEFT, fill=Y, expand=True)
# placement end

if __name__ == '__main__':

    main_window.mainloop()
