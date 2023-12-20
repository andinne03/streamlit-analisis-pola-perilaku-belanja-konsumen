import streamlit as st 
import pandas as pd 
import numpy as np
from mlxtend.frequent_patterns import association_rules, apriori

st.markdown("<h1 style='text-align: center; color: black;'>Analysis Page </h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>Analisis Pola Perilaku Belanja Konsumen di Sebuah Supermarket dengan Menggunakan Algoritma Apriori</h3>", unsafe_allow_html=True)
st.sidebar.success("Selamat datang di halaman analisis😆!")

#load dataset 
df = pd.read_csv("item.csv")

#mengubah format pada kolom date_time menjadi tipe data datetime
df['date_time'] = pd.to_datetime(df['date_time'], format="%d-%m-%Y %H:%M")

#menambahkan dua kolom baru yaitu month dan day ke dalam DataFrame 
#informasi dari kedua kolom tersebut dari kolom date_time
df["month"] = df['date_time'].dt.month
df["day"] = df['date_time'].dt.weekday

#mengganti kolom month yang awalnya berupa angka 1 - 12, menjadi nama nama bulan yang sesuai 
df["month"].replace([i for i in range(1, 12+1)], ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], inplace=True)
#mengganti kolom day yang mulanya angka 1 sampai 7, menjadi nama nama hari yang sesuai 
df["day"].replace([i for i in range(6+1)], ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], inplace=True)

#membuat fungsi get_data yang berfungsi untuk menyaring data dari DataFrame
#fungsi ini mempunyai 4 parameter, yang masing masing parameternya mmeiliki nilai default kosong
def get_data(period_day='', weekday_weekend='', month='', day=''):
    data = df.copy() #membuat salinan dari df yang disimpan dalam variabel data 
    filtered = data.loc[ #menyaring data dari DataFrame berdasarkan parameter yang telah ditentukan 
        (data["period_day"].str.contains(period_day)) &
        (data["weekday_weekend"].str.contains(weekday_weekend)) &
        (data["month"].str.contains(month.title())) &
        (data["day"].str.contains(day.title()))
    ]
    return filtered if filtered.shape[0] else "No Result!"

#membuat fungsi untuk mengambil input dari pengguna
def user_input_features():
    item = st.selectbox("Item", ['Bread', 'Scandinavian', 'Hot chocolate', 'Jam', 'Cookies', 'Muffin', 'Coffee', 'Pastry', 'Medialuna', 'Tea', 'Tartine', 'Basket', 'Mineral water', 'Farm House', 'Fudge', 'Juice', "Ella's Kitchen Pouches", 'Victorian Sponge', 'Frittata', 'Hearty & Seasonal', 'Soup', 'Pick and Mix Bowls', 'Smoothies', 'Cake', 'Mighty Protein', 'Chicken sand', 'Coke', 'My-5 Fruit Shoot', 'Focaccia', 'Sandwich', 'Alfajores', 'Eggs', 'Brownie', 'Dulce de Leche', 'Honey', 'The BART', 'Granola', 'Fairy Doors', 'Empanadas', 'Keeping It Local', 'Art Tray', 'Bowl Nic Pitt', 'Bread Pudding', 'Adjustment', 'Truffles', 'Chimichurri Oil', 'Bacon', 'Spread', 'Kids biscuit', 'Siblings', 'Caramel bites', 'Jammie Dodgers', 'Tiffin', 'Olum & polenta', 'Polenta', 'The Nomad', 'Hack the stack', 'Bakewell', 'Lemon and coconut', 'Toast', 'Scone', 'Crepes', 'Vegan mincepie', 'Bare Popcorn', 'Muesli', 'Crisps', 'Pintxos', 'Gingerbread syrup', 'Panatone', 'Brioche and salami', 'Afternoon with the baker', 'Salad', 'Chicken Stew', 'Spanish Brunch', 'Raspberry shortbread sandwich', 'Extra Salami or Feta', 'Duck egg', 'Baguette', "Valentine's card", 'Tshirt', 'Vegan Feast', 'Postcard', 'Nomad bag', 'Chocolates', 'Coffee granules ', 'Drinking chocolate spoons ', 'Christmas common', 'Argentina Night', 'Half slice Monster ', 'Gift voucher', 'Cherry me Dried fruit', 'Mortimer', 'Raw bars', 'Tacos/Fajita'])
    period_day = st.selectbox('Period Day', ['Morning', 'Afternoon', 'Night'])
    weekday_weekend = st.selectbox('Weekday / Weekend', ['Weekend', 'Weekday'])
    month = st.select_slider("Month", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    day = st.select_slider('Day', ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], value="Saturday")

    return period_day, weekday_weekend, month, day, item

