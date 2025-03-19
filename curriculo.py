import streamlit as st

# Definindo configurações da página, incluindo o título da aba
st.set_page_config(
    page_title="Currículo Online - Kassio Aquino",  # Título da aba do navegador
    page_icon=":bust_in_silhouette:",
    layout="centered",  # Layout da página
    initial_sidebar_state="collapsed",  # Sidebar inicializada de forma compacta (opcional)
)

# Título da página
st.markdown('<h2 class="small-header">Kassio Ferreira Aquino</h2>', unsafe_allow_html=True)
st.write("""
- **Bairro**: Parque Dez de Novembro
- **Telefone**: [92 98140-1714 (Whatsapp)](https://wa.me/5592981401714) / (92) 9115-6181
- **Email**: kassiomiller@gmail.com
- **LinkedIn**: [Kassio Aquino](https://www.linkedin.com/in/kassio-aquino)
""")

# Criar uma "container" para organizar melhor o layout
with st.container():
    # Seção de Resumo Profissional
    st.markdown('<h4 class="small-header">Resumo Profissional</h4>', unsafe_allow_html=True)
    st.write(""" 
    Profissional com experiência em Python, SQL, automação de processos e qualidade de software. Atuei em ambientes ágeis (Scrum) e com foco em entrega de soluções eficientes. 
    Busco a transição para a área de Análise de Dados, onde posso aplicar minhas habilidades em automação, modelagem de dados e transformar dados em insights valiosos para decisões estratégicas.
    """)

    # Seção de Habilidades Técnicas
    st.markdown('<h4 class="small-header">Habilidades Técnicas</h4>', unsafe_allow_html=True)
    st.write(""" 
    - **Linguagens e Tecnologias:** Python, SQL, Automação de Processos, Banco de Dados (MySQL, SQL Server)
    - **Metodologias Ágeis:** Scrum, DevOps
    - **Versionamento de Código:** Git, GitHub
    - **Automação de Testes:** Selenium, Robot Framework
    - **Ferramentas de Análise de Dados:** Excel Avançado
    - **Integração Contínua (CI/CD)**
    """)

    # Seção de Experiência Profissional
    st.markdown('<h4 class="small-header">Experiência Profissional</h4>', unsafe_allow_html=True)
    st.markdown('<h4 class="small-header">Analista de Testes | Philips Clinical Informatics</h4>', unsafe_allow_html=True)
    st.write("Período: 03/2022 – 12/2023")
    st.write("""
    - Desenvolvimento de scripts de automação de testes em Python, Selenium e Robot Framework para garantir a qualidade do software.
    - Análise e extração de dados de sistemas para geração de relatórios e insights para a equipe de desenvolvimento.
    - Colaboração com equipes ágeis (Scrum), participando ativamente das sprints e contribuindo para o ciclo de vida do software.
    - Implementação de testes automatizados e acompanhamento da qualidade em todas as etapas do processo.
    """)

    # Espaçamento (pular uma linha)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<h4 class="small-header">Analista de Desenvolvimento de Sistemas | Fóton Informática</h4>', unsafe_allow_html=True)
    st.write("Período: 07/2021 – 02/2022")
    st.write("""
    - Desenvolvimento de sistemas de relatórios e automação de processos, buscando otimizar a performance e a eficiência das operações.
    - Implementação de melhorias e ajustes nos sistemas, sempre com foco na qualidade e melhoria contínua.
    - Participação em cerimônias ágeis e soluções para otimização de processos internos.
    """)

    st.markdown('<h4 class="small-header">Analista de Suporte | MMC Com. E Serv. De Impressões Ltda</h4>', unsafe_allow_html=True)
    st.write("Período: 07/2010 – 07/2020")
    st.write("""
    - Administração de infraestrutura de TI, rede e servidores, implementação de políticas de segurança e recuperação de dados.
    - Suporte técnico de hardware e software, instalação de sistemas operacionais e gestão de backups e recuperação.
    - Treinamento de usuários e implementação de melhorias em processos de atendimento.
    """)

    # Seção de Projetos Relevantes
    st.markdown('<h4 class="small-header">Projetos Relevantes</h4>', unsafe_allow_html=True)
    st.markdown('<h4 class="small-header">Sistema Web de Localização e Controle de Estoque</h4>', unsafe_allow_html=True)
    st.write("Trabalho Temporário")
    st.write("""
    - Desenvolvimento de um sistema web para controle de estoque com QR Codes para rastreamento de produtos e melhoria da rastreabilidade.
    - Contribuição significativa para a organização e controle do inventário, aprimorando a precisão e eficiência do processo.
    """)

    # Seção de Formação Acadêmica
    st.markdown('<h4 class="small-header">Formação Acadêmica</h4>', unsafe_allow_html=True)
    st.write("""
    - **Pós-graduação em Gestão da Qualidade de Software**  
    Faculdade Facuminas de Pós-Graduação – Conclusão: 12/2022

    - **Tecnologia em Análise e Desenvolvimento de Software**  
    Centro Universitário do Norte – Conclusão: 03/2013
    """)

    st.markdown('<br>', unsafe_allow_html=True)
    
    # Seção de Certificações
    st.markdown('<h4 class="small-header">Certificações</h4>', unsafe_allow_html=True)
    st.write("""
    - **Introdução à Análise de Dados – Microsoft Power BI**  
    Fundação Bradesco – Conclusão: 06/2024

    - **Python para iniciantes: do zero ao primeiro projeto**  
    Asimov Academy – Conclusão: 11/2024

    - **Python para IA: do zero ao primeiro chatbot**  
    Asimov Academy – Conclusão: 11/2024
    """)

    # Seção de Idiomas
    st.markdown('<h4 class="small-header">Idiomas</h4>', unsafe_allow_html=True)
    st.write("""
    - **Inglês**: CEFR Level A2
    """)

     # Rodapé
    st.write("---")
    st.write("Desenvolvido por Kassio Aquino, utilizando Python.")
