
import streamlit as st
from PIL import Image

# streamlit run SCRIPT.py

def menu():
   
    st.set_page_config(
        page_title ="Portfolio Leonardo",
        layout ="wide",
        initial_sidebar_state = "expanded",
        page_icon=':page_with_curl:',
        
    )

    st.title(":blue[Leonardo Carvalho]")
    # st.header(f"Portfolio :blue[Leonardo Carvalho]")
    
    welcome = '''
                > Esta página foi criada utilizando streamlit, qualquer dúvida em relação ao portfolio ou outras coisas, entre em contato.              
                '''
    st.markdown(welcome)
    st.markdown('---')

# ---------------------------------------
# SIDEBAR
    image = Image.open('./DADOS/leo.jpg')
    st.sidebar.image(image)
    st.sidebar.write("## __Leonardo Carvalho__")

    st.sidebar.write("__Onde me Encontrar:__")
    st.sidebar.markdown(":briefcase: [LinkedIn](https://www.linkedin.com/in/l3omc/)")
    
    st.sidebar.markdown(":space_invader: [Git Hub](https://github.com/l3omc)")
    st.sidebar.write(":e-mail: leocarva95@gmail.com")
      
    st.sidebar.markdown('''__Minhas skills:__  
                        | Data analyst | Data cientist
                        | R | Python | SQL 
                        | QGIS | Power BI
                        | Metabase | Excel avançado
                        | Microsoft Office
                        | ''')
  
    st.sidebar.markdown('''__Minhas Softskills:__  
                        | Aprendizado rápido | Fácil adaptação | Pensamento crítico | Proatividade
                        | Criatividade | Trabalho em Equipe | Empatia | Comunicação | Gerenciamento de tempo 
                        |

                         ''')
    
    st.sidebar.markdown('''__Palavras - Chave:__  
                         WebScraping | Aprendizado de Máquina 
                        |Data Visualization | Business Intelligence 
                        | Data Analytics | Ciência de Dados | Estatística | SQL | Machine Learning 
                        | Estatística Descritiva | Analista de Dados 
                        | Data Scientist | Python | Big Data |
                        
                        ''')
  
    st.write(':wave: Sobre mim :')
    about = '''
            Sou Meteorologista formado pela UFSM, possuo formação técnica em Desenvolvimento de Sistemas (IFSULDEMINAS) 
            e em Técnico em sistemas para internet (IFNMG). Tenho ampla experiência em ETL de dados meteorológicos e sensoriamento remoto, utilizando as linguagens 
            Python e R.
            Atualmente estou migrando de área para trabalhar como analista de dados, onde venho evoluindo meus conhecimentos em elaboração de dashboards com Power BI
            e tratamento de dados utilizando python e excel. 
    '''
    st.markdown(about)
    st.markdown('---')


    # tab1, tab2 = st.tabs(['##### :globe_with_meridians: Maps', '##### :page_with_curl: CV'])
    tab1, tab2, tab3, tab4 = st.tabs(['##### :page_with_curl: CV',"##### :page_with_curl: English CV",
                                       "##### :world_map: Portfolio", "##### :bar_chart: Data Analyst"])

    with tab1: # CV

        st.write('#### :books: Estudando ')

        with st.expander('Ferramentas de Análise de dados '):            
            st.markdown(''' Atualmente em fase final dos cursos de **Analista de BI** na escola DNC e **Aperfeiçoamento de Análise de dados pela UFMA**  
                    - Desenvolvimento de dashboards avançados com Power BI e Excel.    
                    - Tratamento, limpeza e organização de dados com Excel e python.      
                    -  Aplicação de boas práticas em análise exploratória e visualização de dados.    
                    -- **Ferramentas utilizadas :** Power BI | Excel | Python | Pandas | Numpy | SQL | Matiplotlib | requests | BeautifulSoup
                    
                        ''')
        with st.expander('Ferramentas para Ciência de dados '):
            st.markdown(''' Cursando a formação de **Cientista de dados** na escola DNC.    
                            - Modelagem estatística, visualização de dados e construção de pipelines de machine learning.    
                            - Desenvolvimento de aplicações interativas com Streamlit.   
                            -- **Ferramentas utilizadas :** Python | Seaborn| Statsmodels | Scikitlearn | Streamlit | Matplotlib |
                        ''')
        
        
        # ----------------- EXPERIENCIAS E PROJETOS -------
        st.write('#### :coffee: Experiências Profissionais e Projetos')
        
        with st.expander('Dashboard Venda de Produtos. (Projeto curto) '):
             st.markdown('''    
                         **Resumo do Projeto:**    
                                     - Fonte de dados: kaggle   
                                     - Visualização  Power BI    
                                     - Destaques:   Perfil de clientes, vendas totais, locais de captação de venda, tratamento de dados, busca utilizando procv,
                          tabela dinâmica, validação de dados.

                        **Ferramentas:**  Excel 
                        ''')
             bi2 = Image.open('./IMAGENS/EXCEL1.png') 
             bi3 = Image.open('./IMAGENS/EXCEL2.png')           
             colbi1,colbi2 = st.columns(2)
             with colbi1:
                 st.image(bi2, width=600)
             with colbi2:
                 st.image(bi3, width=600)

        with st.expander('Dashboard Venda de Loja (Projeto curto) '):
             st.markdown('''    
                         **Resumo do Projeto:**    
                                     - Fonte de dados: kaggle   
                                     - Visualização  Power BI    
                                     - Destaques:   Perfil de clientes, vendas totais, locais de captação de venda.

                        **Ferramentas:** Power BI | Excel 
                        ''')
             bi2 = Image.open('./IMAGENS/powerbi2.png') 
             bi3 = Image.open('./IMAGENS/powerbi3.png')           
             colbi1,colbi2 = st.columns(2)
             with colbi1:
                 st.image(bi2, width=600)
             with colbi2:
                 st.image(bi3, width=600)

        with st.expander('Dashboard Venda de Gasolina (Projeto curto) '):
             st.markdown('''    
                         **Resumo do Projeto:**    
                                     - Fonte de dados: kaggle   
                                     - Visualização : Power BI    
                                     - Destaques: variação do preço médio da gasolina, regiões com maior impacto, tendências mensais.  

                        **Ferramentas:** Power BI | Excel | Python
                        ''')
             bi1 = Image.open('./IMAGENS/power bi 1.png')            
             colbi1 = st.columns(3)
             with colbi1[1]:
                 st.image(bi1, width=400)

        with st.expander('ETL Análise exploratoria de Vendas de produto (Projeto curto) '):
             st.markdown(''' 
                         Este projeto simples de análise exploratória de uma empresa de vendas, tendo como objetivo principal responder algumas perguntas
                         de interesse do dono da empresa.     
                            **Resumo do Projeto:**       
                                     - Fonte de dados: kaggle     
                                     - Visualização python      
                                     
                            **Ferramentas:**  Python | Pandas | Seaborn | Matplotlib    
                         
                         [Link github do Projeto](https://github.com/l3omc/python_script/tree/main/Analise_exploratoria/Projeto%201)   
                         [Link post no Medium](https://leonardo-carvalho.medium.com/explorando-vendas-com-python-uma-an%C3%A1lise-de-dados-do-zero-ao-insight-1e8c63d083af)
                        ''')
           
        with st.expander('Analista em Meteorologia '):
             st.markdown(''' **AEROESPACIAL ENGENHARIA** Novembro 2024 - Fevereiro 2025  
                         Realizando a extração, análise e o tratamento de dados meteorológicos para projetos de risco climático 
                         utilizando python e excel . 
                         Desenvolvimento de mapas temáticos para avaliação de risco ambiental ao longo de linhas de 
                         transmissão, utilizando softwares livres como o QGIS.

                        ''')

        with st.expander('Analista em Geoprocessamento '):
             st.markdown('''
                         **INOVAGRO CONSULTORIA** Julho 2024 - Novembro 2024  
                            Realizando a produção de mapas temáticos voltados para análises ambientais utilizando imagens de 
                         satélite e bases cartograficas com QGIS. 
                            Levantamentos topográficos em campo com GNSS RTK, utilização do AutoCAD Civil 3D, para a elaboração de plantas topográficas, 
                         para entrega ao cliente.
                            Aerolevantamento com drone, posteriormente com o Agisoft Metashape é feito o processamento das
                            imagens capturadas , visando a geração de ortomosaicos

                        ''')
             
        #------------- FORMAÇÃO ----
        st.write('#### :mortar_board: Formação')
        with st.expander('Graduação'):
            st.markdown(''' - *Bacharelado em Meteorologia*   
                        *Universidade Federal de Santa Maria de Março 2016 a janeiro 2022*   
                        Membro do laboratório de micrometeorologia e instrumentação (LUMET), onde fez partes de projetos de pesquisa onde envolveu instalação de 
                        torres micrometeorológicas, tratamento de dados e utilização em modelagem interação superfície- atmosfera. Tendo como trabalho de conclusão de curso
                        Avaliação da estimativa de fluxos de CO2 utilizando sensoriamento remoto.   

                        ''')
            
        with st.expander('Formação Técnica'):          

            st.markdown(''' 
                        - *Técnico em Geoprocessamento*
                *Universidade Federal de Santa Maria Março 2024- presente *
                
                - *Técnico em Informática para Internet*
                   *Universidade Federal de Santa Maria Março 2016 a janeiro 2022 *

                - *Técnico em Desenvolvimento de sistemas*
                    *Universidade Federal de Santa Maria Março 2016 a janeiro 2022 *
                        
                        ''')
       
        with st.expander('Cursos'):
            st.markdown('''
                - Analista de BI  
                    DNC     
                        Tópicos abordados no curso  :  
                        - Power bi - nível intermediário  
                        - Excel - nível intermediário    
                        - SQL -  Voltado a análise de dados   
                        
                    ''')    
            st.markdown('''
                - Análise de dados   
                    Universidade Federal de Maranhão    
                        Tópicos abordados no curso  :  
                        - Power BI - nível intermediário  
                        - Excel - nível intermediário  
                        - SQL -  Voltado a análise de dados  
                        
                

                - Ciêntista de dados     
                    DNC    
                        Tópicos abordados no curso  :  
                        - Power BI - nível intermediário
                        - Excel - nível intermediário  
                        - SQL -  Voltado a análise de dados  
                          
                        
                        ''')

        # ------------------------------------------------------------------------
        
        
    with tab2: # ENGLISH VERSION
        st.write('#### :books: IN CONSTRUCTION')

        
    with tab3: # PORTFOLIO GEOPROCESSING
        
        st.write('#### :books: Em construção ')
#         
        
    with tab4: # Data analyst
        #
        st.write('#### :books: Em construção ')
        
  

    # st.write("Ferramentas que utilizo:")

    # Lista de ícones e legendas
    st.markdown("""<p style="background-color: white; padding: 10px; border-radius: 8px;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/markdown/markdown-original.svg" height="30" width="40">
                <img src="https://cdn.worldvectorlogo.com/logos/power-bi-1.svg" height="30" width="40">
                <img src="https://logo.svgcdn.com/l/metabase.svg" height="30" width="40">
                <img src="https://cdn.worldvectorlogo.com/logos/looker.svg" height="30" width="40">
                <img src="https://cdn.worldvectorlogo.com/logos/microsoft-excel-2013.svg" height="30" width="40">
                <img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg" height="30" width="40">
                <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" height="30" width="40">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rstudio/rstudio-original.svg" height="30" width="40">
                <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original.svg" height="30" width="40">
            </p>""", unsafe_allow_html=True)

    
if __name__ == '__main__':
    menu()
