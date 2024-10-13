# %%
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox, ttk
import sqlite3
import pandas as pd

# %%

def register(entry_name, drop_categoria, drop_gender, drop_status, entry_duration,entry_responsible):
    #Captura os dados 
    
    name=entry_name.get()
    category_name=drop_categoria.get()
    gender_name=drop_gender.get()
    status_name=drop_status.get()
    duration= entry_duration.get() 
    responsible=entry_responsible.get() 
    
     # Verifica se os dropdowns estão selecionados
    if not category_name or not gender_name or not status_name:
        messagebox.showerror('Erro', 'Por favor, selecione uma categoria, gênero e status.')
        return  # Interrompe a função se não houver seleção 
    
    # Define o category_id com base na categoria escolhida
    if category_name == 'Anime':
        category_id = 1
    elif category_name == 'Documentário':
        category_id = 2
    elif category_name == 'Dorama':
        category_id = 3
    elif category_name == 'Filme':
        category_id = 4
    elif category_name == 'Série':  # Corrigido para "Série"
        category_id = 5
    else:
        category_id = None

        
      # Define o gender_id com base na categoria escolhida
    if gender_name == 'Ação':
        gender_id = 1
    elif gender_name == 'Aventura':
        gender_id = 2
    elif gender_name == 'Animação':
        gender_id = 3
    elif gender_name == 'Comédia':
        gender_id = 4
    elif gender_name == 'Drama':
        gender_id = 5
    elif gender_name == 'Ficção':
        gender_id = 6
    elif gender_name == 'Romance':
        gender_id = 7
    elif gender_name == 'Terror':
        gender_id = 8
        
    else:
        gender_id = None  # Caso a categoria não esteja na lista
        
    # Define o status_id com base na categoria escolhida
    if status_name == 'Para assistir':
        status_id = 1
    elif status_name == 'Assistindo':
        status_id = 2
    elif status_name == 'Assistido': 
        status_id = 3
    else:
        status_id = None  # Caso a categoria não esteja na lista
    
    
    #Insere em banco de dados
    con = sqlite3.connect("myshowlist.db")
    cursor = con.cursor()
    cursor.execute( """insert into shows (gender_id, category_id, status_id, name, duration, responsible) VALUES (?, ?, ?, ?, ?, ?)""",
                (gender_id,category_id,status_id,name,duration,responsible)
                )   
    con.commit()
    con.close()    
    
    
    
    # Delete dados do usuario nas caixas de texto
    entry_name.delete(0,'end')
    entry_duration.delete(0,'end')
    entry_responsible.delete(0,'end')
    drop_categoria.set("")
    drop_gender.set("")
    drop_status.set("")
   
    
    messagebox.showinfo('Sucesso','Programa Cadastrado!')
       

def new_prog():
    cadastro = ctk.CTkToplevel()
    cadastro.title('Cadastrar Show')
    
    #Nome do show
    label_name = ctk.CTkLabel(cadastro, text="Digite o nome do Programa:").grid(row=1, column=1, padx=10, pady=10)
    entry_name = ctk.CTkEntry(cadastro, width=150)       
    entry_name.grid(row=1, column=2,sticky="ew",  padx=10, pady=10)
    
    #Category
    label_category = ctk.CTkLabel(cadastro, text="Escolha a categoria:").grid(row=2, column=1, padx=10, pady=10)
    categories=['Anime','Documentário','Dorama','Filme','Série']
    drop_categoria = ctk.CTkComboBox (cadastro,width=150,values=categories)
    drop_categoria.grid(row=2, column=2, padx=10, pady=10)
    
    #Gender
    label_gender = ctk.CTkLabel(cadastro, text="Escolha o gênero:").grid(row=3, column=1, padx=10, pady=10)
    genders=['Ação','Aventura','Animação','Comédia','Drama','Ficção','Romance','Terror']
    drop_gender = ctk.CTkComboBox (cadastro,width=150,values=genders)
    drop_gender.grid(row=3, column=2,sticky="ew",  padx=10, pady=10)
    
    #Status
    label_status = ctk.CTkLabel(cadastro, text="Escolha o status:").grid(row=4, column=1, padx=10, pady=10)
    status=['Para assistir', 'Assistindo', 'Assistido']
    drop_status = ctk.CTkComboBox (cadastro,width=150,values=status)
    drop_status.grid(row=4, column=2,sticky="ew",  padx=10, pady=10)
    
    #Duracao
    label_duration = ctk.CTkLabel(cadastro, text="Digite a duração:").grid(row=5, column=1, padx=10, pady=10)
    entry_duration = ctk.CTkEntry(cadastro, width=150)       
    entry_duration.grid(row=5, column=2,sticky="ew",  padx=10, pady=10)
    
    #Responsible
    label_responsible = ctk.CTkLabel(cadastro, text="Cadastrador por:").grid(row=6, column=1, padx=10, pady=10)
    entry_responsible = ctk.CTkEntry(cadastro, width=150)       
    entry_responsible.grid(row=6, column=2,sticky="ew",  padx=10, pady=10)
    
    #bt Cadastrar
    bt_cadastrar = ctk.CTkButton(cadastro, text="Cadastrar",width=25,  
                             command=lambda: register(entry_name, drop_categoria, drop_gender, drop_status, entry_duration,entry_responsible))
    bt_cadastrar.grid(row=7, column=1,sticky="ew",  padx=10, pady=10)
    
    #close window
    bt_voltar = ctk.CTkButton(cadastro, text='Voltar',width=25,command=cadastro.destroy)
    bt_voltar.grid(row=7, column=2,sticky="ew", padx=10, pady=10)
    
