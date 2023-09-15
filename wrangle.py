import pandas as pd
from env import get_connection
import os
from sklearn.model_selection import train_test_split

def get_zillow_data():
    
    filename = 'zillow.csv'
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)    
    else:    
        url = get_connection('zillow')   
        sql = '''SELECT *

        FROM properties_2017
        FULL JOIN predictions_2017 USING (parcelid)
        LEFT JOIN airconditioningtype USING (airconditioningtypeid)
        LEFT JOIN architecturalstyletype USING (architecturalstyletypeid)
        LEFT JOIN buildingclasstype USING (buildingclasstypeid)
        LEFT JOIN heatingorsystemtype USING (heatingorsystemtypeid)
        LEFT JOIN propertylandusetype USING (propertylandusetypeid)
        LEFT JOIN storytype USING (storytypeid)
        LEFT JOIN typeconstructiontype USING (typeconstructiontypeid)
        WHERE transactiondate <= '2017-12-31';
        '''   
        df = pd.read_sql(sql, url)        
        df.to_csv(filename, index=False)    
        return df