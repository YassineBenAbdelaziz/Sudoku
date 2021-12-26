"""
The Game class handles the gui settings and the game main loop
** __init__ : main constructor
** createGrid : creates the grid graphics
** createTextCells : creates text objects and display text from the sukoku grid made with the solver class
** updateText : updates text objects attributes when creating a new game
** up, down , left , right : handles the cell selector position through user keyboard inputs
** write : writes number into actuel cell position
** writeNumber : called on every key number click event, checks the source of the event and calls write with requested number as argument
** bind : binds the inputs to their callback functions
** reset : creates a new game
** newgame : creates a thread to handle the reset methods, binded to "new game" button  
** solve : called on "Solve" button click, solves the player grid and submits the verdict
** pack : place the widgets on the screen
** run : runs the game main loop
"""

from tkinter import Button, Tk,Canvas,W,Label,DISABLED,NORMAL
from Solver import Solver
from threading import Thread


class Game :

    def __init__(self) :
        
        self.window = Tk()
        self.window.geometry("400x500")
        self.window.title("Sudoku")
        self.window.resizable(False,False)

        self.button1 = Button(self.window,text="New Game",command=self.newgame, font=("Purisa", 14), width=10)
        self.button2 = Button(self.window,text="Solve",command=self.solve, font=("Purisa", 14),  width=10)
        self.label1 = Label(self.window, text="",font=("Purisa", 10))
        self.label2 = Label(self.window, text="Use keyboard to play.",font=("Purisa", 10))
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

        self.restrictedCell = []
        self.playerGrid = []
        self.createGrid()
        
        self.solver = Solver()
        self.solver.copyEmptyGrid()
        self.solver.createFilledGrid()
        self.solver.copySolvedGrid()
        self.solver.clearGrid()
        self.playerGrid = self.solver.getGrid()
        self.createTextCells(self.solver.getGrid())


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




    def createTextCells(self,grid):
        x0 = 22
        y0 = 22 
        for i in range(81):
            if grid[i//9][i%9] == 0 :
                self.canvas.create_text(x0,y0,text="",tag=f"cell{i}",font=("Purisa", 14),fill="blue")
            else :
                self.restrictedCell.append(i)
                self.canvas.create_text(x0,y0,text=f"{grid[i//9][i%9]}",tag=f"cell{i}",font=("Purisa", 14))
            x0 += 43
            if i % 9 == 8 : 
                x0 = 22
                y0 += 43 


    def updateText(self,grid) :
        for i in range(81):
            if grid[i//9][i%9] == 0 :
                self.canvas.itemconfig(f"cell{i}",text="",fill="blue")
            else :
                self.restrictedCell.append(i)
                self.canvas.itemconfig(f"cell{i}",text=f"{grid[i//9][i%9]}",fill="black")
     



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


    def write(self,char) :
        cell = ( self.rec_y0 // 43 ) * 9 + (self.rec_x0 // 43 )
        try :
            self.playerGrid[ self.rec_y0 // 43 ][ self.rec_x0 // 43 ] = int(char)
        except ValueError :
            self.playerGrid[ self.rec_y0 // 43 ][ self.rec_x0 // 43 ] = 0
        if cell not in self.restrictedCell :    
            self.canvas.itemconfig(f"cell{cell}",text=char) 


    def writeNumber(self,event) :
        if event.keysym == "0" :
            self.write("")
        elif event.keysym == "1" :
            self.write("1")
        elif event.keysym == "2" :
            self.write("2")
        elif event.keysym == "3" :
            self.write("3")
        elif event.keysym == "4" :
            self.write("4")
        elif event.keysym == "5" :
            self.write("5")
        elif event.keysym == "6" :
            self.write("6")
        elif event.keysym == "7" :
            self.write("7")
        elif event.keysym == "8" :
            self.write("8")
        else :
            self.write("9")



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

    def reset(self) :
        self.label1.configure(text="Loading ...") 
        self.button1.configure(state=DISABLED)
        self.button2.configure(state=DISABLED)
        self.rec_x0 = 172
        self.rec_y0 = 172
        self.canvas.coords(self.id,self.rec_x0,self.rec_y0,
        self.rec_x0 + 43,self.rec_y0 + 43)
        self.restrictedCell = []
        self.solver.copyEmptyGrid()
        self.solver.createFilledGrid()
        self.solver.copySolvedGrid()
        self.solver.clearGrid()
        self.playerGrid = self.solver.getGrid()
        self.updateText(self.solver.getGrid())
        self.label1.configure(text="")
        self.button1.configure(state=NORMAL)
        self.button2.configure(state=NORMAL)


    def newgame(self) :
        thread = Thread(target=self.reset,name="resetThread")
        if not thread.is_alive() :
            thread.start()



    def solve(self) :
        mistake = False
        solvedGrid = self.solver.getSolvedGrid()
        for y in range(9) :
            for x in range(9) :
                if solvedGrid[y][x] != self.playerGrid[y][x] :
                    cell = y * 9 + x
                    self.canvas.itemconfig(f"cell{cell}",text=f"{solvedGrid[y][x]}",fill="red")
                    mistake = True

        if mistake : 
            self.label1.configure(text="Defeat. Better luck next time.")
        else :
            self.label1.configure(text="Victory!")



    def pack(self) :
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=3)
        self.button1.grid(column=0, row=0, sticky=W, padx=5, pady=5)
        self.button2.grid(column=0, row=1, sticky=W, padx=5, pady=5)
        self.label1.grid(column=1, row=0, sticky=W,  padx=5, pady=5)
        self.label2.grid(column=1, row=1, sticky=W,  padx=5, pady=5)
        self.canvas.grid(column=0, row=2, columnspan=2, padx=5, pady=5)

    def run(self) :
        self.window.mainloop()



