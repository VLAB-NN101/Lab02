import torch

def train(x_train,label):
    ### Implement from here ###
    
    return w,b

def main():

    x_train = torch.tensor([0.0, 1.0, 2.0, 3.0, 4.0])
    label = torch.tensor([2.0, 4.0, 6.0, 8.0, 10.0])
    x_test = torch.tensor([5.0, 10.0, 8.0])
    
    w,b = train(x_train, label) # Implement this
    
    y = w*x_test + b
    return y
    
main()
