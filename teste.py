from tkinter import font
from numpy.core.fromnumeric import size
from numpy.core.numeric import True_
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from datetime import datetime

#df = pd.read_csv('atendimentos.csv', sep=';',encoding='cp1252',usecols=[1,2,7,9,11,14,55,56,57])
df = pd.read_csv('atendimentos.csv', sep=';',encoding='cp1252',usecols=[3,4,5,7,8,12,15,16,20,26,29,30,34,35,38,39,41,44,46,49,51,54,60,61,62,63,64,65])
root = tk.Tk()
root.title('Controle de Retorno Safra')
dimension='1300x680'
root.geometry(dimension)
root.configure(background='RoyalBlue')
root.resizable(False,False)


#responsive
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

#data de hoje
local_dt = datetime.now()
dt_hoje = local_dt.strftime("%d/%m/%y - %H:%M:%S")



atendimento_ag_mob = df.loc[(df[' STATUS'] == 'EM ATENDIMENTO') & (df[' QT. AGENDAMENTO'] == 0) & (df[' ACAO PRÉ-BAIXA MOBILE'] == 'PRE-AGENDAMENTO') ]
atendimento_ag_ctb = df.loc[(df[' STATUS'] == 'EM ATENDIMENTO') & (df[' QT. AGENDAMENTO'] == 0) & (df[' ACAO PRÉ-BAIXA CENTRAL'] == 'PRE-AGENDAMENTO') & (df[' MOTIVO AGENDAMENTO'] != 'PROBLEMA DE ATIVAÇÃO DE POS')& (df[' MOTIVO AGENDAMENTO'] != 'EQUIPAMENTO COM PROBLEMAS') ]

atendimento_ag_ctb_troca = df.loc[(df[' STATUS'] == 'EM ATENDIMENTO') & (df[' QT. AGENDAMENTO'] == 0)  & (df[' MOTIVO AGENDAMENTO'] == 'PROBLEMA DE ATIVAÇÃO DE POS')]
atendimento_ag_ctb_troca_equi = df.loc[(df[' STATUS'] == 'EM ATENDIMENTO') & (df[' QT. AGENDAMENTO'] == 0) & (df[' MOTIVO AGENDAMENTO'] == 'EQUIPAMENTO COM PROBLEMAS')]

atendimento_pre_enc = df.loc[(df[' STATUS'] == 'EM ATENDIMENTO') & (df[' ACAO PRÉ-BAIXA MOBILE'] == 'PRE-ENCERRAMENTO')]
atendimento_pre_enc = atendimento_pre_enc.reset_index(drop=True)
atendimento_pre_ativ = df.loc[(df[' STATUS'] == 'EM ATENDIMENTO') & (df[' ACAO PRÉ-BAIXA'] == 'PRE-ENCERRAMENTO')]
atendimento_pre_ativ = atendimento_pre_ativ.reset_index(drop=True)
atendimento_canc_ctb = df.loc[(df[' STATUS'] == 'EM ATENDIMENTO') & (df[' ACAO PRÉ-BAIXA CENTRAL'] == 'PRE-CANCELAMENTO')]
atendimento_canc_ctb = atendimento_canc_ctb.reset_index(drop=True)

atendimento_canc_mob = df.loc[(df[' STATUS'] == 'EM ATENDIMENTO') & (df[' ACAO PRÉ-BAIXA MOBILE'] == 'PRE-CANCELAMENTO')]
atendimento_canc_mob = atendimento_canc_mob.reset_index(drop=True)
atendimento_fora = df.loc[(df['SLA'] == 'FORA') & (df[' STATUS'] == "EM ATENDIMENTO")& (df['MOBILE'] == "NÃO")& (df['PRÉ-BAIXA'] == "NÃO")& (df['PB CENTRAL'] == "NÃO")]
atendimento_fora = atendimento_fora.reset_index(drop=True)
atendimento_ag_mob2 = atendimento_ag_mob[' SERVIÇO'].value_counts()

atendimento_pre_enc2 = atendimento_pre_enc[' SERVIÇO'].value_counts()
atendimento_pre_ativ2 = atendimento_pre_ativ[' SERVIÇO'].value_counts()

atendimento_fora_tec = atendimento_fora[' TÉCNICO'].value_counts()

atendimento_cxs = df.loc[(df[' STATUS'] == 'EM ATENDIMENTO') & (df[' TÉCNICO'] == 'ANDERSON AZEVEDO MARIANI')]
atendimento_geziel = df.loc[(df[' STATUS'] == 'EM ATENDIMENTO') & (df[' TÉCNICO'] == 'GEZIEL BARBOSA DA SILVA')]

atendimento_ag_mob = atendimento_ag_mob.reset_index(drop=True)
atendimento_ag_ctb = atendimento_ag_ctb.reset_index(drop=True)

teste = atendimento_ag_ctb[' TÉCNICO'].value_counts()
teste4 = atendimento_ag_mob[' TÉCNICO'].value_counts()
tecnicos_troca = atendimento_ag_ctb_troca[' TÉCNICO'].value_counts()
tecnicos_troca_equi = atendimento_ag_ctb_troca_equi[' TÉCNICO'].value_counts()
teste1 = atendimento_ag_ctb[' TÉCNICO']
teste3 = len(teste.index)
atendimento_canc_ctb2 = atendimento_canc_ctb[' SERVIÇO'].value_counts()
atendimento_canc_mob2 = atendimento_canc_mob[' SERVIÇO'].value_counts()
atendimento_fora2 = atendimento_fora[' TÉCNICO'].value_counts()
teste_canc = len(atendimento_canc_ctb)

soma_troca = len(tecnicos_troca.index) + len(tecnicos_troca_equi.index)

total_atendimento = df.loc[(df[' STATUS'] == 'EM ATENDIMENTO' )]
total_atendimento = total_atendimento.reset_index(drop=True)
total_pendente = df.loc[(df[' STATUS'] == 'PENDENTE' )]
total_enc = df.loc[(df[' STATUS'] == 'ENCERRADO' )]
total_cancel = df.loc[(df[' STATUS'] == 'CANCELADO' )]
total_pendente = total_pendente.reset_index(drop=True)
total_enc = total_enc.reset_index(drop=True)
total_cancel = total_cancel.reset_index(drop=True)
total_pre = df.loc[(df[' STATUS'] == 'PRÉ-SAÍDA' )]
total_pre = total_pre.reset_index(drop=True)

