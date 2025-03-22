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
- **Bairro**: Nossa Senhora das Graças - Navegantes
- **Telefone**: [92 98140-1714 (Whatsapp)](https://wa.me/5592981401714) / (92) 99115-6181
- **Email**: kassiomiller@gmail.com
- **LinkedIn**: [Kassio Aquino](https://www.linkedin.com/in/kassio-aquino)
""")

# Criação do seletor de abas
aba_selecionada = st.selectbox(
    "Escolha a seção:",
    ("Currículo", "Carta de Apresentação")
)

# Conteúdo do Currículo
if aba_selecionada == "Currículo":
    # Criar uma "container" para organizar melhor o layout
    with st.container():
        # Seção de Resumo Profissional
        st.markdown('<h4 class="small-header">Resumo Profissional</h4>', unsafe_allow_html=True)
        st.write(""" 
        Profissional com experiência em **Python**, **SQL**, **automação de processos**, **qualidade de software** e **suporte técnico**. Atuei em ambientes ágeis (Scrum) e com foco em entrega de soluções eficientes. Busco novas oportunidades, não só na área de **TI**, mas também em áreas **administrativas**, **operacionais** e de **suporte**, onde minha experiência em **gestão de processos**, **soluções técnicas** e **melhoria de processos** possa agregar valor.
        """)

        # Seção de Habilidades Técnicas
        st.markdown('<h4 class="small-header">Habilidades Técnicas</h4>', unsafe_allow_html=True)
        st.write(""" 
        - **Linguagens e Tecnologias:** Python, SQL, Automação de Processos, Banco de Dados (MySQL, SQL Server)
        - **Metodologias Ágeis:** Scrum, DevOps
        - **Versionamento de Código:** Git, GitHub
        - **Automação de Testes:** Selenium, Robot Framework
        - **Ferramentas de Análise de Dados:** Excel Avançado
        """)

        # Seção de Habilidades Transferíveis
        st.markdown('<h4 class="small-header">Habilidades Transferíveis</h4>', unsafe_allow_html=True)
        st.write("""
        - **Gestão de Processos**: Experiência em otimização de processos internos, melhoria da eficiência e organização de operações.
        - **Atendimento e Suporte**: Capacidade de fornecer suporte técnico e administrativo de qualidade, garantindo uma comunicação eficaz com as equipes.
        - **Coordenação de Projetos**: Experiência em ambientes ágeis, com habilidades para coordenar e gerenciar projetos técnicos e operacionais.
        - **Gestão de Inventário e Logística**: Experiência no gerenciamento de processos de estoque e operações logísticas.
        - **Pacote Office**: Conhecimento avançado em Excel, PowerPoint e Word, com ênfase em análise de dados, relatórios e apresentações.
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

# Conteúdo da Carta de Apresentação
elif aba_selecionada == "Carta de Apresentação":
    st.markdown('<h3 class="small-header">Carta de Apresentação</h3>', unsafe_allow_html=True)
    st.write("""
    Prezado(a) Recrutador(a),
    
    Sou Kassio Ferreira Aquino, profissional com experiência em **Python**, **SQL**, **automação de processos**, e **qualidade de software**. Trabalhei em ambientes ágeis e sempre busquei implementar soluções que otimizem processos e entreguem resultados de forma eficiente. Minha trajetória inclui tanto a automação de processos técnicos quanto a gestão e melhoria de operações.
    
    Atualmente, estou buscando novas oportunidades não apenas na área de **TI**, mas também em setores **administrativos**, **operacionais** e **de suporte**. Acredito que minhas habilidades em **gestão de processos**, **automação** e **suporte técnico** podem agregar valor a sua organização, além de contribuir para o sucesso da equipe.
    
    Fico à disposição para mais detalhes e para um eventual bate-papo.
    
    Atenciosamente,  
    Kassio Ferreira Aquino
    """)

