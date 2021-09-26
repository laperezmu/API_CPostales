import pandas as pd
import mysql.connector

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)



route = r'C:\Users\user\Desktop\proyecto_cd\RecursosBD_SEPOMEX\CPdescarga.xls'
colonias = pd.DataFrame()
municipios = pd.DataFrame()
estados = pd.DataFrame()

# for x in range(0,32):

#    excelS = pd.read_excel(route,
#                           sheet_name= x,
#                           dtype=str,
#                          ) 

#    excelS['c_CP'] =  excelS['c_estado']+excelS['c_mnpio']

#    tabla_colonias = excelS.loc[excelS['d_tipo_asenta']=='Colonia', ['d_codigo', 'd_asenta','c_CP']]
#    colonias = pd.concat([colonias,
#                          tabla_colonias])

#    # tabla_municipios = excelS.loc[excelS['d_tipo_asenta']=='Colonia', ['c_CP', 'D_mnpio','c_estado']].drop_duplicates()
#    # municipios = pd.concat([municipios,
#    #                         tabla_municipios])
   
#    # tabla_estados = excelS[['c_estado', 'd_estado']]
#    # estados = pd.concat([estados,
#    #                      tabla_estados]).drop_duplicates()



# compression_opts = dict(method='zip',
#                         archive_name='out.csv')  
# colonias.to_csv('out.zip', encoding='utf-8-sig', index=False,
#           compression=compression_opts)  



