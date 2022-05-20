import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import psapy.FluidProps
import psapy.BeggsandBrill as BB
from tkinter import *
import tkinter as tk
from tkinter import ttk
import pandas as pd
import seaborn as sns
from psapy.Vogel import VogelIPR
sns.set_style('darkgrid', {"axes.facecolor": ".9"})

main = tk.Tk()
tabControl = ttk.Notebook(main)

main.title('Traverse Curve Plotting')
main.geometry('650x400')

root = ttk.Frame(tabControl)
root2 = ttk.Frame(tabControl)

tabControl.add(root, text='Traverse Curve')
tabControl.add(root2, text='IPR and VLP')
tabControl.pack(expand=1, fill="both")

#=================================Start of Tab1============
#Frame 1
'''
Inputs
        Oil Rate
        Water Rate
        GOR
'''
frame1 = Frame(root)

frame1 = tk.Frame(root)
frame1.pack(fill= X, ipady=20)

qoil_label = Label(frame1, text = "Q oil")
qoil_label.place( relx= 0.1, rely= 0.1, relwidth=0.1, relheight=0.7)

qoil_entry = Entry(frame1)
qoil_entry.insert(0,100)
qoil_entry.place(relx = 0.2, rely = 0.1, relwidth = 0.1, relheight = 0.7)

qwater_label = Label(frame1, text = "Q water")
qwater_label.place( relx= 0.3, rely= 0.1, relwidth=0.2, relheight=0.7)

qwater_entry = Entry(frame1)
qwater_entry.insert(0, 50)
qwater_entry.place(relx = 0.5, rely = 0.1, relwidth = 0.1, relheight = 0.7)

gor_label = Label(frame1, text = "GOR")
gor_label.place( relx= 0.6, rely= 0.1, relwidth=0.2, relheight=0.7)

gor_entry = Entry(frame1)
gor_entry.insert(0, 300)
gor_entry.place(relx = 0.8, rely = 0.1, relwidth = 0.1, relheight = 0.7)

#Frame 2
'''
Inputs
        Gas Gravity
        Oil Gravity
        Wtr Gravity
'''
frame2 = tk.Frame(root)
frame2.pack(fill= X, ipady=20)

gas_gravity_label = Label(frame2, text = "γ gas")
gas_gravity_label.place( relx= 0.1, rely= 0.1, relwidth=0.1, relheight=0.7)

gas_gravity_entry = Entry(frame2)
gas_gravity_entry.insert(0, 0.65)
gas_gravity_entry.place(relx = 0.2, rely = 0.1, relwidth = 0.1, relheight = 0.7)

oil_gravity_label = Label(frame2, text = "γ oil")
oil_gravity_label.place( relx= 0.3, rely= 0.1, relwidth=0.2, relheight=0.7)

oil_gravity_entry = Entry(frame2)
oil_gravity_entry.insert(0, 35)
oil_gravity_entry.place(relx = 0.5, rely = 0.1, relwidth = 0.1, relheight = 0.7)

water_gravity_label = Label(frame2, text = "γ water")
water_gravity_label.place( relx= 0.6, rely= 0.1, relwidth=0.2, relheight=0.7)

water_gravity_entry = Entry(frame2)
water_gravity_entry.insert(0, 1.07)
water_gravity_entry.place(relx = 0.8, rely = 0.1, relwidth = 0.1, relheight = 0.7)

#Frame 3
'''
Inputs
        Diameter
        Angle
        Thp
'''
frame3 = tk.Frame(root)
frame3.pack(fill= X, ipady=20)

diameter_label = Label(frame3, text = "Diameter")
diameter_label.place( relx= 0.1, rely= 0.1, relwidth=0.1, relheight=0.7)

diameter_entry = Entry(frame3)
diameter_entry.insert(0, 2.441)
diameter_entry.place(relx = 0.2, rely = 0.1, relwidth = 0.1, relheight = 0.7)

angle_label = Label(frame3, text = "θ")
angle_label.place( relx= 0.3, rely= 0.1, relwidth=0.2, relheight=0.7)

angle_entry = Entry(frame3)
angle_entry.insert(0, 90.0)
angle_entry.place(relx = 0.5, rely = 0.1, relwidth = 0.1, relheight = 0.7)

Thp_label = Label(frame3, text = "Thp")
Thp_label.place( relx= 0.6, rely= 0.1, relwidth=0.2, relheight=0.7)

Thp_entry = Entry(frame3)
Thp_entry.insert(0, 150.0)
Thp_entry.place(relx = 0.8, rely = 0.1, relwidth = 0.1, relheight = 0.7)


#Frame 4
'''
Inputs
        Tht
        Twf
        depth
'''
frame4 = tk.Frame(root)
frame4.pack(fill= X, ipady=20)

