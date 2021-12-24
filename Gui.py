from tkinter import Tk,Canvas


class Game :

    def __init__(self) :
        
        self.window = Tk()
        self.window.geometry("400x500")
        self.window.title("Sudoku")

        self.canvas = Canvas(
        self.window,background="white",width=380,height=380,
        highlightthickness=4, highlightbackground="black"
        )

        self.rec_x0 = 172
        self.rec_y0 = 172

        self.id = self.canvas.create_rectangle(
        self.rec_x0,self.rec_y0,
        self.rec_x0 + 43,self.rec_y0 + 43,outline="#A2FF33",fill="#A2FF33"
        )

        self.createGrid()
        self.createTextCells()
        self.bind()
        self.pack()
        




    def createGrid(self) :
        x0 = 43
        y0 = 43
        for i in range(8):
            if i % 3 == 2 :
                self.canvas.create_line(0,y0,390,y0,width=4)
                self.canvas.create_line(x0,0,x0,390,width=4)
                
            self.canvas.create_line(0,y0,390,y0,width=2)
            self.canvas.create_line(x0,0,x0,390,width=2)
            y0 = y0 + 43
            x0 = x0 + 43




    def createTextCells(self):
        x0 = 22
        y0 = 22 
        for i in range(81):
            self.canvas.create_text(x0,y0,text="",tag=f"cell{i}",font=("Purisa", 14))
            x0 += 43
            if i % 9 == 8 : 
                x0 = 22
                y0 += 43 


    def up(self,event) :
        if self.rec_y0 - 43 >= 0 :
            self.canvas.move(self.id,0,-43)
            self.rec_y0 -= 43


    def down(self,event) :
        if self.rec_y0 + 43 <= 380 :
            self.canvas.move(self.id,0,+43)
            self.rec_y0 += 43

    def right(self,event) :
        if self.rec_x0 + 43 <= 380 :
            self.canvas.move(self.id,+43,0)
            self.rec_x0 += 43

    def left(self,event) :    

        if self.rec_x0 - 43 >= 0 :
            self.canvas.move(self.id,-43,0)
            self.rec_x0 -= 43


    def update(self,char) :
        cell = ( self.rec_y0 // 43 ) * 9 + (self.rec_x0 // 43 )    
        self.canvas.itemconfig(f"cell{cell}",text=char) 


    def writeNumber(self,event) :
        if event.keysym == "0" :
            self.update("")
        elif event.keysym == "1" :
            self.update("1")
        elif event.keysym == "2" :
            self.update("2")
        elif event.keysym == "3" :
            self.update("3")
        elif event.keysym == "4" :
            self.update("4")
        elif event.keysym == "5" :
            self.update("5")
        elif event.keysym == "6" :
            self.update("6")
        elif event.keysym == "7" :
            self.update("7")
        elif event.keysym == "8" :
            self.update("8")
        else :
            self.update("9")



    def bind(self):    
        self.window.bind("<Up>",self.up)
        self.window.bind("<Down>",self.down)
        self.window.bind("<Right>",self.right)
        self.window.bind("<Left>",self.left)
        self.window.bind("<9>",self.writeNumber)
        self.window.bind("<8>",self.writeNumber)
        self.window.bind("<7>",self.writeNumber)
        self.window.bind("<6>",self.writeNumber)
        self.window.bind("<Key-5>",self.writeNumber)
        self.window.bind("<Key-4>",self.writeNumber)
        self.window.bind("<Key-3>",self.writeNumber)
        self.window.bind("<Key-2>",self.writeNumber)
        self.window.bind("<Key-1>",self.writeNumber)
        self.window.bind("<0>",self.writeNumber)
    

    def pack(self) :
        self.canvas.pack(pady=50)

    def run(self) :
        self.window.mainloop()


game = Game()
game.run()