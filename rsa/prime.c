   1. unsigned long long mod2(unsigned long long a,unsigned long long b,unsigned long long n)  
   2. //计算a*b%n的，防止a*b的时候超过unsigned long long的范围  
   3. {  
   4.     unsigned long long sum=0;  
   5.     int i;  
   6.     for(i=61;i>=0;i--)  
   7.     {  
   8.         sum<<=1;  
   9.         if(b&(unsigned long long)1<<i)  
  10.             sum+=a;  
  11.         sum%=n;  
  12.     }  
  13.     return sum;  
  14. }  
  15. unsigned long long mod(unsigned long long a,unsigned long long b,unsigned long long n)  
  16. //模取幕，计算a^b%n；  
  17. {  
  18.     unsigned long long m=1;  
  19.     int i=60;  
  20.     while(!b&(unsigned long long)1<<i)  
  21.         i--;  
  22.     while(i>=0)  
  23.     {  
  24.         m=mod2(m,m,n);  
  25.         if(b&(unsigned long long)1<<i)  
  26.             m=mod2(m,a,n);  
  27.         i--;  
  28.     }  
  29.     return m;  
  30. }  
  31. bool witness(unsigned long long a,unsigned long long n)  
  32. {  
  33.     int i=0;  
  34.     unsigned long long t2,t=n-1;  
  35.     while(t%2==0)  
  36.     {  
  37.         t>>=1;  
  38.         i++;  
  39.     }  
  40.     t=mod(a,t,n);  
  41.     for(;i>0;i--)  
  42.     {  
  43.         t2=mod2(t,t,n);  
  44.         if(t2==1&&t!=1&&t!=n-1)  
  45.             return true;  
  46.         t=t2;  
  47.     }  
  48.     if(t!=1)  
  49.         return true;  
  50.     return false;  
  51. }  
  52. bool miller_rabin(unsigned long long n)  
  53. {  
  54.     int i;  
  55.     unsigned long long t;  
  56.     for(i=0;i<10;i++)//其中10是测试的次数，越大出错率越小，一般应用取10就够  
  57.     {  
  58.         t=(double)rand()/RAND_MAX*(n-2)+1;  
  59.         if(witness(t,n))  
  60.         return false;  
  61.     }  
  62.     return true;  
  63.     //n是要测试的正数，如果是质数返回true，合数返回false  
  64. }  