Tht_label = Label(frame4, text = "Tht")
Tht_label.place( relx= 0.1, rely= 0.1, relwidth=0.1, relheight=0.7)

Tht_entry = Entry(frame4)
Tht_entry.insert(0, 100.0)
Tht_entry.place(relx = 0.2, rely = 0.1, relwidth = 0.1, relheight = 0.7)

Twf_label = Label(frame4, text = "Twf")
Twf_label.place( relx= 0.3, rely= 0.1, relwidth=0.2, relheight=0.7)

Twf_entry = Entry(frame4)
Twf_entry.insert(0, 150.0)
Twf_entry.place(relx = 0.5, rely = 0.1, relwidth = 0.1, relheight = 0.7)

depth_label = Label(frame4, text = "Depth")
depth_label.place( relx= 0.6, rely= 0.1, relwidth=0.2, relheight=0.7)

depth_entry = Entry(frame4)
depth_entry.insert(0, 5000)
depth_entry.place(relx = 0.8, rely = 0.1, relwidth = 0.1, relheight = 0.7)

frame5 = tk.Frame(root)
frame5.pack(fill= X, ipady=20)



#=================================================End of Tab 1 ####



#=================================================Start of Tab 2 ###

'''
Frame 12 Inputs

    Res_Presssure
    Bubble Point Pressure
    Pwf
'''
frame12 = Frame(root2)

frame12 = tk.Frame(root2)
frame12.pack(fill= X, ipady=20)

Pres_label = Label(frame12, text = "Pres")
Pres_label.place( relx= 0.1, rely= 0.1, relwidth=0.1, relheight=0.7)

Pres_entry = Entry(frame12)
Pres_entry.insert(0,3000)
Pres_entry.place(relx = 0.2, rely = 0.1, relwidth = 0.1, relheight = 0.7)

Pb_label = Label(frame12, text = "Pb")
Pb_label.place( relx= 0.3, rely= 0.1, relwidth=0.2, relheight=0.7)

Pb_entry = Entry(frame12)
Pb_entry.insert(0, 2500)
Pb_entry.place(relx = 0.5, rely = 0.1, relwidth = 0.1, relheight = 0.7)

Pwf_label = Label(frame12, text = "Pwf")
Pwf_label.place( relx= 0.6, rely= 0.1, relwidth=0.2, relheight=0.7)

Pwf_entry = Entry(frame12)
Pwf_entry.insert(0, 2700)
Pwf_entry.place(relx = 0.8, rely = 0.1, relwidth = 0.1, relheight = 0.7)

#Frame 2
'''
Inputs
        Flow Rate
        Num of Points
'''
frame22 = tk.Frame(root2)
frame22.pack(fill= X, ipady=20)

flowrate_label = Label(frame22, text = "Flow Rate")
flowrate_label.place( relx= 0.1, rely= 0.1, relwidth=0.1, relheight=0.7)

flowrate_entry = Entry(frame22)
flowrate_entry.insert(0, 235)
flowrate_entry.place(relx = 0.2, rely = 0.1, relwidth = 0.1, relheight = 0.7)

n_points_label = Label(frame22, text = "No. Points")
n_points_label.place( relx= 0.3, rely= 0.1, relwidth=0.2, relheight=0.7)

n_points_entry = Entry(frame22)
n_points_entry.insert(0, 35)
n_points_entry.place(relx = 0.5, rely = 0.1, relwidth = 0.1, relheight = 0.7)


#====================================================End of Tab 2 ===============

def get_delta_p():
        oil_rate = float(qoil_entry.get())
        water_rate =  float(qwater_entry.get())
        gor =  float(gor_entry.get())
        gas_grav =  float(gas_gravity_entry.get())
        oil_grav =  float(oil_gravity_entry.get())
        wtr_grav =  float(water_gravity_entry.get())
        diameter = float(diameter_entry.get())
        angle =  float(angle_entry.get())
        thp =  float(Thp_entry.get())
        tht =  float(Tht_entry.get())
        twf =  float(Twf_entry.get())
        depth =  float(depth_entry.get())
        sample_size =  50

        def temp_gradient(t0,t1, depth):
            if depth==0:
                return 0
            else:
                return abs(t0-t1)/depth

        t_grad = temp_gradient(tht,twf, depth)
        depths = np.linspace(0, depth, sample_size)
        temps = tht + t_grad * depths

        def pressure_traverse(gor):
            p=[]
            dpdz=[]
            for i in range(len(depths)):

                if i==0:
                    p.append(thp)
                else:
                    dz = (depths[i]-depths[i-1])
                    pressure = p[i-1]+dz*dpdz[i-1]
                    p.append(pressure)

                dpdz_step = BB.Pgrad(p[i], temps[i], oil_rate, water_rate, gor, gas_grav, oil_grav, wtr_grav, diameter, angle)
                dpdz.append(dpdz_step)

            return p, dpdz

        p, dpdz =pressure_traverse(gor)
        beso_label['text'] = f'{round(p[-1], 2)} psi'


