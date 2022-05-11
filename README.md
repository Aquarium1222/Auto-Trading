# Auto_Trading

#### [DSAI_HW2-Auto_Trading](https://docs.google.com/document/d/178uDDUq_5UD7MaNghHdJGPW97_w2HJ8rDYxUXRWv36w/edit#heading=h.5ec4624ic8t4)

---
test the code by running 

```python trader.py --training "Training Data" -- testing "Testing Data" --output output.csv```

---
## Method 1 - 支持向量迴歸 (Support Vector Regression, SVR)
SVR_1：找到某一個超平面，使所有的樣本點離超平面的偏差總和最小化，並預測未來一天之開盤價。

### Framework 1
<img src="./SVR_1.png" alt="Cover" width="70%"/>

----

## Method 2 - 支持向量迴歸 (Support Vector Regression, SVR)
SVR_2：找到某一個超平面，使所有的樣本點離超平面的偏差總和最小化，並預測未來兩天之開盤價。

### Framework 2
<img src="./SVR_2.png" alt="Cover" width="90%"/>

---

### Action analysis
* 三種狀態：沒有持股、持有一股、做空一股
* 三種動作：買入、無動作、賣出（沒有持股時執行賣出動作為做空）
<img src="./0_slot.png" alt="Cover" width="70%"/>

<img src="./1_slot.png" alt="Cover" width="70%"/>

<img src="./-1_slot.png" alt="Cover" width="70%"/>

---

### Data pre-processing
取出開盤價，並作最小值最大值正規化 (Min-Max Normalization)，這樣會較好訓練，並用處理完的開盤價資料去預測未來的開盤價

---

### Parameter Setting
下圖為利用 SVR_1 預測一天開盤價（橘色線段）、利用 SVR_2 預測兩天開盤價（非藍色與非橘色的其餘線段），圖片標題為 SVR_C 的參數設置為多少以及賺得的利潤，利潤藉由預測出來之開盤價與上述 Action analysis 求得，最終 SVR_C 設為 3。

<img src="./SVR_C.png" alt="Cover" width="70%"/>
