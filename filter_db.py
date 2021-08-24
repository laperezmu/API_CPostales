import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)



route = r'C:\Users\user\Desktop\proyecto_cd\RecursosBD_SEPOMEX\CPdescarga.xls'
colonias = pd.DataFrame()
municipios = pd.DataFrame()
estados = pd.DataFrame()

for x in range(0,32):

   # excelS = pd.read_excel(route,
   #                        sheet_name= x 
   #                       ) 
   # tabla_colonias = excelS.loc[excelS['d_tipo_asenta']=='Colonia', ['d_codigo', 'd_asenta','c_mnpio']]
   # colonias = pd.concat([colonias,
   #                       tabla_colonias])


   excelS = pd.read_excel(route,
                          sheet_name= x 
                         ) 
   tabla_municipios = excelS.loc[excelS['d_tipo_asenta']=='Colonia', ['c_mnpio', 'D_mnpio','c_estado']].drop_duplicates()
   municipios = pd.concat([municipios,
                           tabla_municipios])
   

   # excelS = pd.read_excel(route,
   #                        sheet_name= x 
   #                       ) 
   # tabla_estados = excelS[['c_estado', 'd_estado']]
   # estados = pd.concat([estados,
   #                      tabla_estados]).drop_duplicates()


compression_opts = dict(method='zip',
                        archive_name='out_Municipios.csv')  

# colonias.to_csv('outCol.zip', index=False,
#           compression=compression_opts)  

municipios.to_csv('outMun.zip', index=False,
          compression=compression_opts)  

# estados.to_csv('outEst.zip', index=False,
#           compression=compression_opts)  