def plotting():
        oil_rate = float(qoil_entry.get())
        water_rate =  float(qwater_entry.get())
        gor =  float(gor_entry.get())
        gas_grav =  float(gas_gravity_entry.get())
        oil_grav =  float(oil_gravity_entry.get())
        wtr_grav =  float(water_gravity_entry.get())
        diameter = float(diameter_entry.get())
        angle =  float(angle_entry.get())
        thp =  float(Thp_entry.get())
        tht =  float(Tht_entry.get())
        twf =  float(Twf_entry.get())
        depth =  float(depth_entry.get())
        sample_size =  50

        def temp_gradient(t0,t1, depth):
            if depth==0:
                return 0
            else:
                return abs(t0-t1)/depth

        t_grad = temp_gradient(tht,twf, depth)
        depths = np.linspace(0, depth, sample_size)
        temps = tht + t_grad * depths

        def pressure_traverse(gor):
            p=[]
            dpdz=[]
            for i in range(len(depths)):

                if i==0:
                    p.append(thp)
                else:
                    dz = (depths[i]-depths[i-1])
                    pressure = p[i-1]+dz*dpdz[i-1]
                    p.append(pressure)

                dpdz_step = BB.Pgrad(p[i], temps[i], oil_rate, water_rate, gor, gas_grav, oil_grav, wtr_grav, diameter, angle)
                dpdz.append(dpdz_step)

            return p, dpdz

        p, dpdz =pressure_traverse(gor)
        #-------------------------------
        glr=[400,500,600,700]
        fw = (water_rate / (oil_rate + water_rate))
        gor = [x / (1-fw) for x in glr]
        fig, ax = plt.subplots()
        fig.set_size_inches(20,75)

        for r in gor:
            p, dpdz =pressure_traverse(r)
            plt.plot(p, depths, label=f'GLR: {round(r*(1-fw),0)}')
        # ax = scatter.axes

        ax.invert_yaxis()
        ax.set_xlabel('X LABEL')
        ax.xaxis.set_label_position('top')
        ax.xaxis.tick_top()
        ax.set_title(f'Oil Rate: {oil_rate} \nWater Rate: {water_rate} \nDiameter:{diameter} \nAngle:{angle}', loc='center', fontsize=13, y=0.98 ,pad=-70)
        plt.xlabel('Pressure (Psi)')
        plt.ylabel('Depth (ft)')
        plt.ylim(depth+500,0)
        plt.legend()
        plt.grid(color='red', alpha=0.2)
        plt.show()



def vlp(rates):
    bhps =[]
    for q in rates:
        p, dpdz = pressure_traverse(q)
        bhp = p[-1]
        bhps.append(bhp)
    return bhps

def vlp_plotting():
        oil_rate = float(qoil_entry.get())
        water_rate =  float(qwater_entry.get())
        gor =  float(gor_entry.get())
        gas_grav =  float(gas_gravity_entry.get())
        oil_grav =  float(oil_gravity_entry.get())
        wtr_grav =  float(water_gravity_entry.get())
        diameter = float(diameter_entry.get())
        angle =  float(angle_entry.get())
        thp =  float(Thp_entry.get())
        tht =  float(Tht_entry.get())
        twf =  float(Twf_entry.get())
        depth =  float(depth_entry.get())
        sample_size =  50

        fw = water_rate / (oil_rate + water_rate)

        def temp_gradient(t0,t1, depth):
            if depth==0:
                return 0
            else:
                return abs(t0-t1)/depth

        t_grad = temp_gradient(tht,twf, depth)
        depths = np.linspace(0, depth, sample_size)
        temps = tht + t_grad * depths

        def pressure_traverse(rate):
            p=[]
            dpdz=[]
            for i in range(len(depths)):

                if i==0:
                    p.append(thp)
                else:
                    dz = (depths[i]-depths[i-1])
                    pressure = p[i-1]+dz*dpdz[i-1]
                    p.append(pressure)

                dpdz_step = BB.Pgrad(p[i], temps[i], (rate * (1-fw)), rate * fw, gor, gas_grav, oil_grav, wtr_grav, diameter, angle)
                dpdz.append(dpdz_step)

            return p, dpdz



        def vlp(rates):
            bhps =[]
            for q in rates:
                p, dpdz = pressure_traverse(q)
                bhp = p[-1]
                bhps.append(bhp)
            return bhps

        rates = np.linspace(100, 5000, 50)
        bhps = vlp(rates)
        plt.plot(rates, bhps, '-')
        plt.xlabel('Rate')
        plt.ylabel('Pressure')

        plt.show()

