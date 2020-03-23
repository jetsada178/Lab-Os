import Tkinter as tk
import os
import subprocess 
root = tk.Tk()
root.geometry("690x500+0+0")
root.title("Firewall")
okp = str(subprocess.check_output(['ufw','status']))
print(okp)



Tops = tk.Frame(root,width = 600,height=100,bd=14,bg="blue",relief="raise")
Tops.pack(side=tk.TOP)
Lefts = tk.Frame(root,width = 500,height=100,bd=14,bg="red",relief="raise")
Lefts.pack(side=tk.LEFT)
Rights = tk.Frame(root,width = 500,height=100,bd=14,bg="green",relief="raise")
Rights.pack(side=tk.RIGHT)

lblInfo = tk.Label(Tops,font=('TkDefaultFont',20),text = "Firewall",bg="yellow",bd=10,justify='center')
lblInfo.grid(row=0,column=1)
## status firewall
lblstatus = tk.Label(Tops,font=('TkDefaultFont',20,'bold'),text="Firewall status :",bg="Yellow",bd=10)
lblstatus.grid(row=1,column=0)
##status = StringVar()
##status.set("Status")
lblstatus = tk.Label(Tops,font=('TkDefaultFont',20,'bold'),text=okp,bd=8)
lblstatus.grid(row=1,column=1)

##mainOpen firewall
lblopen = tk.Label(Lefts,font=('TkDefaultFont',20,'bold'),text = "firewall Active :")
lblopen.grid(row=0,column=0)
btnopen = tk.Button(Rights,fg='black',font=('TkDefaultFont',20,'bold'),text="Open firewall",command=lambda:open(1))
btnopen.grid(row=0,column=0)
##mainClose firewall
lblclose = tk.Label(Lefts,font=('TkDefaultFont',20,'bold'),text="Firewall Stopped : ")
lblclose.grid(row=1,column=0)
btnclose = tk.Button(Rights,fg='black',font=('TkDefaultFont',20,'bold'),text="Close firewall",command=lambda:open(2))
btnclose.grid(row=1,column=0)
##function
def open(args):
	##txtstatus.config(text="hello")
	if args == 1:
		print("sudo ufw enable")
		os.system("sudo ufw enable")
		lblstatus.config(text="ON")
	if args == 2:
		print("sudo ufw disable")
		os.system("sudo ufw disable")
		lblstatus.config(text="OFF")
root.mainloop()
