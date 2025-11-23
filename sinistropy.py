#pip install pyautogui
import pyautogui

#pip install time
import time

#pip install pandas
import pandas

tabela = pandas.read_excel("sinistros.xlsx")
print(tabela)

pyautogui.PAUSE = 0.5


#Abrir o navegador



#pyautogui.press("win")
#pyautogui.write("moz")
#pyautogui.press("enter")
#time.sleep(5)

#pyautogui.hotkey('alt', 'tab')

#Abrir link do site

#pyautogui.click(local de link)
#pyautogui.hotkey(crlt, v)
#time.sleep(3)

#Para cada linha da minha tabela
for linha in tabela.index:

    #Preencher cada campo

    pyautogui.click(x=601, y=296)
    pyautogui.write("Paulo Leandro")
    pyautogui.press("tab")
    pyautogui.write("paulo@ibagy.com.br")
    pyautogui.press("tab")

    #codigo slim


    contrato = tabela.loc[linha, "contrato"]
    pyautogui.write(str(contrato))

    #tipo de garantia
    pyautogui.click(x=618, y=453)

    #loft
    pyautogui.click(x=539, y=527)

    #competencia
    pyautogui.click(x=536, y=499)

    #01
    pyautogui.click(x=569, y=570)


    #fraude
    pyautogui.click(x=575, y=547)
    #nao
    pyautogui.click(x=532, y=602)

    #Clicar em enviar

    pyautogui.click(x=680, y=579)

    time.sleep(10)

    #Re-abrir o site
    pyautogui.click(x=190, y=95)
    time.sleep(5)







    #Repetir o processo

