class Univariate:
    def quanqual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            if(dataset[columnName].dtype=="object"):
                qual.append(columnName)
            else:
                quan.append(columnName)   
        return quan,qual;