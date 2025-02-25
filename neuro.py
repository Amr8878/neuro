
def tanh(x):
    return (2 / (1 + (2.71828 ** (-2 * x)))) - 1


i1, i2 = 0.05, 0.10 


w = [0.2, -0.3, 0.4, -0.2, 0.1, -0.5]  


b1, b2 = 0.5, 0.7


net_h1 = w[0] * i1 + w[1] * i2 + b1
net_h2 = w[2] * i1 + w[3] * i2 + b1

out_h1 = tanh(net_h1)
out_h2 = tanh(net_h2)


net_o1 = w[4] * out_h1 + w[5] * out_h2 + b2
out_o1 = tanh(net_o1)


print(f"Hidden layer outputs: h1={out_h1:.6f}, h2={out_h2:.6f}")
print(f"Output layer result: o1={out_o1:.6f}")


# In[ ]:




