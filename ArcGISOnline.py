#!/usr/bin/env python
# coding: utf-8

# ## Welcome to your notebook.
# 

# #### Run this cell to connect to your GIS and get started:

# In[3]:


from arcgis.gis import GIS
gis = GIS("home")


# #### Now you are ready to start!

# In[4]:


map1 = gis.map("Atlanta, GA")
map1


# In[2]:


map1 = gis.map("Atlanta,GA")


# In[5]:


# Item Added From Toolbar
# Title: Atlanta Police Crime Reports UCR 2009 to March 2020 | Type: Feature Service | Owner: emelineR
item = gis.content.get("0856147c8eee49f29470c46e5a6da6ed")
item


# In[6]:


map1.add_layer(item)


# In[ ]:




