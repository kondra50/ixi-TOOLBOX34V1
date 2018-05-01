from numpy import *

from sklearn import  linear_model

def  compute_error_for_goven_point(b,m,points):
    totalError = 0
    for i in range(0,len(points)):
        x=points[i,0]
        y= points(i,1)
        totalError+=(y-(m*x +b)) **2
    return totalError/float(len(points))





def step_gradiant(b_current,m_current, points, learning_rate):
    b_gradient= 0
    m_gradient = 0
    N=float(len(points))
    for i in range(0, len(points)):
        x=points(i,1)
        y=points(i,0)
        b_gradient+= -(2/N)*(y-((m_current * x)+ b_current))
        m_gradient+= -(2/N)*x*(y-((m_current * x)+ b_current))
    new_b= b_current -(learning_rate * b_gradient)
    new_m= m_current -(learning_rate * b_gradient)
    return [new_b,new_m]

def gradient_descent_runner(points,initial_b,initial_m,learning_rate,num_iterations):
    b=initial_b
    m=initial_m
    for i in range(num_iterations):
        b,m= step_gradiant(b,m, array(points), learning_rate)
    return [b,m]


def run():
    points= genfromtxt('data.csv',delimiter=',')
    learning_rate=0.00001
    initial_b=0
    initial_m=0
    num_iterations=1000
    [b,m]= gradient_descent_runner(points,initial_b,initial_m,learning_rate,num_iterations)
    print(m)
    print(b)


if  __name__ == '__ main __':
    run()