def sorteador():
    sort_menu = ctk.CTkToplevel()
    sort_menu.title('Sortear Show')   
    
    def sort_all():
        #Recebe os dados do banco de dados
        con = sqlite3.connect("myshowlist.db")
        cursor = con.cursor()
        query = """ select 
        id,
        name,
        status_id
        from shows
        where status_id == 1

        """
        #Cria o data frame para guardar os dados
        df_all=pd.read_sql_query(query,con )
        
        
         # Verifica se há dados disponíveis
        if df_all.empty:
            messagebox.showerror('Erro', 'Não há shows disponíveis para sortear.')
            return
        
        # Sorteia um show aleatório
        random_show = df_all.sample(n=1).iloc[0]
        
        #Altera o status do show para Assistindo
        cursor.execute( f""" UPDATE shows   
                       set status_id = 2    
                       where id == {random_show['id']}  
                       """ )   
        con.commit()
        con.close()  
        
        # Exibe o show sorteado
        messagebox.showinfo('Programa Sorteado', f"O programa sorteado é: {random_show['name']} (ID: {random_show['id']})")
   
    def sort_filme():
        #Recebe os dados do banco de dados
        con = sqlite3.connect("myshowlist.db")
        cursor = con.cursor()
        query = """ select 
        id,
        name,
        status_id
        from shows
        where status_id == 1 and category_id == 4

        """
        #Cria o data frame para guardar os dados
        df_movie=pd.read_sql_query(query,con )
        
        
         # Verifica se há dados disponíveis
        if df_movie.empty:
            messagebox.showerror('Erro', 'Não há filmes disponíveis para sortear.')
            return
        
        # Sorteia um filme aleatório
        random_show = df_movie.sample(n=1).iloc[0]
        
        #Altera o status do filme para Assistindo
        cursor.execute( f""" UPDATE shows   
                       set status_id = 2    
                       where id == {random_show['id']}  
                       """ )   
        con.commit()
        con.close()  
        
        # Exibe o show sorteado
        messagebox.showinfo('Filme Sorteado', f"O filme sorteado é: {random_show['name']} (ID: {random_show['id']})")
        
    def sort_anime():
                #Recebe os dados do banco de dados
        con = sqlite3.connect("myshowlist.db")
        cursor = con.cursor()
        query = """ select 
        id,
        name,
        status_id
        from shows
        where status_id == 1 and category_id == 1

        """
        #Cria o data frame para guardar os dados
        df_movie=pd.read_sql_query(query,con )
        
        
         # Verifica se há dados disponíveis
        if df_movie.empty:
            messagebox.showerror('Erro', 'Não há animes disponíveis para sortear.')
            return
        
        # Sorteia um anime aleatório
        random_show = df_movie.sample(n=1).iloc[0]
        
        #Altera o status do filme para Assistindo
        cursor.execute( f""" UPDATE shows   
                       set status_id = 2    
                       where id == {random_show['id']}  
                       """ )   
        con.commit()
        con.close()  
        
        # Exibe o show sorteado
        messagebox.showinfo('Anime Sorteado', f"O anime sorteado é: {random_show['name']} (ID: {random_show['id']})")
    
    def sort_doc():
                #Recebe os dados do banco de dados
        con = sqlite3.connect("myshowlist.db")
        cursor = con.cursor()
        query = """ select 
        id,
        name,
        status_id
        from shows
        where status_id == 1 and category_id == 2

        """
        #Cria o data frame para guardar os dados
        df_movie=pd.read_sql_query(query,con )
        
        
         # Verifica se há dados disponíveis
        if df_movie.empty:
            messagebox.showerror('Erro', 'Não há documentários disponíveis para sortear.')
            return
        
        # Sorteia um filme aleatório
        random_show = df_movie.sample(n=1).iloc[0]
        
        #Altera o status do documentário para Assistindo
        cursor.execute( f""" UPDATE shows   
                       set status_id = 2    
                       where id == {random_show['id']}  
                       """ )   
        con.commit()
        con.close()  
        
        # Exibe o show sorteado
        messagebox.showinfo('Documentário Sorteado', f"O documentário sorteado é: {random_show['name']} (ID: {random_show['id']})")

    def sort_dorama():
                #Recebe os dados do banco de dados
        con = sqlite3.connect("myshowlist.db")
        cursor = con.cursor()
        query = """ select 
        id,
        name,
        status_id
        from shows
        where status_id == 1 and category_id == 3

        """
        #Cria o data frame para guardar os dados
        df_movie=pd.read_sql_query(query,con )
        
        
         # Verifica se há dados disponíveis
        if df_movie.empty:
            messagebox.showerror('Erro', 'Não há doramas disponíveis para sortear.')
            return
        
        # Sorteia um dorama aleatório
        random_show = df_movie.sample(n=1).iloc[0]
        
        #Altera o status do dorama para Assistindo
        cursor.execute( f""" UPDATE shows   
                       set status_id = 2    
                       where id == {random_show['id']}  
                       """ )   
        con.commit()
        con.close()  
        
        # Exibe o show sorteado
        messagebox.showinfo('Dorama Sorteado', f"O dorama sorteado é: {random_show['name']} (ID: {random_show['id']})")
    
    def sort_serie():
                #Recebe os dados do banco de dados
        con = sqlite3.connect("myshowlist.db")
        cursor = con.cursor()
        query = """ select 
        id,
        name,
        status_id
        from shows
        where status_id == 1 and category_id == 5

        """
        #Cria o data frame para guardar os dados
        df_movie=pd.read_sql_query(query,con )
        
        
         # Verifica se há dados disponíveis
        if df_movie.empty:
            messagebox.showerror('Erro', 'Não há séries disponíveis para sortear.')
            return
        
        # Sorteia uma série aleatório
        random_show = df_movie.sample(n=1).iloc[0]
        
        #Altera o status do filme para Assistindo
        cursor.execute( f""" UPDATE shows   
                       set status_id = 2    
                       where id == {random_show['id']}  
                       """ )   
        con.commit()
        con.close()  
        
        # Exibe o show sorteado
        messagebox.showinfo('Série Sorteada', f"A série sorteado é: {random_show['name']} (ID: {random_show['id']})")
    
    #bt sorteador all
    bt_sort_all = ctk.CTkButton(sort_menu, text="Aleatório",width=25, command=sort_all)
    bt_sort_all.grid(row=1, column=1,sticky="ew",  padx=10, pady=10)
    
    #bt sorteador filmes
    bt_sort_filme = ctk.CTkButton(sort_menu, text="Sortear um filme",width=25,command=sort_filme)
    bt_sort_filme.grid(row=1, column=2,sticky="ew",  padx=10, pady=10)
    
    #bt sorteador série
    bt_sort_serie = ctk.CTkButton(sort_menu, text="Sortear uma série",width=25,command=sort_serie)
    bt_sort_serie.grid(row=2, column=1,sticky="ew",  padx=10, pady=10)
    
    #bt sorteador anime
    bt_sort_anime = ctk.CTkButton(sort_menu, text="Sortear um anime",width=25,command=sort_anime)
    bt_sort_anime.grid(row=2, column=2,sticky="ew",  padx=10, pady=10)
    
     #bt sorteador Dorama
    bt_sort_dorama = ctk.CTkButton(sort_menu, text="Sortear um dorama",width=25,command=sort_dorama)
    bt_sort_dorama.grid(row=3, column=1,sticky="ew",  padx=10, pady=10)
    
     #bt sorteador Documentario
    bt_sort_documentario = ctk.CTkButton(sort_menu, text="Sortear um documentário",width=25,command=sort_doc)
    bt_sort_documentario.grid(row=3, column=2,sticky="ew",  padx=10, pady=10)
    
    #close window
    bt_voltar = ctk.CTkButton(sort_menu, text='Voltar',width=25,command=sort_menu.destroy)
    bt_voltar.grid(row=7, column=2,sticky="ew", padx=10, pady=10)

