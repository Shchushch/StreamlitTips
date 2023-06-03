import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(path)
selects = ("Таблица с данными","Гистограмма счетов", "Связь между чеком и чаевыми",
"Связь между чеком, чаевыми и размером столика","Связь между днём недели и размером счёта",
"Зависимость чаевых от дня недели и пола", "Боксплот с суммой счетов по времни суток",
"Гистограммы чаевых по времени суток", "Связь почти всех данных")
choice_dict ={selects[x]:x for x in range(len(selects))}
write = lambda x: st.write(f"""### {selects[x]}""")


st.write("""### 👈 Слева можно выбрать желаемые данные
# Учебное веб-приложение с ислледованием данных по чаевым в ресторане""")

chosen = st.sidebar.selectbox("Выберите данные, которые хотите посмотреть", selects)
if st.sidebar.button("Отпраздновать!"):
    st.balloons()
if st.sidebar.button("""~Не жми сюда~\n
                     💸💸💸💸💸"""):
    st.video(open('Rick.mp4','rb').read(),)
match choice_dict[chosen]:
    case 0:
        write(0)
        st.dataframe(tips,width=500)

    case 1:
        const=1
        
        tab,tabd = st.tabs([selects[const],selects[0]]) 
        
        with tab:
            write(const)
            fig = plt.figure()
            sns.histplot(data=tips,x='total_bill')
            st.pyplot(fig)
        with tabd:
            st.dataframe(tips,width=500)  

    case 2:
        const=2
        
        tab,tabd = st.tabs([selects[const],selects[0]]) 

        with tab:
            write(const)
            fig = plt.figure()
            sns.scatterplot(data=tips,x='tip',y='total_bill')
            st.pyplot(fig)
        with tabd:
            st.dataframe(tips,width=500)  
        
    case 3:
        const=3
        tab,tabd = st.tabs([selects[const],selects[0]]) 

        with tab:
            write(const)
            fig= plt.figure()
            sns.scatterplot(data=tips, x='total_bill',y='tip',size='size',sizes=(tips['size'].min(),tips['size'].max()*10),hue='size')
            st.pyplot(fig)
        with tabd:
            st.dataframe(tips,width=500)  
    case 4:
        const=4
        
        tab,tabd = st.tabs([selects[const],selects[0]])  

        with tab:
            write(const)
            fig = plt.figure()
            sns.barplot(data=tips, x=tips['day'].sort_values(),y='total_bill')
            st.pyplot(fig)
        with tabd:
            st.dataframe(tips,width=500)  
    case 5:
        const=5
        
        tab,tabd = st.tabs([selects[const],selects[0]])  
        
        with tab:
            write(const)
            gender_dict={'Female':'red','Male':'blue'}
            fig= plt.figure()
            sns.swarmplot(data= tips,x=tips['tip'],y=tips['day'],hue='sex',palette=gender_dict,size=4)
            st.pyplot(fig)
        with tabd:
            st.dataframe(tips,width=500)  
    case 6:
        const=6
        
        tab,tabd = st.tabs([selects[const],selects[0]])  
        
        with tab:
            write(const)
            fig= plt.figure()
            sns.boxplot(data=tips,x='time',y='total_bill')
            st.pyplot(fig)

        with tabd:
            st.dataframe(tips,width=500)  
    case 7:
        const=7
        
        tab,tabd = st.tabs([selects[const],selects[0]])  
        
        with tab: 
            write(const)
            fig, ax = plt.subplots(1,2)
            sns.histplot(data=tips.loc[tips['time']=='Lunch'], x='tip', ax=ax[0],)
            sns.histplot(data=tips.loc[tips['time']=='Dinner'],x='tip', ax=ax[1])
            st.pyplot(fig)
        with tabd:
            st.dataframe(tips,width=500)  
    case 8:
        const=8
        
        tab,tabd = st.tabs([selects[const],selects[0]])  
        #fig =plt.figure()
        with tab:
            write(const)
            st.pyplot(sns.relplot(data=tips,col='sex',x='total_bill',y='tip',hue='smoker'))
        with tabd:
            st.dataframe(tips,width=500)
#os.system("streamlit run tips.py")    
        