def semComando():
   print("oi")
def select_mob():
   value = str(listbox_tec_ag_mob.get(ACTIVE))
   tit = "Dados do Agendamento Mobile"
   size = "800x500"
   new = Tk()
   new.geometry(size)
   new.title(tit)
   new.resizable(False,False)
   my_frame = Frame(new)
   my_frame.pack(pady=5)
   text_scroll = Scrollbar(my_frame)
   text_scroll.pack(side=RIGHT, fill=Y)
   my_text = Text(my_frame, width=90,height=25,font=("Helvetica",12),selectbackground="yellow",selectforeground="black",undo=True,yscrollcommand=text_scroll)
   my_text.pack()
   text_scroll.config(command=my_text.yview) 

   agend = atendimento_ag_mob.loc[(atendimento_ag_mob[' SERVIÇO'] == value) ]
   agend_os = agend.set_index(['NUMERO O.S. CS1'])
   agend_tec = agend.set_index([' TÉCNICO'])
   agend_cit = agend.set_index([' CIDADE'])
   quebra = "--------------"*9

   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END,"                  Serviço: ")
   my_text.insert(END,value)
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END,"Numero Os: ")
   my_text.insert(END,"\n")
   for x in range(len(agend_os)):
      my_text.insert(END,agend_os.index[x])
      my_text.insert(END,", ")
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END,"Técnico: ")
   my_text.insert(END,"\n")
   for x in range(len(agend_tec)):
      my_text.insert(END,"\n")
      my_text.insert(END,x)
      my_text.insert(END," - ")
      my_text.insert(END,agend_tec.index[x])
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END,"Cidade: ")
   my_text.insert(END,"\n")
   for x in range(len(agend_cit)):
      my_text.insert(END,"\n")
      my_text.insert(END,x)
      my_text.insert(END," - ")
      my_text.insert(END,agend_cit.index[x])
   new.mainloop()
def select_pre_canc():
   value = str(listbox_tec_canc.get(ACTIVE))
   quebra="------------"*10
   tit = "Dados do Cancelamento"
   size = "800x500"
   new = Tk()
   new.geometry(size)
   new.title(tit)
   new.resizable(False,False)
   my_frame = Frame(new)
   my_frame.pack(pady=5)
   text_scroll = Scrollbar(my_frame)
   text_scroll.pack(side=RIGHT, fill=Y)

   my_text = Text(my_frame, width=90,height=25,font=("Helvetica",12),selectbackground="yellow",selectforeground="black",undo=True,yscrollcommand=text_scroll)
   my_text.pack()
   text_scroll.config(command=my_text.yview)
   pre_tec_ctb= atendimento_canc_ctb.loc[(atendimento_canc_ctb[' SERVIÇO'] == value) ]
   pre_tec_mob= atendimento_canc_mob.loc[(atendimento_canc_mob[' SERVIÇO'] == value) ]
   tecnico = pre_tec_ctb[' TÉCNICO'].value_counts()
   tecnico_mob = pre_tec_mob[' TÉCNICO'].value_counts()
   tecnico_os = pre_tec_ctb['NUMERO O.S. CS1'].value_counts()
   tecnico_os_mob = pre_tec_mob['NUMERO O.S. CS1'].value_counts()
   def save():
      file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Documento de Texto",".txt")])
      conteudo = str(my_text.get(1.0,END))
      file.write(conteudo)

   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END,"                  Serviço: ")
   my_text.insert(END,value)
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END,"Número Os: ")
   my_text.insert(END,"\n")
   for x in range(len(tecnico_os)):
      my_text.insert(END,tecnico_os.index[x])
      my_text.insert(END,", ")
   for x in range(len(tecnico_os_mob)):
      my_text.insert(END,tecnico_os_mob.index[x])
      my_text.insert(END,", ")
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END,"OS Lista: ")
   my_text.insert(END,"\n")
   my_text.insert(END,"\n")
   for s in range(len(tecnico_os)):
      my_text.insert(END,tecnico_os.index[s])
      my_text.insert(END,"\n")
   for s in range(len(tecnico_os_mob)):
      my_text.insert(END,tecnico_os_mob.index[s])
      my_text.insert(END,"\n")
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END,"Técnico: ")
   my_text.insert(END,"\n")
   for x in range(len(pre_tec_ctb)):
      my_text.insert(END,"\n")
      my_text.insert(END,tecnico[x])
      my_text.insert(END," - ")
      my_text.insert(END,tecnico.index[x])
   for x in range(len(pre_tec_mob)):
      my_text.insert(END,"\n")
      my_text.insert(END,tecnico_mob[x])
      my_text.insert(END," - ")
      my_text.insert(END,tecnico_mob.index[x])
   label_salvar = tk.Button(new, text='SALVAR',bg='blue', fg="white",command=save)
   label_salvar.place(relx=0.04,rely=.935,relheight=.05,relwidth=.07)

   new.mainloop()
