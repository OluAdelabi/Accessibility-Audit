TBM = ['Asfar Azmi', 'Gerold Bepler', 'Julie L. Boerner', 'Aliccia Bollig-Fischer', 'George S. Brush', 'Fei Chen', 'Ana deCarvalho', 'Alan Dombkowski', 'Qingping Dou', 'Yubin Ge', 'David Gorski', 'Ahmad R. Heydari', 'Maik Hüttemann', 'Michael C. Joiner', 'David Kessel', 'Seong Ho Kim', 'Jing Li', 'Wanqing Liu', 'Larry H. Matherly', 'Raymond R. Mattingly', 'Ramzi Mohammad', 'Stephan Patrick', 'Lori Pile', 'Manohar Ratnam', 'Ramandeep Rattan', 'John Reiners', 'Arun K. Rishi', 'Malathy Shekhar', 'Michael A. Tainsky', 'Jeffrey W. Taub', 'Gen Sheng Wu', 'Guojun Wu', 'Zeng-Quan Yang', 'Xiaohong (Mary) Zhang']

accessID = [('Judith Abrams', 'ah5741'), ('Asfar Azmi', 'dt9860'), ('Jennifer Beebe-Dimmer', 'ag4941'), ('Gerold Bepler', 'ej3086'), ('Julie Boerner', 'ay3001'), ('Aliccia Bollig-Fischer', 'au6242'), ('George Brush', 'ah2377'), ('Sreenivasa Chinni', 'ad6413'), ('Michele Cote', 'ag9147'), ('Ana deCarvalho', 'dt8357'), ('Alan Dombkowski', 'ak6050'), ('Qingping Dou', 'ar6637'), ('Fei Chen', 'el3014'), ('Rodrigo Fernandez-Valdivia', 'fg0332'), ('Rafael Fridman', 'aa2721'), ('Yubin Ge', 'ag5038'), ('Gen Wu', 'ah2761'), ('Heather Gibson', 'ax1572'), ('David Gorski', 'dz8037'), ('Guojun Wu', 'bb3003'), ('Ahmad Heydari', 'ad5692'), ('Kenneth Honn', 'ac5978'), ('Maik Huttemann', 'ah6179'), ('Jian Wang', 'ah2453'), ('Michael Joiner', 'ed5785'), ('Kang Chen', 'ff2630'), ('David Kessel', 'cw0581'), ('Benjamin Kidder', 'ff2646'), ('Seongho Kim', 'fn4867'), ('Hyeong Kim', 'aa4695'), ('Jing Li', 'bb8374'), ('Karin List', 'ci3803'), ('Haipeng Liu', 'ct0405'), ('Wanqing Liu', 'gm2360'), ('Larry Matherly', 'bx9706'), ('Raymond Mattingly', 'ae8291'), ('Qing-Sheng Mi', 'ef7838'), ('Ramzi Mohammad', 'ad5717'), ('Stephan Patrick', 'fk4300'), ('Lori Pile', 'at1230'), ('Izabela Podgorski', 'ak5520'), ('Kristen Purrington', 'fn6868'), ('Manohar Ratnam', 'ea3489'), ('Ramandeep Rattan', 'ga2779'), ('Avraham Raz', 'aa2711'), ('John Reiners', 'ad5180'), ('Arun Rishi', 'af7487'), ('Ann Schwartz', 'cb5742'), ('Malathy Shekhar', 'ad5552'), ('Shijie Sheng', 'ae4524'), ('Anthony Shields', 'ac2597'), ('Michael Tainsky', 'af7502'), ('Jeffrey Taub', 'aa1325'), ('Nerissa Viola', 'fx1674'), ('Kay-Uwe Wagner', 'gq0641'), ('Wei-Zen Wei', 'aa2007'), ('Wei Chen', 'dt8340'), ('Youming Xie', 'ao5390'), ('Zeng-Quan Yang', 'av7882'), ('Xiaohong Zhang', 'ga5554')]

for id in accessID:
    if id[0] in TBM:
        print(id[1])