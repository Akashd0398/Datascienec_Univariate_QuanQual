class Univariate():
      
      def quanQual(dataset):
          qual=[]
          quan=[]
          for columnames in dataset.columns:
            #print(columnames)
              if(dataset[columnames].dtypes=='O'):
                #print('qual')
                  qual.append(columnames)
              else:
                #print('quan')
                  quan.append(columnames)
          return qual,quan

      def FreqTable(columnames,dataset):
          import pandas as pd
          fTable=pd.DataFrame(columns=["Unique_Values","Frequency","Relative Frequency","Cumsum"])
          fTable["Unique_Values"]=dataset[columnames].value_counts().index
          fTable["Frequency"]=dataset[columnames].value_counts().values
          fTable["Relative Frequency"]=(fTable["Frequency"]/fTable.shape[0])
          fTable["Cumsum"]=fTable["Relative Frequency"].cumsum()
          return fTable

      def univariate(dataset,quan):
          import pandas as pd
          import numpy as np
          descriptive=pd.DataFrame(index=(["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%",
                                       "Q4:100%","IQR","1.5rule","lesser","greater","min","max","Skew","Kurtosis"]),columns = quan)
          for columnames in quan:
              descriptive[columnames]["Mean"] = dataset[columnames].mean()
              descriptive[columnames]["Median"] = dataset[columnames].median()
              descriptive[columnames]["Mode"] = dataset[columnames].mode()[0]
              descriptive[columnames]["Q1:25%"] = np.percentile(dataset[columnames],25)
              descriptive[columnames]["Q2:50%"] = np.percentile(dataset[columnames],50)
              descriptive[columnames]["Q3:75%"] = np.percentile(dataset[columnames],75)
              descriptive[columnames]["99%"] = np.percentile(dataset[columnames],99)
              descriptive[columnames]["Q4:100%"] = np.percentile(dataset[columnames],100)
              descriptive[columnames]["IQR"] = descriptive[columnames]["Q3:75%"] - descriptive[columnames]["Q1:25%"]
              descriptive[columnames]["1.5rule"] = 1.5 * descriptive[columnames]["IQR"]
              descriptive[columnames]["lesser"] = descriptive[columnames]["Q1:25%"] - descriptive[columnames]["1.5rule"]
              descriptive[columnames]["greater"] = descriptive[columnames]["Q3:75%"] + descriptive[columnames]["1.5rule"]
              descriptive[columnames]["min"] = dataset[columnames].min()
              descriptive[columnames]["max"] = dataset[columnames].max()
              descriptive[columnames]["Skew"] = dataset[columnames].skew()
              descriptive[columnames]["Kurtosis"] = dataset[columnames].kurtosis()
          return descriptive

    
    
