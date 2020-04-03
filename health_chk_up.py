#health check up
def bp(s,d):
    if s<120 and d<80:
        print('you have normal condition')
    elif s in range(120,130) and d < 80:
        print('ypur bp has elevated')
    elif s in range(130,140) or d in range (80,90):
        print('you are having hypertension stage 1')
    elif s >=140 and d >=90:
        print('you are having hyper tension stage 2')
    elif s>180 or d >120:
        print('you are having hypertension stage 3.... consult a doctor immediately ')
    
def bmi(w,h):
    BMI=w/h**2
    print('your bmi is', BMI )

    

    
#main program
chk_type=input('what do you want to analyse[bp/bmi]: ')

if chk_type=='bp':
        s=int( input('please enter your systolic bp: '))
        d=int( input('please enter your diastolic bp: '))
        bp(s,d)
elif chk_type=='bmi':
        w=float(input('please enter your weight in kgs: '))
        h=float(input('please enter your height in (m): '))
        bmi(w,h)