##Buttons for Tab 1
frame5 = tk.Frame(root)
frame5.pack(fill= X, ipady=20)

calc_pressure_drop = Button(frame5, text='Draw Traverse Curves', command=lambda: plotting())
calc_pressure_drop.place(relx = 0.1, rely=0.1, relwidth=0.35, relheight=0.7)

calc_pressure_drop = Button(frame5, text='Draw VLP', command=lambda: vlp_plotting())
calc_pressure_drop.place(relx = 0.6, rely=0.1, relwidth=0.35, relheight=0.7)

frame6 = tk.Frame(root)
frame6.pack(fill= X, ipady=20)

beso_label = Label(frame6, text = "Delta P will show up here")
beso_label.place( relx = 0.6, rely=0.1, relwidth=0.35, relheight=0.7)

calc_pressure_drop = Button(frame6, text='Calculate ΔP', command=lambda: get_delta_p())
calc_pressure_drop.place(relx = 0.1, rely=0.1, relwidth=0.35, relheight=0.7)
##Buttons for Tab 2

def ipr_plotting():
        Pres = float(Pres_entry.get())
        Pb =  float(Pb_entry.get())
        Pwf =  float(Pwf_entry.get())
        flowrate =  float(flowrate_entry.get())
        n_points =  float(n_points_entry.get())
        ipr_values = VogelIPR(Pres, Pb, Pwf, flowrate, n_points)
        plt.plot(ipr_values[0], ipr_values[1])
        plt.xlabel('Q')
        plt.ylabel('Pwf')
        plt.show()


def draw_vlp_ipr():

    def vlp_plotting():
        oil_rate = float(qoil_entry.get())
        water_rate =  float(qwater_entry.get())
        gor =  float(gor_entry.get())
        gas_grav =  float(gas_gravity_entry.get())
        oil_grav =  float(oil_gravity_entry.get())
        wtr_grav =  float(water_gravity_entry.get())
        diameter = float(diameter_entry.get())
        angle =  float(angle_entry.get())
        thp =  float(Thp_entry.get())
        tht =  float(Tht_entry.get())
        twf =  float(Twf_entry.get())
        depth =  float(depth_entry.get())
        sample_size =  50

        fw = water_rate / (oil_rate + water_rate)

        def temp_gradient(t0,t1, depth):
            if depth==0:
                return 0
            else:
                return abs(t0-t1)/depth

        t_grad = temp_gradient(tht,twf, depth)
        depths = np.linspace(0, depth, sample_size)
        temps = tht + t_grad * depths

        def pressure_traverse(rate):
            p=[]
            dpdz=[]
            for i in range(len(depths)):

                if i==0:
                    p.append(thp)
                else:
                    dz = (depths[i]-depths[i-1])
                    pressure = p[i-1]+dz*dpdz[i-1]
                    p.append(pressure)

                dpdz_step = BB.Pgrad(p[i], temps[i], (rate * (1-fw)), rate * fw, gor, gas_grav, oil_grav, wtr_grav, diameter, angle)
                dpdz.append(dpdz_step)

            return p, dpdz



        def vlp(rates):
            bhps =[]
            for q in rates:
                p, dpdz = pressure_traverse(q)
                bhp = p[-1]
                bhps.append(bhp)
            return bhps

        rates = np.linspace(100, 5000, 50)
        bhps = vlp(rates)
        plt.plot(rates, bhps, '-', label= "VLP Curve")


    def ipr_plotting():
        Pres = float(Pres_entry.get())
        Pb =  float(Pb_entry.get())
        Pwf =  float(Pwf_entry.get())
        flowrate =  float(flowrate_entry.get())
        n_points =  float(n_points_entry.get())
        ipr_values = VogelIPR(Pres, Pb, Pwf, flowrate, n_points)
        plt.plot(ipr_values[0], ipr_values[1], label = 'IPR Curve')

    create_vlp = vlp_plotting()
    create_ipr = ipr_plotting()
    plt.title("VLP and IPR Curves")
    plt.xlabel('Flow Rate')
    plt.ylabel('Pressure')
    plt.legend()
    plt.show()






frame32 = tk.Frame(root2)
frame32.pack(fill= X, ipady=20)

calc_pressure_drop = Button(frame32, text='Draw IPR', command=lambda: ipr_plotting())
calc_pressure_drop.place(relx = 0.1, rely=0.1, relwidth=0.35, relheight=0.7)

calc_pressure_drop = Button(frame32, text='VLP IPR', command=lambda: print(draw_vlp_ipr()))
calc_pressure_drop.place(relx = 0.6, rely=0.1, relwidth=0.35, relheight=0.7)

root.mainloop()