def alter_status():
    alt_status = ctk.CTkToplevel()
    alt_status.title('Alterar Status')
    
    def register_status():
        id=entry_id.get()
        status_name=drop_stats.get()
        
        #Define o status_id com base na categoria escolhida
        'Para assistir', 'Assistindo', 'Assistido', 'Dropado'
        if status_name == 'Para assistir':
            status_id = 1
        elif status_name == 'Assistindo':
            status_id = 2
        elif status_name == 'Assistido':
            status_id = 3
        elif status_name == 'Dropado':
            status_id = 4
        else:
            status_id = None
        
        
        
        con = sqlite3.connect("myshowlist.db")
        cursor = con.cursor()

                
        #Altera o status do show para Assistindo
        cursor.execute( f""" UPDATE shows   
                       set status_id = {status_id}    
                       where id == {id}  
                       """ )   
        con.commit()
        con.close()
        
        # Delete dados do usuario nas caixas de texto
        entry_id.delete(0,'end')
        drop_stats.set("")
          
        
        messagebox.showinfo('Sucesso','Status Alterado!')
        
        
    
    def validar_numero(valor, modo):
        if modo == "1":  # Inserindo texto
            # Verifica se o valor é vazio ou se é um número válido (apenas inteiro)
            if valor == "" or valor.isdigit():
                return True
            else:
                messagebox.showerror("Erro", "Por favor, digite apenas números inteiros.")
                return False
        else:  # Deletando texto
            return True

    # Registro da função de validação
    validar_numero_cmd = alt_status.register(validar_numero)
    
    #ID do show
    label_id = ctk.CTkLabel(alt_status, text="Digite o ID do show:").grid(row=1, column=1, padx=10, pady=10)
    entry_id = ctk.CTkEntry(alt_status, width=30,validate="key", validatecommand=(validar_numero_cmd, '%P'))       
    entry_id.grid(row=1, column=2,sticky="ew",  padx=10, pady=10)
    
    #Category
    label_stats = ctk.CTkLabel(alt_status, text="Selecione o Status:").grid(row=2, column=1, padx=10, pady=10)
    stats=['Para assistir', 'Assistindo', 'Assistido', 'Dropado']
    drop_stats = ctk.CTkComboBox (alt_status,width=150,values=stats)
    drop_stats.grid(row=2, column=2,sticky="ew",  padx=10, pady=10)
    
    #bt registrar
    bt_register = ctk.CTkButton(alt_status, text="Registrar novo Status",width=25,command=register_status)
    bt_register.grid(row=7, column=1,sticky="ew",  padx=10, pady=10)
    
    #close window
    bt_voltar = ctk.CTkButton(alt_status, text='Voltar',width=25,command=alt_status.destroy)
    bt_voltar.grid(row=7, column=2,sticky="ew", padx=10, pady=10)
    
