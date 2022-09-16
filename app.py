from flask import Flask, redirect, url_for, request, render_template
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__)

new_df = pickle.load(open('new_df.pkl',"rb"))


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict",methods=['POST'])
def pred():
   tp=[]
   c = 0
   f = []
   l = 0
   ans = ""
   if request.method == 'POST':
      print(new_df.head())
      data = (request.form['final'])
      for i in data.split(" "):
          if i=='0':
              tp.append("Butter milk")
          if i=='1':
              tp.append("Yogurt")
          if i=='2':
              tp.append("Whole milk")
          if i=='3':
              tp.append("Hygiene articles")
          if i=='4':
              tp.append("Curd")
          if i=='5':
              tp.append("Margarine")
          if i=='6':
              tp.append("Liver loaf")
          if i=='7':
              tp.append("Soda")
          if i=='8':
              tp.append("Frankfurter")
          if i=='9':
              tp.append("Soups")
          if i=='10':
              tp.append("Pastry")
          
          if i=='11':
              tp.append("Other vegetables")
          if i=='12':
              tp.append("Sausage")
          if i=='13':
              tp.append("Rolls/buns")
          if i=='14':
              tp.append("Spread cheese")
          if i=='15':
              tp.append("Frozen fish")
          if i=='16':
              tp.append("Soft cheese")
          if i=='17':
              tp.append("Ham")
          if i=='18':
              tp.append("Misc. beverages")
          if i=='19':
              tp.append("Meat")
          if i=='20':
              tp.append("Frozen vegetables")
          if i=='21':
              tp.append("Canned beer")
          
          if i=='22':
              tp.append("Bottled beer")
          if i=='23':
              tp.append("Tropical fruit")
          if i=='24':
              tp.append("Root vegetables")
              
      if len(tp)==1:
            item = tp[0]
            for i,d in new_df.iterrows():
                if len(d['left_rule'])==1:
                    for j in d['left_rule']:
                        if item == j:
                            f.append(d['right_rule'])

            if len(f)!=0:
                ans = f[0]
                ans = ", ".join(ans)
      else:
            c = 0
            l = len(tp)
            
            for i,d in new_df.iterrows():
                c = 0
                if len(tp) == len(d['left_rule']):
                    for k in tp:
                        if k in d['left_rule']:
                            c = c+1
                    if c == l:
                        ans = d['right_rule']
                        ans = ", ".join(ans)
                        c = 0
                        
      p = ", ".join(tp)
      if ans=="":
          ans = "No recommendations found!!"
      else:
          ans = "Customers who bought {0} also bought {1}".format(p,ans) 
      
      return render_template('index.html',data=ans)
if __name__ == '__main__':
   app.run(debug = True)