def select_pre_ativ():
   quebra = "--------------"*9
   value = str(listbox_tec_ativ.get(ACTIVE))
   tit = "Dados da Ativação"
   size = "800x500"
   new = Tk()
   new.geometry(size)
   new.title(tit)
   new.resizable(False,False)
   my_frame = Frame(new)
   my_frame.pack(pady=5)
   text_scroll = Scrollbar(my_frame)
   text_scroll.pack(side=RIGHT, fill=Y)
   my_text = Text(my_frame, width=80,height=23,font=("Helvetica",12),selectbackground="yellow",selectforeground="black",undo=True,yscrollcommand=text_scroll)
   my_text.pack()
   text_scroll.config(command=my_text.yview) 
   pre_ativ = atendimento_pre_ativ.loc[(atendimento_pre_ativ[' SERVIÇO'] == value) ]
   pre_ativ = pre_ativ.reset_index(drop=True)
   tecnico = pre_ativ[' TÉCNICO']
   tecnico = pre_ativ[' TÉCNICO'].value_counts()
   tecnico_os = pre_ativ['NUMERO O.S. CS1']
   tecnico_os = pre_ativ['NUMERO O.S. CS1'].value_counts()
   serie_pre =  pre_ativ[' SERIAL A RETIRAR']
   serie_pre =  pre_ativ[' SERIAL A RETIRAR'].value_counts()
   tecnico_dt = pre_ativ[' DTHR PRE-BAIXA']
   tecnico_dt = pre_ativ[' DTHR PRE-BAIXA'].value_counts()
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END,"                  Serviço: ")
   my_text.insert(END,value)
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END,"Técnico: ")
   my_text.insert(END,"\n")
   for x in range(len(tecnico)):
      my_text.insert(END,"\n")
      my_text.insert(END,tecnico[x])
      my_text.insert(END," - ")
      my_text.insert(END,tecnico.index[x])

   my_text.insert(END,"\n")
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   cont = 0
   my_text.insert(END,"O.s: ")
   my_text.insert(END,"\n")
   for x in range(len(tecnico_os)):
      my_text.insert(END,cont)
      my_text.insert(END," - ")
      my_text.insert(END,tecnico_os.index[x])
      my_text.insert(END,"\n")
      cont+=1
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)  
   my_text.insert(END,"\n")
   my_text.insert(END,"O.s separada: ")
   my_text.insert(END,"\n")
   cont=1
   for x in range(len(tecnico_os)):
      my_text.insert(END,tecnico_os.index[x])
      my_text.insert(END,", ")
      cont+=1
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)  
   my_text.insert(END,"\n")
   my_text.insert(END, "Série a Devolver: ")
   my_text.insert(END,"\n")
   cont=0
   for i in range(len(serie_pre)):
      my_text.insert(END,"\n")
      my_text.insert(END,cont) 
      my_text.insert(END," - ") 
      my_text.insert(END,serie_pre.index[i])
      cont+=1
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)  
   my_text.insert(END,"\n")
   cont=0
   my_text.insert(END, "Data e Hora da Baixa: ")
   my_text.insert(END,"\n")
   for i in range(len(tecnico_dt)): 
      my_text.insert(END,"\n")
      my_text.insert(END,cont)  
      my_text.insert(END," - ")
      my_text.insert(END,tecnico_dt[i])
      my_text.insert(END," - ")
      my_text.insert(END,tecnico_dt.index[i])
      cont+=1
   
   new.mainloop()
def select_pre_enc():
   quebra = "--------------"*9
   value = str(listbox_tec_pre.get(ACTIVE))
   tit = "Dados do Encerramento"
   size = "800x500"
   new = Tk()
   new.geometry(size)
   new.title(tit)
   new.resizable(False,False)
   my_frame = Frame(new)
   my_frame.pack(pady=5)
   text_scroll = Scrollbar(my_frame)
   text_scroll.pack(side=RIGHT, fill=Y)
   my_text = Text(my_frame, width=80,height=23,font=("Helvetica",12),selectbackground="yellow",selectforeground="black",undo=True,yscrollcommand=text_scroll)
   my_text.pack()
   text_scroll.config(command=my_text.yview) 
   
   pre_tec= atendimento_pre_enc.loc[(atendimento_pre_enc[' SERVIÇO'] == value) ]
   tecnico = pre_tec[' TÉCNICO']
   tecnico = pre_tec[' TÉCNICO'].value_counts()
   tecnico_os = pre_tec['NUMERO O.S. CS1']
   tecnico_os = pre_tec['NUMERO O.S. CS1'].value_counts()
   tecnico_dt = pre_tec[' DTHR PRÉ-BAIXA MOBILE']
   tecnico_dt = pre_tec[' DTHR PRÉ-BAIXA MOBILE'].value_counts()
   obs_pre = pre_tec[' OBSERVAÇÃO']
   obs_pre = pre_tec[' OBSERVAÇÃO'].value_counts()
   modelo = pre_tec[' MODELO EQUIPAMENTO']
   modelo = pre_tec[' MODELO EQUIPAMENTO'].value_counts()
   serie_pre =  pre_tec[' SERIAL A RETIRAR']
   serie_pre =  pre_tec[' SERIAL A RETIRAR'].value_counts()
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END,"                  Serviço: ")
   my_text.insert(END,value)
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END,"Técnico: ")
   my_text.insert(END,"\n")
   for x in range(len(tecnico)):
      my_text.insert(END,"\n")
      my_text.insert(END,tecnico[x])
      my_text.insert(END," - ")
      my_text.insert(END,tecnico.index[x])

   my_text.insert(END,"\n")
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   cont = 0
   my_text.insert(END,"O.s: ")
   my_text.insert(END,"\n")
   for x in range(len(tecnico_os)):
      my_text.insert(END,cont)
      my_text.insert(END," - ")
      my_text.insert(END,tecnico_os.index[x])
      my_text.insert(END,"\n")
      cont+=1
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)  
   my_text.insert(END,"\n")
   my_text.insert(END,"O.s separada: ")
   my_text.insert(END,"\n")
   cont=1
   for x in range(len(tecnico_os)):
      my_text.insert(END,tecnico_os.index[x])
      my_text.insert(END,", ")
      cont+=1
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)  
   my_text.insert(END,"\n")
   cont=0
   my_text.insert(END, "Data e Hora da Baixa: ")
   my_text.insert(END,"\n")
   for i in range(len(tecnico_dt)): 
      my_text.insert(END,"\n")
      my_text.insert(END,cont)  
      my_text.insert(END," - ")
      my_text.insert(END,tecnico_dt[i])
      my_text.insert(END," - ")
      my_text.insert(END,tecnico_dt.index[i])
      cont+=1
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END, "Modelo Equipamento: ")
   my_text.insert(END,"\n")
   for i in range(len(modelo)):
      my_text.insert(END,"\n") 
      my_text.insert(END,modelo[i])
      my_text.insert(END," - ")
      my_text.insert(END,modelo.index[i])
      my_text.insert(END,"\n")
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")

   my_text.insert(END, "Série a Devolver: ")
   my_text.insert(END,"\n")
   cont=0
   for i in range(len(serie_pre)):
      my_text.insert(END,"\n")
      my_text.insert(END,cont) 
      my_text.insert(END," - ") 
      my_text.insert(END,serie_pre.index[i])
      cont+=1
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   cont=0
   my_text.insert(END, "Observação atendimento: ")
   my_text.insert(END,"\n")
   for i in range(len(obs_pre)):
      my_text.insert(END,"\n") 
      my_text.insert(END,cont) 
      my_text.insert(END," - ")
      my_text.insert(END,obs_pre.index[i])
      my_text.insert(END,"\n")
      cont+=1
   my_text.insert(END,"\n")
   new.mainloop()