def exportar():
    export = ctk.CTkToplevel()
    export.title('Exportar Listas')
    
    def exp_completa():    
    
        #Busca no Banco de dados
        con = sqlite3.connect("myshowlist.db")
        query = """ SELECT s.id, s.name , c.category_name , g.gender_name , c.category_name, s2.status_name , s.responsible 
                    FROM shows s , category c , gender g , status s2 
                    WHERE s.gender_id = g.gender_id AND s.category_id = c.category_id AND s.status_id = s2.status_id ;      
        """
        #salva no dataframe o retorno do select
        df_completa = pd.read_sql(query,con)
        con.close()
        #exporta pro excel
        df_completa.to_excel('lista_completa.xlsx',index=False)   
        messagebox.showinfo("Sucesso", "Excel Exportado")
    
    def exp_assistir():    
    
        #Busca no Banco de dados
        con = sqlite3.connect("myshowlist.db")
        query = """ SELECT s.id, s.name, c.category_name, g.gender_name, s2.status_name, s.responsible 
                    FROM shows s 
                    JOIN category c ON s.category_id = c.category_id 
                    JOIN gender g ON s.gender_id = g.gender_id 
                    JOIN status s2 ON s.status_id = s2.status_id 
                    WHERE s.status_id = 1;     
        """
        #salva no dataframe o retorno do select
        df_completa = pd.read_sql(query,con)
        con.close()
        #exporta pro excel
        df_completa.to_excel('lista_fila.xlsx',index=False)   
        messagebox.showinfo("Sucesso", "Excel Exportado")
    
    def exp_assistindo():    
    
        #Busca no Banco de dados
        con = sqlite3.connect("myshowlist.db")
        query = """ SELECT s.id, s.name, c.category_name, g.gender_name, s2.status_name, s.responsible 
                    FROM shows s 
                    JOIN category c ON s.category_id = c.category_id 
                    JOIN gender g ON s.gender_id = g.gender_id 
                    JOIN status s2 ON s.status_id = s2.status_id 
                    WHERE s.status_id = 2;     
        """
        #salva no dataframe o retorno do select
        df_completa = pd.read_sql(query,con)
        con.close()
        #exporta pro excel
        df_completa.to_excel('lista_assistindo.xlsx',index=False)   
        messagebox.showinfo("Sucesso", "Excel Exportado")    
     
    def exp_assistido():    
    
        #Busca no Banco de dados
        con = sqlite3.connect("myshowlist.db")
        query = """ SELECT s.id, s.name, c.category_name, g.gender_name, s2.status_name, s.responsible 
                    FROM shows s 
                    JOIN category c ON s.category_id = c.category_id 
                    JOIN gender g ON s.gender_id = g.gender_id 
                    JOIN status s2 ON s.status_id = s2.status_id 
                    WHERE s.status_id = 3;     
        """
        #salva no dataframe o retorno do select
        df_completa = pd.read_sql(query,con)
        con.close()
        #exporta pro excel
        df_completa.to_excel('lista_assistido.xlsx',index=False)   
        messagebox.showinfo("Sucesso", "Excel Exportado")    
      
    def exp_dropado():    
    
        #Busca no Banco de dados
        con = sqlite3.connect("myshowlist.db")
        query = """ SELECT s.id, s.name, c.category_name, g.gender_name, s2.status_name, s.responsible 
                    FROM shows s 
                    JOIN category c ON s.category_id = c.category_id 
                    JOIN gender g ON s.gender_id = g.gender_id 
                    JOIN status s2 ON s.status_id = s2.status_id 
                    WHERE s.status_id = 4;     
        """
        #salva no dataframe o retorno do select
        df_completa = pd.read_sql(query,con)
        con.close()
        #exporta pro excel
        df_completa.to_excel('lista_dropado.xlsx',index=False)   
        messagebox.showinfo("Sucesso", "Excel Exportado")   
          
    #bt exportar all
    bt_exp_all = ctk.CTkButton(export, text="Exportar Lista Completa",width=25,command=exp_completa)
    bt_exp_all.grid(row=1, column=1,sticky="ew",  padx=10, pady=10)
    
    #bt exportar para assistir
    bt_exp_assitir = ctk.CTkButton(export, text="Exportar Fila",width=25,command=exp_assistir)
    bt_exp_assitir.grid(row=1, column=2,sticky="ew",  padx=10, pady=10)
        
    #bt exportar assistindo
    bt_exp_assistindo = ctk.CTkButton(export, text="Exportar Assistindo",width=25,command=exp_assistindo)
    bt_exp_assistindo.grid(row=2, column=1,sticky="ew",  padx=10, pady=10)
    
    #bt exportar assistido
    bt_exp_assistido = ctk.CTkButton(export, text="Exportar Assistido",width=25,command=exp_assistido)
    bt_exp_assistido.grid(row=2, column=2,sticky="ew",  padx=10, pady=10)
    
    #bt exportar dropado
    bt_exp_dropado = ctk.CTkButton(export, text="Exportar Dropado",width=25,command=exp_dropado)
    bt_exp_dropado.grid(row=3, column=1,sticky="ew",  padx=10, pady=10)
       
    #close window
    bt_voltar = ctk.CTkButton(export, text='Voltar',width=25,command=export.destroy)
    bt_voltar.grid(row=3, column=2,sticky="ew", padx=10, pady=10)
    
menus = ctk.CTk()
menus.title('Menu')
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
   

#Cadastrar Programa
bt_cadastro = ctk.CTkButton(menus, text="Cadastrar",width=25, command= new_prog)
bt_cadastro.grid(row=1, column=1, sticky="ew", padx=10, pady=10)

#Sorteador
bt_sorteador = ctk.CTkButton(menus, text="Sortear",width=25, command=sorteador)
bt_sorteador.grid(row=1, column=2,sticky="ew",  padx=10, pady=10)

#Alterar status
bt_status = ctk.CTkButton(menus, text="Alterar Status",width=25,command=alter_status)
bt_status.grid(row=5, column=1,sticky="ew",  padx=10, pady=10)

#Gerar listas
bt_listas = ctk.CTkButton(menus, text="Exportar listas",width=25,command=exportar)
bt_listas.grid(row=5, column=2,sticky="ew",  padx=10, pady=10)

#close
bt_sair = ctk.CTkButton(menus, text='Sair',width=25,command=menus.destroy)
bt_sair.grid(row=7, column=2,sticky="ew", padx=10, pady=10)


menus.mainloop()

# %%



