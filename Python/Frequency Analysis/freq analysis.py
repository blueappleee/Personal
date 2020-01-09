import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
standardfreq = [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]
newfreq1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
objects = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
newmessage = []
newfreq = []
newmessage1 = input()

for i in range(len(newmessage1)):
    lettr = newmessage1[i]
    if ord(lettr.lower()) >= 97 and ord(lettr.lower()) <= 122:
        newmessage.append(lettr.lower())

for i in range(len(newmessage)):
    letter = newmessage[i]
    ind = letters.index(letter)
    newfreq1[ind] = newfreq1[ind]+1
    
for i in range(26):
    freq1 = round((newfreq1[i]/(len(newmessage))*100),3)
    newfreq.append(freq1)

print(newfreq1)
print(newfreq)
print(standardfreq)


fig, ax = plt.subplots(1,1)
 
plt.xlabel('Letter')
plt.ylabel('Frequency')
plt.title('English frequency analysis')

ax.plot(objects,newfreq,color='red',label='Message frequency')
ax.plot(objects,standardfreq,color='blue',label='Standard frequency')

ax.legend(loc='best')

ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
if max(newfreq) >= max(standardfreq):
    ax.set_ylim((0),(max(newfreq)+1))
else:
    ax.set_ylim((0),(max(standardfreq)+1))
ax.set_xlim(0,26)
    
plt.show()