def select_troca_ctb():
   quebra = "--------------"*9
   value = str(listbox_troc_tec.get(ACTIVE))
   tit = "Dados do Agendamento com Troca"
   size = "800x500"
   new = Tk()
   new.geometry(size)
   new.title(tit)
   new.resizable(False,False)
   


   my_frame = Frame(new)
   my_frame.pack(pady=5)
   text_scroll = Scrollbar(my_frame)
   text_scroll.pack(side=RIGHT, fill=Y)
   my_text = Text(my_frame, width=80,height=23,font=("Helvetica",12),selectbackground="yellow",selectforeground="black",undo=True,yscrollcommand=text_scroll)
   my_text.pack()
   text_scroll.config(command=my_text.yview) 
   novo_troca= atendimento_ag_ctb_troca.loc[(atendimento_ag_ctb_troca[' TÉCNICO'] == value) ]
   novo_troca_equip = atendimento_ag_ctb_troca_equi.loc[(atendimento_ag_ctb_troca_equi[' TÉCNICO'] == value) ]
   modelo = novo_troca.set_index([' MODELO EQUIPAMENTO']) 
   modelo_equip = novo_troca_equip.set_index([' MODELO EQUIPAMENTO'])
   novo_os = novo_troca.set_index(['NUMERO O.S. CS1'])
   novo_os_equi = novo_troca_equip.set_index(['NUMERO O.S. CS1'])
   novo_serv = novo_troca[' SERVIÇO']
   novo_serv = novo_serv.value_counts()
   novo_serv_equip = novo_troca_equip[' SERVIÇO']
   novo_serv_equip = novo_serv_equip.value_counts()

   motivo_troca = novo_troca.set_index([' MOTIVO AGENDAMENTO'])
   motivo_troca_equip = novo_troca_equip.set_index([' MOTIVO AGENDAMENTO'])
 
   data_os = novo_troca[' DTHR LIMITE']
   data_os = data_os.value_counts()
   data_os_equip = novo_troca_equip[' DTHR LIMITE']
   data_os_equip = data_os_equip.value_counts()

   hora_ctb_os = novo_troca[' DTHR PRE-BAIXA CENTRAL']
   hora_ctb_os = hora_ctb_os.value_counts()
   hora_ctb_os_equip = novo_troca_equip[' DTHR PRE-BAIXA CENTRAL']
   hora_ctb_os_equip = hora_ctb_os_equip.value_counts()

   cit_ctb_os = novo_troca[' CIDADE']
   cit_ctb_os = cit_ctb_os.value_counts()
   cit_ctb_os_equip = novo_troca_equip[' CIDADE']
   cit_ctb_os_equip = cit_ctb_os_equip.value_counts()

   end_ctb_os = novo_troca[' ENDEREÇO']
   end_ctb_os = end_ctb_os.value_counts()


   quebra = "--------------"*9
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END,"                  Técnico: ")
   my_text.insert(END,value)
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)

   my_text.insert(END,"\n")
   my_text.insert(END,"O.s Separada: ")
   my_text.insert(END,"\n")
   for i in range(len(novo_os)):    
      my_text.insert(END,novo_os.index[i])
      my_text.insert(END,", ")
   for i in range(len(novo_os_equi)): 
      my_text.insert(END,novo_os_equi.index[i])
      my_text.insert(END,", ")
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END,"Serviços: ")
   my_text.insert(END,"\n")
   for i in range(len(novo_serv)):    
      my_text.insert(END,novo_serv.index[i])
      my_text.insert(END,", ")
   for i in range(len(novo_serv_equip)):    
      my_text.insert(END,novo_serv_equip.index[i])
      my_text.insert(END,", ")
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)   
   my_text.insert(END,"\n")
   my_text.insert(END, "Vencimentos: ")
   my_text.insert(END,"\n")
   for i in range(len(data_os)):   
      my_text.insert(END,data_os[i])
      my_text.insert(END," - ") 
      my_text.insert(END,data_os.index[i])
      my_text.insert(END," , ")
   for i in range(len(data_os_equip)):   
      my_text.insert(END,data_os_equip[i])
      my_text.insert(END," - ") 
      my_text.insert(END,data_os_equip.index[i])
      my_text.insert(END," , ")
      my_text.insert(END,"\n")
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)   
   my_text.insert(END,"\n")
   my_text.insert(END, "Motivo Agendamento: ")
   my_text.insert(END,"\n")
   for i in range(len(motivo_troca)):   
      my_text.insert(END,motivo_troca.index[i])
      my_text.insert(END," , ")
   for i in range(len(motivo_troca_equip)):   
      my_text.insert(END,motivo_troca_equip.index[i])
      my_text.insert(END," , ")
      my_text.insert(END,"\n")
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)   
   my_text.insert(END,"\n")
   my_text.insert(END, "Modelo Equipamento: ")
   my_text.insert(END,"\n")
   for i in range(len(modelo)):   
      my_text.insert(END,modelo.index[i])
      my_text.insert(END," , ")
   for i in range(len(modelo_equip)):   
      my_text.insert(END,modelo_equip.index[i])
      my_text.insert(END," , ")
      my_text.insert(END,"\n")
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)   
   my_text.insert(END,"\n")
   my_text.insert(END, "Cidade: ")
   my_text.insert(END,"\n")
   for i in range(len(cit_ctb_os)):   
      my_text.insert(END,cit_ctb_os.index[i])
      my_text.insert(END," , ")
   for i in range(len(modelo_equip)):   
      my_text.insert(END,cit_ctb_os_equip.index[i])
      my_text.insert(END," , ")
      my_text.insert(END,"\n")
   new.mainloop()

def select_ctb():
  
   value = str(listbox_tec_ag_ctb.get(ACTIVE))
   tit = "Dados do Agendamento CTBSEQ"
   size = "800x500"
   new = Tk()
   new.geometry(size)
   new.title(tit)
   new.resizable(False,False)
   my_frame = Frame(new)
   my_frame.pack(pady=5)
   text_scroll = Scrollbar(my_frame)
   text_scroll.pack(side=RIGHT, fill=Y)
   my_text = Text(my_frame, width=90,height=25,font=("Helvetica",12),selectbackground="yellow",selectforeground="black",undo=True,yscrollcommand=text_scroll)
   my_text.pack()
   text_scroll.config(command=my_text.yview) 
   
   
   novo = atendimento_ag_ctb.loc[(atendimento_ag_ctb[' TÉCNICO'] == value) ]
   novo2 = novo.set_index(['NUMERO O.S. CS1'])
   novo_serv = novo[' SERVIÇO']
   novo_serv = novo_serv.value_counts()
   data_os = novo[' DTHR LIMITE']
   data_os = data_os.value_counts()
   hora_ctb_os = novo[' DTHR PRE-BAIXA CENTRAL']
   hora_ctb_os = hora_ctb_os.value_counts()
   cit_ctb_os = novo[' CIDADE']
   cit_ctb_os = cit_ctb_os.value_counts()
   end_ctb_os = novo[' ENDEREÇO']
   end_ctb_os = end_ctb_os.value_counts()
   motivo_agend = novo.set_index([' MOTIVO AGENDAMENTO'])
   quebra = "--------------"*9
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END,"                  Técnico: ")
   my_text.insert(END,value)
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END,"O.s Separada: ")
   my_text.insert(END,"\n")
   for i in range(len(novo2)):    
      my_text.insert(END,novo2.index[i])
      my_text.insert(END,", ")

   my_text.insert(END,"\n")
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END,"Serviços: ")
   my_text.insert(END,"\n")
   for i in range(len(novo_serv)):    
      my_text.insert(END,novo_serv.index[i])
      my_text.insert(END,", ")
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)
   
   my_text.insert(END,"\n")
   my_text.insert(END, "Vencimentos: ")
   my_text.insert(END,"\n")
   for i in range(len(data_os)):   
      my_text.insert(END,"\n")
      my_text.insert(END,data_os[i])
      my_text.insert(END," - ") 
      my_text.insert(END,data_os.index[i])

   my_text.insert(END,"\n")
   my_text.insert(END,quebra)   
   my_text.insert(END,"\n")
   my_text.insert(END, "Motivo do Agendamento: ")
   my_text.insert(END,"\n")
   cont=0
   for i in range(len(motivo_agend)): 
      my_text.insert(END,"\n")
      my_text.insert(END,cont)  
      my_text.insert(END," - ")
      my_text.insert(END,motivo_agend.index[i])
      cont+=1
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END, "Data e Hora da Baixa: ")
   my_text.insert(END,"\n")
   cont=0
   for i in range(len(hora_ctb_os)):   
      my_text.insert(END,"\n")
      my_text.insert(END,i)
      my_text.insert(END," - ") 
      my_text.insert(END,hora_ctb_os.index[i])
      cont=+1
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END, "Cidade: ")
   my_text.insert(END,"\n")
   for i in range(len(cit_ctb_os)):   
      my_text.insert(END,"\n")
      my_text.insert(END,cit_ctb_os.index[i])
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END,"O.s: ")
   my_text.insert(END,"\n")
   cont=0
   for i in range(len(novo2)): 
      my_text.insert(END,"\n")   
      my_text.insert(END,cont)
      my_text.insert(END," - ")
      my_text.insert(END,novo2.index[i])
      
      cont+=1
   
   
   new.mainloop()


def select():
   select_ctb()
 
   #messagebox.showinfo(title="INFORMATIVO",message=str(listbox_tec_ag_ctb.get(ACTIVE)))

def select_troca():
   select_troca_ctb()

def select_atraso():
   quebra = "--------------"*9
   value = str(listbox_serv_atraso.get(ACTIVE))
   tit = "Dados do Atraso"
   size = "1200x600"
   new = Tk()
   new.geometry(size)
   new.title(tit)
   new.resizable(False,False)
   my_frame = Frame(new)
   my_frame.pack(pady=5)
   text_scroll = Scrollbar(my_frame)
   text_scroll.pack(side=RIGHT, fill=Y)
   my_text = Text(my_frame, width=120,height=25,font=("Helvetica",12),selectbackground="yellow",selectforeground="black",undo=True,yscrollcommand=text_scroll)
   my_text.pack()
   text_scroll.config(command=my_text.yview) 
   tec_atraso = atendimento_fora.loc[(atendimento_fora[' TÉCNICO'] == value) ]
   vencimento = tec_atraso[' DTHR LIMITE']
   vencimento = vencimento.reset_index(drop=True)
   os_tec = tec_atraso.set_index(['NUMERO O.S. CS1'])
   cidade_tec = tec_atraso.set_index([' CIDADE'])
   serv_tec = tec_atraso.set_index([' SERVIÇO'])
   dt_saida_campo = tec_atraso.set_index([' DTHR SAÍDA PARA CAMPO'])
   bairro_tec = tec_atraso.set_index([' BAIRRO'])
   texto_tec = "                  Técnico: "
   nome_cliente = tec_atraso.set_index([' NOME FANTASIA'])

   def save():
      file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Documento de Texto",".txt")])
      conteudo = str(my_text.get(1.0,END))
      file.write(conteudo)

   my_text.insert(END,quebra)
   my_text.insert(END,"\n")
   my_text.insert(END,texto_tec)
   my_text.insert(END,value)
   my_text.insert(END,"                          Atrasos: ")
   my_text.insert(END,len(tec_atraso))
   my_text.insert(END,"\n")
   my_text.insert(END,quebra)
 
   
   for x in range(len(os_tec)):
      my_text.insert(END,"\n")
      my_text.insert(END,"\n")
      #my_text.insert(END,"                 Ordem               Vencimento                    Saída a Campo                    Cidade                             Serviço                                  Bairro")
      my_text.insert(END,"\n")
      
      my_text.insert(END,x)
      
      my_text.insert(END,"  -   ")
      my_text.insert(END,"O.S: ")
      my_text.insert(END,os_tec.index[x])
      my_text.insert(END,"\n")
      my_text.insert(END,quebra)
      my_text.insert(END,"\n")
      my_text.insert(END,"\n")  
      my_text.insert(END,'Vencimento: ')
      my_text.insert(END,vencimento[x])
      my_text.insert(END,"   |   ")
      my_text.insert(END,'Saída a Campo: ')
      my_text.insert(END,dt_saida_campo.index[x])
      my_text.insert(END,"   |   ")
      my_text.insert(END,'Serviço: ')
      #my_text.insert(END,"                 ")
      my_text.insert(END,serv_tec.index[x])
      my_text.insert(END,"     |   ")
      my_text.insert(END,'Cidade: ')
      my_text.insert(END,cidade_tec.index[x])
      
      my_text.insert(END,"     |   ")
      my_text.insert(END,'Bairro: ')
      my_text.insert(END,bairro_tec.index[x])

      my_text.insert(END,"     |   ")
      my_text.insert(END,'Cliente: ')
      my_text.insert(END,nome_cliente.index[x])
      my_text.insert(END,"\n")
      my_text.insert(END,quebra)
      
   my_text.insert(END,"\n")
   my_text.insert(END,"\n")
   my_text.insert(END,"O.s separada: ")
   my_text.insert(END,"\n")
   cont=1
   for x in range(len(os_tec)):
      my_text.insert(END,os_tec.index[x])
      my_text.insert(END,", ")
      cont+=1
   my_text.insert(END,"\n")
   #for x in range(len(bairro_tec)):
   label_salvar = tk.Button(new, text='SALVAR',bg='blue', fg="white",command=save)
   label_salvar.place(relx=0.04,rely=0.8,relheight=.05,relwidth=.05)
   
   new.mainloop()





text_ag = tk.Label(root, text='AGENDAMENTOS ',bg='RoyalBlue', fg="white")
text_ag.place(relx=0.01,rely=0.04,relheight=.02,relwidth=.1)

text_qtd_ag = tk.Label(root, text='QTD ',bg='RoyalBlue', fg="black")
text_qtd_ag.place(relx=0.12,rely=0.04,relheight=.02,relwidth=.05)

text_tec_ag = tk.Label(root, text='TÉCNICO ',bg='RoyalBlue', fg="black")
text_tec_ag.place(relx=0.18,rely=0.04,relheight=.02,relwidth=.15)

text_qtd_pre = tk.Label(root, text='QTD ',bg='RoyalBlue', fg="black")
text_qtd_pre.place(relx=0.46,rely=0.04,relheight=.02,relwidth=.05)

text_tec_pre = tk.Label(root, text='SERVIÇOS ',bg='RoyalBlue', fg="black")
text_tec_pre.place(relx=0.52,rely=0.04,relheight=.02,relwidth=.15)

text_pre_enc = tk.Label(root, text='PRÉ-ENCERRAMENTO ',bg='RoyalBlue', fg="white")
text_pre_enc.place(relx=0.35,rely =0.04,relheight=.02,relwidth=.1)

text_pre_enc = tk.Label(root, text='PRÉ-CANCELAMENTO ',bg='RoyalBlue', fg="white")
text_pre_enc.place(relx=0.35,rely =0.405,relheight=.02,relwidth=.1)

text_tot_atend = tk.Label(root, text='EM ATENDIMENTO',bg='RoyalBlue', fg="black")
text_tot_atend.place(relx=0.325,rely=0.82,relheight=.02,relwidth=.15)

text_tot_sb_atend = tk.Label(root, text='EM ATENDIMENTO (S)',bg='RoyalBlue', fg="black")
text_tot_sb_atend.place(relx=0.325,rely=0.86,relheight=.02,relwidth=.15)

text_tot_sb_atend = tk.Label(root, text='CANCELADO',bg='RoyalBlue', fg="black")
text_tot_sb_atend.place(relx=0.54,rely=0.86,relheight=.02,relwidth=.15)
text_tot_sb_atend = tk.Label(root, text='FINALIZADOS',bg='RoyalBlue', fg="black")
text_tot_sb_atend.place(relx=0.54,rely=0.9,relheight=.02,relwidth=.15)

text_tot_sb_atend = tk.Label(root, text='ENCERRADO ',bg='RoyalBlue', fg="black")
text_tot_sb_atend.place(relx=0.54,rely=0.82,relheight=.02,relwidth=.15)

text_tot_sb_atend = tk.Label(root, text='PENDENTE',bg='RoyalBlue', fg="black")
text_tot_sb_atend.place(relx=0.325,rely=0.9,relheight=.02,relwidth=.15)

text_tot_sb_atend = tk.Label(root, text='PRÉ-SAÍDA',bg='RoyalBlue', fg="black")
text_tot_sb_atend.place(relx=0.325,rely=0.94,relheight=.02,relwidth=.15)

text_last_upd = tk.Label(root, text='LAST UPDATE ',bg='RoyalBlue', fg="black")
text_last_upd.place(relx=0.78,rely=0.94,relheight=.02,relwidth=.15)

text_ativacao = tk.Label(root, text="ATIVAÇÃO ",bg='RoyalBlue', fg="white")
text_ativacao.place(relx=0.68,rely=0.04,relheight=.02,relwidth=.1)

text_ativacao = tk.Label(root, text="ATRASO ",bg='RoyalBlue', fg="white")
text_ativacao.place(relx=0.68,rely=0.405,relheight=.02,relwidth=.1)

text_qtd_ativ = tk.Label(root, text='QTD ',bg='RoyalBlue', fg="black")
text_qtd_ativ.place(relx=0.78,rely=0.04,relheight=.02,relwidth=.05)

text_serv_ativ = tk.Label(root, text='SERVIÇOS ',bg='RoyalBlue', fg="black")
text_serv_ativ.place(relx=0.82,rely=0.04,relheight=.02,relwidth=.15)
#total_serviços

button_color = "Tomato"
label_ag_mob = tk.Button(root, text='MOBILE \n AGENDAMENTOS',bg=button_color, fg="white", command=select_mob)
label_ag_mob.place(relx=0.01,rely=0.065,relheight=.13,relwidth=.1)

label_pre_enc = tk.Button(root, text='ENCERRAR ',bg=button_color, fg="white",command=select_pre_enc)
label_pre_enc.place(relx=0.35,rely=0.065,relheight=.3,relwidth=.1)

label_pre_canc = tk.Button(root, text='CANCELAR ',bg=button_color, fg="white",command=select_pre_canc)
label_pre_canc.place(relx=0.35,rely=0.43,relheight=.3,relwidth=.1)

label_pre_canc = tk.Button(root, text='FORA DO PRAZO',bg='red', fg="white",command=select_atraso)
label_pre_canc.place(relx=0.675,rely=0.43,relheight=.3,relwidth=.1)

label_ag_ctb = tk.Button(root, text='CTBSEQ \n AGENDAMENTOS ',bg=button_color, fg="white",command=select)
label_ag_ctb.place(relx=0.01,rely=0.2,relheight=.45,relwidth=.1)

text_tec_ctb = tk.Button(root, text='CTBSEQ TROCA ',bg=button_color, fg="white",command=select_troca)
text_tec_ctb.place(relx=0.01,rely=0.69,relheight=.25,relwidth=.1)

label_pre_ativ = tk.Button(root, text='ENCERRAR ',bg=button_color, fg="white",command=select_pre_ativ)
label_pre_ativ.place(relx=0.675,rely=0.065,relheight=.3,relwidth=.1)

list_color="white"
fundo_total_cores = "yellow"
fundo_red = "red"
#LISTBOX
listbox_qtd_ag_mob = Listbox(root,bg=list_color, fg="black")
listbox_qtd_ag_mob.place(relx=0.12,rely=0.065,relheight=.13,relwidth=.05)

listbox_tec_ag_mob = Listbox(root,bg=list_color, fg="black")
listbox_tec_ag_mob.place(relx=0.18,rely=0.065,relheight=.13,relwidth=.15)

listbox_qtd_pre = Listbox(root,bg=list_color, fg="black")
listbox_qtd_pre.place(relx=0.46,rely=0.065,relheight=.3,relwidth=.05)

listbox_tec_pre = Listbox(root,bg=list_color, fg="black")
listbox_tec_pre.place(relx=0.52,rely=0.065,relheight=.3,relwidth=.15)

listbox_qtd_canc = Listbox(root,bg=list_color, fg="black")
listbox_qtd_canc.place(relx=0.46,rely=0.43,relheight=.3,relwidth=.05)

listbox_tec_canc = Listbox(root,bg=list_color, fg="black")
listbox_tec_canc.place(relx=0.52,rely=0.43,relheight=.3,relwidth=.15)

listbox_tec_ag_ctb = Listbox(root,bg=list_color, fg="black")
listbox_tec_ag_ctb.place(relx=0.18,rely=0.2,relheight=.45,relwidth=.15)

listbox_qtd_ag_ctb = Listbox(root,bg=list_color, fg="black")
listbox_qtd_ag_ctb.place(relx=0.12,rely=0.2,relheight=.45,relwidth=.05)

listbox_qtd_ag_tot_ctb = Listbox(root,bg=fundo_total_cores, fg="black")
listbox_qtd_ag_tot_ctb.place(relx=0.12,rely=0.655,relheight=.03,relwidth=.05)

listbox_qtd_tot_pre = Listbox(root,bg=fundo_total_cores, fg="black")
listbox_qtd_tot_pre.place(relx=0.46,rely=0.37,relheight=.03,relwidth=.05)

listbox_serv_tot_pre = Listbox(root,bg=fundo_total_cores, fg="black")
listbox_serv_tot_pre.place(relx=0.52,rely=0.37,relheight=.03,relwidth=.15)

listbox_qtd_tot_canc = Listbox(root,bg=fundo_total_cores, fg="black")
listbox_qtd_tot_canc.place(relx=0.46,rely=0.735,relheight=.03,relwidth=.05)
listbox_tec_tot_canc = Listbox(root,bg=fundo_total_cores, fg="black")
listbox_tec_tot_canc.place(relx=0.52,rely=0.735,relheight=.03,relwidth=.15)

listbox_qtd_ag_tot_ctb_tec = Listbox(root,bg=fundo_total_cores, fg="black")
listbox_qtd_ag_tot_ctb_tec.place(relx=0.18,rely=0.655,relheight=.03,relwidth=.15)

listbox_qtd_ag_tot_troc = Listbox(root,bg=fundo_total_cores, fg="black")
listbox_qtd_ag_tot_troc.place(relx=0.12,rely=0.945,relheight=.03,relwidth=.05)

listbox_qtd_ag_tot_troc_tec = Listbox(root,bg=fundo_total_cores, fg="black")
listbox_qtd_ag_tot_troc_tec.place(relx=0.18,rely=0.945,relheight=.03,relwidth=.15)

listbox_qtd_tot_atraso = Listbox(root,bg=fundo_total_cores, fg="black")
listbox_qtd_tot_atraso.place(relx=0.78,rely=0.735,relheight=.03,relwidth=.05)

listbox_troc_qtd = Listbox(root,bg=list_color, fg="black")
listbox_troc_qtd.place(relx=0.12,rely=0.69,relheight=.25,relwidth=.05)

listbox_troc_tec = Listbox(root,bg=list_color, fg="black")
listbox_troc_tec.place(relx=0.18,rely=0.69,relheight=.25,relwidth=.15)


#listbox_qtd_ag_mob.insert(END,len(atendimento_ag_mob))
listbox_qtd_ag_tot_ctb.insert(END,len(atendimento_ag_ctb))
listbox_qtd_ag_tot_ctb_tec.insert(END,teste3)

listbox_tot_aten = Listbox(root,bg=fundo_total_cores, fg="black")
listbox_tot_aten.place(relx=0.46,rely=0.815,relheight=.03,relwidth=.1)

listbox_tot_sb_aten = Listbox(root,bg=fundo_total_cores, fg="black")
listbox_tot_sb_aten.place(relx=0.46,rely=0.855,relheight=.03,relwidth=.1)

listbox_tot_pendente = Listbox(root,bg=fundo_total_cores, fg="black")
listbox_tot_pendente.place(relx=0.46,rely=0.895,relheight=.03,relwidth=.1)

listbox_tot_pre = Listbox(root,bg=fundo_total_cores, fg="black")
listbox_tot_pre.place(relx=0.46,rely=0.935,relheight=.03,relwidth=.1)

listbox_tot_enc = Listbox(root,bg=fundo_total_cores, fg="black")
listbox_tot_enc.place(relx=0.65,rely=0.815,relheight=.03,relwidth=.1)

