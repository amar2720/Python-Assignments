#!/usr/bin/env python
# coding: utf-8

# ### 1.Create a zoo.py file first. Define the hours() function, which prints the string 'Open 9-5 daily'. Then, use the interactive interpreter to import the zoo module and call its hours() function.

# In[4]:


def hours():
    print('Open 9-5 daily')
hours()


# In[ ]:


# Interactive console output
"""
>>> import Assignment_18
Open 9-5 daily

"""


# ### 2.In the interactive interpreter, import the zoo module as menagerie and call its hours() function.

# In[9]:


# Interactive console output
"""
>>> import Assignment_18 as menagerie
>>> menagerie.hours()
Open 9-5 daily
"""


# ### 3. Using the interpreter, explicitly import and call the hours() function from zoo.

# In[10]:


# Interactive console outout

"""
>>> from Assignment_18 import hours
>>> hours()
Open 9-5 daily
"""


# ### 4. Import the hours() function as info and call it.

# In[11]:


# Interactive console output
"""
>>> from Assignment_18 import hours as info
>>> info()
Open 9-5 daily
"""


# ### 5.Create a plain dictionary with the key-value pairs 'a': 1, 'b': 2, and 'c': 3, and print it out.

# In[13]:


# Interactive console output
"""
>>> plain = {'a':1,'b':2,'c':3}
>>> plain
{'a': 1, 'b': 2, 'c': 3}
"""


# ### 6.Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the same order as plain?

# In[14]:


# Interactive console output
"""
>>> from collections import OrderedDict
>>> fancy = OrderedDict([('a',1),('b',2),('c',2)])
>>> fancy
OrderedDict([('a', 1), ('b', 2), ('c', 2)])
"""


# ### 7. Make a default dictionary called dict_of_lists and pass it the argument list. Make the list dict_of_lists['a'] and append the value 'something for a' to it in one assignment. Print dict_of_lists['a'].

# In[15]:


# Interactive console output
"""
>>> from collections import defaultdict
>>> dict_of_lists = defaultdict(list)
>>> dict_of_lists['a'].append('something for a')
>>> dict_of_lists['a']
['something for a']
"""


# In[ ]:




