#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def clean_gender_column(df1):
    '''
    This function will take a Pandas DataFrame as an input and it will replace the values in\n",
    the \"GENDER\" column ins such a way that any gender which is not Male or Female with be \n",
    replaced by \"U\" otherwise the genders will be either \"F\" or \"M\"\n",
    
    Inputs:
    df: Pandas DataFrame
    Outputs:
    A pandas DataFrame with the values in the \"gender\" column cleaned.
    '''
   
    df2 = df1.copy()
       
    df2[['GENDER']] = df2[['GENDER']].astype(str)
    
    if "gender" not in df2.columns:
        return df2
    else:
    
        #df2['GENDER'] = df2['GENDER'].apply(lambda x: x[0].upper if x[0].upper in ['M', 'F'] else \"U\")\n",
        df2['GENDER'] = list(map(lambda x: x[0].upper() if x[0].upper() in ['M', 'F'] else "U", df2['GENDER']))
        return df2


# In[ ]:


def drop_null(df1):
    '''
    This function will drop null values from df1
   
    Inputs:
    df: Pandas DataFrame
    
    Outputs:
    A pandas DataFrame with the values null values dropped.
    '''
    
    df2 = df1.copy()
    df3 = df2.dropna()
    return df3


# In[ ]:


def drop_duplicates(df1):
    '''
    This function will drop duplicates  from df1
    
    Inputs:
    df: Pandas DataFrame
    
    Outputs
    A pandas DataFrame with the values null values dropped.
    '''
    
    df2 = df1.copy()
    df3 = df2.drop_duplicates()
    return df3

