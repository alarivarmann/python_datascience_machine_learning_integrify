#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def mlp(x,w1,w2):
    onecol = torch.ones((N,1),dtype=torch.float)
    x = torch.cat((onecol,x),1)
    hidden_values = (x @ w1).clamp(min=0)
    hidden_values = torch.cat((onecol,hidden_values),1)
    return  hidden_values @ w2 

def mse_(tensor1,tensor2):
    diff = tensor1-tensor2
    mse_ = torch.sum(diff**2) / diff.numel()
    return mse_