#memanggil fungsi user_input_features untuk mendapatkan nilai yang sudah diinput atau dipilih oleh pengguna 
#variabel2 tsb akan menyimpan nilai yang telah diinputkan oleh pengguna 
period_day, weekday_weekend, month, day, item = user_input_features()

#memanggil fungsi get_data 
#data merupakan DataFrame yang telah melewati proses filter kolom 
data = get_data(period_day.lower(), weekday_weekend.lower(), month, day)

#membuat fungsi encode dimana output nya merupakan bilangan biner yaitu 0 dan 1 
def encode(x):
  if x <= 0:
    return 0
  elif x >= 1:
    return 1

#perhitungan algoritma apriori 
if type(data) != type("No Result"): #kondisi ketika data tidak dalam keadaan kosong 
   item_count = data.groupby(["Transaction", "Item"])["Item"].count().reset_index(name="Count") #menghitung jumlah item dalam setiap transaksi 
   item_count_pivot = item_count.pivot_table(index='Transaction', columns='Item', values='Count', aggfunc='sum').fillna(0) #data diubah ke dalam bentuk pivot tabel supaya lebih ringkas dan mudah dipahami. 
   item_count_pivot = item_count_pivot.applymap(encode) #mengonversi nilai nilai di dalam tabel pivot menjadi bilangan biner yaitu 0 atau 1 

   support = 0.01 #menentukan batas support 
   frequent_items = apriori(item_count_pivot, min_support=support, use_colnames=True) #menemukan itemset yang sering muncul dengan batas support yang telah ditentukan sebelumnya

   #kode di bawah ini berfungsi untuk menghasilkan aturan asosiasi dengan metrik lift (menghitung seberapa kuat hubungan antara dua item)
   #dimana pada a#artinya aturan asosiasi yang dihasilkan, harus memiliki nilai lift setidaknya 1 atau lebih. 
   metric = "lift" #Lift mengukur seberapa besar probabilitas munculnya dua item bersama-sama (dalam suatu aturan) dibandingkan dengan probabilitas munculnya keduanya secara independen. 
   min_threshold = 1 #batas minimum untuk metrik lift 
   ##penjelasan dari kode di atas 
   #lift = 1 -> dua item sifatnya independen. Artinya tidak ada asosiasi yang signifikan antara kedua item tersebut.
   #lift > 1 -> kemunculan satu item meningkatkan kemungkinan kemunculan item lainnya. Semakin besar nilai lift, semakin kuat hubungan tersebut. 

   rules = association_rules(frequent_items, metric=metric, min_threshold=min_threshold)[["antecedents","consequents","support","confidence","lift"]]
   rules.sort_values('confidence', ascending=False,inplace=True)

#membuat fungsi yang berguna untuk mengubah daftar/list pada kolom menjadi string yang dipisahkan dengan koma 
def parse_list(x):
   x = list(x)
   if len(x) == 1:
      return x[0]
   elif len(x) > 1:
      return ", ".join(x)

#pada fungsi ini memanggil fungsi parse_list untuk mengubah list pada kolom menjadi string 
def return_item_df(item_antecedents):
   data = rules[["antecedents", "consequents"]].copy()

   data["antecedents"] = data["antecedents"].apply(parse_list) #mengubah kolom antecedent menjadi string 
   data["consequents"] = data["consequents"].apply(parse_list) #mengubah kolom consequents menjadi string 

   return list(data.loc[data["antecedents"] == item_antecedents].iloc[0,:])



if type(data) != type("No Result"):
   st.markdown("**Hasil Rekomendasi** : ")
   st.success(f"Jika konsumen membeli **{item}**, maka kemungkinan besar mereka juga akan membeli **{return_item_df(item)[1]}** secara bersamaan")

st.markdown("**Saran** : ")
st.markdown(f"1. Pihak supermarket dapat melakukan penataan untuk produk **{item}**,**{return_item_df(item)[1]}** secara berdekatan.")
st.markdown(f"2. Pihak supermarket dapat melakukan sistem bundling yang disertai dengan pemberian diskon untuk produk **{item}**,**{return_item_df(item)[1]}**.")
st.markdown(f"3. Dengan mengetahui pola belanja konsumen, pihak supermarket dapat mengelola stok atau persediaan untuk produk **{item}**,**{return_item_df(item)[1]}** secara lebih efisien.")
