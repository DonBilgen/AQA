data1=['Notes', 'WorkSpace', 'React', 'Angular', 'Veu', 'General', 'Downloads', 'Word File.doc', 'Excel File.doc']

data2=['notes', 'workspace', 'react', 'angular', 'veu', 'general', 'downloads', 'wordFile', 'excelFile']

data_1=str(data1).replace(' ','').replace('.doc','').lower()
data_2=str(data2).replace(' ','').lower()

assert  data_1==data_2, 'Error: not='