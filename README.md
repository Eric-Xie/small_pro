# 一些python实现的小程序

收集比较好玩的小案例、面试题，主要来自知乎、segfault等，涉及数学、算法等领域，python实现。

## 案例一：红包派发

**问题**
发一个随机红包，100块钱给10个人。每个人最多12块钱，最少6块钱。怎么分？

**思路**
因为100块分10个人，可选范围是6到12。所以可以随机地在6~12分给全部人就可以了。但可能会出现派不完或者不够分的情况，所以实际上每个人的选择区间不一定是6~12，也取决于先抽到钱的人。假如他们都抽到的金额接近总体平均值，那么这个区间就会保持在6~12，假如连续开头三个人都抽到6，那么第四个人的区间就会缩小，下限会提高。然而一旦她抽到了12，又会让下一位的选择区间变大了一点。但总体来看，越接近尾声，选择区间会缩小，直到最后一个人选择时，他的选择上限和下限是恰好相等的。

这里满足四个条件：
1.剩余金额除以人数不能大于12
2.剩余金额除以人数不能小于6
3.每个人都只能在6~12里选
4.总金额100分为10个人

m为总金额,n为人数，min选择下限，max为选择上限, x为已经抽取的数值，y为已经抽取的人数，方程式为 min <= (m-x-z)/(n-y-1) <= max，z就是下一个人要抽取的金额。