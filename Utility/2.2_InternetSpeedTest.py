import psutil
import time
from tkinter import *


# while True:
#     s1 = psutil.net_io_counters(pernic=True)['en0']
#     time.sleep(1)
#     s2 = psutil.net_io_counters(pernic=True)['en0']
#     result = s2.bytes_recv - s1.bytes_recv
#     print(result/1024)


# s1
# {'Ethernet 9': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0),
#  'Local Area Connection* 11': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0),
#  'Local Area Connection* 15': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0),
#  'Ethernet 2': snetio(bytes_sent=21677986, bytes_recv=29526, packets_sent=74073, packets_recv=153, errin=0, errout=0, dropin=0, dropout=0),
#  'Ethernet 3': snetio(bytes_sent=22413168, bytes_recv=29526, packets_sent=91699, packets_recv=153, errin=0, errout=0, dropin=0, dropout=0),
#  'Ethernet 10': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0),
#  'Wi-Fi 5': snetio(bytes_sent=197714484, bytes_recv=3875951491, packets_sent=1626361, packets_recv=3743803, errin=0, errout=0, dropin=0, dropout=0),
#  'Loopback Pseudo-Interface 1': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0)}


def make_app():
    app = Tk()
    app.geometry('300x150')
    app.config(bg='#303030')
    Label(text='Speed Monitor',
          font=('Hack', 25, 'bold'),
          bg='#303030',
          fg='white').pack()
    Label(name='lb2',
          text='_kb/s',
          font=('Hack', 20, 'bold'),
          bg='#303030',
          fg='white').pack()
    return app


def speed_test():
    s1 = psutil.net_io_counters(pernic=True)['Wi-Fi 5']
    time.sleep(1)
    s2 = psutil.net_io_counters(pernic=True)['Wi-Fi 5']
    result = s2.bytes_recv - s1.bytes_recv
    print(result / 1024)
    return str(result / 1024) + 'kb/s'


def ui_update(do):
    data = do()
    lb2 = app.children['lb2']
    lb2.config(text=data)
    app.after(1000, lambda: ui_update(do))


app = make_app()
app.after(1000, lambda: ui_update(speed_test))
app.mainloop()