listbox_tot_canc = Listbox(root,bg=fundo_total_cores, fg="black")
listbox_tot_canc.place(relx=0.65,rely=0.855,relheight=.03,relwidth=.1)
listbox_tot_finaliz = Listbox(root,bg=fundo_total_cores, fg="black")
listbox_tot_finaliz.place(relx=0.65,rely=0.895,relheight=.03,relwidth=.1)

listbox_dt_hoje = Listbox(root,bg=fundo_red, fg="black")
listbox_dt_hoje.place(relx=0.89,rely=0.935,relheight=.03,relwidth=.1)

listbox_serv_atraso = Listbox(root,bg=list_color, fg="black")
listbox_serv_atraso.place(relx=0.838,rely=0.43,relheight=.3,relwidth=.15)

listbox_tot_atraso = Listbox(root,bg=fundo_total_cores, fg="black")
listbox_tot_atraso.place(relx=0.838,rely=0.735,relheight=.03,relwidth=.15)

listbox_qtd_atraso = Listbox(root,bg=list_color, fg="black")
listbox_qtd_atraso.place(relx=0.78,rely=0.43,relheight=.3,relwidth=.05)

listbox_qtd_ativ = Listbox(root,bg=list_color, fg="black")
listbox_qtd_ativ.place(relx=0.78,rely=0.065,relheight=.3,relwidth=.05)

listbox_tec_ativ = Listbox(root,bg=list_color, fg="black")
listbox_tec_ativ.place(relx=0.84,rely=0.065,relheight=.3,relwidth=.15)

listbox_qtd_tot_ativ = Listbox(root,bg=fundo_total_cores, fg="black")
listbox_qtd_tot_ativ.place(relx=0.78,rely=0.37,relheight=.03,relwidth=.05)

listbox_serv_tot_ativ = Listbox(root,bg=fundo_total_cores, fg="black")
listbox_serv_tot_ativ.place(relx=0.84,rely=0.37,relheight=.03,relwidth=.15)

#TOTAL QUANTIDADES TROCA EQUIP
total_canc = len(atendimento_canc_ctb2) + len(atendimento_canc_mob2)

soma_tec_troca = len(atendimento_ag_ctb_troca)+len(atendimento_ag_ctb_troca_equi)
listbox_qtd_ag_tot_troc_tec.insert(END,soma_troca)
listbox_qtd_ag_tot_troc.insert(END,soma_tec_troca)

for x in range(len(atendimento_ag_mob2)):
   listbox_qtd_ag_mob.insert(END,atendimento_ag_mob2[x])
   listbox_tec_ag_mob.insert(END,atendimento_ag_mob2.index[x])

for i in range(len(teste)):
   listbox_tec_ag_ctb.insert(END,teste.index[i])
for i in range(len(teste)):
   listbox_qtd_ag_ctb.insert(END,teste[i])

for i in range(len(tecnicos_troca)):
   listbox_troc_tec.insert(END,tecnicos_troca.index[i])
   listbox_troc_qtd.insert(END,tecnicos_troca[i])

for i in range(len(tecnicos_troca_equi)):
   listbox_troc_tec.insert(END,tecnicos_troca_equi.index[i])  
   listbox_troc_qtd.insert(END,tecnicos_troca_equi[i])

for i in range(len(atendimento_pre_enc2)):
   listbox_tec_pre.insert(END,atendimento_pre_enc2.index[i]) 

for i in range(len(atendimento_pre_enc2)):
   listbox_qtd_pre.insert(END,atendimento_pre_enc2[i])

listbox_serv_tot_pre.insert(END, len(atendimento_pre_enc2))
listbox_qtd_tot_pre.insert(END, len(atendimento_pre_enc))

for x in range(len(atendimento_canc_ctb2)):
   listbox_qtd_canc.insert(END,atendimento_canc_ctb2[x])

for x in range(len(atendimento_canc_mob2)):
   listbox_qtd_canc.insert(END,atendimento_canc_mob2[x])

for x in range(len(atendimento_canc_ctb2)):
   listbox_tec_canc.insert(END,atendimento_canc_ctb2.index[x])

for x in range(len(atendimento_canc_mob2)):
   listbox_tec_canc.insert(END,atendimento_canc_mob2.index[x])

for i in range(len(atendimento_pre_ativ2)):
   listbox_tec_ativ.insert(END,atendimento_pre_ativ2.index[i]) 

for i in range(len(atendimento_pre_ativ2)):
   listbox_qtd_ativ.insert(END,atendimento_pre_ativ2[i])

lista = []

for x in range(len(atendimento_canc_ctb2)): 
   lista.append(atendimento_canc_ctb2[x])
for i in range(len(atendimento_canc_mob2)): 
   lista.append(atendimento_canc_mob2[i])

for x in range(len(atendimento_fora_tec)):
   listbox_serv_atraso.insert(END, atendimento_fora_tec.index[x])
   listbox_qtd_atraso.insert(END, atendimento_fora_tec[x])
      
listbox_qtd_tot_canc.insert(END,sum(lista))
listbox_tec_tot_canc.insert(END, total_canc)
total_com_baixa = sum(lista) + len(atendimento_pre_enc)
total_sem_baixa = len(total_atendimento) - total_com_baixa - len(atendimento_pre_ativ)
listbox_tot_aten.insert(END,len(total_atendimento))
listbox_tot_sb_aten.insert(END,total_sem_baixa)
listbox_tot_pendente.insert(END,len(total_pendente))
listbox_tot_pre.insert(END,len(total_pre))

listbox_qtd_tot_ativ.insert(END,len(atendimento_pre_ativ))
listbox_serv_tot_ativ.insert(END,len(atendimento_pre_ativ2))
listbox_dt_hoje.insert(END,dt_hoje)


listbox_tot_enc.insert(END,len(total_enc))
listbox_tot_canc.insert(END,len(total_cancel))
listbox_qtd_tot_atraso.insert(END,sum(atendimento_fora_tec))
listbox_tot_atraso.insert(END,len(atendimento_fora2))
listbox_tot_finaliz.insert(END,len(total_cancel)+len(total_enc))

max = df[' DTHR LIMITE'].max()
min = df[' DTHR LIMITE'].min()

root.mainloop()