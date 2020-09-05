#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install datapackage


# In[1]:


from datapackage import Package

package = Package('https://datahub.io/core/s-and-p-500-companies-financials/datapackage.json')

# print list of all resources:
print(package.resource_names)

# print processed tabular data (if exists any)
for resource in package.resources:
    if resource.descriptor['datahub']['type'] == 'derived/csv':
        print(resource.read())
        
        
        
        


# In[1]:


import datapackage
import pandas as pd

data_url = 'https://datahub.io/core/s-and-p-500-companies/datapackage.json'

# to load Data Package into storage
package = datapackage.Package(data_url)

# to load only tabular data
resources = package.resources
for resource in resources:
    if resource.tabular:
        data = pd.read_csv(resource.descriptor['path'])
        print (data)


# In[4]:


data.info


# In[ ]:




