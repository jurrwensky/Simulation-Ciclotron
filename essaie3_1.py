from visual import *

# construction du cyclotro

d = 0.1     # 10 cm
R = 1       # 1 m
D = 2       # 2 m
dee = cylinder( pos=(0,0,-0.05), axis=(0,0,0.1), radius=1.1*R, color=color.orange, opacity=0.4)
interstice = box( pos=(0,0,0), size=(d,2.2*R,0.102), color=color.black, opacity=0.5)
tunnel = box( pos=(R/2.,-R,0), size=(R,0.05,0.1), color=color.orange, opacity=0.4)
cible = box( pos=(D,-R,0), size=(0.05,0.5,0.5), color=color.green)

scene.center = (0.5, 0, 0)
scene.range =(4.2, 1.4, 1)

# construction de la charg
Carbon12= sphere(pos=(0,-0.132,0), radius=0.03)
#charge ionisé 3 fois du carbone12
qCarbon12=3*1.602*10**-19
#masse du carbone12
mCarbon12=12*1.67*10**-27
#champ magnétique null
B0=vector(0,0,0)
#champ magnétique max
Bmax=vector(0,0,-0.6)
#Potentiel électrique
v5=150000
#Vitesse initial de la particule
vCarbon12=vector(0,0,0)
#Force electrique initial
Fe=vector(0,0,0)
#Force magnétique initial
Fm=vector(0,0,0)
#Trace du parcours avec la couleur vert de la charge
trace=curve(color=color.green)
#intervalle de temps
dt = 0.00000000001
#vecteur d'accélération inital
a=vector(0,0,0)
#Calcul de la période du cyclotron
T=((2*3.14*mCarbon12))/(qCarbon12*mag(Bmax))
#postition maximal en y du cyclotron
Pmax=1.1
#postition minimal en y du cyclotron
Pmin=-1.1
#nombre de tours cyclotron
n=13
while 1:
        rate(50000)
        #Champ magnetique dans le Dee
        if -d/2<=Carbon12.pos.x<=d/2 and Pmin<=Carbon12.pos.y<=Pmax:B=B0
        else: B=Bmax
        #Difference de potentielle dans l'interstice
        if  -d/2<Carbon12.pos.x<d/2 and Pmin<=Carbon12.pos.y<=0:v5=150000#difference de potentielle pour la partie inférieur du cyclotron
        if  -d/2<Carbon12.pos.x<d/2 and 0<Carbon12.pos.y<=Pmax:v5=-150000#Difference de potentielle pour la partie supérieur du clyclotron
        if  Carbon12.pos.x<-d/2 or Carbon12.pos.x>d/2:v5=0#Difference de potentielle nul dans l'interstice
        
        #Lorsque la charge arrive vers le tunelle , le volt , le champ magnétique et l'accelation est nul
        if  Carbon12.pos.y<=-R and Carbon12.pos.x>=R/2:
            v5=0
            B=B0
            a=vector(0,0,0)
            
        #Lorsque la charge touche la cible , afficher la vitesse du carbon12 , afficher la période du cyclotron et arreter le programme avec (break)          
        if Carbon12.pos.x>=D and Carbon12.pos.y<=-R:
            print("la vitesse est de :", mag(vCarbon12))
            print ("la periode est de :",T)
            print ("le temps pour sortir du cyclotron est de ",n*T) #temps a la sortir du cyclotron
            break
               
        
        #Equation de la force electrique   
        Fe=vector((v5*qCarbon12)/d,0,0)
        #Equation de la magnétique
        Fm=qCarbon12*cross(vCarbon12,B)
        #Equation d'accelation causé par les 2 forces par la 2em loi de Newton
        a=(Fe+Fm)/mCarbon12


        #equation Mrua
        Carbon12.pos=Carbon12.pos+vCarbon12*dt+0.5*a*dt**2 #equation du changement de postion en  x de l'électron apres un intervalle de temps
        vCarbon12=vCarbon12+a*dt#equation du changement de la vitesse de l'électron , selon l'axe x, apres un intervalle de temps
        
        trace.append(pos=Carbon12.pos)#executer la trace

        #j'obtiens une vitesse en utilisant l'equation: V=squrt((V*qCarbon12*2)/mCarbon12)et la periode: T=((2*3.14*mCarbon12))/(qCarbon12*mag(Bmax))
        #jai obtenue 13717718.6677 pour la vitesse et 4.36437786101e-07 pour la période
        #le temps que le carbon 12 met a sortir du cyclotron est different du nombre de tour fois la période car le programme prend en compte la partie de l'interstice pour calculer le temps

