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